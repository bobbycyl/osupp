from collections.abc import Generator
from typing import NamedTuple, Optional

from .core import Array, BeatmapExtensions, Dictionary, HitResult, IBeatmap, Mod, OsuModClassic, OsuRuleset, ProcessorCommand, ProcessorWorkingBeatmap, ScoreInfo, Slider, SliderRepeat, SliderTick
from .util import re_deserialize


# 对应 OsuSimulateCommand.cs 的 generateHitResults
def generate_hit_results(
    beatmap: IBeatmap,
    accuracy: float,
    count_miss: int,
    count_meh: Optional[int] = None,
    count_ok: Optional[int] = None,
    count_large_tick_misses: Optional[int] = None,
    count_slider_tail_misses: Optional[int] = None,
    *,
    count_large_tick_hits: Optional[int] = None,
    count_slider_tail_hits: Optional[int] = None,
) -> dict[HitResult | str, int]:
    count_great: int
    total_result_count: int = beatmap.HitObjects.Count

    if count_meh is not None or count_ok is not None:
        count_great = total_result_count - (count_ok or 0) - (count_meh or 0) - count_miss
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
            count_ok = round(count_100_estimate)
            count_meh = round(count_100_estimate + count_50_estimate) - count_ok
        elif relevant_accuracy >= 1.0 / 6:
            count_100_estimate = 6 * relevant_result_count * relevant_accuracy - relevant_result_count
            count_50_estimate = relevant_result_count - count_100_estimate
            count_ok = round(count_100_estimate)
            count_meh = round(count_100_estimate + count_50_estimate) - count_ok
        else:
            count_50_estimate = 6 * relevant_result_count * relevant_accuracy
            count_ok = 0
            count_meh = round(count_50_estimate)
            # 似乎这里并不需要重新计算 miss 数量？
            # count_miss = total_result_count - count_meh
        count_great = int(total_result_count - (count_ok or 0) - (count_meh or 0) - count_miss)

    result = {HitResult.Great: count_great, HitResult.Ok: count_ok or 0, HitResult.Meh: count_meh or 0, HitResult.Miss: count_miss}

    if count_large_tick_misses is not None:
        result[HitResult.LargeTickMiss] = count_large_tick_misses

    if count_slider_tail_misses is not None:
        slider_count = sum(1 for obj in beatmap.HitObjects if isinstance(obj, Slider))
        result[HitResult.SliderTailHit] = slider_count - count_slider_tail_misses

    # 以下是个人新增内容，新增的键值对在内部处理时直接用 Python 字符串作为键名，在后续传递回 C# 时会删除
    if count_large_tick_hits is not None:
        result["large_tick_hits"] = count_large_tick_hits
    if count_slider_tail_hits is not None:
        # 这里确保直接传递 slider_tail_hits 数量的优先级更高
        result[HitResult.SliderTailHit] = count_slider_tail_hits

    return result


# 对应 OsuSimulateCommand.cs 的 GetAccuracy
def get_accuracy(beatmap: IBeatmap, statistics: dict[HitResult | str, int], mods: Array[Mod]):
    count_great: int = statistics[HitResult.Great]
    count_ok: int = statistics[HitResult.Ok]
    count_meh: int = statistics[HitResult.Meh]
    count_miss: int = statistics[HitResult.Miss]
    total = 6 * count_great + 2 * count_ok + count_meh
    max_score = 6 * (count_great + count_ok + count_meh + count_miss)

    if HitResult.SliderTailHit in statistics:
        count_slider_tail_hit = statistics[HitResult.SliderTailHit]
        count_sliders = sum(1 for obj in beatmap.HitObjects if isinstance(obj, Slider))
        total += 3 * count_slider_tail_hit
        max_score += 3 * count_sliders

    if HitResult.LargeTickMiss in statistics or "large_tick_hits" in statistics:
        count_large_tick_miss = statistics.get(HitResult.LargeTickMiss, 0)
        count_large_ticks = sum(1 for obj in beatmap.HitObjects for nested in obj.NestedHitObjects if isinstance(nested, (SliderTick, SliderRepeat)))
        count_large_tick_hit = statistics.get("large_tick_hits", count_large_ticks - count_large_tick_miss)
        total += 0.6 * count_large_tick_hit
        max_score += 0.6 * count_large_ticks

    if max_score == 0:
        return 0.0

    return total / max_score


