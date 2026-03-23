from System.Collections.Generic import IEnumerable
from System.Collections import IDictionary
from System import Enum
from System import Exception
from System.Reflection import MethodBase
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Game.Beatmaps import IBeatmap
from osu.Game.Rulesets.Mania.Beatmaps.Patterns import Pattern
from osu.Game.Rulesets.Mania.Beatmaps.Patterns import PatternGenerator
from osu.Game.Rulesets.Objects import HitObject
from osu.Game.Utils import LegacyRandom
from osuTK import Vector2
from typing import Final
class HitCirclePatternGenerator(LegacyPatternGenerator):
    """"""
    def __init__(self, random: LegacyRandom, hitObject: HitObject, beatmap: IBeatmap, totalColumns: int, previousPattern: Pattern, previousTime: float, previousPosition: Vector2, density: float, lastStair: PatternType):
        """
        
        :param random: 
        :param hitObject: 
        :param beatmap: 
        :param totalColumns: 
        :param previousPattern: 
        :param previousTime: 
        :param previousPosition: 
        :param density: 
        :param lastStair: 
        """
    @property
    def StairType(self) -> PatternType:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def Generate(self) -> IEnumerable[Pattern]:
        """
        
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class LegacyPatternGenerator(ABC, PatternGenerator):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Generate(self) -> IEnumerable[Pattern]:
        """
        
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    class NotEnoughColumnsException(Exception, ISerializable):
        """"""
        def __init__(self):
            """"""
        @property
        def Data(self) -> IDictionary:
            """"""
        @property
        def HResult(self) -> int:
            """"""
        @HResult.setter
        def HResult(self, value: int) -> None: ...
        @property
        def HelpLink(self) -> str:
            """"""
        @HelpLink.setter
        def HelpLink(self, value: str) -> None: ...
        @property
        def InnerException(self) -> Exception:
            """"""
        @property
        def Message(self) -> str:
            """"""
        @property
        def Source(self) -> str:
            """"""
        @Source.setter
        def Source(self, value: str) -> None: ...
        @property
        def StackTrace(self) -> str:
            """"""
        @property
        def TargetSite(self) -> MethodBase:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetBaseException(self) -> Exception:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
class PassThroughPatternGenerator(LegacyPatternGenerator):
    """"""
    def __init__(self, random: LegacyRandom, hitObject: HitObject, beatmap: IBeatmap, totalColumns: int, previousPattern: Pattern):
        """
        
        :param random: 
        :param hitObject: 
        :param beatmap: 
        :param totalColumns: 
        :param previousPattern: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def Generate(self) -> IEnumerable[Pattern]:
        """
        
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class PatternType(Enum):
    """"""
    _None: PatternType = ...
    """"""
    ForceStack: PatternType = ...
    """"""
    ForceNotStack: PatternType = ...
    """"""
    KeepSingle: PatternType = ...
    """"""
    LowProbability: PatternType = ...
    """"""
    Alternate: PatternType = ...
    """"""
    ForceSigSlider: PatternType = ...
    """"""
    ForceNotSlider: PatternType = ...
    """"""
    Gathered: PatternType = ...
    """"""
    Mirror: PatternType = ...
    """"""
    Reverse: PatternType = ...
    """"""
    Cycle: PatternType = ...
    """"""
    Stair: PatternType = ...
    """"""
    ReverseStair: PatternType = ...
    """"""
class SliderPatternGenerator(LegacyPatternGenerator):
    """"""
    EndTime: Final[int] = ...
    """
    
    :return: 
    """
    SegmentDuration: Final[int] = ...
    """
    
    :return: 
    """
    SpanCount: Final[int] = ...
    """
    
    :return: 
    """
    StartTime: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self, random: LegacyRandom, hitObject: HitObject, beatmap: IBeatmap, totalColumns: int, previousPattern: Pattern):
        """
        
        :param random: 
        :param hitObject: 
        :param beatmap: 
        :param totalColumns: 
        :param previousPattern: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def Generate(self) -> IEnumerable[Pattern]:
        """
        
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class SpinnerPatternGenerator(LegacyPatternGenerator):
    """"""
    def __init__(self, random: LegacyRandom, hitObject: HitObject, beatmap: IBeatmap, totalColumns: int, previousPattern: Pattern):
        """
        
        :param random: 
        :param hitObject: 
        :param beatmap: 
        :param totalColumns: 
        :param previousPattern: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def Generate(self) -> IEnumerable[Pattern]:
        """
        
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""