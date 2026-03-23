from System.Collections.Generic import List
from System import Object
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Game.Rulesets.Taiko.Difficulty.Preprocessing.Rhythm.Data import SamePatternsGroupedHitObjects
from osu.Game.Rulesets.Taiko.Difficulty.Preprocessing.Rhythm.Data import SameRhythmHitObjectGrouping
from osu.Game.Rulesets.Taiko.Difficulty.Preprocessing import TaikoDifficultyHitObject
from typing import Final
class TaikoRhythmData(Object):
    """"""
    Ratio: Final[float] = ...
    """
    
    :return: 
    """
    SamePatternsGroupedHitObjects: Final[SamePatternsGroupedHitObjects] = ...
    """
    
    :return: 
    """
    SameRhythmGroupedHitObjects: Final[SameRhythmHitObjectGrouping] = ...
    """
    
    :return: 
    """
    def __init__(self, current: TaikoDifficultyHitObject):
        """
        
        :param current: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class TaikoRhythmDifficultyPreprocessor(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ProcessAndAssign(cls, hitObjects: List[TaikoDifficultyHitObject]) -> None:
        """
        
        :param hitObjects: 
        """
    def ToString(self) -> str:
        """"""