from System import Array
from System.Collections.Generic import IComparer
from System import Object
from System import Type
from __future__ import annotations
from abc import ABC
from typing import Generic
from typing import TypeVar
T = TypeVar("T")
class LegacySortHelper(ABC, Generic[T], Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Sort(cls, keys: Array[T], comparer: IComparer[T]) -> None:
        """
        
        :param keys: 
        :param comparer: 
        """
    def ToString(self) -> str:
        """"""