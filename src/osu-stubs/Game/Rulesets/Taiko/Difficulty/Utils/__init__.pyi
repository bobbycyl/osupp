from System.Collections.Generic import Dictionary
from System.Collections.Generic import IReadOnlyList
from System.Collections.Generic import List
from System import Object
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Game.Rulesets.Taiko.Difficulty.Preprocessing import TaikoDifficultyHitObject
from typing import ClassVar
from typing import Final
from typing import TypeVar
T = TypeVar("T")
class DeltaTimeNormaliser(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Normalise(cls, hitObjects: IReadOnlyList[TaikoDifficultyHitObject], marginOfError: float) -> Dictionary[TaikoDifficultyHitObject, float]:
        """
        
        :param hitObjects: 
        :param marginOfError: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class IHasInterval:
    """"""
    @property
    def Interval(self) -> float:
        """
        
        :return: 
        """
class IntervalGroupingUtils(ABC, Object):
    """"""
    MARGIN_OF_ERROR: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GroupByInterval(cls, objects: IReadOnlyList[T]) -> List[List[T]]:
        """
        
        :param objects: 
        :return: 
        """
    def ToString(self) -> str:
        """"""