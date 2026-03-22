from Alba.CsConsoleFormat import Document
from McMaster.Extensions.CommandLineUtils import CommandLineApplication
from McMaster.Extensions.CommandLineUtils import IConsole
from PerformanceCalculator import ApiCommand
from System import Object
from System import Type
from __future__ import annotations
from osu.Game.Rulesets.Difficulty import DifficultyAttributes
from osu.Game.Rulesets.Difficulty import PerformanceAttributes
from osu.Game.Scoring import ScoreInfo
class LegacyScorePerformanceCommand(ScorePerformanceCommand):
    """"""
    def __init__(self):
        """"""
    @property
    def ClientId(self) -> str:
        """
        
        :return: 
        """
    @property
    def ClientSecret(self) -> str:
        """
        
        :return: 
        """
    @property
    def Console(self) -> IConsole:
        """
        
        :return: 
        """
    @property
    def OnlineAttributes(self) -> bool:
        """
        
        :return: 
        """
    @OnlineAttributes.setter
    def OnlineAttributes(self, value: bool) -> None: ...
    @property
    def OutputJson(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RulesetId(self) -> int:
        """
        
        :return: 
        """
    @RulesetId.setter
    def RulesetId(self, value: int) -> None: ...
    @property
    def ScoreId(self) -> int:
        """
        
        :return: 
        """
    @ScoreId.setter
    def ScoreId(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def Execute(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def OnExecute(self, app: CommandLineApplication, console: IConsole) -> None:
        """
        
        :param app: 
        :param console: 
        """
    def OutputDocument(self, document: Document) -> None:
        """
        
        :param document: 
        """
    def OutputPerformance(self, score: ScoreInfo, performanceAttributes: PerformanceAttributes, difficultyAttributes: DifficultyAttributes) -> None:
        """
        
        :param score: 
        :param performanceAttributes: 
        :param difficultyAttributes: 
        """
    def ToString(self) -> str:
        """"""
class PerformanceListingCommand(Object):
    """"""
    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def OnExecute(self, app: CommandLineApplication, console: IConsole) -> int:
        """
        
        :param app: 
        :param console: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class ReplayPerformanceCommand(ApiCommand):
    """"""
    def __init__(self):
        """"""
    @property
    def ClientId(self) -> str:
        """
        
        :return: 
        """
    @property
    def ClientSecret(self) -> str:
        """
        
        :return: 
        """
    @property
    def Console(self) -> IConsole:
        """
        
        :return: 
        """
    @property
    def OutputJson(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Replay(self) -> str:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def Execute(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def OnExecute(self, app: CommandLineApplication, console: IConsole) -> None:
        """
        
        :param app: 
        :param console: 
        """
    def OutputDocument(self, document: Document) -> None:
        """
        
        :param document: 
        """
    def OutputPerformance(self, score: ScoreInfo, performanceAttributes: PerformanceAttributes, difficultyAttributes: DifficultyAttributes) -> None:
        """
        
        :param score: 
        :param performanceAttributes: 
        :param difficultyAttributes: 
        """
    def ToString(self) -> str:
        """"""
class ScorePerformanceCommand(ApiCommand):
    """"""
    def __init__(self):
        """"""
    @property
    def ClientId(self) -> str:
        """
        
        :return: 
        """
    @property
    def ClientSecret(self) -> str:
        """
        
        :return: 
        """
    @property
    def Console(self) -> IConsole:
        """
        
        :return: 
        """
    @property
    def OnlineAttributes(self) -> bool:
        """
        
        :return: 
        """
    @OnlineAttributes.setter
    def OnlineAttributes(self, value: bool) -> None: ...
    @property
    def OutputJson(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreId(self) -> int:
        """
        
        :return: 
        """
    @ScoreId.setter
    def ScoreId(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def Execute(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def OnExecute(self, app: CommandLineApplication, console: IConsole) -> None:
        """
        
        :param app: 
        :param console: 
        """
    def OutputDocument(self, document: Document) -> None:
        """
        
        :param document: 
        """
    def OutputPerformance(self, score: ScoreInfo, performanceAttributes: PerformanceAttributes, difficultyAttributes: DifficultyAttributes) -> None:
        """
        
        :param score: 
        :param performanceAttributes: 
        :param difficultyAttributes: 
        """
    def ToString(self) -> str:
        """"""