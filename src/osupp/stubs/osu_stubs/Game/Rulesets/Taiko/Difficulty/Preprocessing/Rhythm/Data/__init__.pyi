from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IReadOnlyList
from System.Collections.Generic import List
from System import Object
from System import Type
from __future__ import annotations
from osu.Game.Rulesets.Taiko.Difficulty.Preprocessing import TaikoDifficultyHitObject
from osu.Game.Rulesets.Taiko.Difficulty.Utils import IHasInterval
from typing import Final
from typing import Optional
class SamePatternsGroupedHitObjects(Object):
    """"""
    def __init__(self, previous: SamePatternsGroupedHitObjects, groups: List[SameRhythmHitObjectGrouping]):
        """
        
        :param previous: 
        :param groups: 
        """
    @property
    def AllHitObjects(self) -> IEnumerable[TaikoDifficultyHitObject]:
        """
        
        :return: 
        """
    @property
    def FirstHitObject(self) -> TaikoDifficultyHitObject:
        """
        
        :return: 
        """
    @property
    def GroupInterval(self) -> float:
        """
        
        :return: 
        """
    @property
    def Groups(self) -> IReadOnlyList[SameRhythmHitObjectGrouping]:
        """
        
        :return: 
        """
    @property
    def IntervalRatio(self) -> float:
        """
        
        :return: 
        """
    @property
    def Previous(self) -> SamePatternsGroupedHitObjects:
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
class SameRhythmHitObjectGrouping(Object, IHasInterval):
    """"""
    HitObjectInterval: Final[Optional[float]] = ...
    """
    
    :return: 
    """
    HitObjectIntervalRatio: Final[float] = ...
    """
    
    :return: 
    """
    HitObjects: Final[List[TaikoDifficultyHitObject]] = ...
    """
    
    :return: 
    """
    Previous: Final[SameRhythmHitObjectGrouping] = ...
    """
    
    :return: 
    """
    def __init__(self, previous: SameRhythmHitObjectGrouping, hitObjects: List[TaikoDifficultyHitObject]):
        """
        
        :param previous: 
        :param hitObjects: 
        """
    @property
    def Duration(self) -> float:
        """
        
        :return: 
        """
    @property
    def FirstHitObject(self) -> TaikoDifficultyHitObject:
        """
        
        :return: 
        """
    @property
    def Interval(self) -> float:
        """
        
        :return: 
        """
    @property
    def StartTime(self) -> float:
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