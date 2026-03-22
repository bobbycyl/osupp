from System.Collections.Generic import IEnumerable
from System import Object
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Game.Rulesets.Mania.Objects import ManiaHitObject
from typing import overload
class Pattern(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def ColumnWithObjects(self) -> int:
        """
        
        :return: 
        """
    @property
    def HitObjects(self) -> IEnumerable[ManiaHitObject]:
        """
        
        :return: 
        """
    @overload
    def Add(self, other: Pattern) -> None:
        """
        
        :param other: 
        """
    @overload
    def Add(self, hitObject: ManiaHitObject) -> None:
        """
        
        :param hitObject: 
        """
    def Clear(self) -> None:
        """"""
    def ColumnHasObject(self, column: int) -> bool:
        """
        
        :param column: 
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
class PatternGenerator(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Generate(self) -> IEnumerable[Pattern]:
        """
        
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""