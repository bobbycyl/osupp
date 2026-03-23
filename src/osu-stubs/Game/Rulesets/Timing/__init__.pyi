from System import IComparable
from System import Object
from System import Type
from __future__ import annotations
from osu.Game.Beatmaps.ControlPoints import EffectControlPoint
from osu.Game.Beatmaps.ControlPoints import IControlPoint
from osu.Game.Beatmaps.ControlPoints import TimingControlPoint
from typing import Final
from typing import overload
class MultiplierControlPoint(Object, IComparable[MultiplierControlPoint], IControlPoint):
    """"""
    BaseBeatLength: Final[float] = ...
    """
    
    :return: 
    """
    EffectPoint: Final[EffectControlPoint] = ...
    """
    
    :return: 
    """
    TimingPoint: Final[TimingControlPoint] = ...
    """
    
    :return: 
    """
    Velocity: Final[float] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, time: float):
        """
        
        :param time: 
        """
    @property
    def Multiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def Time(self) -> float:
        """
        
        :return: 
        """
    @Time.setter
    def Time(self, value: float) -> None: ...
    def CompareTo(self, other: MultiplierControlPoint) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""