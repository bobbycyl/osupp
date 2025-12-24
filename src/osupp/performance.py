from typing import Optional

from .core import Array, BeatmapExtensions, Dictionary, HitResult, IBeatmap, Mod, OsuModClassic, OsuRuleset, ProcessorCommand, ProcessorWorkingBeatmap, ScoreInfo, Slider, SliderRepeat, SliderTick
from .util import re_deserialize


# 对应 OsuSimulateCommand.cs 的 generateHitResults
def generate_hit_results(
    beatmap: IBeatmap,
    accuracy: float,
    count_miss: int,
    count_meh: Optional[int] = None,
    count_good: Optional[int] = None,
    count_large_tick_misses: Optional[int] = None,
    count_slider_tail_misses: Optional[int] = None,
) -> Dictionary[HitResult, int]:
    count_great: int
    total_result_count: int = beatmap.HitObjects.Count

    if count_meh is not None or count_good is not None:
        count_great = total_result_count - (count_good or 0) - (count_meh or 0) - count_miss
    else:
        relevant_result_count = total_result_count - count_miss
        if relevant_result_count <= 0:
            relevant_accuracy = 0.0
        else:
            relevant_accuracy = accuracy * total_result_count / relevant_result_count
        relevant_accuracy = max(0.0, min(1.0, relevant_accuracy))

        if relevant_accuracy >= 0.25:
            ratio_50_to_100 = (1 - (relevant_accuracy - 0.25) / 0.75) ** 2
            count_100_estimate = 6 * relevant_result_count * (1 - relevant_accuracy) / (5 * ratio_50_to_100 + 4)
            count_50_estimate = count_100_estimate * ratio_50_to_100
            count_good = round(count_100_estimate)
            count_meh = round(count_100_estimate + count_50_estimate) - count_good
        elif relevant_accuracy >= 1.0 / 6:
            count_100_estimate = 6 * relevant_result_count * relevant_accuracy - relevant_result_count
            count_50_estimate = relevant_result_count - count_100_estimate
            count_good = round(count_100_estimate)
            count_meh = round(count_100_estimate + count_50_estimate) - count_good
        else:
            count_50_estimate = 6 * relevant_result_count * relevant_accuracy
            count_good = 0
            count_meh = round(count_50_estimate)
            count_miss = total_result_count - count_meh
        count_great = int(total_result_count - (count_good or 0) - (count_meh or 0) - count_miss)

    # 构建结果字典
    result = Dictionary[HitResult, int]()
    result[HitResult.Great] = count_great
    result[HitResult.Ok] = count_good or 0
    result[HitResult.Meh] = count_meh or 0
    result[HitResult.Miss] = count_miss

    if count_large_tick_misses is not None:
        result[HitResult.LargeTickMiss] = count_large_tick_misses

    if count_slider_tail_misses is not None:
        slider_count = sum(1 for obj in beatmap.HitObjects if isinstance(obj, Slider))
        result[HitResult.SliderTailHit] = slider_count - count_slider_tail_misses

    return result


# 对应 OsuSimulateCommand.cs 的 GetAccuracy
def get_accuracy(beatmap: IBeatmap, statistics: dict[HitResult, int], mods: Array[Mod]):
    count_great: int = statistics[HitResult.Great]
    count_good: int = statistics[HitResult.Ok]
    count_meh: int = statistics[HitResult.Meh]
    count_miss: int = statistics[HitResult.Miss]
    total = 6 * count_great + 2 * count_good + count_meh
    max_score = 6 * (count_great + count_good + count_meh + count_miss)

    if HitResult.SliderTailHit in statistics:
        count_slider_tail_hit = statistics[HitResult.SliderTailHit]
        count_sliders = sum(1 for obj in beatmap.HitObjects if isinstance(obj, Slider))
        total += 3 * count_slider_tail_hit
        max_score += 3 * count_sliders

    if HitResult.LargeTickMiss in statistics:
        count_large_tick_miss = statistics[HitResult.LargeTickMiss]
        count_large_ticks = sum(1 for obj in beatmap.HitObjects for nested in obj.NestedHitObjects if isinstance(nested, (SliderTick, SliderRepeat)))
        count_large_tick_hit = count_large_ticks - count_large_tick_miss
        total += 0.6 * count_large_tick_hit
        max_score += 0.6 * count_large_ticks

    if max_score == 0:
        return 0.0

    return total / max_score


def calculate_osu_performance(
    beatmap_path: str,
    mods: Optional[list[str]] = None,
    mod_options: Optional[list[str]] = None,
    accuracy_percent: float = 100.0,
    combo: Optional[int] = None,
    misses: int = 0,
    mehs: Optional[int] = None,
    goods: Optional[int] = None,
    large_tick_misses: int = 0,
    slider_tail_misses: int = 0,
) -> dict:
    working_beatmap = ProcessorWorkingBeatmap(beatmap_path)
    ruleset = OsuRuleset()
    if mods is None:
        mods = []
    if mod_options is None:
        mod_options = []
    mod_array = ProcessorCommand.ParseMods(ruleset, Array[str](mods), Array[str](mod_options))
    beatmap = working_beatmap.GetPlayableBeatmap(ruleset.RulesetInfo, mod_array)

    if any(isinstance(m, OsuModClassic) and m.NoSliderHeadAccuracy.Value for m in mod_array):
        hit_results = generate_hit_results(beatmap, accuracy_percent / 100.0, misses, mehs, goods, None, None)
    else:
        hit_results = generate_hit_results(beatmap, accuracy_percent / 100.0, misses, mehs, goods, large_tick_misses, slider_tail_misses)

    score_info = ScoreInfo()
    score_info.BeatmapInfo = working_beatmap.BeatmapInfo
    score_info.Ruleset = ruleset.RulesetInfo
    score_info.Accuracy = get_accuracy(beatmap, hit_results, mod_array)
    score_info.MaxCombo = BeatmapExtensions.GetMaxCombo(beatmap) if combo is None else combo
    score_info.Statistics = hit_results
    score_info.Mods = mod_array

    difficulty_calculator = ruleset.CreateDifficultyCalculator(working_beatmap)
    difficulty_attributes = difficulty_calculator.Calculate(mod_array)

    performance_calculator = ruleset.CreatePerformanceCalculator()
    performance_attributes = performance_calculator.Calculate(score_info, difficulty_attributes)

    return {
        "beatmap_info": re_deserialize(working_beatmap.BeatmapInfo),
        "performance_attributes": re_deserialize(performance_attributes),
        "difficulty_attributes": re_deserialize(difficulty_attributes),
    }
