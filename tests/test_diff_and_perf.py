import orjson

from osupp.core import init_osu_tools

init_osu_tools(r"C:\Users\bobbycyl\Projects\osu-tools\PerformanceCalculator\bin\Release\net8.0")
from osupp.difficulty import calculate_difficulty
from osupp.performance import CatchPerformance, ManiaPerformance, OsuPerformance, TaikoPerformance, calculate_catch_performance, calculate_mania_performance, calculate_osu_performance, calculate_taiko_performance
from osupp.util import Result

# 准备测试结果
DIFF_RESULT = '{"star_rating":8.340159453660592,"max_combo":1782,"aim_difficulty":4.464371148872465,"aim_difficult_slider_count":229.3534837920631,"speed_difficulty":3.5505915358962152,"speed_note_count":322.6236688454787,"slider_factor":0.9672502717561137,"aim_top_weighted_slider_factor":0.455429594945989,"speed_top_weighted_slider_factor":0.4901857094088748,"aim_difficult_strain_count":155.50956192853607,"speed_difficult_strain_count":91.93918738759285,"nested_score_per_object":27.145174371451745,"legacy_score_base_multiplier":4.0,"maximum_legacy_combo_score":52235232.0}'.encode()
PERF_RESULT = '{"beatmap_info":{"DifficultyName":"Expert","Ruleset":{"ShortName":"osu","OnlineID":0,"Name":"osu!","InstantiationInfo":"osu.Game.Rulesets.Osu.OsuRuleset, osu.Game.Rulesets.Osu","LastAppliedDifficultyVersion":0,"Available":true},"Difficulty":{"DrainRate":5.0,"CircleSize":4.0,"OverallDifficulty":9.0,"ApproachRate":9.5,"SliderMultiplier":2.4,"SliderTickRate":1.0,"Parent":null},"Metadata":{"Title":"Storyteller","title_unicode":"Storyteller","Artist":"TRUE","artist_unicode":"TRUE","Author":{"OnlineID":1,"Username":"IOException","CountryCode":"Unknown","CountryString":"Unknown","IsBot":false,"Parent":null},"Source":"転生したらスライムだった件 第2期","tags":"TenSura 転スラ slime isekai That Time I Got Reincarnated as a Slime Season 2 Second 2nd Tensei shitara Slime suraimu Datta Ken Opening Rimuru Tempest リムル＝テンペスト Mikami Satoru Japanese Anime 唐沢 美帆","UserTags":[],"PreviewTime":46928,"AudioFile":"audio.mp3","BackgroundFile":"background.jpg"},"UserSettings":{"Offset":0.0,"Parent":null},"BeatmapSet":{"OnlineID":1701699,"DateAdded":"0001-01-01T00:00:00+00:00","DateSubmitted":null,"DateRanked":null,"Beatmaps":[],"Files":[],"Status":-3,"StatusInt":-3,"DeletePending":false,"Hash":"","Protected":false,"MaxStarDifficulty":0.0,"MaxLength":0.0,"MaxBPM":0.0,"AllBeatmapsUpToDate":true},"File":null,"Status":-3,"StatusInt":-3,"OnlineID":3477131,"Length":0.0,"BPM":0.0,"Hash":"","StarRating":-1.0,"MD5Hash":"","OnlineMD5Hash":"","LastLocalUpdate":null,"LastOnlineUpdate":null,"MatchesOnlineVersion":true,"EndTimeObjectCount":-1,"TotalObjectCount":-1,"LastPlayed":null,"BeatDivisor":4,"EditorTimestamp":null,"Path":null,"OnlineInfo":null,"MaxCombo":null},"performance_attributes":{"aim":174.73109835635245,"speed":65.9287498902982,"accuracy":75.88045126391914,"flashlight":0.0,"effective_miss_count":2.0,"speed_deviation":19.02604166245195,"combo_based_estimated_miss_count":2.0,"score_based_estimated_miss_count":null,"aim_estimated_slider_breaks":0.0,"speed_estimated_slider_breaks":0.0,"pp":329.88507381066114},"difficulty_attributes":{"star_rating":6.5573244947961955,"max_combo":1782,"aim_difficulty":3.5558149089835958,"aim_difficult_slider_count":212.31669845952544,"speed_difficulty":2.7088692600431186,"speed_note_count":293.2978143642428,"slider_factor":0.9665365858109283,"aim_top_weighted_slider_factor":0.4435754833342557,"speed_top_weighted_slider_factor":0.43512697356246866,"aim_difficult_strain_count":134.77529861943125,"speed_difficult_strain_count":84.41053188379207,"nested_score_per_object":27.145174371451745,"legacy_score_base_multiplier":4.0,"maximum_legacy_combo_score":52235232.0}}'.encode()
MAX_PP = 447.7962728743737
MAX_PP_CL = 428.8027574955315
MAX_LEGACY_SCORE = 52235232.0
MANIA_DIFF_RESULT = '{"star_rating":2.7225192199819594,"max_combo":1763}'.encode()
CONVERTED_TAIKO_DIFF_RESULT = '{"star_rating":4.109442845494353,"max_combo":1701,"rhythm_difficulty":0.6425571223517397,"mono_stamina_factor":0.05261358376107376,"consistency_factor":0.7278190105371712}'.encode()
# score_id 2398632684
TAIKO_SCORE_RESULT = """{
  "score": {
    "ruleset_id": 1,
    "beatmap_id": 4434797,
    "beatmap": "YOASOBI - Shukufuku (TV Size) (Roxy-) [Linkff's Blessings]",
    "mods": [],
    "total_score": 0,
    "legacy_total_score": 0,
    "accuracy": 97.57785467128028,
    "combo": 272,
    "statistics": {
      "great": 552,
      "ok": 24,
      "meh": 0,
      "miss": 2
    }
  },
  "performance_attributes": {
    "difficulty": 137.27124726685588,
    "accuracy": 72.13943966159503,
    "estimated_unstable_rate": 173.65148639719936,
    "pp": 209.4106869284509
  },
  "difficulty_attributes": {
    "star_rating": 4.69127575774839,
    "max_combo": 578,
    "rhythm_difficulty": 1.207647054231082,
    "mono_stamina_factor": 3.5053680191451437E-09,
    "consistency_factor": 0.743943628941786
  }
}""".encode()
# score_id 1958652967
CATCH_SCORE_RESULT = """{
  "score": {
    "ruleset_id": 2,
    "beatmap_id": 2158794,
    "beatmap": "FictionJunction feat. LiSA - from the edge (TV Size) (rew0825) [Rain]",
    "mods": [
      {
        "acronym": "NF"
      },
      {
        "acronym": "CL"
      }
    ],
    "total_score": 0,
    "legacy_total_score": 815404,
    "accuracy": 97.58364312267658,
    "combo": 226,
    "statistics": {
      "great": 335,
      "large_tick_hit": 28,
      "small_tick_hit": 162,
      "small_tick_miss": 6,
      "miss": 7
    }
  },
  "performance_attributes": {
    "pp": 65.07833234682607
  },
  "difficulty_attributes": {
    "star_rating": 3.4317628194478838,
    "max_combo": 370
  }
}""".encode()
# score_id 3429471304
MANIA_SCORE_RESULT = """{
  "score": {
    "ruleset_id": 3,
    "beatmap_id": 4364723,
    "beatmap": "Sayuri - Hana no Tou (TV Size) (Revv-)",
    "mods": [],
    "total_score": 925600,
    "legacy_total_score": 0,
    "accuracy": 98.01490000000001,
    "combo": 842,
    "statistics": {
      "good": 55,
      "miss": 1,
      "great": 403,
      "perfect": 878,
      "ignore_hit": 370
    }
  },
  "performance_attributes": {
    "difficulty": 136.4007143845721,
    "pp": 136.4007143845721
  },
  "difficulty_attributes": {
    "star_rating": 3.9607623796643003,
    "max_combo": 1491
  }
}""".encode()
# score_id 2215549105
MANIA_CL_SCORE_RESULT = """{
  "score": {
    "ruleset_id": 3,
    "beatmap_id": 767046,
    "beatmap": "typeMARS - Triumph & Regret ([ A v a l o n ])",
    "mods": [
      {
        "acronym": "CL"
      }
    ],
    "total_score": 892623,
    "legacy_total_score": 936915,
    "accuracy": 97.0753,
    "combo": 2554,
    "statistics": {
      "ok": 20,
      "meh": 5,
      "good": 190,
      "miss": 10,
      "great": 1199,
      "perfect": 2429
    }
  },
  "performance_attributes": {
    "difficulty": 270.6198265466546,
    "pp": 270.6198265466546
  },
  "difficulty_attributes": {
    "star_rating": 5.481878020967975,
    "max_combo": 3994
  }
}""".encode()