class Performance(NamedTuple):
    accuracy_percent: float = 100.0
    combo: Optional[int] = None
    misses: int = 0
    mehs: Optional[int] = None
    oks: Optional[int] = None
    large_tick_misses: int = 0
    slider_tail_misses: int = 0
    large_tick_hits: Optional[int] = None
    slider_tail_hits: Optional[int] = None


def calculate_osu_performance(
    beatmap_path: str,
    mods: Optional[list[str]] = None,
    mod_options: Optional[list[str]] = None,
) -> Generator[dict, Optional[Performance], dict]:
    """生成器模式的计算器，在计算同一谱面时只需要创建一次计算器，提高效率

    第一次返回 difficulty_attributes

    后续每次计算返回 performance_attributes

    传入 None 则结束计算

    生成器结束返回 beatmap_info
    """
    working_beatmap = ProcessorWorkingBeatmap(beatmap_path)
    ruleset = OsuRuleset()
    if mods is None:
        mods = []
    if mod_options is None:
        mod_options = []
    mod_array = ProcessorCommand.ParseMods(ruleset, Array[str](mods), Array[str](mod_options))
    beatmap = working_beatmap.GetPlayableBeatmap(ruleset.RulesetInfo, mod_array)

    difficulty_calculator = ruleset.CreateDifficultyCalculator(working_beatmap)
    difficulty_attributes = difficulty_calculator.Calculate(mod_array)
    performance_calculator = ruleset.CreatePerformanceCalculator()

    sent = yield re_deserialize(difficulty_attributes)

    while sent:
        accuracy_percent: float = sent.accuracy_percent
        combo: Optional[int] = sent.combo
        misses: int = sent.misses
        mehs: Optional[int] = sent.mehs
        oks: Optional[int] = sent.oks
        large_tick_misses: int = sent.large_tick_misses
        slider_tail_misses: int = sent.slider_tail_misses
        large_tick_hits: Optional[int] = sent.large_tick_hits
        slider_tail_hits: Optional[int] = sent.slider_tail_hits

        if any(isinstance(m, OsuModClassic) and m.NoSliderHeadAccuracy.Value for m in mod_array):
            hit_results = generate_hit_results(beatmap, accuracy_percent / 100.0, misses, mehs, oks, None, None)
        else:
            hit_results = generate_hit_results(beatmap, accuracy_percent / 100.0, misses, mehs, oks, large_tick_misses, slider_tail_misses, count_large_tick_hits=large_tick_hits, count_slider_tail_hits=slider_tail_hits)

        score_info = ScoreInfo()
        score_info.BeatmapInfo = working_beatmap.BeatmapInfo
        score_info.Ruleset = ruleset.RulesetInfo
        score_info.Accuracy = get_accuracy(beatmap, hit_results, mod_array)
        score_info.MaxCombo = BeatmapExtensions.GetMaxCombo(beatmap) if combo is None else combo

        # 这里要把 Python 字典转换为 C# 字典，同时排除个人新增的一些键
        dotnet_statistics = Dictionary[HitResult, int]()
        for k, v in hit_results.items():
            if k not in ["large_tick_hits"]:
                dotnet_statistics[k] = v
        score_info.Statistics = dotnet_statistics
        score_info.Mods = mod_array

        performance_attributes = performance_calculator.Calculate(score_info, difficulty_attributes)

        sent = yield re_deserialize(performance_attributes)

    return re_deserialize(working_beatmap.BeatmapInfo)
