import os
import sys
from typing import Any, TYPE_CHECKING, cast

from clr_loader import get_coreclr
from pythonnet import set_runtime

# 内部状态变量，记录是否已加载
_runtime_initialized = False
_dotnet_libs_imported = False

if TYPE_CHECKING:
    from .stubs.PerformanceCalculator_stubs import (
        LegacyHelper as LegacyHelper,
        ProcessorWorkingBeatmap as ProcessorWorkingBeatmap,
        ProcessorCommand as ProcessorCommand,
    )

    # osu.Game 命名空间
    from .stubs.osu_stubs.Game.Beatmaps import (
        IBeatmap as IBeatmap,
        BeatmapExtensions as BeatmapExtensions,
    )
    from .stubs.osu_stubs.Game.Configuration import (
        SettingSourceExtensions as SettingSourceExtensions,
        SettingSourceAttribute as SettingSourceAttribute,
    )
    from .stubs.osu_stubs.Game.Rulesets import Ruleset as Ruleset
    from .stubs.osu_stubs.Game.Rulesets.Mods import Mod as Mod, ModClassic as ModClassic
    from .stubs.osu_stubs.Game.Rulesets.Scoring import HitResult as HitResult
    from .stubs.osu_stubs.Game.Rulesets.Objects import HitObject as HitObject
    from .stubs.osu_stubs.Game.Rulesets.Difficulty.Preprocessing import (
        DifficultyHitObject as DifficultyHitObject,
    )

    # osu.Game.Rulesets.Osu 命名空间
    from .stubs.osu_stubs.Game.Rulesets.Osu import OsuRuleset as OsuRuleset
    from .stubs.osu_stubs.Game.Rulesets.Osu.Difficulty import (
        OsuDifficultyAttributes as OsuDifficultyAttributes,
        OsuPerformanceAttributes as OsuPerformanceAttributes,
    )
    from .stubs.osu_stubs.Game.Rulesets.Osu.Difficulty.Skills import (
        Aim as Aim,
        Speed as Speed,
    )
    from .stubs.osu_stubs.Game.Rulesets.Osu.Mods import OsuModClassic as OsuModClassic
    from .stubs.osu_stubs.Game.Rulesets.Osu.Objects import (
        Slider as Slider,
        SliderTick as SliderTick,
        SliderRepeat as SliderRepeat,
    )
    from .stubs.osu_stubs.Game.Rulesets.Osu.Difficulty.Preprocessing import (
        OsuDifficultyHitObject as OsuDifficultyHitObject,
    )

    # osu.Game.Rulesets.Taiko 命名空间
    from .stubs.osu_stubs.Game.Rulesets.Taiko import TaikoRuleset as TaikoRuleset

    # osu.Game.Rulesets.Catch 命名空间
    from .stubs.osu_stubs.Game.Rulesets.Catch import CatchRuleset as CatchRuleset
    from .stubs.osu_stubs.Game.Rulesets.Catch.Objects import (
        Droplet as Droplet,
        TinyDroplet as TinyDroplet,
        Fruit as Fruit,
        JuiceStream as JuiceStream,
    )

    # osu.Game.Rulesets.Mania 命名空间
    from .stubs.osu_stubs.Game.Rulesets.Mania import ManiaRuleset as ManiaRuleset
    from .stubs.osu_stubs.Game.Rulesets.Mania.Objects import HoldNote as HoldNote
    from .stubs.osu_stubs.Game.Scoring import ScoreInfo as ScoreInfo
    from .stubs.osu_stubs.Game.Utils import ModUtils as ModUtils

    # 其他
    import System as System
    from System import (
        Array as Array,
        OperationCanceledException as _NetOperationCanceledException,
        ValueTuple as ValueTuple,
    )
    from System.Collections.Generic import Dictionary as Dictionary, List as List
    from System.Reflection import BindingFlags as BindingFlags

    # noinspection PyPep8Naming
    class JsonConvert:
        @staticmethod
        def SerializeObject(Object: Any) -> str: ...

    OperationCanceledException = cast(
        type[RuntimeError],
        cast(object, _NetOperationCanceledException),
    )


