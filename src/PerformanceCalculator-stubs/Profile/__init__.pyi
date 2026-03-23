from Alba.CsConsoleFormat import Document
from McMaster.Extensions.CommandLineUtils import CommandLineApplication
from McMaster.Extensions.CommandLineUtils import IConsole
from PerformanceCalculator import ApiCommand
from System import Array
from System import Object
from System import Type
from __future__ import annotations
from osu.Game.Beatmaps import BeatmapInfo
from osu.Game.Rulesets.Difficulty import DifficultyAttributes
from osu.Game.Rulesets.Difficulty import PerformanceAttributes
from osu.Game.Scoring import ScoreInfo
from typing import Final
from typing import Optional
class ProfileCommand(ApiCommand):
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
    def ProfileName(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ruleset(self) -> Optional[int]:
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
class UserPlayInfo(Object):
    """"""
    Accuracy: Final[float] = ...
    """
    
    :return: 
    """
    Beatmap: Final[BeatmapInfo] = ...
    """
    
    :return: 
    """
    Combo: Final[int] = ...
    """
    
    :return: 
    """
    LivePP: Final[float] = ...
    """
    
    :return: 
    """
    LocalPP: Final[float] = ...
    """
    
    :return: 
    """
    MaxCombo: Final[int] = ...
    """
    
    :return: 
    """
    MissCount: Final[float] = ...
    """
    
    :return: 
    """
    Mods: Final[Array[str]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""