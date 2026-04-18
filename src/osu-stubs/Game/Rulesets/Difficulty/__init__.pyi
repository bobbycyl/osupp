from System import Array
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IReadOnlyDictionary
from System.Collections.Generic import List
from System import IComparable
from System import IEquatable
from System import Object
from System.Threading import CancellationToken
from System.Threading.Tasks import Task
from System import Type
from System import ValueTuple
from __future__ import annotations
from abc import ABC
from osu.Framework.Graphics import Colour4
from osu.Framework.Localisation import LocalisableString
from osu.Game.Beatmaps import IBeatmapOnlineInfo
from osu.Game.Beatmaps import IWorkingBeatmap
from osu.Game.Rulesets.Difficulty.RulesetBeatmapAttribute import AdditionalMetric
from osu.Game.Rulesets.Mods import Mod
from osu.Game.Scoring import ScoreInfo
from typing import Final
from typing import Optional
from typing import Tuple
from typing import overload
class DifficultyAttributes(Object):
    """"""
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, mods: Array[Mod], starRating: float):
        """
        
        :param mods: 
        :param starRating: 
        """
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
class DifficultyCalculator(ABC, Object):
    """"""
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
class PerformanceAttributes(Object):
    """"""
    def __init__(self):
        """"""
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
class PerformanceBreakdown(Object):
    """"""
    def __init__(self, performance: PerformanceAttributes, perfectPerformance: PerformanceAttributes):
        """
        
        :param performance: 
        :param perfectPerformance: 
        """
    @property
    def PerfectPerformance(self) -> PerformanceAttributes:
        """
        
        :return: 
        """
    @PerfectPerformance.setter
    def PerfectPerformance(self, value: PerformanceAttributes) -> None: ...
    @property
    def Performance(self) -> PerformanceAttributes:
        """
        
        :return: 
        """
    @Performance.setter
    def Performance(self, value: PerformanceAttributes) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class PerformanceCalculator(ABC, Object):
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
class PerformanceDisplayAttribute(Object):
    """"""
    def __init__(self, propertyName: str, displayName: str, value: float):
        """
        
        :param propertyName: 
        :param displayName: 
        :param value: 
        """
    @property
    def DisplayName(self) -> str:
        """
        
        :return: 
        """
    @property
    def PropertyName(self) -> str:
        """
        
        :return: 
        """
    @property
    def Value(self) -> float:
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
class RulesetBeatmapAttribute(Object):
    """"""
    def __init__(self, label: LocalisableString, acronym: str, originalValue: float, adjustedValue: float, maxValue: float):
        """
        
        :param label: 
        :param acronym: 
        :param originalValue: 
        :param adjustedValue: 
        :param maxValue: 
        """
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AdditionalMetrics(self) -> Array[AdditionalMetric]:
        """
        
        :return: 
        """
    @AdditionalMetrics.setter
    def AdditionalMetrics(self, value: Array[AdditionalMetric]) -> None: ...
    @property
    def AdjustedValue(self) -> float:
        """
        
        :return: 
        """
    @property
    def Description(self) -> Optional[LocalisableString]:
        """
        
        :return: 
        """
    @Description.setter
    def Description(self, value: Optional[LocalisableString]) -> None: ...
    @property
    def Label(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def MaxValue(self) -> float:
        """
        
        :return: 
        """
    @property
    def OriginalValue(self) -> float:
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
    class AdditionalMetric(Object, IEquatable[RulesetBeatmapAttribute.AdditionalMetric]):
        """"""
        def __init__(self, Name: LocalisableString, Value: LocalisableString, Colour: Optional[Colour4] = ...):
            """"""
        @property
        def Colour(self) -> Optional[Colour4]:
            """"""
        @Colour.setter
        def Colour(self, value: Optional[Colour4]) -> None: ...
        @property
        def Name(self) -> LocalisableString:
            """"""
        @Name.setter
        def Name(self, value: LocalisableString) -> None: ...
        @property
        def Value(self) -> LocalisableString:
            """"""
        @Value.setter
        def Value(self, value: LocalisableString) -> None: ...
        def Deconstruct(self, Name: LocalisableString, Value: LocalisableString, Colour: Optional[Colour4]) -> Tuple[None, LocalisableString, LocalisableString, Optional[Colour4]]:
            """"""
        @overload
        def Equals(self, obj: object) -> bool:
            """"""
        @overload
        def Equals(self, other: RulesetBeatmapAttribute.AdditionalMetric) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __eq__(self, other: RulesetBeatmapAttribute.AdditionalMetric) -> bool:
            """"""
        def __ne__(self, other: RulesetBeatmapAttribute.AdditionalMetric) -> bool:
            """"""
        @classmethod
        def op_Equality(cls, left: RulesetBeatmapAttribute.AdditionalMetric, right: RulesetBeatmapAttribute.AdditionalMetric) -> bool:
            """"""
        @classmethod
        def op_Inequality(cls, left: RulesetBeatmapAttribute.AdditionalMetric, right: RulesetBeatmapAttribute.AdditionalMetric) -> bool:
            """"""
class TimedDifficultyAttributes(Object, IComparable[TimedDifficultyAttributes]):
    """"""
    Attributes: Final[DifficultyAttributes] = ...
    """
    
    :return: 
    """
    Time: Final[float] = ...
    """
    
    :return: 
    """
    def __init__(self, time: float, attributes: DifficultyAttributes):
        """
        
        :param time: 
        :param attributes: 
        """
    def CompareTo(self, other: TimedDifficultyAttributes) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""