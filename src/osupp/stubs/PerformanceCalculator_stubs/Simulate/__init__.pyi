from Alba.CsConsoleFormat import Document
from McMaster.Extensions.CommandLineUtils import CommandLineApplication
from McMaster.Extensions.CommandLineUtils import IConsole
from PerformanceCalculator import ProcessorCommand
from System import Array
from System import Object
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Game.Rulesets.Difficulty import DifficultyAttributes
from osu.Game.Rulesets.Difficulty import PerformanceAttributes
from osu.Game.Rulesets import Ruleset
from osu.Game.Scoring import ScoreInfo
from typing import Optional
class CatchSimulateCommand(SimulateCommand):
    """"""
    def __init__(self):
        """"""
    @property
    def Accuracy(self) -> float:
        """
        
        :return: 
        """
    @property
    def Beatmap(self) -> str:
        """
        
        :return: 
        """
    @property
    def Combo(self) -> Optional[int]:
        """
        
        :return: 
        """
    @property
    def Console(self) -> IConsole:
        """
        
        :return: 
        """
    @property
    def Goods(self) -> Optional[int]:
        """
        
        :return: 
        """
    @property
    def LegacyTotalScore(self) -> Optional[int]:
        """
        
        :return: 
        """
    @property
    def Mehs(self) -> Optional[int]:
        """
        
        :return: 
        """
    @property
    def Misses(self) -> int:
        """
        
        :return: 
        """
    @property
    def ModOptions(self) -> Array[str]:
        """
        
        :return: 
        """
    @ModOptions.setter
    def ModOptions(self, value: Array[str]) -> None: ...
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
    def PercentCombo(self) -> float:
        """
        
        :return: 
        """
    @property
    def Ruleset(self) -> Ruleset:
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
class ManiaSimulateCommand(SimulateCommand):
    """"""
    def __init__(self):
        """"""
    @property
    def Accuracy(self) -> float:
        """
        
        :return: 
        """
    @property
    def Beatmap(self) -> str:
        """
        
        :return: 
        """
    @property
    def Combo(self) -> Optional[int]:
        """
        
        :return: 
        """
    @property
    def Console(self) -> IConsole:
        """
        
        :return: 
        """
    @property
    def Goods(self) -> Optional[int]:
        """
        
        :return: 
        """
    @property
    def LegacyTotalScore(self) -> Optional[int]:
        """
        
        :return: 
        """
    @property
    def Mehs(self) -> Optional[int]:
        """
        
        :return: 
        """
    @property
    def Misses(self) -> int:
        """
        
        :return: 
        """
    @property
    def ModOptions(self) -> Array[str]:
        """
        
        :return: 
        """
    @ModOptions.setter
    def ModOptions(self, value: Array[str]) -> None: ...
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
    def PercentCombo(self) -> float:
        """
        
        :return: 
        """
    @property
    def Ruleset(self) -> Ruleset:
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
class OsuSimulateCommand(SimulateCommand):
    """"""
    def __init__(self):
        """"""
    @property
    def Accuracy(self) -> float:
        """
        
        :return: 
        """
    @property
    def Beatmap(self) -> str:
        """
        
        :return: 
        """
    @property
    def Combo(self) -> Optional[int]:
        """
        
        :return: 
        """
    @property
    def Console(self) -> IConsole:
        """
        
        :return: 
        """
    @property
    def Goods(self) -> Optional[int]:
        """
        
        :return: 
        """
    @property
    def LegacyTotalScore(self) -> Optional[int]:
        """
        
        :return: 
        """
    @property
    def Mehs(self) -> Optional[int]:
        """
        
        :return: 
        """
    @property
    def Misses(self) -> int:
        """
        
        :return: 
        """
    @property
    def ModOptions(self) -> Array[str]:
        """
        
        :return: 
        """
    @ModOptions.setter
    def ModOptions(self, value: Array[str]) -> None: ...
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
    def PercentCombo(self) -> float:
        """
        
        :return: 
        """
    @property
    def Ruleset(self) -> Ruleset:
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
class SimulateCommand(ABC, ProcessorCommand):
    """"""
    @property
    def Accuracy(self) -> float:
        """
        
        :return: 
        """
    @property
    def Beatmap(self) -> str:
        """
        
        :return: 
        """
    @property
    def Combo(self) -> Optional[int]:
        """
        
        :return: 
        """
    @property
    def Console(self) -> IConsole:
        """
        
        :return: 
        """
    @property
    def Goods(self) -> Optional[int]:
        """
        
        :return: 
        """
    @property
    def LegacyTotalScore(self) -> Optional[int]:
        """
        
        :return: 
        """
    @property
    def Mehs(self) -> Optional[int]:
        """
        
        :return: 
        """
    @property
    def Misses(self) -> int:
        """
        
        :return: 
        """
    @property
    def ModOptions(self) -> Array[str]:
        """
        
        :return: 
        """
    @ModOptions.setter
    def ModOptions(self, value: Array[str]) -> None: ...
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
    def PercentCombo(self) -> float:
        """
        
        :return: 
        """
    @property
    def Ruleset(self) -> Ruleset:
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
class SimulateListingCommand(Object):
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
class TaikoSimulateCommand(SimulateCommand):
    """"""
    def __init__(self):
        """"""
    @property
    def Accuracy(self) -> float:
        """
        
        :return: 
        """
    @property
    def Beatmap(self) -> str:
        """
        
        :return: 
        """
    @property
    def Combo(self) -> Optional[int]:
        """
        
        :return: 
        """
    @property
    def Console(self) -> IConsole:
        """
        
        :return: 
        """
    @property
    def Goods(self) -> Optional[int]:
        """
        
        :return: 
        """
    @property
    def LegacyTotalScore(self) -> Optional[int]:
        """
        
        :return: 
        """
    @property
    def Mehs(self) -> Optional[int]:
        """
        
        :return: 
        """
    @property
    def Misses(self) -> int:
        """
        
        :return: 
        """
    @property
    def ModOptions(self) -> Array[str]:
        """
        
        :return: 
        """
    @ModOptions.setter
    def ModOptions(self, value: Array[str]) -> None: ...
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
    def PercentCombo(self) -> float:
        """
        
        :return: 
        """
    @property
    def Ruleset(self) -> Ruleset:
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