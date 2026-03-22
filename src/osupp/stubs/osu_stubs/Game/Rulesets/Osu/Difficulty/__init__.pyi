from System import Array
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IReadOnlyDictionary
from System.Collections.Generic import IReadOnlyList
from System.Collections.Generic import List
from System import Object
from System.Threading import CancellationToken
from System.Threading.Tasks import Task
from System import Type
from System import ValueTuple
from __future__ import annotations
from osu.Game.Beatmaps import IBeatmap
from osu.Game.Beatmaps import IBeatmapOnlineInfo
from osu.Game.Beatmaps import IWorkingBeatmap
from osu.Game.Rulesets.Difficulty import DifficultyAttributes
from osu.Game.Rulesets.Difficulty import DifficultyCalculator
from osu.Game.Rulesets.Difficulty import PerformanceAttributes
from osu.Game.Rulesets.Difficulty import PerformanceCalculator
from osu.Game.Rulesets.Difficulty import PerformanceDisplayAttribute
from osu.Game.Rulesets.Difficulty import TimedDifficultyAttributes
from osu.Game.Rulesets import IRulesetInfo
from osu.Game.Rulesets.Mods import Mod
from osu.Game.Rulesets.Scoring.Legacy import ILegacyScoreSimulator
from osu.Game.Rulesets.Scoring.Legacy import LegacyBeatmapConversionDifficultyInfo
from osu.Game.Rulesets.Scoring.Legacy import LegacyScoreAttributes
from osu.Game.Scoring import ScoreInfo
from typing import ClassVar
from typing import Final
from typing import Optional
from typing import overload
class OsuDifficultyAttributes(DifficultyAttributes):
    """"""
    def __init__(self):
        """"""
    @property
    def AimDifficultSliderCount(self) -> float:
        """
        
        :return: 
        """
    @AimDifficultSliderCount.setter
    def AimDifficultSliderCount(self, value: float) -> None: ...
    @property
    def AimDifficultStrainCount(self) -> float:
        """
        
        :return: 
        """
    @AimDifficultStrainCount.setter
    def AimDifficultStrainCount(self, value: float) -> None: ...
    @property
    def AimDifficulty(self) -> float:
        """
        
        :return: 
        """
    @AimDifficulty.setter
    def AimDifficulty(self, value: float) -> None: ...
    @property
    def AimTopWeightedSliderFactor(self) -> float:
        """
        
        :return: 
        """
    @AimTopWeightedSliderFactor.setter
    def AimTopWeightedSliderFactor(self, value: float) -> None: ...
    @property
    def DrainRate(self) -> float:
        """
        
        :return: 
        """
    @DrainRate.setter
    def DrainRate(self, value: float) -> None: ...
    @property
    def FlashlightDifficulty(self) -> float:
        """
        
        :return: 
        """
    @FlashlightDifficulty.setter
    def FlashlightDifficulty(self, value: float) -> None: ...
    @property
    def HitCircleCount(self) -> int:
        """
        
        :return: 
        """
    @HitCircleCount.setter
    def HitCircleCount(self, value: int) -> None: ...
    @property
    def LegacyScoreBaseMultiplier(self) -> float:
        """
        
        :return: 
        """
    @LegacyScoreBaseMultiplier.setter
    def LegacyScoreBaseMultiplier(self, value: float) -> None: ...
    @property
    def MaxCombo(self) -> int:
        """
        
        :return: 
        """
    @MaxCombo.setter
    def MaxCombo(self, value: int) -> None: ...
    @property
    def MaximumLegacyComboScore(self) -> float:
        """
        
        :return: 
        """
    @MaximumLegacyComboScore.setter
    def MaximumLegacyComboScore(self, value: float) -> None: ...
    @property
    def Mods(self) -> Array[Mod]:
        """
        
        :return: 
        """
    @Mods.setter
    def Mods(self, value: Array[Mod]) -> None: ...
    @property
    def NestedScorePerObject(self) -> float:
        """
        
        :return: 
        """
    @NestedScorePerObject.setter
    def NestedScorePerObject(self, value: float) -> None: ...
    @property
    def SliderCount(self) -> int:
        """
        
        :return: 
        """
    @SliderCount.setter
    def SliderCount(self, value: int) -> None: ...
    @property
    def SliderFactor(self) -> float:
        """
        
        :return: 
        """
    @SliderFactor.setter
    def SliderFactor(self, value: float) -> None: ...
    @property
    def SpeedDifficultStrainCount(self) -> float:
        """
        
        :return: 
        """
    @SpeedDifficultStrainCount.setter
    def SpeedDifficultStrainCount(self, value: float) -> None: ...
    @property
    def SpeedDifficulty(self) -> float:
        """
        
        :return: 
        """
    @SpeedDifficulty.setter
    def SpeedDifficulty(self, value: float) -> None: ...
    @property
    def SpeedNoteCount(self) -> float:
        """
        
        :return: 
        """
    @SpeedNoteCount.setter
    def SpeedNoteCount(self, value: float) -> None: ...
    @property
    def SpeedTopWeightedSliderFactor(self) -> float:
        """
        
        :return: 
        """
    @SpeedTopWeightedSliderFactor.setter
    def SpeedTopWeightedSliderFactor(self, value: float) -> None: ...
    @property
    def SpinnerCount(self) -> int:
        """
        
        :return: 
        """
    @SpinnerCount.setter
    def SpinnerCount(self, value: int) -> None: ...
    @property
    def StarRating(self) -> float:
        """
        
        :return: 
        """
    @StarRating.setter
    def StarRating(self, value: float) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def FromDatabaseAttributes(self, values: IReadOnlyDictionary[int, float], onlineInfo: IBeatmapOnlineInfo) -> None:
        """
        
        :param values: 
        :param onlineInfo: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ShouldSerializeFlashlightDifficulty(self) -> bool:
        """
        
        :return: 
        """
    def ToDatabaseAttributes(self) -> IEnumerable[ValueTuple, object]:
        """
        
        :return: 
        """
    def ToString(self) -> str:
        """"""
class OsuDifficultyCalculator(DifficultyCalculator):
    """"""
    def __init__(self, ruleset: IRulesetInfo, beatmap: IWorkingBeatmap):
        """
        
        :param ruleset: 
        :param beatmap: 
        """
    @property
    def Version(self) -> int:
        """
        
        :return: 
        """
    @overload
    def Calculate(self, cancellationToken: CancellationToken = ...) -> DifficultyAttributes:
        """
        
        :param cancellationToken: 
        :return: 
        """
    @overload
    def Calculate(self, mods: IEnumerable[Mod], cancellationToken: CancellationToken = ...) -> DifficultyAttributes:
        """
        
        :param mods: 
        :param cancellationToken: 
        :return: 
        """
    def CalculateAllLegacyCombinations(self, cancellationToken: CancellationToken = ...) -> IEnumerable[DifficultyAttributes]:
        """
        
        :param cancellationToken: 
        :return: 
        """
    @classmethod
    def CalculateRateAdjustedApproachRate(cls, approachRate: float, clockRate: float) -> float:
        """
        
        :param approachRate: 
        :param clockRate: 
        :return: 
        """
    @classmethod
    def CalculateRateAdjustedOverallDifficulty(cls, overallDifficulty: float, clockRate: float) -> float:
        """
        
        :param overallDifficulty: 
        :param clockRate: 
        :return: 
        """
    @overload
    def CalculateTimed(self, cancellationToken: CancellationToken = ...) -> List[TimedDifficultyAttributes]:
        """
        
        :param cancellationToken: 
        :return: 
        """
    @overload
    def CalculateTimed(self, mods: IEnumerable[Mod], cancellationToken: CancellationToken = ...) -> List[TimedDifficultyAttributes]:
        """
        
        :param mods: 
        :param cancellationToken: 
        :return: 
        """
    def CreateDifficultyAdjustmentModCombinations(self) -> Array[Mod]:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class OsuLegacyScoreMissCalculator(Object):
    """"""
    def __init__(self, scoreInfo: ScoreInfo, attributes: OsuDifficultyAttributes):
        """
        
        :param scoreInfo: 
        :param attributes: 
        """
    def Calculate(self) -> float:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class OsuLegacyScoreSimulator(Object, ILegacyScoreSimulator):
    """"""
    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLegacyScoreMultiplier(self, mods: IReadOnlyList[Mod], difficulty: LegacyBeatmapConversionDifficultyInfo) -> float:
        """
        
        :param mods: 
        :param difficulty: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def Simulate(self, workingBeatmap: IWorkingBeatmap, playableBeatmap: IBeatmap) -> LegacyScoreAttributes:
        """
        
        :param workingBeatmap: 
        :param playableBeatmap: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class OsuPerformanceAttributes(PerformanceAttributes):
    """"""
    def __init__(self):
        """"""
    @property
    def Accuracy(self) -> float:
        """
        
        :return: 
        """
    @Accuracy.setter
    def Accuracy(self, value: float) -> None: ...
    @property
    def Aim(self) -> float:
        """
        
        :return: 
        """
    @Aim.setter
    def Aim(self, value: float) -> None: ...
    @property
    def AimEstimatedSliderBreaks(self) -> float:
        """
        
        :return: 
        """
    @AimEstimatedSliderBreaks.setter
    def AimEstimatedSliderBreaks(self, value: float) -> None: ...
    @property
    def ComboBasedEstimatedMissCount(self) -> float:
        """
        
        :return: 
        """
    @ComboBasedEstimatedMissCount.setter
    def ComboBasedEstimatedMissCount(self, value: float) -> None: ...
    @property
    def EffectiveMissCount(self) -> float:
        """
        
        :return: 
        """
    @EffectiveMissCount.setter
    def EffectiveMissCount(self, value: float) -> None: ...
    @property
    def Flashlight(self) -> float:
        """
        
        :return: 
        """
    @Flashlight.setter
    def Flashlight(self, value: float) -> None: ...
    @property
    def ScoreBasedEstimatedMissCount(self) -> Optional[float]:
        """
        
        :return: 
        """
    @ScoreBasedEstimatedMissCount.setter
    def ScoreBasedEstimatedMissCount(self, value: Optional[float]) -> None: ...
    @property
    def Speed(self) -> float:
        """
        
        :return: 
        """
    @Speed.setter
    def Speed(self, value: float) -> None: ...
    @property
    def SpeedDeviation(self) -> Optional[float]:
        """
        
        :return: 
        """
    @SpeedDeviation.setter
    def SpeedDeviation(self, value: Optional[float]) -> None: ...
    @property
    def SpeedEstimatedSliderBreaks(self) -> float:
        """
        
        :return: 
        """
    @SpeedEstimatedSliderBreaks.setter
    def SpeedEstimatedSliderBreaks(self, value: float) -> None: ...
    @property
    def Total(self) -> float:
        """
        
        :return: 
        """
    @Total.setter
    def Total(self, value: float) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAttributesForDisplay(self) -> IEnumerable[PerformanceDisplayAttribute]:
        """
        
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class OsuPerformanceCalculator(PerformanceCalculator):
    """"""
    PERFORMANCE_BASE_MULTIPLIER: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @overload
    def Calculate(self, score: ScoreInfo, beatmap: IWorkingBeatmap) -> PerformanceAttributes:
        """
        
        :param score: 
        :param beatmap: 
        :return: 
        """
    @overload
    def Calculate(self, score: ScoreInfo, attributes: DifficultyAttributes) -> PerformanceAttributes:
        """
        
        :param score: 
        :param attributes: 
        :return: 
        """
    def CalculateAsync(self, score: ScoreInfo, attributes: DifficultyAttributes, cancellationToken: CancellationToken) -> Task[PerformanceAttributes]:
        """
        
        :param score: 
        :param attributes: 
        :param cancellationToken: 
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class OsuRatingCalculator(Object):
    """"""
    def __init__(self, mods: Array[Mod], totalHits: int, approachRate: float, overallDifficulty: float, mechanicalDifficultyRating: float, sliderFactor: float):
        """
        
        :param mods: 
        :param totalHits: 
        :param approachRate: 
        :param overallDifficulty: 
        :param mechanicalDifficultyRating: 
        :param sliderFactor: 
        """
    @classmethod
    def CalculateDifficultyRating(cls, difficultyValue: float) -> float:
        """
        
        :param difficultyValue: 
        :return: 
        """
    @classmethod
    def CalculateVisibilityBonus(cls, mods: Array[Mod], approachRate: float, visibilityFactor: float = ..., sliderFactor: float = ...) -> float:
        """
        
        :param mods: 
        :param approachRate: 
        :param visibilityFactor: 
        :param sliderFactor: 
        :return: 
        """
    def ComputeAimRating(self, aimDifficultyValue: float) -> float:
        """
        
        :param aimDifficultyValue: 
        :return: 
        """
    def ComputeFlashlightRating(self, flashlightDifficultyValue: float) -> float:
        """
        
        :param flashlightDifficultyValue: 
        :return: 
        """
    def ComputeSpeedRating(self, speedDifficultyValue: float) -> float:
        """
        
        :param speedDifficultyValue: 
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""