def test():
    # 设置测试参数
    beatmap_path = r"./3477131.osu"
    mods = ["HD", "DT"]
    mod_options1 = ["DT_speed_change=1.3", "DT_adjust_pitch=true"]
    mod_options2 = ["DT_speed_change=1.3", "DT_adjust_pitch=True"]
    mod_options3 = ["DT_speed_change=1.3", "DT_adjust_pitch=1"]
    mod_options4 = ["DT_speed_change=1.3", "DT_adjust_pitch=1.0"]
    mod_options5 = ["DT_speed_change=1.3", "DT_adjust_pitch=false"]
    mod_options6 = ["DT_speed_change=1.3", "DT_adjust_pitch=False"]
    mod_options7 = ["DT_speed_change=1.3", "DT_adjust_pitch=0"]

    perf_result_obj = Result(orjson.loads(PERF_RESULT))
    perf_result_diff = perf_result_obj["difficulty_attributes"]
    perf_result_attr = perf_result_obj["performance_attributes"]
    perf_result_info = perf_result_obj["beatmap_info"]

    # === 第一部分：测试 difficulty 计算 ===
    assert orjson.dumps(calculate_difficulty(beatmap_path, mods, mod_options1)) == DIFF_RESULT
    assert orjson.dumps(calculate_difficulty(beatmap_path, mods, mod_options2)) == DIFF_RESULT
    assert orjson.dumps(calculate_difficulty(beatmap_path, mods, mod_options3)) == DIFF_RESULT
    assert orjson.dumps(calculate_difficulty(beatmap_path, mods, mod_options4)) == DIFF_RESULT
    assert orjson.dumps(calculate_difficulty(beatmap_path, mods, mod_options5)) == DIFF_RESULT
    assert orjson.dumps(calculate_difficulty(beatmap_path, mods, mod_options6)) == DIFF_RESULT
    assert orjson.dumps(calculate_difficulty(beatmap_path, mods, mod_options7)) == DIFF_RESULT

    # === 第二部分：测试 performance 计算 ===
    calculator = calculate_osu_performance(beatmap_path)
    try:
        # 第一次拿到的是 difficulty
        diff_attr = next(calculator)
        # 进行 3 次计算
        perf1_attr = calculator.send(OsuPerformance(combo=706, misses=2, mehs=4, oks=34, large_tick_misses=0, slider_tail_misses=7))
        perf2_attr = calculator.send(OsuPerformance(combo=706, misses=2, mehs=4, oks=34, large_tick_hits=57, slider_tail_hits=485))
        perf_max_attr = calculator.send(OsuPerformance())
        # 分别校验 performance 结果
        assert diff_attr._get_pure() == perf_result_diff
        assert perf1_attr == perf_result_attr
        assert perf2_attr == perf_result_attr
        assert perf_max_attr["pp"] == MAX_PP
        assert diff_attr["key_not_exists"] == 0.0
        # 结束时拿到谱面信息
        calculator.send(None)
    except StopIteration as e:
        assert e.value == perf_result_info


