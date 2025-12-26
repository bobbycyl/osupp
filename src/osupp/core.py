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
        clr.AddReference("Newtonsoft.Json")

        from PerformanceCalculator import ProcessorWorkingBeatmap, ProcessorCommand
        from osu.Game.Beatmaps import IBeatmap, BeatmapExtensions
        from osu.Game.Rulesets import Ruleset
        from osu.Game.Rulesets.Mods import Mod
        from osu.Game.Rulesets.Scoring import HitResult
        from osu.Game.Rulesets.Osu import OsuRuleset
        from osu.Game.Rulesets.Osu.Difficulty import OsuDifficultyAttributes, OsuPerformanceAttributes
        from osu.Game.Rulesets.Osu.Mods import OsuModClassic
        from osu.Game.Rulesets.Osu.Objects import Slider, SliderTick, SliderRepeat
        from osu.Game.Scoring import ScoreInfo
        from System import Array, OperationCanceledException
        from System.Collections.Generic import Dictionary
        from Newtonsoft.Json import JsonConvert

        # 将类型绑定到全局变量，使其对外可见
        globals().update(
            {
                "ProcessorWorkingBeatmap": ProcessorWorkingBeatmap,
                "ProcessorCommand": ProcessorCommand,
                "IBeatmap": IBeatmap,
                "BeatmapExtensions": BeatmapExtensions,
                "Ruleset": Ruleset,
                "Mod": Mod,
                "HitResult": HitResult,
                "OsuRuleset": OsuRuleset,
                "OsuDifficultyAttributes": OsuDifficultyAttributes,
                "OsuPerformanceAttributes": OsuPerformanceAttributes,
                "OsuModClassic": OsuModClassic,
                "Slider": Slider,
                "SliderTick": SliderTick,
                "SliderRepeat": SliderRepeat,
                "ScoreInfo": ScoreInfo,
                "Array": Array,
                "OperationCanceledException": OperationCanceledException,
                "Dictionary": Dictionary,
                "JsonConvert": JsonConvert,
            },
        )

        _dotnet_libs_imported = True
