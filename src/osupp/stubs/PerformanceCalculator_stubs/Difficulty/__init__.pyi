from Alba.CsConsoleFormat import Document
from McMaster.Extensions.CommandLineUtils import CommandLineApplication
from McMaster.Extensions.CommandLineUtils import IConsole
from PerformanceCalculator import ProcessorCommand
from System import Array
from System import Object
from System import Type
from __future__ import annotations
from osu.Game.Rulesets.Difficulty import DifficultyAttributes
from osu.Game.Rulesets.Difficulty import PerformanceAttributes
from osu.Game.Scoring import ScoreInfo
from typing import Optional
class DifficultyCommand(ProcessorCommand):
    """"""
    def __init__(self):
        """"""
    @property
    def Console(self) -> IConsole:
        """
        
        :return: 
        """
    @property
    def ModOptions(self) -> Array[str]:
        """
        
        :return: 
        """
    @property
    def Mods(self) -> Array[str]:
        """
        
        :return: 
        """
    @property
    def OutputJson(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Path(self) -> str:
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
class LegacyScoreAttributesCommand(ProcessorCommand):
    """"""
    def __init__(self):
        """"""
    @property
    def Console(self) -> IConsole:
        """
        
        :return: 
        """
    @property
    def Mods(self) -> Array[str]:
        """
        
        :return: 
        """
    @property
    def OutputJson(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Path(self) -> str:
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
class LegacyScoreConversionCommand(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Beatmap(self) -> str:
        """
        
        :return: 
        """
    @property
    def Gekis(self) -> int:
        """
        
        :return: 
        """
    @Gekis.setter
    def Gekis(self, value: int) -> None: ...
    @property
    def Goods(self) -> int:
        """
        
        :return: 
        """
    @Goods.setter
    def Goods(self, value: int) -> None: ...
    @property
    def Greats(self) -> int:
        """
        
        :return: 
        """
    @Greats.setter
    def Greats(self, value: int) -> None: ...
    @property
    def Katus(self) -> int:
        """
        
        :return: 
        """
    @Katus.setter
    def Katus(self, value: int) -> None: ...
    @property
    def MaxCombo(self) -> int:
        """
        
        :return: 
        """
    @MaxCombo.setter
    def MaxCombo(self, value: int) -> None: ...
    @property
    def Mehs(self) -> int:
        """
        
        :return: 
        """
    @Mehs.setter
    def Mehs(self, value: int) -> None: ...
    @property
    def Misses(self) -> int:
        """
        
        :return: 
        """
    @Misses.setter
    def Misses(self, value: int) -> None: ...
    @property
    def Mods(self) -> Array[str]:
        """
        
        :return: 
        """
    @property
    def Ruleset(self) -> int:
        """
        
        :return: 
        """
    @property
    def TotalScore(self) -> int:
        """
        
        :return: 
        """
    @TotalScore.setter
    def TotalScore(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
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
    def ToString(self) -> str:
        """"""
class ModsCommand(ProcessorCommand):
    """"""
    def __init__(self):
        """"""
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