def test_classic():
    beatmap_path = r"./3477131.osu"
    mods = ["CL"]
    calculator = calculate_osu_performance(beatmap_path, mods)
    diff_attr = next(calculator)
    perf_attr = calculator.send(OsuPerformance())
    calculator.close()
    assert diff_attr["maximum_legacy_combo_score"] == MAX_LEGACY_SCORE
    assert perf_attr["pp"] == MAX_PP_CL


def test_strange():
    # 4429119 很奇怪，osu-tools 会无法处理，只能在 Python 层面做一个错误拦截，这里测试拦截效果
    beatmap_path = r"./4429119.osu"
    mods = ["EZ"]
    diff_attr = calculate_difficulty(beatmap_path, mods)
    assert diff_attr["star_rating"] == 0.0
    calculator = calculate_osu_performance(beatmap_path)
    try:
        diff_attr2 = next(calculator)
        assert diff_attr2["star_rating"] == 0.0
        _ = calculator.send(OsuPerformance())
        _ = calculator.send(OsuPerformance())
        _ = calculator.send(OsuPerformance())
        _ = calculator.send(OsuPerformance())
        _ = calculator.send(OsuPerformance())
    except StopIteration as e:
        assert e.value["DifficultyName"] == "Beyond Obliteration"


def test_more_rulesets_diff():
    mania_path = "./4103079.osu"
    assert orjson.dumps(calculate_difficulty(mania_path)) == MANIA_DIFF_RESULT
    converted_taiko_path = "./3477131.osu"
    assert orjson.dumps(calculate_difficulty(converted_taiko_path, ruleset_id=1)) == CONVERTED_TAIKO_DIFF_RESULT


def test_taiko_perf():
    beatmap_path = "./4434797.osu"
    calculator = calculate_taiko_performance(beatmap_path)
    next(calculator)
    assert calculator.send(TaikoPerformance(combo=272, oks=24, misses=2)) == orjson.loads(TAIKO_SCORE_RESULT)["performance_attributes"]


def test_catch_perf():
    beatmap_path = "./2158794.osu"
    calculator = calculate_catch_performance(beatmap_path, mods=["NF", "CL"])
    next(calculator)
    assert calculator.send(CatchPerformance(combo=226, misses=7, large_tick_hits=28, small_tick_hits=162)) == orjson.loads(CATCH_SCORE_RESULT)["performance_attributes"]


def test_mania_perf():
    beatmap_path = "./4364723.osu"
    calculator = calculate_mania_performance(beatmap_path)
    next(calculator)
    assert calculator.send(ManiaPerformance(goods=55, misses=1, greats=403)) == orjson.loads(MANIA_SCORE_RESULT)["performance_attributes"]


def test_mania_cl_perf():
    beatmap_path = "./767046.osu"
    calculator = calculate_mania_performance(beatmap_path, mods=["CL"])
    next(calculator)
    assert calculator.send(ManiaPerformance(oks=20, mehs=5, goods=190, misses=10, greats=1199)) == orjson.loads(MANIA_CL_SCORE_RESULT)["performance_attributes"]
