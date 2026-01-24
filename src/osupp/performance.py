from collections.abc import Generator
from functools import singledispatch
from typing import NamedTuple, Optional, Union

from .config import _CONFIG
from .core import (
    Aim,
    Array,
    BeatmapExtensions,
    CatchRuleset,
    Dictionary,
    DifficultyHitObject,
    Droplet,
    Fruit,
    HitResult,
    HoldNote,
    IBeatmap,
    JuiceStream,
    List,
    ManiaRuleset,
    Mod,
    ModClassic,
    ModUtils,
    OperationCanceledException,
    OsuDifficultyHitObject,
    OsuModClassic,
    OsuRuleset,
    ProcessorCommand,
    ProcessorWorkingBeatmap,
    Ruleset,
    ScoreInfo,
    Slider,
    SliderRepeat,
    SliderTick,
    Speed,
    TaikoRuleset,
    TinyDroplet,
)
from .util import Result, re_deserialize


# 对应 OsuSimulateCommand.cs 的 generateHitResults
def generate_osu_hit_results(
    beatmap: IBeatmap,
    accuracy: float,
    count_miss: int,
    count_meh: Optional[int] = None,
    count_ok: Optional[int] = None,
    count_large_tick_misses: Optional[int] = None,
    count_slider_tail_misses: Optional[int] = None,
    *,
    # 为了便于使用，Slider Tick 和 Slider Tail 可以直接传递 Hit 数，如果使用，这将覆盖二者的 Miss 数设置
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
    # 逻辑在最后确保传递 Hit 数的优先级最高
    if count_large_tick_hits is not None:
        result["large_tick_hits"] = count_large_tick_hits
    if count_slider_tail_hits is not None:
        result[HitResult.SliderTailHit] = count_slider_tail_hits

    return result


# 对应 OsuSimulateCommand.cs 的 GetAccuracy
def get_osu_accuracy(beatmap: IBeatmap, statistics: dict[HitResult | str, int], mods: Array[Mod]):
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


# 对应 TaikoSimulateCommand.cs 的 generateHitResults
def generate_taiko_hit_results(
    beatmap: IBeatmap,
    accuracy: float,
    count_miss: int,
    count_ok: Optional[int] = None,
) -> dict[HitResult, int]:
    total_result_count = BeatmapExtensions.GetMaxCombo(beatmap)

    count_great: int

    if count_ok is not None:
        count_great = total_result_count - count_ok - count_miss
    else:
        target_total = int(round(accuracy * total_result_count * 2))
        count_great = target_total - (total_result_count - count_miss)
        count_ok = total_result_count - count_great - count_miss

    return {
        HitResult.Great: count_great,
        HitResult.Ok: count_ok,
        HitResult.Meh: 0,
        HitResult.Miss: count_miss,
    }


# 对应 TaikoSimulateCommand.cs 的 GetAccuracy
def get_taiko_accuracy(beatmap: IBeatmap, statistics: dict[HitResult, int], mods: Array[Mod]):
    count_great = statistics[HitResult.Great]
    count_ok = statistics[HitResult.Ok]
    count_miss = statistics[HitResult.Miss]
    total = count_great + count_ok + count_miss

    if total == 0:
        return 0.0

    return ((2 * count_great) + count_ok) / (2 * total)


# 对应 CatchSimulateCommand.cs 的 generateHitResults
def generate_catch_hit_results(
    beatmap: IBeatmap,
    accuracy: float,
    count_miss: int,
    count_small_tick_hit: Optional[int] = None,
    count_large_tick_hit: Optional[int] = None,
) -> dict[HitResult, int]:
    max_combo = BeatmapExtensions.GetMaxCombo(beatmap)
    max_small_tick_hit = sum(1 for obj in beatmap.HitObjects if isinstance(obj, JuiceStream) for nested in obj.NestedHitObjects if isinstance(nested, TinyDroplet))
    max_large_tick_hit = sum(1 for obj in beatmap.HitObjects if isinstance(obj, JuiceStream) for nested in obj.NestedHitObjects if isinstance(nested, Droplet)) - max_small_tick_hit
    max_great = sum(1 if isinstance(obj, Fruit) else sum(1 for nested in obj.NestedHitObjects if isinstance(nested, Fruit)) if isinstance(obj, JuiceStream) else 0 for obj in beatmap.HitObjects)

    if count_large_tick_hit is None:
        count_large_tick_hit = max(0, max_large_tick_hit - count_miss)

    count_great = max_great - (count_miss - (max_large_tick_hit - count_large_tick_hit))

    if count_small_tick_hit is None:
        count_small_tick_hit = int(round(accuracy * (max_combo + max_small_tick_hit))) - count_great - count_large_tick_hit

    count_small_tick_miss = max_small_tick_hit - count_small_tick_hit

    return {
        HitResult.Great: count_great,
        HitResult.LargeTickHit: count_large_tick_hit,
        HitResult.SmallTickHit: count_small_tick_hit,
        HitResult.SmallTickMiss: count_small_tick_miss,
        HitResult.Miss: count_miss,
    }


# 对应 CatchSimulateCommand.cs 的 GetAccuracy
def get_catch_accuracy(beatmap: IBeatmap, statistics: dict[HitResult, int], mods: Array[Mod]):
    hits = statistics[HitResult.Great] + statistics[HitResult.LargeTickHit] + statistics[HitResult.SmallTickHit]
    total = hits + statistics[HitResult.Miss] + statistics[HitResult.SmallTickMiss]

    if total == 0:
        return 0.0

    return hits / total


# 对应 ManiaSimulateCommand.cs 的 generateHitResults
def generate_mania_hit_results(
    beatmap: IBeatmap,
    mods: Array[Mod],
    accuracy: float,
    count_miss: int,
    count_meh: Optional[int] = None,
    count_ok: Optional[int] = None,
    count_good: Optional[int] = None,
    count_great: Optional[int] = None,
) -> dict[HitResult, int]:
    is_classic = any(isinstance(m, ModClassic) for m in mods)
    total_hits = beatmap.HitObjects.Count
    if not is_classic:
        total_hits += sum(1 for obj in beatmap.HitObjects if isinstance(obj, HoldNote))

    if count_meh is not None or count_ok is not None or count_good is not None or count_great is not None:
        count_perfect = total_hits - (count_miss + (count_meh or 0) + (count_ok or 0) + (count_good or 0) + (count_great or 0))
        return {
            HitResult.Perfect: count_perfect,
            HitResult.Great: count_great or 0,
            HitResult.Good: count_good or 0,
            HitResult.Ok: count_ok or 0,
            HitResult.Meh: count_meh or 0,
            HitResult.Miss: count_miss,
        }

    perfect_value = 60 if is_classic else 61

    target_total = int(round(accuracy * total_hits * perfect_value))

    remaining_hits = total_hits - count_miss
    delta = max(target_total - (10 * remaining_hits), 0)

    count_perfect = min(delta // (perfect_value - 10), remaining_hits)
    delta -= count_perfect * (perfect_value - 10)
    remaining_hits -= count_perfect

    count_great = min(delta // 50, remaining_hits)
    delta -= count_great * 50
    remaining_hits -= count_great

    count_good = min(delta // 30, remaining_hits)
    delta -= count_good * 30
    remaining_hits -= count_good

    count_ok = min(delta // 10, remaining_hits)
    remaining_hits -= count_ok

    count_meh = remaining_hits

    return {
        HitResult.Perfect: count_perfect,
        HitResult.Great: count_great,
        HitResult.Ok: count_ok,
        HitResult.Good: count_good,
        HitResult.Meh: count_meh,
        HitResult.Miss: count_miss,
    }


# 对应 ManiaSimulateCommand.cs 的 GetAccuracy
def get_mania_accuracy(beatmap: IBeatmap, statistics: dict[HitResult, int], mods: Array[Mod]):
    count_perfect = statistics[HitResult.Perfect]
    count_great = statistics[HitResult.Great]
    count_good = statistics[HitResult.Good]
    count_ok = statistics[HitResult.Ok]
    count_meh = statistics[HitResult.Meh]
    count_miss = statistics[HitResult.Miss]

    is_classic = any(isinstance(m, ModClassic) for m in mods)
    perfect_weight = 300 if is_classic else 305

    total = (perfect_weight * count_perfect) + (300 * count_great) + (200 * count_good) + (100 * count_ok) + (50 * count_meh)
    max_score = perfect_weight * (count_perfect + count_great + count_good + count_ok + count_meh + count_miss)

    if max_score == 0:
        return 0.0

    return total / max_score


class OsuPerformance(NamedTuple):
    accuracy_percent: float = 100.0
    combo: Optional[int] = None
    misses: int = 0
    mehs: Optional[int] = None
    oks: Optional[int] = None
    large_tick_misses: int = 0
    slider_tail_misses: int = 0
    large_tick_hits: Optional[int] = None
    slider_tail_hits: Optional[int] = None


class TaikoPerformance(NamedTuple):
    accuracy_percent: float = 100.0
    combo: Optional[int] = None
    misses: int = 0
    oks: Optional[int] = None


class CatchPerformance(NamedTuple):
    accuracy_percent: float = 100.0
    combo: Optional[int] = None
    misses: int = 0
    small_tick_hits: Optional[int] = None
    large_tick_hits: Optional[int] = None


class ManiaPerformance(NamedTuple):
    accuracy_percent: float = 100.0
    misses: int = 0
    mehs: Optional[int] = None
    oks: Optional[int] = None
    goods: Optional[int] = None
    greats: Optional[int] = None


# 对应 SimulateCommand.cs 的 GenerateHitResults
@singledispatch
def generate_hit_result(perf, beatmap: IBeatmap, mods: Array[Mod]) -> dict[HitResult | str, int]:
    raise NotImplementedError


@generate_hit_result.register(OsuPerformance)
def _(perf: OsuPerformance, beatmap: IBeatmap, mods: Array[Mod]):
    # 这里完全依赖 mods 判断是否是 Classic，Slider Tick 和 Slider Tail 的值不作为判断方式
    if any(isinstance(m, OsuModClassic) and m.NoSliderHeadAccuracy.Value for m in mods):
        return generate_osu_hit_results(beatmap, perf.accuracy_percent / 100.0, perf.misses, perf.mehs, perf.oks, None, None)
    else:
        return generate_osu_hit_results(beatmap, perf.accuracy_percent / 100.0, perf.misses, perf.mehs, perf.oks, perf.large_tick_misses, perf.slider_tail_misses, count_large_tick_hits=perf.large_tick_hits, count_slider_tail_hits=perf.slider_tail_hits)


@generate_hit_result.register(TaikoPerformance)
def _(perf: TaikoPerformance, beatmap: IBeatmap, mods: Array[Mod]):
    return generate_taiko_hit_results(beatmap, perf.accuracy_percent / 100.0, perf.misses, perf.oks)


@generate_hit_result.register(CatchPerformance)
def _(perf: CatchPerformance, beatmap: IBeatmap, mods: Array[Mod]):
    return generate_catch_hit_results(beatmap, perf.accuracy_percent / 100.0, perf.misses, perf.small_tick_hits, perf.large_tick_hits)


@generate_hit_result.register(ManiaPerformance)
def _(perf: ManiaPerformance, beatmap: IBeatmap, mods: Array[Mod]):
    return generate_mania_hit_results(beatmap, mods, perf.accuracy_percent / 100.0, perf.misses, perf.mehs, perf.oks, perf.goods, perf.greats)


def get_accuracy(perf, beatmap: IBeatmap, statistics: dict[HitResult | str, int], mods: Array[Mod]):
    match perf:
        case OsuPerformance():
            return get_osu_accuracy(beatmap, statistics, mods)
        case TaikoPerformance():
            return get_taiko_accuracy(beatmap, statistics, mods)
        case CatchPerformance():
            return get_catch_accuracy(beatmap, statistics, mods)
        case ManiaPerformance():
            return get_mania_accuracy(beatmap, statistics, mods)
        case _:
            raise NotImplementedError


def calculate_performance(
    beatmap_path: str,
    ruleset: Ruleset,
    mods: Optional[list[str]] = None,
    mod_options: Optional[list[str]] = None,
    **kwargs,
) -> Generator[Result, Union[OsuPerformance, TaikoPerformance, CatchPerformance, ManiaPerformance, None], Result]:
    working_beatmap = ProcessorWorkingBeatmap(beatmap_path)
    if mods is None:
        mods = []
    if mod_options is None:
        mod_options = []
    mod_array = ProcessorCommand.ParseMods(ruleset, Array[str](mods), Array[str](mod_options))

    difficulty_calculator = ruleset.CreateDifficultyCalculator(working_beatmap)

    # 如果难度计算失败，则直接返回，后面的步骤全部失效，避免进一步耗时（虽然这已经很耗时了的说）
    # 虽然从数据分析的角度，剔除异常值是最好的选择
    # 但是使用这个库的目的不一定是数据分析，因此还是把所有内容都呈现出来
    try:
        difficulty_attributes = difficulty_calculator.Calculate(mod_array)
    except OperationCanceledException:
        pass
    else:
        beatmap = working_beatmap.GetPlayableBeatmap(ruleset.RulesetInfo, mod_array)

        # 额外处理：主模式 strainTimeline patch
        if kwargs.get("strain_timeline") and _CONFIG["strain_timeline"]:
            clock_rate = ModUtils.CalculateRateWithMods(mod_array)

            # 对应 osu 项目 OsuDifficultyCalculator.cs 的 CreateDifficultyHitObjects
            objects = List[DifficultyHitObject]()
            for i in range(1, beatmap.HitObjects.Count):
                objects.Add(
                    OsuDifficultyHitObject(
                        beatmap.HitObjects[i],
                        beatmap.HitObjects[i - 1],
                        clock_rate,
                        objects,
                        objects.Count,
                    ),
                )

            aim = Aim(mod_array, True)
            speed = Speed(mod_array)

            for obj in objects:
                aim.Process(obj)
                speed.Process(obj)

            aim_strain_timeline = [(x.Item1, x.Item2) for x in aim.StrainTimeline]
            speed_strain_timeline = [(x.Item1, x.Item2) for x in speed.StrainTimeline]

            sent = yield re_deserialize(difficulty_attributes, aim_strain_timeline=aim_strain_timeline, speed_strain_timeline=speed_strain_timeline)
        else:
            sent = yield re_deserialize(difficulty_attributes)

        performance_calculator = ruleset.CreatePerformanceCalculator()
        while sent:
            hit_results = generate_hit_result(sent, beatmap, mod_array)

            score_info = ScoreInfo()
            score_info.BeatmapInfo = working_beatmap.BeatmapInfo
            score_info.Ruleset = ruleset.RulesetInfo
            score_info.Accuracy = get_accuracy(sent, beatmap, hit_results, mod_array)
            score_info.MaxCombo = sent.combo if hasattr(sent, "combo") and sent.combo is not None else BeatmapExtensions.GetMaxCombo(beatmap)

            # 这里要把 Python 字典转换为 C# 字典，同时排除个人新增的一些键
            net_statistics = Dictionary[HitResult, int]()
            for k, v in hit_results.items():
                if k not in ["large_tick_hits"]:
                    net_statistics[k] = v
            score_info.Statistics = net_statistics
            score_info.Mods = mod_array

            performance_attributes = performance_calculator.Calculate(score_info, difficulty_attributes)

            sent = yield re_deserialize(performance_attributes)

    return re_deserialize(working_beatmap.BeatmapInfo)


def calculate_osu_performance(
    beatmap_path: str,
    mods: Optional[list[str]] = None,
    mod_options: Optional[list[str]] = None,
) -> Generator[Result, Optional[OsuPerformance], Result]:
    """生成器模式的 osu! performance 计算器，在多次计算同一谱面时只需要创建一次计算器，提高效率

    第一次返回 ``difficulty_attributes``

    后续每次传入 ``OsuPerformance`` 返回 ``performance_attributes``

    传入 ``None`` 则结束计算

    生成器结束返回 ``beatmap_info``
    """
    return calculate_performance(beatmap_path, OsuRuleset(), mods, mod_options, strain_timeline=True)


def calculate_taiko_performance(
    beatmap_path: str,
    mods: Optional[list[str]] = None,
    mod_options: Optional[list[str]] = None,
) -> Generator[Result, Optional[TaikoPerformance], Result]:
    """生成器模式的 osu!taiko performance 计算器，在多次计算同一谱面时只需要创建一次计算器，提高效率

    第一次返回 ``difficulty_attributes``

    后续每次传入 ``TaikoPerformance`` 返回 ``performance_attributes``

    传入 ``None`` 则结束计算

    生成器结束返回 ``beatmap_info``
    """
    return calculate_performance(beatmap_path, TaikoRuleset(), mods, mod_options)


def calculate_catch_performance(
    beatmap_path: str,
    mods: Optional[list[str]] = None,
    mod_options: Optional[list[str]] = None,
) -> Generator[Result, Optional[CatchPerformance], Result]:
    """生成器模式的 osu!catch performance 计算器，在多次计算同一谱面时只需要创建一次计算器，提高效率

    第一次返回 ``difficulty_attributes``

    后续每次传入 ``CatchPerformance`` 返回 ``performance_attributes``

    传入 ``None`` 则结束计算

    生成器结束返回 ``beatmap_info``
    """
    return calculate_performance(beatmap_path, CatchRuleset(), mods, mod_options)


def calculate_mania_performance(
    beatmap_path: str,
    mods: Optional[list[str]] = None,
    mod_options: Optional[list[str]] = None,
) -> Generator[Result, Optional[ManiaPerformance], Result]:
    """生成器模式的 osu!mania performance 计算器，在多次计算同一谱面时只需要创建一次计算器，提高效率

    第一次返回 ``difficulty_attributes``

    后续每次传入 ``ManiaPerformance`` 返回 ``performance_attributes``

    传入 ``None`` 则结束计算

    生成器结束返回 ``beatmap_info``
    """
    return calculate_performance(beatmap_path, ManiaRuleset(), mods, mod_options)
