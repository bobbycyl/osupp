from System.Collections.Generic import List
from System import Object
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Game.Rulesets.Difficulty.Preprocessing import DifficultyHitObject
from osu.Game.Rulesets.Taiko.Difficulty.Preprocessing.Colour.Data import AlternatingMonoPattern
from osu.Game.Rulesets.Taiko.Difficulty.Preprocessing.Colour.Data import MonoStreak
from osu.Game.Rulesets.Taiko.Difficulty.Preprocessing.Colour.Data import RepeatingHitPatterns
from osu.Game.Rulesets.Taiko.Difficulty.Preprocessing import TaikoDifficultyHitObject
from typing import Final
class TaikoColourData(Object):
    """"""
    AlternatingMonoPattern: Final[AlternatingMonoPattern] = ...
    """
    
    :return: 
    """
    MonoStreak: Final[MonoStreak] = ...
    """
    
    :return: 
    """
    RepeatingHitPattern: Final[RepeatingHitPatterns] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def NextColourChange(self) -> TaikoDifficultyHitObject:
        """
        
        :return: 
        """
    @property
    def PreviousColourChange(self) -> TaikoDifficultyHitObject:
        """
        
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
class TaikoColourDifficultyPreprocessor(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ProcessAndAssign(cls, hitObjects: List[DifficultyHitObject]) -> None:
        """
        
        :param hitObjects: 
        """
    def ToString(self) -> str:
        """"""