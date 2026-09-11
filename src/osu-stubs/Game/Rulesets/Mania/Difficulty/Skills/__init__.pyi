from System import Array
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IReadOnlyList
from System import Type
from __future__ import annotations
from osu.Game.Rulesets.Difficulty.Preprocessing import DifficultyHitObject
from osu.Game.Rulesets.Difficulty.Skills import StrainDecaySkill
from osu.Game.Rulesets.Mods import Mod
class Strain(StrainDecaySkill):
    """"""
    def __init__(self, mods: Array[Mod], totalColumns: int):
        """
        
        :param mods: 
        :param totalColumns: 
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