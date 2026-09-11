from System import Array
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IReadOnlyList
from System import Type
from __future__ import annotations
from osu.Game.Rulesets.Difficulty.Preprocessing import DifficultyHitObject
from osu.Game.Rulesets.Difficulty.Skills import HarmonicSkill
from osu.Game.Rulesets.Difficulty.Skills import StrainSkill
from osu.Game.Rulesets.Difficulty.Skills import VariableLengthStrainSkill
from osu.Game.Rulesets.Difficulty.Skills.VariableLengthStrainSkill import StrainPeak
from osu.Game.Rulesets.Mods import Mod
from typing import Final
class Aim(VariableLengthStrainSkill):
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
    def CountTopWeightedSliders(self, difficultyValue: float) -> float:
        """
        
        :param difficultyValue: 
        :return: 
        """
    def CountTopWeightedStrains(self, difficultyValue: float) -> float:
        """
        
        :param difficultyValue: 
        :return: 
        """
    def DifficultyValue(self) -> float:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetCurrentStrainPeaks(self) -> IEnumerable[VariableLengthStrainSkill.StrainPeak]:
        """
        
        :return: 
        """
    def GetDifficultSliders(self) -> float:
        """
        
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetObjectDifficulties(self) -> IReadOnlyList[float]:
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
    def __init__(self, mods: Array[Mod], totalObjects: int):
        """
        
        :param mods: 
        :param totalObjects: 
        """
    def CountTopWeightedStrains(self, difficultyValue: float) -> float:
        """
        
        :param difficultyValue: 
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
    def GetObjectDifficulties(self) -> IReadOnlyList[float]:
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
class Reading(HarmonicSkill):
    """"""
    def __init__(self, mods: Array[Mod]):
        """
        
        :param mods: 
        """
    def CountTopWeightedObjectDifficulties(self, difficultyValue: float) -> float:
        """
        
        :param difficultyValue: 
        :return: 
        """
    def DifficultyValue(self) -> float:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectDifficulties(self) -> IReadOnlyList[float]:
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
class Speed(HarmonicSkill):
    """"""
    def __init__(self, mods: Array[Mod]):
        """
        
        :param mods: 
        """
    def CountTopWeightedObjectDifficulties(self, difficultyValue: float) -> float:
        """
        
        :param difficultyValue: 
        :return: 
        """
    def CountTopWeightedSliders(self, difficultyValue: float) -> float:
        """
        
        :param difficultyValue: 
        :return: 
        """
    def DifficultyValue(self) -> float:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectDifficulties(self) -> IReadOnlyList[float]:
        """
        
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def Process(self, current: DifficultyHitObject) -> None:
        """
        
        :param current: 
        """
    def RelevantObjectCount(self) -> float:
        """
        
        :return: 
        """
    def ToString(self) -> str:
        """"""