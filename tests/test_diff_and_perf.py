import orjson

import osupp as _osupp
from osu.Game.Rulesets.Osu import OsuRuleset
from osupp.difficulty import calculate_difficulty
from osupp.performance import (
    CatchPerformance,
    ManiaPerformance,
    OsuPerformance,
    TaikoPerformance,
    calculate_catch_performance,
    calculate_mania_performance,
    calculate_osu_performance,
    calculate_performance,
    calculate_taiko_performance,
)
from osupp.util import Result

assert _osupp

# 准备测试结果
def load_res(filename):
    with open(filename, "rb") as fi_b:
        return orjson.loads(fi_b.read())


DIFF_RESULT = load_res("DIFF_RESULT.json")["results"][0]["attributes"]
PERF_RESULT = load_res("PERF_RESULT.json")
MAX_PP = load_res("MAX_PP.json")["performance_attributes"]["pp"]
MAX_PP_CL = load_res("MAX_PP_CL.json")["performance_attributes"]["pp"]
MAX_LEGACY_SCORE = load_res("MAX_PP.json")["difficulty_attributes"]["maximum_legacy_combo_score"]
MANIA_DIFF_RESULT = load_res("MANIA_DIFF_RESULT.json")["results"][0]["attributes"]
CONVERTED_TAIKO_DIFF_RESULT = load_res("CONVERTED_TAIKO_DIFF_RESULT.json")["results"][0]["attributes"]
# score_id 2398632684
TAIKO_SCORE_RESULT = load_res("TAIKO_SCORE_RESULT.json")
# score_id 1958652967
CATCH_SCORE_RESULT = load_res("CATCH_SCORE_RESULT.json")
# score_id 3429471304
MANIA_SCORE_RESULT = load_res("MANIA_SCORE_RESULT.json")
# score_id 2215549105
MANIA_CL_SCORE_RESULT = load_res("MANIA_CL_SCORE_RESULT.json")


def test():
    # 设置测试参数
    beatmap_path = r"./cache/3477131.osu"
    mods = ["HD", "DT"]
    mod_options1 = ["DT_speed_change=1.3", "DT_adjust_pitch=true"]
    mod_options2 = ["DT_speed_change=1.3", "DT_adjust_pitch=True"]
    mod_options3 = ["DT_speed_change=1.3", "DT_adjust_pitch=1"]
    mod_options4 = ["DT_speed_change=1.3", "DT_adjust_pitch=1.0"]
    mod_options5 = ["DT_speed_change=1.3", "DT_adjust_pitch=false"]
    mod_options6 = ["DT_speed_change=1.3", "DT_adjust_pitch=False"]
    mod_options7 = ["DT_speed_change=1.3", "DT_adjust_pitch=0"]

    perf_result_obj = Result(PERF_RESULT)
    perf_result_diff = perf_result_obj["difficulty_attributes"]
    perf_result_attr = perf_result_obj["performance_attributes"]
    # perf_result_info = perf_result_obj["beatmap_info"]

    # === 第一部分：测试 difficulty 计算 ===
    assert calculate_difficulty(beatmap_path, mods, mod_options1) == DIFF_RESULT
    assert calculate_difficulty(beatmap_path, mods, mod_options2) == DIFF_RESULT
    assert calculate_difficulty(beatmap_path, mods, mod_options3) == DIFF_RESULT
    assert calculate_difficulty(beatmap_path, mods, mod_options4) == DIFF_RESULT
    assert calculate_difficulty(beatmap_path, mods, mod_options5) == DIFF_RESULT
    assert calculate_difficulty(beatmap_path, mods, mod_options6) == DIFF_RESULT
    assert calculate_difficulty(beatmap_path, mods, mod_options7) == DIFF_RESULT
    calculator = calculate_performance(beatmap_path, None, mods, mod_options1)
    diff_attr = next(calculator)
    # 硬编码区开始
    assert diff_attr["__ek_cs_orig"] == 4.0
    assert diff_attr["__ek_ar_orig"] == 9.5
    assert diff_attr["__ek_od_orig"] == 9.0
    assert diff_attr["__ek_hp_orig"] == 5.0
    assert round(diff_attr["__ek_ar_adj"], 2) == 10.31
    assert round(diff_attr["__ek_od_adj"], 2) == 10.0
    assert diff_attr["__ek_clock_rate"] == 1.3
    assert int(diff_attr["__ek_most_common_bpm_orig"]) == 192
    # 硬编码区结束

    # === 第二部分：测试 performance 计算 ===
    calculator = calculate_osu_performance(beatmap_path)
    try:
        # 第一次拿到的是 difficulty
        diff_attr = next(calculator)
        # 进行 3 次计算
        perf1_attr = calculator.send(
            OsuPerformance(
                combo=706,
                misses=2,
                mehs=4,
                oks=34,
                large_tick_misses=0,
                slider_tail_misses=7,
            ),
        )
        perf2_attr = calculator.send(
            OsuPerformance(
                combo=706,
                misses=2,
                mehs=4,
                oks=34,
                large_tick_hits=57,
                slider_tail_hits=485,
            ),
        )
        perf_max_attr = calculator.send(OsuPerformance())
        # 分别校验 performance 结果
        assert diff_attr._get_pure() == perf_result_diff
        assert perf1_attr == perf_result_attr
        assert perf2_attr == perf_result_attr
        assert perf_max_attr["pp"] == MAX_PP
        # 硬编码区开始
        assert diff_attr["__ek_strain_count"] == 643
        assert int(diff_attr["__ek_hit_length_orig"]) == 262500
        # 硬编码区结束

        assert diff_attr["key_not_exists"] is None
        # 结束时拿到谱面信息
        calculator.send(None)
    except StopIteration:
        # 这里的谱面信息没有在线信息，所以没必要校对了
        pass

    calculator1 = calculate_osu_performance(beatmap_path, mods=["AD"], mod_options=["AD_style=Linear"])
    calculator2 = calculate_osu_performance(beatmap_path, mods=["AD"], mod_options=["AD_style=0"])
    for c in (calculator1, calculator2):
        _ = next(c)
        perf_attr = c.send(OsuPerformance())
        assert perf_attr["pp"] == MAX_PP


