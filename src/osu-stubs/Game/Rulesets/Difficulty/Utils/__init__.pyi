from System import Array
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEnumerator
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System import IDisposable
from System import Object
from System import Type
from System import ValueType
from __future__ import annotations
from abc import ABC
from typing import Generic
from typing import Iterator
from typing import TypeVar
from typing import overload
T = TypeVar("T")
class DifficultyCalculationUtils(ABC, Object):
    """"""
    @classmethod
    def BPMToMilliseconds(cls, bpm: float, delimiter: int = ...) -> float:
        """
        
        :param bpm: 
        :param delimiter: 
        :return: 
        """
    @classmethod
    def BellCurve(cls, x: float, mean: float, width: float, multiplier: float = ...) -> float:
        """
        
        :param x: 
        :param mean: 
        :param width: 
        :param multiplier: 
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def Erf(cls, x: float) -> float:
        """
        
        :param x: 
        :return: 
        """
    @classmethod
    def ErfInv(cls, x: float) -> float:
        """
        
        :param x: 
        :return: 
        """
    @classmethod
    def Erfc(cls, x: float) -> float:
        """
        
        :param x: 
        :return: 
        """
    @classmethod
    def ErfcInv(cls, x: float) -> float:
        """
        
        :param x: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def Logistic(cls, exponent: float, maxValue: float = ...) -> float:
        """
        
        :param exponent: 
        :param maxValue: 
        :return: 
        """
    @classmethod
    @overload
    def Logistic(cls, x: float, midpointOffset: float, multiplier: float, maxValue: float = ...) -> float:
        """
        
        :param x: 
        :param midpointOffset: 
        :param multiplier: 
        :param maxValue: 
        :return: 
        """
    @classmethod
    def MillisecondsToBPM(cls, ms: float, delimiter: int = ...) -> float:
        """
        
        :param ms: 
        :param delimiter: 
        :return: 
        """
    @classmethod
    def Norm(cls, p: float, values: Array[float]) -> float:
        """
        
        :param p: 
        :param values: 
        :return: 
        """
    @classmethod
    def ReverseLerp(cls, x: float, start: float, end: float) -> float:
        """
        
        :param x: 
        :param start: 
        :param end: 
        :return: 
        """
    @classmethod
    def Smootherstep(cls, x: float, start: float, end: float) -> float:
        """
        
        :param x: 
        :param start: 
        :param end: 
        :return: 
        """
    @classmethod
    def Smoothstep(cls, x: float, start: float, end: float) -> float:
        """
        
        :param x: 
        :param start: 
        :param end: 
        :return: 
        """
    @classmethod
    def SmoothstepBellCurve(cls, x: float, mean: float = ..., width: float = ...) -> float:
        """
        
        :param x: 
        :param mean: 
        :param width: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class ReverseQueue(Generic[T], Object, IEnumerable[T], IEnumerable):
    """"""
    def __init__(self, initialCapacity: int):
        """
        
        :param initialCapacity: 
        """
    @property
    def Count(self) -> int:
        """
        
        :return: 
        """
    def Clear(self) -> None:
        """"""
    def Dequeue(self) -> T:
        """
        
        :return: 
        """
    def Enqueue(self, item: T) -> None:
        """
        
        :param item: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __getitem__(self, index: int) -> T:
        """
        
        :param index: 
        :return: 
        """
    def __iter__(self) -> Iterator[T]:
        """"""
    def __len__(self) -> int:
        """
        
        :return: 
        """
    class Enumerator(Generic[T], ValueType, IEnumerator[T], IEnumerator, IDisposable):
        """"""
        @property
        def Current(self) -> T:
            """"""
        def Dispose(self) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def MoveNext(self) -> bool:
            """"""
        def Reset(self) -> None:
            """"""
        def ToString(self) -> str:
            """"""