from ManagedBass import ChannelType
from System import Array
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IReadOnlyList
from System import Enum
from System.IO import Stream
from System import Object
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Framework.Graphics import Colour4
from osu.Game.Beatmaps.ControlPoints import TimingControlPoint
from osu.Game.Beatmaps import IWorkingBeatmap
from osu.Game.Rulesets.Edit import BeatmapVerifierContext
from osu.Game.Rulesets.Objects import HitObject
from osu.Game.Storyboards import StoryboardVideo
from typing import ClassVar
from typing import Final
from typing import Optional
from typing import overload
class AudioCheckUtils(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetAudioFormat(cls, data: Stream) -> ChannelType:
        """
        
        :param data: 
        :return: 
        """
    @classmethod
    def GetAudioFormatFromFile(cls, context: BeatmapVerifierContext, filename: str) -> ChannelType:
        """
        
        :param context: 
        :param filename: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def HasAudioExtension(cls, filename: str) -> bool:
        """
        
        :param filename: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class CheckCategory(Enum):
    """"""
    Timing: CheckCategory = ...
    """"""
    Metadata: CheckCategory = ...
    """"""
    Resources: CheckCategory = ...
    """"""
    Audio: CheckCategory = ...
    """"""
    Files: CheckCategory = ...
    """"""
    Compose: CheckCategory = ...
    """"""
    Spread: CheckCategory = ...
    """"""
    Settings: CheckCategory = ...
    """"""
    HitObjects: CheckCategory = ...
    """"""
    Events: CheckCategory = ...
    """"""
class CheckMetadata(Object):
    """"""
    Category: Final[CheckCategory] = ...
    """
    
    :return: 
    """
    Description: Final[str] = ...
    """
    
    :return: 
    """
    Scope: Final[CheckScope] = ...
    """
    
    :return: 
    """
    def __init__(self, category: CheckCategory, description: str, scope: CheckScope = ...):
        """
        
        :param category: 
        :param description: 
        :param scope: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class CheckScope(Enum):
    """"""
    Difficulty: CheckScope = ...
    """"""
    BeatmapSet: CheckScope = ...
    """"""
class ICheck:
    """"""
    @property
    def Metadata(self) -> CheckMetadata:
        """
        
        :return: 
        """
    @property
    def PossibleTemplates(self) -> IEnumerable[IssueTemplate]:
        """
        
        :return: 
        """
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
class Issue(Object):
    """"""
    Arguments: Final[Array[object]] = ...
    """
    
    :return: 
    """
    HitObjects: Final[IReadOnlyList[HitObject]] = ...
    """
    
    :return: 
    """
    Template: Final[IssueTemplate] = ...
    """
    
    :return: 
    """
    Time: Final[Optional[float]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, template: IssueTemplate, args: Array[object]):
        """
        
        :param template: 
        :param args: 
        """
    @overload
    def __init__(self, hitObjects: IEnumerable[HitObject], template: IssueTemplate, args: Array[object]):
        """
        
        :param hitObjects: 
        :param template: 
        :param args: 
        """
    @overload
    def __init__(self, time: Optional[float], template: IssueTemplate, args: Array[object]):
        """
        
        :param time: 
        :param template: 
        :param args: 
        """
    @overload
    def __init__(self, hitObject: HitObject, template: IssueTemplate, args: Array[object]):
        """
        
        :param hitObject: 
        :param template: 
        :param args: 
        """
    @property
    def Check(self) -> ICheck:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEditorTimestamp(self) -> str:
        """
        
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class IssueTemplate(Object):
    """"""
    Check: Final[ICheck] = ...
    """
    
    :return: 
    """
    Type: Final[IssueType] = ...
    """
    
    :return: 
    """
    UnformattedMessage: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self, check: ICheck, type: IssueType, unformattedMessage: str):
        """
        
        :param check: 
        :param type: 
        :param unformattedMessage: 
        """
    @property
    def Colour(self) -> Colour4:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMessage(self, args: Array[object]) -> str:
        """
        
        :param args: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class IssueType(Enum):
    """"""
    Problem: IssueType = ...
    """"""
    Warning: IssueType = ...
    """"""
    Error: IssueType = ...
    """"""
    Negligible: IssueType = ...
    """"""
class ResourcesCheckUtils(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetDifficultyVideo(cls, workingBeatmap: IWorkingBeatmap) -> StoryboardVideo:
        """
        
        :param workingBeatmap: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def HasAnyStoryboardElementPresent(cls, workingBeatmap: IWorkingBeatmap) -> bool:
        """
        
        :param workingBeatmap: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class TimingCheckUtils(ABC, Object):
    """"""
    TIME_OFFSET_TOLERANCE_MS: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FindExactMatchingTimingPoint(cls, timingPoints: IEnumerable[TimingControlPoint], time: float) -> TimingControlPoint:
        """
        
        :param timingPoints: 
        :param time: 
        :return: 
        """
    @classmethod
    def FindMatchingTimingPoint(cls, timingPoints: IEnumerable[TimingControlPoint], time: float) -> TimingControlPoint:
        """
        
        :param timingPoints: 
        :param time: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""