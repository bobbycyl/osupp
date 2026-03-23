from System import Object
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Game.Rulesets.Difficulty.Preprocessing import DifficultyHitObject
from osu.Game.Rulesets.Taiko.Difficulty.Preprocessing import TaikoDifficultyHitObject
class ColourEvaluator(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def EvaluateDifficultyOf(cls, hitObject: DifficultyHitObject) -> float:
        """
        
        :param hitObject: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class ReadingEvaluator(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def EvaluateDifficultyOf(cls, noteObject: TaikoDifficultyHitObject) -> float:
        """
        
        :param noteObject: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class RhythmEvaluator(Object):
    """"""
    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def EvaluateDifficultyOf(cls, hitObject: DifficultyHitObject, hitWindow: float) -> float:
        """
        
        :param hitObject: 
        :param hitWindow: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class StaminaEvaluator(ABC, Object):
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