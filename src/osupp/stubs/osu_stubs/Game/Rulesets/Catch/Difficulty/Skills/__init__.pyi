from System import Array
from System.Collections.Generic import IEnumerable
from System import Type
from __future__ import annotations
from osu.Game.Rulesets.Difficulty.Preprocessing import DifficultyHitObject
from osu.Game.Rulesets.Difficulty.Skills import StrainDecaySkill
from osu.Game.Rulesets.Mods import Mod
class Movement(StrainDecaySkill):
    """"""
    def __init__(self, mods: Array[Mod], halfCatcherWidth: float, clockRate: float):
        """
        
        :param mods: 
        :param halfCatcherWidth: 
        :param clockRate: 
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
    def ToString(self) -> str:
        """"""