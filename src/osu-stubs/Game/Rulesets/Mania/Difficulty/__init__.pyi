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
from typing import overload
class ManiaDifficultyAttributes(DifficultyAttributes):
    """"""
    def __init__(self):
        """"""
    @property
    def MaxCombo(self) -> int:
        """
        
        :return: 
        """
    @MaxCombo.setter
    def MaxCombo(self, value: int) -> None: ...
    @property
    def Mods(self) -> Array[Mod]:
        """
        
        :return: 
        """
    @Mods.setter
    def Mods(self, value: Array[Mod]) -> None: ...
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
    def ToDatabaseAttributes(self) -> IEnumerable[ValueTuple, object]:
        """
        
        :return: 
        """
    def ToString(self) -> str:
        """"""
class ManiaDifficultyCalculator(DifficultyCalculator):
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
class ManiaLegacyScoreSimulator(Object, ILegacyScoreSimulator):
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
class ManiaPerformanceAttributes(PerformanceAttributes):
    """"""
    def __init__(self):
        """"""
    @property
    def Difficulty(self) -> float:
        """
        
        :return: 
        """
    @Difficulty.setter
    def Difficulty(self, value: float) -> None: ...
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
class ManiaPerformanceCalculator(PerformanceCalculator):
    """"""
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