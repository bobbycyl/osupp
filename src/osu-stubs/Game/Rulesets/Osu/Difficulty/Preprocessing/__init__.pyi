from System.Collections.Generic import List
from System import Type
from __future__ import annotations
from osu.Game.Rulesets.Difficulty.Preprocessing import DifficultyHitObject
from osu.Game.Rulesets.Objects import HitObject
from osuTK import Vector2
from typing import ClassVar
from typing import Final
from typing import Optional
class OsuDifficultyHitObject(DifficultyHitObject):
    """"""
    AdjustedDeltaTime: Final[float] = ...
    """
    
    :return: 
    """
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
    LastObject: Final[HitObject] = ...
    """
    
    :return: 
    """
    MIN_DELTA_TIME: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    NORMALISED_DIAMETER: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    NORMALISED_RADIUS: Final[ClassVar[int]] = ...
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
    @property
    def Angle(self) -> Optional[float]:
        """
        
        :return: 
        """
    @property
    def HitWindowGreat(self) -> float:
        """
        
        :return: 
        """
    @property
    def LazyEndPosition(self) -> Optional[Vector2]:
        """
        
        :return: 
        """
    @property
    def LazyJumpDistance(self) -> float:
        """
        
        :return: 
        """
    @property
    def LazyTravelDistance(self) -> float:
        """
        
        :return: 
        """
    @property
    def LazyTravelTime(self) -> float:
        """
        
        :return: 
        """
    @property
    def MinimumJumpDistance(self) -> float:
        """
        
        :return: 
        """
    @property
    def MinimumJumpTime(self) -> float:
        """
        
        :return: 
        """
    @property
    def SmallCircleBonus(self) -> float:
        """
        
        :return: 
        """
    @property
    def TravelDistance(self) -> float:
        """
        
        :return: 
        """
    @property
    def TravelTime(self) -> float:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetDoubletapness(self, osuNextObj: OsuDifficultyHitObject) -> float:
        """
        
        :param osuNextObj: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Next(self, forwardsIndex: int) -> DifficultyHitObject:
        """
        
        :param forwardsIndex: 
        :return: 
        """
    def OpacityAt(self, time: float, hidden: bool) -> float:
        """
        
        :param time: 
        :param hidden: 
        :return: 
        """
    def Previous(self, backwardsIndex: int) -> DifficultyHitObject:
        """
        
        :param backwardsIndex: 
        :return: 
        """
    def ToString(self) -> str:
        """"""