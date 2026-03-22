from System import Array
from System.Collections.Generic import IEnumerable
from System import Object
from System import Type
from __future__ import annotations
from osu.Framework.Graphics import Colour4
from osu.Game.Rulesets.Edit import BeatmapVerifierContext
from osu.Game.Rulesets.Edit.Checks import CheckAbnormalDifficultySettings
from osu.Game.Rulesets.Edit.Checks import CheckLowestDiffDrainTime
from osu.Game.Rulesets.Edit.Checks.Components import CheckMetadata
from osu.Game.Rulesets.Edit.Checks.Components import ICheck
from osu.Game.Rulesets.Edit.Checks.Components import Issue
from osu.Game.Rulesets.Edit.Checks.Components import IssueTemplate
from osu.Game.Rulesets.Edit.Checks.Components import IssueType
from typing import Final
class CheckTaikoAbnormalDifficultySettings(CheckAbnormalDifficultySettings, ICheck):
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
class CheckTaikoInconsistentSkipBarLine(Object, ICheck):
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
    class IssueTemplateInconsistentOmitFirstBarLine(IssueTemplate):
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
class CheckTaikoLowestDiffDrainTime(CheckLowestDiffDrainTime, ICheck):
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