from System.Collections.Generic import IReadOnlyList
from System import Object
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Game.Rulesets.Difficulty.Preprocessing import DifficultyHitObject
from osu.Game.Rulesets.Mods import Mod
class AimEvaluator(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def EvaluateDifficultyOf(cls, current: DifficultyHitObject, withSliderTravelDistance: bool) -> float:
        """
        
        :param current: 
        :param withSliderTravelDistance: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class FlashlightEvaluator(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def EvaluateDifficultyOf(cls, current: DifficultyHitObject, hidden: bool) -> float:
        """
        
        :param current: 
        :param hidden: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class RhythmEvaluator(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def EvaluateDifficultyOf(cls, current: DifficultyHitObject) -> float:
        """
        
        :param current: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class SpeedEvaluator(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def EvaluateDifficultyOf(cls, current: DifficultyHitObject, mods: IReadOnlyList[Mod]) -> float:
        """
        
        :param current: 
        :param mods: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""