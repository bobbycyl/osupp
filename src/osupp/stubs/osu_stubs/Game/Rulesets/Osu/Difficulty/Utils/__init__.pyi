from System.Collections.Generic import IReadOnlyCollection
from System import Object
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Game.Beatmaps import IBeatmap
class LegacyScoreUtils(ABC, Object):
    """"""
    @classmethod
    def CalculateDifficultyPeppyStars(cls, beatmap: IBeatmap) -> int:
        """
        
        :param beatmap: 
        :return: 
        """
    @classmethod
    def CalculateNestedScorePerObject(cls, beatmap: IBeatmap, objectCount: int) -> float:
        """
        
        :param beatmap: 
        :param objectCount: 
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
class OsuStrainUtils(ABC, Object):
    """"""
    @classmethod
    def CountTopWeightedSliders(cls, sliderStrains: IReadOnlyCollection[float], difficultyValue: float) -> float:
        """
        
        :param sliderStrains: 
        :param difficultyValue: 
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