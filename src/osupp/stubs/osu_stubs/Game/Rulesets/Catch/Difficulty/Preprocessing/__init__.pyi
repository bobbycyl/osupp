from System.Collections.Generic import List
from System import Type
from __future__ import annotations
from osu.Game.Rulesets.Catch.Objects import PalpableCatchHitObject
from osu.Game.Rulesets.Difficulty.Preprocessing import DifficultyHitObject
from osu.Game.Rulesets.Objects import HitObject
from typing import ClassVar
from typing import Final
class CatchDifficultyHitObject(DifficultyHitObject):
    """"""
    BaseObject: Final[HitObject] = ...
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
    LastNormalizedPosition: Final[float] = ...
    """
    
    :return: 
    """
    LastObject: Final[HitObject] = ...
    """
    
    :return: 
    """
    NORMALIZED_HALF_CATCHER_WIDTH: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    NormalizedPosition: Final[float] = ...
    """
    
    :return: 
    """
    StartTime: Final[float] = ...
    """
    
    :return: 
    """
    StrainTime: Final[float] = ...
    """
    
    :return: 
    """
    def __init__(self, hitObject: HitObject, lastObject: HitObject, clockRate: float, halfCatcherWidth: float, objects: List[DifficultyHitObject], index: int):
        """
        
        :param hitObject: 
        :param lastObject: 
        :param clockRate: 
        :param halfCatcherWidth: 
        :param objects: 
        :param index: 
        """
    @property
    def BaseObject(self) -> PalpableCatchHitObject:
        """
        
        :return: 
        """
    @property
    def DistanceMoved(self) -> float:
        """
        
        :return: 
        """
    @property
    def ExactDistanceMoved(self) -> float:
        """
        
        :return: 
        """
    @property
    def LastObject(self) -> PalpableCatchHitObject:
        """
        
        :return: 
        """
    @property
    def LastPlayerPosition(self) -> float:
        """
        
        :return: 
        """
    @property
    def PlayerPosition(self) -> float:
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
    def Previous(self, backwardsIndex: int) -> DifficultyHitObject:
        """
        
        :param backwardsIndex: 
        :return: 
        """
    def ToString(self) -> str:
        """"""