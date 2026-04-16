from System import Array
from System.Collections.Generic import IEnumerable
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Game.Rulesets.Difficulty.Preprocessing import DifficultyHitObject
from osu.Game.Rulesets.Difficulty.Skills import StrainSkill
from osu.Game.Rulesets.Mods import Mod
from typing import Final
class Aim(OsuStrainSkill):
    """"""
    IncludeSliders: Final[bool] = ...
    """
    
    :return: 
    """
    def __init__(self, mods: Array[Mod], includeSliders: bool):
        """
        
        :param mods: 
        :param includeSliders: 
        """
    def CountTopWeightedSliders(self) -> float:
        """
        
        :return: 
        """
    def CountTopWeightedStrains(self) -> float:
        """
        
        :return: 
        """
    def DifficultyValue(self) -> float:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetCurrentStrainPeaks(self) -> IEnumerable[float]:
        """
        
        :return: 
        """
    def GetDifficultSliders(self) -> float:
        """
        
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetObjectStrains(self) -> IEnumerable[float]:
        """
        
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def Process(self, current: DifficultyHitObject) -> None:
        """
        
        :param current: 
        """
    def ToString(self) -> str:
        """"""
class Flashlight(StrainSkill):
    """"""
    def __init__(self, mods: Array[Mod]):
        """
        
        :param mods: 
        """
    def CountTopWeightedStrains(self) -> float:
        """
        
        :return: 
        """
    @classmethod
    def DifficultyToPerformance(cls, difficulty: float) -> float:
        """
        
        :param difficulty: 
        :return: 
        """
    def DifficultyValue(self) -> float:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetCurrentStrainPeaks(self) -> IEnumerable[float]:
        """
        
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetObjectStrains(self) -> IEnumerable[float]:
        """
        
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def Process(self, current: DifficultyHitObject) -> None:
        """
        
        :param current: 
        """
    def ToString(self) -> str:
        """"""
class OsuStrainSkill(ABC, StrainSkill):
    """"""
    def CountTopWeightedStrains(self) -> float:
        """
        
        :return: 
        """
    @classmethod
    def DifficultyToPerformance(cls, difficulty: float) -> float:
        """
        
        :param difficulty: 
        :return: 
        """
    def DifficultyValue(self) -> float:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetCurrentStrainPeaks(self) -> IEnumerable[float]:
        """
        
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetObjectStrains(self) -> IEnumerable[float]:
        """
        
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def Process(self, current: DifficultyHitObject) -> None:
        """
        
        :param current: 
        """
    def ToString(self) -> str:
        """"""
class Speed(OsuStrainSkill):
    """"""
    def __init__(self, mods: Array[Mod]):
        """
        
        :param mods: 
        """
    def CountTopWeightedSliders(self) -> float:
        """
        
        :return: 
        """
    def CountTopWeightedStrains(self) -> float:
        """
        
        :return: 
        """
    def DifficultyValue(self) -> float:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetCurrentStrainPeaks(self) -> IEnumerable[float]:
        """
        
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetObjectStrains(self) -> IEnumerable[float]:
        """
        
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def Process(self, current: DifficultyHitObject) -> None:
        """
        
        :param current: 
        """
    def RelevantNoteCount(self) -> float:
        """
        
        :return: 
        """
    def ToString(self) -> str:
        """"""