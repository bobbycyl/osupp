import os
import sys

from clr_loader import get_coreclr
from pythonnet import set_runtime

home_dir = os.environ.get("OSU_TOOLS_HOME")
if home_dir is None:
    raise ValueError("'OSU_TOOLS_HOME' environment variable not set")
cli_build_dir = os.path.join(
    home_dir,
    "PerformanceCalculator",
    "bin",
    "Release",
    "net8.0",
)
gui_build_dir = os.path.join(
    home_dir,
    "PerformanceCalculatorGUI",
    "bin",
    "Release",
    "net8.0",
)
runtime_config = os.path.join(
    cli_build_dir,
    "PerformanceCalculator.runtimeconfig.json",
)
rt = get_coreclr(runtime_config=runtime_config)
set_runtime(rt)
sys.path.append(cli_build_dir)
sys.path.append(gui_build_dir)

import clr  # noqa: E402

# 以下导入顺序非 alphabetic
clr.AddReference("PerformanceCalculator")  # ty:ignore[unresolved-attribute]
clr.AddReference("PerformanceCalculatorGUI")  # ty:ignore[unresolved-attribute]
clr.AddReference("osu.Game")  # ty:ignore[unresolved-attribute]
clr.AddReference("osu.Game.Rulesets.Osu")  # ty:ignore[unresolved-attribute]
clr.AddReference("osu.Game.Rulesets.Taiko")  # ty:ignore[unresolved-attribute]
clr.AddReference("osu.Game.Rulesets.Catch")  # ty:ignore[unresolved-attribute]
clr.AddReference("osu.Game.Rulesets.Mania")  # ty:ignore[unresolved-attribute]
clr.AddReference("Newtonsoft.Json")  # ty:ignore[unresolved-attribute]
