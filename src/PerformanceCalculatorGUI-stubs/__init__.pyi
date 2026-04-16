from osu.Game.Rulesets.Osu.Difficulty import (
    OsuDifficultyCalculator,
)
from osu.Game.Rulesets.Taiko.Difficulty import (
    TaikoDifficultyCalculator,
)
from osu.Game.Rulesets.Catch.Difficulty import (
    CatchDifficultyCalculator,
)
from osu.Game.Rulesets.Mania.Difficulty import (
    ManiaDifficultyCalculator,
)
from System import Array
from osu.Game.Rulesets.Difficulty.Preprocessing import DifficultyHitObject
from osu.Game.Rulesets.Difficulty.Skills import Skill

class IExtendedDifficultyCalculator:
    def GetSkills(self) -> Array[Skill]: ...
    def GetDifficultyHitObjects(self) -> Array[DifficultyHitObject]: ...

class ExtendedOsuDifficultyCalculator(OsuDifficultyCalculator, IExtendedDifficultyCalculator): ...
class ExtendedTaikoDifficultyCalculator(TaikoDifficultyCalculator, IExtendedDifficultyCalculator): ...
class ExtendedCatchDifficultyCalculator(CatchDifficultyCalculator, IExtendedDifficultyCalculator): ...
class ExtendedManiaDifficultyCalculator(ManiaDifficultyCalculator, IExtendedDifficultyCalculator): ...
