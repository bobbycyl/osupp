from System import Object
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Game.Rulesets.Difficulty.Preprocessing import DifficultyHitObject
class MovementEvaluator(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def EvaluateDifficultyOf(cls, current: DifficultyHitObject, catcherSpeedMultiplier: float) -> float:
        """
        
        :param current: 
        :param catcherSpeedMultiplier: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""