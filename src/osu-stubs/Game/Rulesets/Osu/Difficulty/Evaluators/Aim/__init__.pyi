from System import Object
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Game.Rulesets.Difficulty.Preprocessing import DifficultyHitObject
class AgilityEvaluator(ABC, Object):
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
class FlowAimEvaluator(ABC, Object):
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
class SnapAimEvaluator(ABC, Object):
    """"""
    @classmethod
    def CalcAngleAcuteness(cls, angle: float) -> float:
        """
        
        :param angle: 
        :return: 
        """
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