def test_classic():
    beatmap_path = r"./cache/3477131.osu"
    mods = ["CL"]
    calculator = calculate_osu_performance(beatmap_path, mods)
    diff_attr = next(calculator)
    perf_attr = calculator.send(OsuPerformance())
    calculator.close()
    assert diff_attr["maximum_legacy_combo_score"] == MAX_LEGACY_SCORE
    assert perf_attr["pp"] == MAX_PP_CL


def test_strange():
    # 4429119 很奇怪，osu-tools 会无法处理，只能在 Python 层面做一个错误拦截，这里测试拦截效果
    beatmap_path = r"./cache/4429119.osu"
    mods = ["EZ"]
    diff_attr = calculate_difficulty(beatmap_path, mods)
    assert diff_attr["star_rating"] is None
    calculator = calculate_performance(beatmap_path, OsuRuleset(), [], [], False)
    try:
        diff_attr2 = next(calculator)
        # 硬编码区开始
        assert round(diff_attr2["star_rating"], 2) == 1647.66
        assert diff_attr2["__ek_cs_orig"] == 10.0
        assert diff_attr2["__ek_ar_orig"] == 0.0
        assert diff_attr2["__ek_od_orig"] == 10.0
        assert diff_attr2["__ek_most_common_bpm_orig"] == 10000.0
        perf_attr2 = calculator.send(OsuPerformance())
        assert round(perf_attr2["aim"], 2) == 3780396261.62
        assert round(perf_attr2["speed"], 2) == 122.58
        assert round(perf_attr2["pp"], 0)  == 4309651772
        # 硬编码区结束
    except StopIteration as e:
        assert e.value["DifficultyName"] == "Beyond Obliteration"


def test_more_rulesets_diff():
    mania_path = "./cache/4103079.osu"
    assert calculate_difficulty(mania_path) == MANIA_DIFF_RESULT
    converted_taiko_path = "./cache/3477131.osu"
    assert calculate_difficulty(converted_taiko_path, ruleset_id=1) == CONVERTED_TAIKO_DIFF_RESULT


def test_taiko_perf():
    beatmap_path = "./cache/4434797.osu"
    calculator = calculate_taiko_performance(beatmap_path)
    next(calculator)
    assert calculator.send(TaikoPerformance(combo=272, oks=24, misses=2)) == TAIKO_SCORE_RESULT["performance_attributes"]


def test_catch_perf():
    beatmap_path = "./cache/2158794.osu"
    calculator = calculate_catch_performance(beatmap_path, mods=["NF", "CL"])
    next(calculator)
    assert (
        calculator.send(
            CatchPerformance(
                combo=226,
                misses=7,
                large_tick_hits=28,
                small_tick_hits=162,
            ),
        )
        == CATCH_SCORE_RESULT["performance_attributes"]
    )


def test_mania_perf():
    beatmap_path = "./cache/4364723.osu"
    calculator = calculate_mania_performance(beatmap_path)
    next(calculator)
    assert calculator.send(ManiaPerformance(goods=55, misses=1, greats=403)) == MANIA_SCORE_RESULT["performance_attributes"]


def test_mania_cl_perf():
    beatmap_path = "./cache/767046.osu"
    calculator = calculate_mania_performance(beatmap_path, mods=["CL"])
    next(calculator)
    assert (
        calculator.send(
            ManiaPerformance(oks=20, mehs=5, goods=190, misses=10, greats=1199),
        )
        == MANIA_CL_SCORE_RESULT["performance_attributes"]
    )
