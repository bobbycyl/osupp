from System.Collections.Generic import List
from System import Object
from System import Type
from __future__ import annotations
from osu.Game.Rulesets.Taiko.Difficulty.Preprocessing import TaikoDifficultyHitObject
from osu.Game.Rulesets.Taiko.Objects import HitType
from typing import Final
from typing import Optional
class AlternatingMonoPattern(Object):
    """"""
    Index: Final[int] = ...
    """
    
    :return: 
    """
    MonoStreaks: Final[List[MonoStreak]] = ...
    """
    
    :return: 
    """
    Parent: Final[RepeatingHitPatterns] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def FirstHitObject(self) -> TaikoDifficultyHitObject:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def HasIdenticalMonoLength(self, other: AlternatingMonoPattern) -> bool:
        """
        
        :param other: 
        :return: 
        """
    def IsRepetitionOf(self, other: AlternatingMonoPattern) -> bool:
        """
        
        :param other: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class MonoStreak(Object):
    """"""
    Index: Final[int] = ...
    """
    
    :return: 
    """
    Parent: Final[AlternatingMonoPattern] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def FirstHitObject(self) -> TaikoDifficultyHitObject:
        """
        
        :return: 
        """
    @property
    def HitObjects(self) -> List[TaikoDifficultyHitObject]:
        """
        
        :return: 
        """
    @property
    def HitType(self) -> Optional[HitType]:
        """
        
        :return: 
        """
    @property
    def LastHitObject(self) -> TaikoDifficultyHitObject:
        """
        
        :return: 
        """
    @property
    def RunLength(self) -> int:
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
class RepeatingHitPatterns(Object):
    """"""
    AlternatingMonoPatterns: Final[List[AlternatingMonoPattern]] = ...
    """
    
    :return: 
    """
    Previous: Final[RepeatingHitPatterns] = ...
    """
    
    :return: 
    """
    def __init__(self, previous: RepeatingHitPatterns):
        """
        
        :param previous: 
        """
    @property
    def FirstHitObject(self) -> TaikoDifficultyHitObject:
        """
        
        :return: 
        """
    @property
    def RepetitionInterval(self) -> int:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def FindRepetitionInterval(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""