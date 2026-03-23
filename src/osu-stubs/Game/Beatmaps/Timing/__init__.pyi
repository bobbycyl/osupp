from System import IComparable
from System import IEquatable
from System import Object
from System import Type
from __future__ import annotations
from typing import ClassVar
from typing import Final
from typing import overload
class BreakPeriod(Object, IComparable[BreakPeriod], IEquatable[BreakPeriod]):
    """"""
    GAP_AFTER_BREAK: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    GAP_BEFORE_BREAK: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    MIN_BREAK_DURATION: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    MIN_GAP_DURATION: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    def __init__(self, startTime: float, endTime: float):
        """
        
        :param startTime: 
        :param endTime: 
        """
    @property
    def Duration(self) -> float:
        """
        
        :return: 
        """
    @property
    def EndTime(self) -> float:
        """
        
        :return: 
        """
    @property
    def HasEffect(self) -> bool:
        """
        
        :return: 
        """
    @property
    def StartTime(self) -> float:
        """
        
        :return: 
        """
    def CompareTo(self, other: BreakPeriod) -> int:
        """"""
    def Contains(self, time: float) -> bool:
        """
        
        :param time: 
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: BreakPeriod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersects(self, other: BreakPeriod) -> bool:
        """
        
        :param other: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    def __contains__(self, time: float) -> bool:
        """
        
        :param time: 
        :return: 
        """
class TimeSignature(Object, IEquatable[TimeSignature]):
    """"""
    def __init__(self, numerator: int):
        """
        
        :param numerator: 
        """
    @property
    def Numerator(self) -> int:
        """
        
        :return: 
        """
    SimpleQuadruple: Final[ClassVar[TimeSignature]] = ...
    """
    
    :return: 
    """
    SimpleTriple: Final[ClassVar[TimeSignature]] = ...
    """
    
    :return: 
    """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: TimeSignature) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""