# noinspection PyUnresolvedReferences
def init_osu_tools(build_dir):
    global _runtime_initialized, _dotnet_libs_imported

    if not _runtime_initialized:
        runtime_config = os.path.join(
            build_dir,
            "PerformanceCalculator.runtimeconfig.json",
        )
        rt = get_coreclr(runtime_config=runtime_config)
        set_runtime(rt)
        sys.path.append(build_dir)

        _runtime_initialized = True

    if not _dotnet_libs_imported:
        import clr

        # 以下导入顺序非 alphabetic
        clr.AddReference("PerformanceCalculator")  # ty:ignore[unresolved-attribute]
        clr.AddReference("osu.Game")  # ty:ignore[unresolved-attribute]
        clr.AddReference("osu.Game.Rulesets.Osu")  # ty:ignore[unresolved-attribute]
        clr.AddReference("osu.Game.Rulesets.Taiko")  # ty:ignore[unresolved-attribute]
        clr.AddReference("osu.Game.Rulesets.Catch")  # ty:ignore[unresolved-attribute]
        clr.AddReference("osu.Game.Rulesets.Mania")  # ty:ignore[unresolved-attribute]
        clr.AddReference("Newtonsoft.Json")  # ty:ignore[unresolved-attribute]

        # PerformanceCalculator 命名空间
        from PerformanceCalculator import (
            LegacyHelper,
            ProcessorWorkingBeatmap,
            ProcessorCommand,
        )  # ty:ignore[unresolved-import]

        # osu.Game 命名空间
        from osu.Game.Beatmaps import (
            IBeatmap,
            BeatmapExtensions,
        )  # ty:ignore[unresolved-import]
        from osu.Game.Configuration import (
            SettingSourceExtensions,
            SettingSourceAttribute,
        )  # ty:ignore[unresolved-import]
        from osu.Game.Rulesets import Ruleset  # ty:ignore[unresolved-import]
        from osu.Game.Rulesets.Mods import (
            Mod,
            ModClassic,
        )  # ty:ignore[unresolved-import]
        from osu.Game.Rulesets.Scoring import HitResult  # ty:ignore[unresolved-import]
        from osu.Game.Rulesets.Objects import HitObject  # ty:ignore[unresolved-import]
        from osu.Game.Rulesets.Difficulty.Preprocessing import (
            DifficultyHitObject,
        )  # ty:ignore[unresolved-import]

        # osu.Game.Rulesets.Osu 命名空间
        from osu.Game.Rulesets.Osu import OsuRuleset  # ty:ignore[unresolved-import]
        from osu.Game.Rulesets.Osu.Difficulty import (
            OsuDifficultyAttributes,
            OsuPerformanceAttributes,
        )  # ty:ignore[unresolved-import]
        from osu.Game.Rulesets.Osu.Difficulty.Skills import (
            Aim,
            Speed,
        )  # ty:ignore[unresolved-import]
        from osu.Game.Rulesets.Osu.Mods import (
            OsuModClassic,
        )  # ty:ignore[unresolved-import]
        from osu.Game.Rulesets.Osu.Objects import (
            Slider,
            SliderTick,
            SliderRepeat,
        )  # ty:ignore[unresolved-import]
        from osu.Game.Rulesets.Osu.Difficulty.Preprocessing import (
            OsuDifficultyHitObject,
        )  # ty:ignore[unresolved-import]

        # osu.Game.Rulesets.Taiko 命名空间
        from osu.Game.Rulesets.Taiko import TaikoRuleset  # ty:ignore[unresolved-import]

        # osu.Game.Rulesets.Catch 命名空间
        from osu.Game.Rulesets.Catch import CatchRuleset  # ty:ignore[unresolved-import]
        from osu.Game.Rulesets.Catch.Objects import (
            Droplet,
            TinyDroplet,
            Fruit,
            JuiceStream,
        )  # ty:ignore[unresolved-import]

        # osu.Game.Rulesets.Mania 命名空间
        from osu.Game.Rulesets.Mania import ManiaRuleset  # ty:ignore[unresolved-import]
        from osu.Game.Rulesets.Mania.Objects import (
            HoldNote,
        )  # ty:ignore[unresolved-import]
        from osu.Game.Scoring import ScoreInfo  # ty:ignore[unresolved-import]
        from osu.Game.Utils import ModUtils  # ty:ignore[unresolved-import]

        # 其他
        import System
        from System import Array, OperationCanceledException, ValueTuple
        from System.Collections.Generic import Dictionary, List
        from System.Reflection import BindingFlags
        from Newtonsoft.Json import JsonConvert  # ty:ignore[unresolved-import]

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
                "HitObject": HitObject,
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
                "TaikoRuleset": TaikoRuleset,
                "CatchRuleset": CatchRuleset,
                "Droplet": Droplet,
                "TinyDroplet": TinyDroplet,
                "Fruit": Fruit,
                "JuiceStream": JuiceStream,
                "ManiaRuleset": ManiaRuleset,
                "HoldNote": HoldNote,
                "ScoreInfo": ScoreInfo,
                "ModUtils": ModUtils,
                "System": System,
                "Array": Array,
                "OperationCanceledException": OperationCanceledException,
                "ValueTuple": ValueTuple,
                "Dictionary": Dictionary,
                "List": List,
                "BindingFlags": BindingFlags,
                "JsonConvert": JsonConvert,
            },
        )

        _dotnet_libs_imported = True
