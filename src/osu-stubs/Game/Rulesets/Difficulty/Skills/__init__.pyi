from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IReadOnlyList
from System import IComparable
from System import Object
from System import Type
from System import ValueType
from __future__ import annotations
from abc import ABC
from osu.Game.Rulesets.Difficulty.Preprocessing import DifficultyHitObject
from osu.Game.Rulesets.Difficulty.Skills.VariableLengthStrainSkill import StrainPeak
class HarmonicSkill(ABC, Skill):
    """"""
    def CountTopWeightedObjectDifficulties(self, difficultyValue: float) -> float:
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
class Skill(ABC, Object):
    """"""
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
class StrainDecaySkill(ABC, StrainSkill):
    """"""
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
class StrainSkill(ABC, Skill):
    """"""
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
class VariableLengthStrainSkill(ABC, Skill):
    """"""
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
    class StrainPeak(ValueType, IComparable[VariableLengthStrainSkill.StrainPeak]):
        """"""
        def __init__(self, value: float, sectionLength: float):
            """"""
        @property
        def SectionLength(self) -> float:
            """"""
        @property
        def Value(self) -> float:
            """"""
        def CompareTo(self, other: VariableLengthStrainSkill.StrainPeak) -> int:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""