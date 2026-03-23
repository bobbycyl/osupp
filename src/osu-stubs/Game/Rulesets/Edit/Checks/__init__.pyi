from System import Array
from System.Collections.Generic import IEnumerable
from System import Object
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Framework.Graphics import Colour4
from osu.Game.Rulesets.Edit import BeatmapVerifierContext
from osu.Game.Rulesets.Edit.Checks.CheckFewHitsounds import IssueTemplateLongPeriod
from osu.Game.Rulesets.Edit.Checks.CheckMutedObjects import IssueTemplateMuted
from osu.Game.Rulesets.Edit.Checks.CheckUnsnappedObjects import IssueTemplateUnsnap
from osu.Game.Rulesets.Edit.Checks.Components import CheckMetadata
from osu.Game.Rulesets.Edit.Checks.Components import ICheck
from osu.Game.Rulesets.Edit.Checks.Components import Issue
from osu.Game.Rulesets.Edit.Checks.Components import IssueTemplate
from osu.Game.Rulesets.Edit.Checks.Components import IssueType
from osu.Game.Rulesets.Objects import HitObject
from typing import ClassVar
from typing import Final
class CheckAbnormalDifficultySettings(ABC, Object, ICheck):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateMoreThanOneDecimal(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, settingName: str, settingValue: float) -> Issue:
            """"""
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
    class IssueTemplateOutOfRange(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, settingName: str, settingValue: float) -> Issue:
            """"""
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
class CheckAudioInVideo(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateFileError(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, filename: str, errorReason: str) -> Issue:
            """"""
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
    class IssueTemplateHasAudioTrack(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, filename: str) -> Issue:
            """"""
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
    class IssueTemplateMissingFile(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, filename: str) -> Issue:
            """"""
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
class CheckAudioPresence(CheckFilePresence, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class CheckAudioQuality(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateNoBitrate(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self) -> Issue:
            """"""
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
    class IssueTemplateTooHighBitrate(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, bitrate: int, maxBitrate: int) -> Issue:
            """"""
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
    class IssueTemplateTooLowBitrate(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, bitrate: int) -> Issue:
            """"""
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
class CheckBackgroundPresence(CheckFilePresence, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class CheckBackgroundQuality(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateLowResolution(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, width: float, height: float) -> Issue:
            """"""
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
    class IssueTemplateTooHighResolution(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, width: float, height: float) -> Issue:
            """"""
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
    class IssueTemplateTooLowResolution(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, width: float, height: float) -> Issue:
            """"""
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
    class IssueTemplateTooUncompressed(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, actualMb: float) -> Issue:
            """"""
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
class CheckBreaks(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateEarlyStart(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, startTime: float, diff: float) -> Issue:
            """"""
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
    class IssueTemplateLateEnd(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, startTime: float, diff: float) -> Issue:
            """"""
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
    class IssueTemplateTooShort(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, startTime: float) -> Issue:
            """"""
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
class CheckConcurrentObjects(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateAlmostConcurrent(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, hitobject: HitObject, nextHitobject: HitObject) -> Issue:
            """"""
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
    class IssueTemplateConcurrent(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, hitobject: HitObject, nextHitobject: HitObject) -> Issue:
            """"""
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
class CheckDelayedHitsounds(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateConsequentDelay(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, filename: str, pureDelay: int) -> Issue:
            """"""
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
    class IssueTemplateDelay(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, filename: str, consequentDelay: int, delay: int) -> Issue:
            """"""
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
    class IssueTemplateDelayNoSilence(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, filename: str, delay: int) -> Issue:
            """"""
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
    class IssueTemplateMinorDelay(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, filename: str, consequentDelay: int, delay: int) -> Issue:
            """"""
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
    class IssueTemplateMinorDelayNoSilence(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, filename: str, delay: int) -> Issue:
            """"""
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
class CheckDrainLength(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateTooShort(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, drainTimeSeconds: int) -> Issue:
            """"""
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
class CheckFewHitsounds(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateLongPeriod(ABC, IssueTemplate):
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
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, time: float, duration: float) -> Issue:
            """"""
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
    class IssueTemplateLongPeriodNegligible(CheckFewHitsounds.IssueTemplateLongPeriod):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, time: float, duration: float) -> Issue:
            """"""
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
    class IssueTemplateLongPeriodProblem(CheckFewHitsounds.IssueTemplateLongPeriod):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, time: float, duration: float) -> Issue:
            """"""
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
    class IssueTemplateLongPeriodWarning(CheckFewHitsounds.IssueTemplateLongPeriod):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, time: float, duration: float) -> Issue:
            """"""
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
    class IssueTemplateNoHitsounds(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self) -> Issue:
            """"""
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
class CheckFilePresence(ABC, Object, ICheck):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateDoesNotExist(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, typeOfFile: str, filename: str) -> Issue:
            """"""
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
    class IssueTemplateNoneSet(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, typeOfFile: str) -> Issue:
            """"""
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
class CheckHitsoundsFormat(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateFormatUnsupported(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, file: str) -> Issue:
            """"""
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
    class IssueTemplateIncorrectFormat(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, file: str) -> Issue:
            """"""
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
class CheckInconsistentAudio(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateInconsistentAudio(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, referenceAudio: str, otherDifficulty: str, otherAudio: str) -> Issue:
            """"""
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
class CheckInconsistentMetadata(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateInconsistentOtherFields(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, fieldName: str, referenceDifficulty: str, currentDifficulty: str, referenceValue: str, currentValue: str) -> Issue:
            """"""
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
    class IssueTemplateInconsistentTags(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, referenceDifficulty: str, currentDifficulty: str, difference: str) -> Issue:
            """"""
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
class CheckInconsistentSettings(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateInconsistentSetting(IssueTemplate):
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
        def __init__(self, check: ICheck, issueType: IssueType):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, fieldName: str, referenceDifficulty: str, currentDifficulty: str, referenceValue: str, currentValue: str) -> Issue:
            """"""
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
class CheckInconsistentTimingControlPoints(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateExtraTimingPoint(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, time: float, difficultyName: str) -> Issue:
            """"""
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
    class IssueTemplateInconsistentBPM(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, time: float, difficultyName: str) -> Issue:
            """"""
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
    class IssueTemplateInconsistentMeter(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, time: float, difficultyName: str) -> Issue:
            """"""
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
    class IssueTemplateMissingTimingPoint(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, time: float, difficultyName: str) -> Issue:
            """"""
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
    class IssueTemplateMissingTimingPointMinor(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, time: float, difficultyName: str) -> Issue:
            """"""
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
class CheckLowestDiffDrainTime(ABC, Object, ICheck):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateTooShort(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, lowestDiffLevel: str, timeType: str, requiredTime: float, currentTime: float) -> Issue:
            """"""
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
class CheckMissingGenreLanguage(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateMissingGenre(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self) -> Issue:
            """"""
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
    class IssueTemplateMissingLanguage(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self) -> Issue:
            """"""
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
class CheckMutedObjects(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateLowVolumeActive(CheckMutedObjects.IssueTemplateMuted):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, hitobject: HitObject, volume: float, time: float, postfix: str = ...) -> Issue:
            """"""
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
    class IssueTemplateMuted(ABC, IssueTemplate):
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
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, hitobject: HitObject, volume: float, time: float, postfix: str = ...) -> Issue:
            """"""
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
    class IssueTemplateMutedActive(CheckMutedObjects.IssueTemplateMuted):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, hitobject: HitObject, volume: float, time: float, postfix: str = ...) -> Issue:
            """"""
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
    class IssueTemplateMutedPassive(CheckMutedObjects.IssueTemplateMuted):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, hitobject: HitObject, volume: float, time: float, postfix: str = ...) -> Issue:
            """"""
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
class CheckPreviewTime(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateHasNoPreviewTime(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self) -> Issue:
            """"""
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
    class IssueTemplatePreviewTimeConflict(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, diffName: str, originalTime: int, conflictTime: int) -> Issue:
            """"""
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
class CheckSongFormat(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateFormatUnsupported(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, file: str) -> Issue:
            """"""
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
    class IssueTemplateIncorrectFormat(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, file: str) -> Issue:
            """"""
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
class CheckTitleMarkers(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateIncorrectMarker(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, titleField: str, correctMarkerFormat: str) -> Issue:
            """"""
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
class CheckTooShortAudioFiles(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateTooShort(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, filename: str, ms: float) -> Issue:
            """"""
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
class CheckUnsnappedObjects(Object, ICheck):
    """"""
    UNSNAP_MS_THRESHOLD: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateLargeUnsnap(CheckUnsnappedObjects.IssueTemplateUnsnap):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, hitobject: HitObject, unsnap: float, time: float, postfix: str = ...) -> Issue:
            """"""
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
    class IssueTemplateSmallUnsnap(CheckUnsnappedObjects.IssueTemplateUnsnap):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, hitobject: HitObject, unsnap: float, time: float, postfix: str = ...) -> Issue:
            """"""
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
    class IssueTemplateUnsnap(ABC, IssueTemplate):
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
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, hitobject: HitObject, unsnap: float, time: float, postfix: str = ...) -> Issue:
            """"""
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
class CheckUnusedAudioAtEnd(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateUnusedAudioAtEnd(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, percentageLeft: float) -> Issue:
            """"""
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
    class IssueTemplateUnusedAudioAtEndStoryboardOrVideo(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, percentageLeft: float) -> Issue:
            """"""
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
class CheckVideoResolution(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateFileError(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, filename: str, errorReason: str) -> Issue:
            """"""
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
    class IssueTemplateHighResolution(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, filename: str, width: int, height: int) -> Issue:
            """"""
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
class CheckVideoUsage(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateDifferentStartTime(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, path: str, difficultyA: str, startA: float, difficultyB: str, startB: float) -> Issue:
            """"""
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
    class IssueTemplateDifferentVideo(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, otherDifficulty: str, currentPath: str, otherPath: str) -> Issue:
            """"""
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
    class IssueTemplateMissingVideo(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, otherDifficulty: str) -> Issue:
            """"""
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
class CheckZeroByteFiles(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateZeroBytes(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, filename: str) -> Issue:
            """"""
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
class CheckZeroLengthObjects(Object, ICheck):
    """"""
    def __init__(self):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    class IssueTemplateZeroLength(IssueTemplate):
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
        def __init__(self, check: ICheck):
            """"""
        @property
        def Colour(self) -> Colour4:
            """
            
            :return: 
            """
        def Create(self, hitobject: HitObject, duration: float) -> Issue:
            """"""
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