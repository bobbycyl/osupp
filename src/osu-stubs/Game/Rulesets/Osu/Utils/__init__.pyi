from System.Collections.Generic import IEnumerable
from System.Collections.Generic import List
from System import Object
from System import Random
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Framework.Graphics.Primitives import RectangleF
from osu.Game.Rulesets.Osu.Beatmaps import OsuBeatmap
from osu.Game.Rulesets.Osu.Objects import OsuHitObject
from osu.Game.Rulesets.Osu.Objects import Slider
from osu.Game.Rulesets.Osu.Utils.OsuHitObjectGenerationUtils import ObjectPositionInfo
from osuTK import Vector2
class OsuHitObjectGenerationUtils(ABC, Object):
    """"""
    @classmethod
    def CalculatePossibleMovementBounds(cls, slider: Slider) -> RectangleF:
        """
        
        :param slider: 
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FlipSliderInPlaceHorizontally(cls, slider: Slider) -> None:
        """
        
        :param slider: 
        """
    @classmethod
    def GeneratePositionInfos(cls, hitObjects: IEnumerable[OsuHitObject]) -> List[OsuHitObjectGenerationUtils.ObjectPositionInfo]:
        """
        
        :param hitObjects: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsHitObjectOnBeat(cls, beatmap: OsuBeatmap, hitObject: OsuHitObject, downbeatsOnly: bool = ...) -> bool:
        """
        
        :param beatmap: 
        :param hitObject: 
        :param downbeatsOnly: 
        :return: 
        """
    @classmethod
    def RandomGaussian(cls, rng: Random, mean: float = ..., stdDev: float = ...) -> float:
        """
        
        :param rng: 
        :param mean: 
        :param stdDev: 
        :return: 
        """
    @classmethod
    def ReflectHorizontallyAlongPlayfield(cls, osuObject: OsuHitObject) -> None:
        """
        
        :param osuObject: 
        """
    @classmethod
    def ReflectVerticallyAlongPlayfield(cls, osuObject: OsuHitObject) -> None:
        """
        
        :param osuObject: 
        """
    @classmethod
    def RepositionHitObjects(cls, objectPositionInfos: IEnumerable[OsuHitObjectGenerationUtils.ObjectPositionInfo]) -> List[OsuHitObject]:
        """
        
        :param objectPositionInfos: 
        :return: 
        """
    @classmethod
    def RotateAwayFromEdge(cls, prevObjectPos: Vector2, posRelativeToPrev: Vector2, rotationRatio: float = ...) -> Vector2:
        """
        
        :param prevObjectPos: 
        :param posRelativeToPrev: 
        :param rotationRatio: 
        :return: 
        """
    @classmethod
    def RotateSlider(cls, slider: Slider, rotation: float) -> None:
        """
        
        :param slider: 
        :param rotation: 
        """
    @classmethod
    def RotateVectorTowardsVector(cls, initial: Vector2, destination: Vector2, rotationRatio: float) -> Vector2:
        """
        
        :param initial: 
        :param destination: 
        :param rotationRatio: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class ObjectPositionInfo(Object):
        """"""
        def __init__(self, hitObject: OsuHitObject):
            """"""
        @property
        def DistanceFromPrevious(self) -> float:
            """"""
        @DistanceFromPrevious.setter
        def DistanceFromPrevious(self, value: float) -> None: ...
        @property
        def HitObject(self) -> OsuHitObject:
            """"""
        @property
        def RelativeAngle(self) -> float:
            """"""
        @RelativeAngle.setter
        def RelativeAngle(self, value: float) -> None: ...
        @property
        def Rotation(self) -> float:
            """"""
        @Rotation.setter
        def Rotation(self, value: float) -> None: ...
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""