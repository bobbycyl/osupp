from collections.abc import Generator
from functools import singledispatch
from typing import Any, Iterable, Literal, NamedTuple, Optional, cast

from System import Array, OperationCanceledException, TimeoutException
from System.Collections.Generic import Dictionary
from System.Threading import CancellationTokenSource

from PerformanceCalculator import LegacyHelper, ProcessorCommand, ProcessorWorkingBeatmap
from PerformanceCalculatorGUI import ExtendedCatchDifficultyCalculator, ExtendedManiaDifficultyCalculator, ExtendedOsuDifficultyCalculator, ExtendedTaikoDifficultyCalculator
from osu.Game.Beatmaps import BeatmapExtensions, IBeatmap
from osu.Game.Rulesets.Catch import CatchRuleset
from osu.Game.Rulesets.Catch.Objects import Droplet, Fruit, JuiceStream, TinyDroplet
from osu.Game.Rulesets.Difficulty import DifficultyAttributes, PerformanceAttributes, RulesetBeatmapAttribute
from osu.Game.Rulesets.Difficulty.Preprocessing import DifficultyHitObject
from osu.Game.Rulesets.Difficulty.Skills import Skill, StrainSkill
from osu.Game.Rulesets.Mania import ManiaRuleset
from osu.Game.Rulesets.Mania.Objects import HoldNote
from osu.Game.Rulesets.Mods import Mod, ModClassic
from osu.Game.Rulesets.Objects import HitObject, HitObjectExtensions
from osu.Game.Rulesets.Osu import OsuRuleset
from osu.Game.Rulesets.Osu.Difficulty.Skills import Aim
from osu.Game.Rulesets.Osu.Mods import OsuModClassic
from osu.Game.Rulesets.Osu.Objects import Slider, SliderRepeat, SliderTick
from osu.Game.Rulesets.Scoring import HitResult
from osu.Game.Rulesets.Taiko import TaikoRuleset
from osu.Game.Scoring import ScoreInfo
from osu.Game.Utils import FormatUtils, ModUtils
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
        count_great = int(
            total_result_count - (count_ok or 0) - (count_meh or 0) - count_miss,
        )

    result: dict[HitResult | str, int] = {
        HitResult.Great: count_great,
        HitResult.Ok: count_ok or 0,
        HitResult.Meh: count_meh or 0,
        HitResult.Miss: count_miss,
    }

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
        count_ok: int = total_result_count - count_great - count_miss

    return {
        HitResult.Great: count_great,
        HitResult.Ok: count_ok,
        HitResult.Meh: 0,
        HitResult.Miss: count_miss,
    }


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
        count_large_tick_hit: int = max(0, max_large_tick_hit - count_miss)

    count_great = max_great - (count_miss - (max_large_tick_hit - count_large_tick_hit))

    if count_small_tick_hit is None:
        count_small_tick_hit: int = int(round(accuracy * (max_combo + max_small_tick_hit))) - count_great - count_large_tick_hit

    count_small_tick_miss = max_small_tick_hit - count_small_tick_hit

    return {
        HitResult.Great: count_great,
        HitResult.LargeTickHit: count_large_tick_hit,
        HitResult.SmallTickHit: count_small_tick_hit,
        HitResult.SmallTickMiss: count_small_tick_miss,
        HitResult.Miss: count_miss,
    }


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

    count_great: int = min(delta // 50, remaining_hits)
    delta -= count_great * 50
    remaining_hits -= count_great

    count_good: int = min(delta // 30, remaining_hits)
    delta -= count_good * 30
    remaining_hits -= count_good

    count_ok: int = min(delta // 10, remaining_hits)
    remaining_hits -= count_ok

    count_meh: int = remaining_hits

    return {
        HitResult.Perfect: count_perfect,
        HitResult.Great: count_great,
        HitResult.Ok: count_ok,
        HitResult.Good: count_good,
        HitResult.Meh: count_meh,
        HitResult.Miss: count_miss,
    }


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
        return generate_osu_hit_results(
            beatmap,
            perf.accuracy_percent / 100.0,
            perf.misses,
            perf.mehs,
            perf.oks,
            None,
            None,
        )
    else:
        return generate_osu_hit_results(
            beatmap,
            perf.accuracy_percent / 100.0,
            perf.misses,
            perf.mehs,
            perf.oks,
            perf.large_tick_misses,
            perf.slider_tail_misses,
            count_large_tick_hits=perf.large_tick_hits,
            count_slider_tail_hits=perf.slider_tail_hits,
        )


@generate_hit_result.register(TaikoPerformance)
def _(perf: TaikoPerformance, beatmap: IBeatmap, mods: Array[Mod]):
    return generate_taiko_hit_results(
        beatmap,
        perf.accuracy_percent / 100.0,
        perf.misses,
        perf.oks,
    )


@generate_hit_result.register(CatchPerformance)
def _(perf: CatchPerformance, beatmap: IBeatmap, mods: Array[Mod]):
    return generate_catch_hit_results(
        beatmap,
        perf.accuracy_percent / 100.0,
        perf.misses,
        perf.small_tick_hits,
        perf.large_tick_hits,
    )


@generate_hit_result.register(ManiaPerformance)
def _(perf: ManiaPerformance, beatmap: IBeatmap, mods: Array[Mod]):
    return generate_mania_hit_results(
        beatmap,
        mods,
        perf.accuracy_percent / 100.0,
        perf.misses,
        perf.mehs,
        perf.oks,
        perf.goods,
        perf.greats,
    )


@singledispatch
def get_accuracy(perf, beatmap: IBeatmap, statistics: dict[HitResult | str, int], mods: Array[Mod]) -> float:
    raise NotImplementedError


# 对应 OsuSimulateCommand.cs 的 GetAccuracy
@get_accuracy.register(OsuPerformance)
def _(
    perf: OsuPerformance,
    beatmap: IBeatmap,
    statistics: dict[HitResult | str, int],
    mods: Array[Mod],
) -> float:
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
        count_large_ticks = sum(1 for obj in cast(list[HitObject], beatmap.HitObjects) for nested in obj.NestedHitObjects if isinstance(nested, (SliderTick, SliderRepeat)))
        count_large_tick_hit = statistics.get("large_tick_hits", count_large_ticks - count_large_tick_miss)
        total += 0.6 * count_large_tick_hit
        max_score += 0.6 * count_large_ticks

    if max_score == 0:
        return 0.0

    return total / max_score


# 对应 TaikoSimulateCommand.cs 的 GetAccuracy
@get_accuracy.register(TaikoPerformance)
def _(
    perf: TaikoPerformance,
    beatmap: IBeatmap,
    statistics: dict[HitResult | str, int],
    mods: Array[Mod],
) -> float:
    count_great = statistics[HitResult.Great]
    count_ok = statistics[HitResult.Ok]
    count_miss = statistics[HitResult.Miss]
    total = count_great + count_ok + count_miss

    if total == 0:
        return 0.0

    return ((2 * count_great) + count_ok) / (2 * total)


# 对应 CatchSimulateCommand.cs 的 GetAccuracy
@get_accuracy.register(CatchPerformance)
def _(
    perf: CatchPerformance,
    beatmap: IBeatmap,
    statistics: dict[HitResult | str, int],
    mods: Array[Mod],
) -> float:
    hits = statistics[HitResult.Great] + statistics[HitResult.LargeTickHit] + statistics[HitResult.SmallTickHit]
    total = hits + statistics[HitResult.Miss] + statistics[HitResult.SmallTickMiss]

    if total == 0:
        return 0.0

    return hits / total


# 对应 ManiaSimulateCommand.cs 的 GetAccuracy
@get_accuracy.register(ManiaPerformance)
def _(
    perf: ManiaPerformance,
    beatmap: IBeatmap,
    statistics: dict[HitResult | str, int],
    mods: Array[Mod],
) -> float:
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


def calculate_performance(
    beatmap_path: str,
    ruleset=None,
    mods=None,
    mod_options=None,
    allow_cancel=True,
) -> Generator[Result, Any, Result]:
    cancellation_token_source = CancellationTokenSource(10_000) if allow_cancel else CancellationTokenSource()
    working_beatmap = ProcessorWorkingBeatmap(beatmap_path)
    if mods is None:
        mods = []
    if mod_options is None:
        mod_options = []
    if ruleset is None:
        ruleset_id: Literal[0, 1, 2, 3] = cast(
            Literal[0, 1, 2, 3],
            working_beatmap.BeatmapInfo.Ruleset.OnlineID,
        )
        ruleset = LegacyHelper.GetRulesetFromLegacyID(ruleset_id)
    mod_array = ProcessorCommand.ParseMods(
        ruleset,
        Array[str](mods),
        Array[str](mod_options),
    )

    match ruleset:
        case OsuRuleset():
            difficulty_calculator = ExtendedOsuDifficultyCalculator(ruleset.RulesetInfo, working_beatmap)
        case TaikoRuleset():
            difficulty_calculator = ExtendedTaikoDifficultyCalculator(ruleset.RulesetInfo, working_beatmap)
        case CatchRuleset():
            difficulty_calculator = ExtendedCatchDifficultyCalculator(ruleset.RulesetInfo, working_beatmap)
        case ManiaRuleset():
            difficulty_calculator = ExtendedManiaDifficultyCalculator(ruleset.RulesetInfo, working_beatmap)
        case _:
            raise NotImplementedError

    # 如果难度计算失败，则直接返回，后面的步骤全部失效，避免进一步耗时（虽然这已经很耗时了的说）
    # 虽然从数据分析的角度，剔除异常值是最好的选择
    # 但是使用这个库的目的不一定是数据分析，因此还是把所有内容都呈现出来
    try:
        difficulty_attributes = difficulty_calculator.Calculate(mod_array) if allow_cancel else difficulty_calculator.Calculate(mod_array, cancellation_token_source.Token)
    except OperationCanceledException:  # ty:ignore[invalid-exception-caught]
        difficulty_attributes = DifficultyAttributes()
    cs_adj = 0.0
    ar_adj = 0.0
    od_adj = 0.0
    hp_adj = 0.0
    cs_orig = 0.0
    ar_orig = 0.0
    od_orig = 0.0
    hp_orig = 0.0
    for attr in cast(Iterable[RulesetBeatmapAttribute], ruleset.GetBeatmapAttributesForDisplay(working_beatmap.BeatmapInfo, mod_array)):
        match attr.Acronym:
            case "CS":
                cs_adj = attr.AdjustedValue
                cs_orig = attr.OriginalValue
            case "AR":
                ar_adj = attr.AdjustedValue
                ar_orig = attr.OriginalValue
            case "OD":
                od_adj = attr.AdjustedValue
                od_orig = attr.OriginalValue
            case "HP":
                hp_adj = attr.AdjustedValue
                hp_orig = attr.OriginalValue

    clock_rate = ModUtils.CalculateRateWithMods(mod_array)
    min_bpm_orig = working_beatmap.Beatmap.ControlPointInfo.BPMMinimum
    max_bpm_orig = working_beatmap.Beatmap.ControlPointInfo.BPMMaximum
    try:
        most_common_bpm_orig = 60000 / working_beatmap.Beatmap.GetMostCommonBeatLength()
        most_common_bpm_adj = FormatUtils.RoundBPM(most_common_bpm_orig, clock_rate)
    except ZeroDivisionError:
        most_common_bpm_orig = float("inf")
        most_common_bpm_adj = float("inf")
    # 注：clock_rate 不会因为 WU、WD 这类模组而变化
    # 在 osuawa 中的 magnitude 则是考虑了这一点进行计算
    min_bpm_adj = FormatUtils.RoundBPM(min_bpm_orig, clock_rate)
    max_bpm_adj = FormatUtils.RoundBPM(max_bpm_orig, clock_rate)

    _skills: Iterable[Skill] = difficulty_calculator.GetSkills()
    _hit_objects: list[HitObject] = list(working_beatmap.Beatmap.HitObjects)
    difficulty_hit_objects: list[DifficultyHitObject] = list(difficulty_calculator.GetDifficultyHitObjects())

    strains: dict[str, list[float]] = {}
    max_strain_len = 0
    for _skill in _skills:
        skill_type = _skill.GetType().Name
        if skill_type == "Aim" and cast(Aim, _skill).IncludeSliders:
            skill_type += " (sliders included)"
        strain = list(cast(Iterable[float], cast(StrainSkill, _skill).GetCurrentStrainPeaks()))
        strains[skill_type] = strain
        if len(strain) > max_strain_len:
            max_strain_len = len(strain)

    sent = yield re_deserialize(
        obj=difficulty_attributes,
        strains=strains,
        difficulty_hit_objects=difficulty_hit_objects,
        cs_adj=cs_adj,
        ar_adj=ar_adj,
        od_adj=od_adj,
        hp_adj=hp_adj,
        cs_orig=cs_orig,
        ar_orig=ar_orig,
        od_orig=od_orig,
        hp_orig=hp_orig,
        clock_rate=clock_rate,
        min_bpm_orig=min_bpm_orig,
        max_bpm_orig=max_bpm_orig,
        most_common_bpm_orig=most_common_bpm_orig,
        min_bpm_adj=min_bpm_adj,
        max_bpm_adj=max_bpm_adj,
        most_common_bpm_adj=most_common_bpm_adj,
        time_until_first_strain_orig=_hit_objects[1].StartTime,  # 官方的 osu-tools 中用的好像是这个值，但是我认为下面一个更准确
        time_until_first_strain_adj=difficulty_hit_objects[0].StartTime if len(difficulty_hit_objects) > 0 else _hit_objects[1].StartTime / clock_rate,
        strain_count=max_strain_len,
        ms_per_strain=400,
        hit_start_orig=_hit_objects[0].StartTime,
        hit_end_orig=max(HitObjectExtensions.GetEndTime(obj) for obj in _hit_objects),
        hit_length_orig=BeatmapExtensions.CalculatePlayableLength(working_beatmap.Beatmap),
        drain_length_orig=BeatmapExtensions.CalculateDrainLength(working_beatmap.Beatmap),
    )

    performance_calculator = ruleset.CreatePerformanceCalculator()
    while sent:
        try:
            beatmap = working_beatmap.GetPlayableBeatmap(ruleset.RulesetInfo, mod_array) if allow_cancel else working_beatmap.GetPlayableBeatmap(ruleset.RulesetInfo, mod_array, cancellation_token_source.Token)
        except TimeoutException:  # ty:ignore[invalid-exception-caught]
            sent = yield re_deserialize(obj=PerformanceAttributes())
            continue

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

        performance_attributes = performance_calculator.Calculate(
            score_info,
            difficulty_attributes,
        )

        sent = yield re_deserialize(obj=performance_attributes)

    return re_deserialize(obj=working_beatmap.BeatmapInfo)


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
    return calculate_performance(beatmap_path, OsuRuleset(), mods, mod_options)


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
