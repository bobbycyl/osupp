from System import Array
from System.Collections.Generic import List
from System import Type
from __future__ import annotations
from osu.Game.Rulesets.Difficulty.Preprocessing import DifficultyHitObject
from osu.Game.Rulesets.Mania.Objects import ManiaHitObject
from osu.Game.Rulesets.Objects import HitObject
from typing import Final
class ManiaDifficultyHitObject(DifficultyHitObject):
    """"""
    BaseObject: Final[HitObject] = ...
    """
    
    :return: 
    """
    Column: Final[int] = ...
    """
    
    :return: 
    """
    ColumnStrainTime: Final[float] = ...
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
    Index: Final[int] = ...
    """
    
    :return: 
    """
    LastObject: Final[HitObject] = ...
    """
    
    :return: 
    """
    PreviousHitObjects: Final[Array[ManiaDifficultyHitObject]] = ...
    """
    
    :return: 
    """
    StartTime: Final[float] = ...
    """
    
    :return: 
    """
    def __init__(self, hitObject: HitObject, lastObject: HitObject, clockRate: float, objects: List[DifficultyHitObject], perColumnObjects: Array[List[DifficultyHitObject]], index: int):
        """
        
        :param hitObject: 
        :param lastObject: 
        :param clockRate: 
        :param objects: 
        :param perColumnObjects: 
        :param index: 
        """
    @property
    def BaseObject(self) -> ManiaHitObject:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Next(self, forwardsIndex: int) -> DifficultyHitObject:
        """
        
        :param forwardsIndex: 
        :return: 
        """
    def NextInColumn(self, forwardsIndex: int) -> ManiaDifficultyHitObject:
        """
        
        :param forwardsIndex: 
        :return: 
        """
    def PrevInColumn(self, backwardsIndex: int) -> ManiaDifficultyHitObject:
        """
        
        :param backwardsIndex: 
        :return: 
        """
    def Previous(self, backwardsIndex: int) -> DifficultyHitObject:
        """
        
        :param backwardsIndex: 
        :return: 
        """
    def ToString(self) -> str:
        """"""