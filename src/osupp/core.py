import os
import sys

from clr_loader import get_coreclr
from pythonnet import set_runtime

# 内部状态变量，记录是否已加载
_runtime_initialized = False
_dotnet_libs_imported = False


def init_osu_tools(build_dir):
    global _runtime_initialized, _dotnet_libs_imported

    if not _runtime_initialized:
        runtime_config = os.path.join(build_dir, "PerformanceCalculator.runtimeconfig.json")
        rt = get_coreclr(runtime_config=runtime_config)
        set_runtime(rt)
        sys.path.append(build_dir)

        _runtime_initialized = True

    if not _dotnet_libs_imported:
        import clr

        clr.AddReference("PerformanceCalculator")
        clr.AddReference("osu.Game")
        clr.AddReference("osu.Game.Rulesets.Osu")
        clr.AddReference("osu.Game.Rulesets.Catch")
        clr.AddReference("osu.Game.Rulesets.Taiko")
        clr.AddReference("osu.Game.Rulesets.Mania")
        clr.AddReference("Newtonsoft.Json")

        from PerformanceCalculator import LegacyHelper, ProcessorWorkingBeatmap, ProcessorCommand
        from osu.Game.Beatmaps import IBeatmap, BeatmapExtensions
        from osu.Game.Configuration import SettingSourceExtensions, SettingSourceAttribute
        from osu.Game.Rulesets import Ruleset
        from osu.Game.Rulesets.Mods import Mod, ModClassic
        from osu.Game.Rulesets.Scoring import HitResult
        from osu.Game.Rulesets.Difficulty.Preprocessing import DifficultyHitObject
        from osu.Game.Rulesets.Osu import OsuRuleset
        from osu.Game.Rulesets.Osu.Difficulty import OsuDifficultyAttributes, OsuPerformanceAttributes
        from osu.Game.Rulesets.Osu.Difficulty.Skills import Aim, Speed
        from osu.Game.Rulesets.Osu.Mods import OsuModClassic
        from osu.Game.Rulesets.Osu.Objects import Slider, SliderTick, SliderRepeat
        from osu.Game.Rulesets.Osu.Difficulty.Preprocessing import OsuDifficultyHitObject
        from osu.Game.Rulesets.Catch import CatchRuleset
        from osu.Game.Rulesets.Catch.Objects import Droplet, TinyDroplet, Fruit, JuiceStream
        from osu.Game.Rulesets.Taiko import TaikoRuleset
        from osu.Game.Rulesets.Mania import ManiaRuleset
        from osu.Game.Rulesets.Mania.Objects import HoldNote
        from osu.Game.Scoring import ScoreInfo
        from osu.Game.Utils import ModUtils
        import System
        from System import Array, OperationCanceledException
        from System.Collections.Generic import Dictionary, List
        from System.Reflection import BindingFlags
        from Newtonsoft.Json import JsonConvert

        # 将类型绑定到全局变量，使其对外可见
        globals().update(
            {
                "LegacyHelper": LegacyHelper,
                "ProcessorWorkingBeatmap": ProcessorWorkingBeatmap,
                "ProcessorCommand": ProcessorCommand,
                "IBeatmap": IBeatmap,
                "BeatmapExtensions": BeatmapExtensions,
                "SettingSourceExtensions": SettingSourceExtensions,
                "SettingSourceAttribute": SettingSourceAttribute,
                "Ruleset": Ruleset,
                "Mod": Mod,
                "ModClassic": ModClassic,
                "HitResult": HitResult,
                "DifficultyHitObject": DifficultyHitObject,
                "OsuRuleset": OsuRuleset,
                "OsuDifficultyAttributes": OsuDifficultyAttributes,
                "OsuPerformanceAttributes": OsuPerformanceAttributes,
                "Aim": Aim,
                "Speed": Speed,
                "OsuModClassic": OsuModClassic,
                "Slider": Slider,
                "SliderTick": SliderTick,
                "SliderRepeat": SliderRepeat,
                "OsuDifficultyHitObject": OsuDifficultyHitObject,
                "CatchRuleset": CatchRuleset,
                "Droplet": Droplet,
                "TinyDroplet": TinyDroplet,
                "Fruit": Fruit,
                "JuiceStream": JuiceStream,
                "TaikoRuleset": TaikoRuleset,
                "ManiaRuleset": ManiaRuleset,
                "HoldNote": HoldNote,
                "ScoreInfo": ScoreInfo,
                "ModUtils": ModUtils,
                "System": System,
                "Array": Array,
                "OperationCanceledException": OperationCanceledException,
                "Dictionary": Dictionary,
                "List": List,
                "BindingFlags": BindingFlags,
                "JsonConvert": JsonConvert,
            },
        )

        _dotnet_libs_imported = True
