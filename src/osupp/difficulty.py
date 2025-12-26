from typing import Optional

from .core import Array, OperationCanceledException, OsuRuleset, ProcessorCommand, ProcessorWorkingBeatmap
from .util import Result, re_deserialize


def calculate_osu_difficulty(beatmap_path: str, mods: Optional[list[str]] = None, mod_options: Optional[list[str]] = None) -> Result:
    working_beatmap = ProcessorWorkingBeatmap(beatmap_path)
    ruleset = OsuRuleset()
    calculator = ruleset.CreateDifficultyCalculator(working_beatmap)

    if mods is None:
        mods = []
    if mod_options is None:
        mod_options = []
    mod_array = ProcessorCommand.ParseMods(ruleset, Array[str](mods), Array[str](mod_options))

    try:
        return re_deserialize(calculator.Calculate(mod_array))
    except OperationCanceledException:
        return Result({})
