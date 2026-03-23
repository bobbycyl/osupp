from System import Array
from System.Collections.Generic import IEnumerable
from System import Object
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Framework.Graphics import Colour4
from osu.Game.Rulesets.Edit import BeatmapVerifierContext
from osu.Game.Rulesets.Edit.Checks import CheckAbnormalDifficultySettings
from osu.Game.Rulesets.Edit.Checks import CheckLowestDiffDrainTime
from osu.Game.Rulesets.Edit.Checks.Components import CheckMetadata
from osu.Game.Rulesets.Edit.Checks.Components import ICheck
from osu.Game.Rulesets.Edit.Checks.Components import Issue
from osu.Game.Rulesets.Edit.Checks.Components import IssueTemplate
from osu.Game.Rulesets.Edit.Checks.Components import IssueType
from osu.Game.Rulesets.Objects import HitObject
from osu.Game.Rulesets.Osu.Edit.Checks.CheckLowDiffOverlaps import IssueTemplateOverlap
from osu.Game.Rulesets.Osu.Edit.Checks.CheckTimeDistanceEquality import IssueTemplateIrregularSpacing
from osu.Game.Rulesets.Osu.Objects import HitCircle
from osu.Game.Rulesets.Osu.Objects import Slider
from osu.Game.Rulesets.Osu.Objects import Spinner
from typing import Final
class CheckLowDiffOverlaps(Object, ICheck):
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
    class IssueTemplateOverlap(ABC, IssueTemplate):
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
        def Create(self, deltaTime: float, hitObjects: Array[HitObject]) -> Issue:
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
    class IssueTemplateShouldNotOverlap(CheckLowDiffOverlaps.IssueTemplateOverlap):
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
        def Create(self, deltaTime: float, hitObjects: Array[HitObject]) -> Issue:
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
    class IssueTemplateShouldOverlap(CheckLowDiffOverlaps.IssueTemplateOverlap):
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
        def Create(self, deltaTime: float, hitObjects: Array[HitObject]) -> Issue:
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
    class IssueTemplateShouldProbablyOverlap(CheckLowDiffOverlaps.IssueTemplateOverlap):
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
        def Create(self, deltaTime: float, hitObjects: Array[HitObject]) -> Issue:
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
class CheckOffscreenObjects(Object, ICheck):
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
    class IssueTemplateOffscreenCircle(IssueTemplate):
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
        def Create(self, circle: HitCircle) -> Issue:
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
    class IssueTemplateOffscreenSlider(IssueTemplate):
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
        def Create(self, slider: Slider, offscreenTime: float) -> Issue:
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
class CheckOsuAbnormalDifficultySettings(CheckAbnormalDifficultySettings, ICheck):
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
class CheckOsuLowestDiffDrainTime(CheckLowestDiffDrainTime, ICheck):
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
class CheckTimeDistanceEquality(Object, ICheck):
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
    class IssueTemplateIrregularSpacing(ABC, IssueTemplate):
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
        def Create(self, expected: float, actual: float, hitObjects: Array[HitObject]) -> Issue:
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
    class IssueTemplateIrregularSpacingProblem(CheckTimeDistanceEquality.IssueTemplateIrregularSpacing):
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
        def Create(self, expected: float, actual: float, hitObjects: Array[HitObject]) -> Issue:
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
    class IssueTemplateIrregularSpacingWarning(CheckTimeDistanceEquality.IssueTemplateIrregularSpacing):
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
        def Create(self, expected: float, actual: float, hitObjects: Array[HitObject]) -> Issue:
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
class CheckTooShortSliders(Object, ICheck):
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
        def Create(self, slider: Slider) -> Issue:
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
class CheckTooShortSpinners(Object, ICheck):
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
        def Create(self, spinner: Spinner) -> Issue:
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
    class IssueTemplateVeryShort(IssueTemplate):
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
        def Create(self, spinner: Spinner) -> Issue:
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