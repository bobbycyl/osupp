from System import Array
from System.Collections.Generic import Dictionary
from System.Collections.Generic import IReadOnlyList
from System.Collections.Generic import List
from System import Enum
from System.IO import TextWriter
from System import Object
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Game.Beatmaps import Beatmap
from osu.Game.Beatmaps import IBeatmap
from osu.Game.IO import LineBufferedReader
from osu.Game.Rulesets import RulesetStore
from osu.Game.Skinning import ISkin
from osu.Game.Storyboards import Storyboard
from osuTK.Graphics import Color4
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import TypeVar
T = TypeVar("T")
TOutput = TypeVar("TOutput")
class Decoder(ABC, Generic[TOutput], Decoder):
    """"""
    def Decode(self, primaryStream: LineBufferedReader, otherStreams: Array[LineBufferedReader]) -> TOutput:
        """
        
        :param primaryStream: 
        :param otherStreams: 
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
class Decoder(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetDecoder(cls, stream: LineBufferedReader) -> Decoder[T]:
        """
        
        :param stream: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def RegisterDependencies(cls, rulesets: RulesetStore) -> None:
        """
        
        :param rulesets: 
        """
    def ToString(self) -> str:
        """"""
class IHasComboColours:
    """"""
    @property
    def ComboColours(self) -> IReadOnlyList[Color4]:
        """
        
        :return: 
        """
    @property
    def CustomComboColours(self) -> List[Color4]:
        """
        
        :return: 
        """
class IHasCustomColours:
    """"""
    @property
    def CustomColours(self) -> Dictionary[str, Color4]:
        """
        
        :return: 
        """
class JsonBeatmapDecoder(Decoder[Beatmap]):
    """"""
    def __init__(self):
        """"""
    def Decode(self, primaryStream: LineBufferedReader, otherStreams: Array[LineBufferedReader]) -> Beatmap:
        """
        
        :param primaryStream: 
        :param otherStreams: 
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Register(cls) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class LegacyBeatmapDecoder(LegacyDecoder[Beatmap]):
    """"""
    ApplyOffsets: Final[bool] = ...
    """
    
    :return: 
    """
    CONTROL_POINT_LENIENCY: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    EARLY_VERSION_TIMING_OFFSET: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MAX_MANIA_KEY_COUNT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    def __init__(self, version: int = ...):
        """
        
        :param version: 
        """
    def Decode(self, primaryStream: LineBufferedReader, otherStreams: Array[LineBufferedReader]) -> Beatmap:
        """
        
        :param primaryStream: 
        :param otherStreams: 
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Register(cls) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class LegacyBeatmapEncoder(Object):
    """"""
    FIRST_LAZER_VERSION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    def __init__(self, beatmap: IBeatmap, skin: ISkin):
        """
        
        :param beatmap: 
        :param skin: 
        """
    def Encode(self, writer: TextWriter) -> None:
        """
        
        :param writer: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class LegacyDecoder(ABC, Generic[T], Decoder[T]):
    """"""
    LATEST_VERSION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MAX_COMBO_COLOUR_COUNT: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    def Decode(self, primaryStream: LineBufferedReader, otherStreams: Array[LineBufferedReader]) -> T:
        """
        
        :param primaryStream: 
        :param otherStreams: 
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
    class Section(Enum):
        """"""
        General: Section = ...
        """"""
        Editor: Section = ...
        """"""
        Metadata: Section = ...
        """"""
        Difficulty: Section = ...
        """"""
        Events: Section = ...
        """"""
        TimingPoints: Section = ...
        """"""
        Colours: Section = ...
        """"""
        HitObjects: Section = ...
        """"""
        Variables: Section = ...
        """"""
        Fonts: Section = ...
        """"""
        CatchTheBeat: Section = ...
        """"""
        Mania: Section = ...
        """"""
class LegacyDifficultyCalculatorBeatmapDecoder(LegacyBeatmapDecoder):
    """"""
    ApplyOffsets: Final[bool] = ...
    """
    
    :return: 
    """
    def __init__(self, version: int = ...):
        """
        
        :param version: 
        """
    def Decode(self, primaryStream: LineBufferedReader, otherStreams: Array[LineBufferedReader]) -> Beatmap:
        """
        
        :param primaryStream: 
        :param otherStreams: 
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Register(cls) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class LegacyStoryboardDecoder(LegacyDecoder[Storyboard]):
    """"""
    def __init__(self, version: int = ...):
        """
        
        :param version: 
        """
    def Decode(self, primaryStream: LineBufferedReader, otherStreams: Array[LineBufferedReader]) -> Storyboard:
        """
        
        :param primaryStream: 
        :param otherStreams: 
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Register(cls) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class Parsing(ABC, Object):
    """"""
    MAX_COORDINATE_VALUE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MAX_PARSE_VALUE: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ParseDouble(cls, input: str, parseLimit: float = ..., allowNaN: bool = ...) -> float:
        """
        
        :param input: 
        :param parseLimit: 
        :param allowNaN: 
        :return: 
        """
    @classmethod
    def ParseFloat(cls, input: str, parseLimit: float = ..., allowNaN: bool = ...) -> float:
        """
        
        :param input: 
        :param parseLimit: 
        :param allowNaN: 
        :return: 
        """
    @classmethod
    def ParseInt(cls, input: str, parseLimit: int = ...) -> int:
        """
        
        :param input: 
        :param parseLimit: 
        :return: 
        """
    def ToString(self) -> str:
        """"""