from System.Collections.Generic import List
from System import Object
from System import Type
from __future__ import annotations
from osu.Game.Rulesets.Objects import HitObject
from typing import Final
class DifficultyHitObject(Object):
    """"""
    BaseObject: Final[HitObject] = ...
    """
    
    :return: 
    """
    ClockRate: Final[float] = ...
    """
    
    :return: 
    """
    DeltaTime: Final[float] = ...
    """
    
    :return: 
    """
    EndTime: Final[float] = ...
    """
    
    :return: 
    """
    HitWindowGreat: Final[float] = ...
    """
    
    :return: 
    """
    Index: Final[int] = ...
    """
    
    :return: 
    """
    LastObject: Final[HitObject] = ...
    """
    
    :return: 
    """
    StartTime: Final[float] = ...
    """
    
    :return: 
    """
    def __init__(self, hitObject: HitObject, lastObject: HitObject, clockRate: float, objects: List[DifficultyHitObject], index: int):
        """
        
        :param hitObject: 
        :param lastObject: 
        :param clockRate: 
        :param objects: 
        :param index: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Next(self, skipCount: int = ...) -> DifficultyHitObject:
        """
        
        :param skipCount: 
        :return: 
        """
    def Previous(self, skipCount: int = ...) -> DifficultyHitObject:
        """
        
        :param skipCount: 
        :return: 
        """
    def ToString(self) -> str:
        """"""