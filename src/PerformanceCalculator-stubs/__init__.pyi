from Alba.CsConsoleFormat import Document
from McMaster.Extensions.CommandLineUtils import CommandLineApplication
from McMaster.Extensions.CommandLineUtils import IConsole
from System import Array
from System.Collections.Generic import IReadOnlyList
from System.IO import Stream
from System import Object
from System.Threading import CancellationToken
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Framework.Audio.Track import Track
from osu.Framework.Audio.Track import Waveform
from osu.Framework.Graphics.Textures import Texture
from osu.Game.Beatmaps import BeatmapInfo
from osu.Game.Beatmaps import BeatmapMetadata
from osu.Game.Beatmaps import BeatmapSetInfo
from osu.Game.Beatmaps import IBeatmap
from osu.Game.Beatmaps import IBeatmapInfo
from osu.Game.Beatmaps import IWorkingBeatmap
from osu.Game.Beatmaps import WorkingBeatmap
from osu.Game.Online import EndpointConfiguration
from osu.Game.Rulesets.Difficulty import DifficultyAttributes
from osu.Game.Rulesets.Difficulty import PerformanceAttributes
from osu.Game.Rulesets import IRulesetInfo
from osu.Game.Rulesets.Mods import Mod
from osu.Game.Rulesets import Ruleset
from osu.Game.Scoring.Legacy import LegacyScoreDecoder
from osu.Game.Scoring import Score
from osu.Game.Scoring import ScoreInfo
from osu.Game.Skinning import ISkin
from osu.Game.Storyboards import Storyboard
from typing import ClassVar
from typing import Final
from typing import Optional
from typing import overload
class ApiCommand(ABC, ProcessorCommand):
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
class LegacyHelper(ABC, Object):
    """"""
    @classmethod
    def CreateDifficultyAttributes(cls, legacyId: int) -> DifficultyAttributes:
        """
        
        :param legacyId: 
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetRulesetFromLegacyID(cls, id: int) -> Ruleset:
        """
        
        :param id: 
        :return: 
        """
    @classmethod
    def GetRulesetShortNameFromId(cls, id: int) -> str:
        """
        
        :param id: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class ProcessorCommand(ABC, Object):
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
    @classmethod
    def ParseMods(cls, ruleset: Ruleset, acronyms: Array[str], options: Array[str]) -> Array[Mod]:
        """
        
        :param ruleset: 
        :param acronyms: 
        :param options: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class ProcessorScoreDecoder(LegacyScoreDecoder):
    """"""
    def __init__(self, beatmap: WorkingBeatmap):
        """
        
        :param beatmap: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Parse(self, stream: Stream) -> Score:
        """
        
        :param stream: 
        :return: 
        """
    @overload
    def Parse(self, scoreInfo: ScoreInfo) -> Score:
        """
        
        :param scoreInfo: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class ProcessorWorkingBeatmap(WorkingBeatmap, IWorkingBeatmap):
    """"""
    BeatmapInfo: Final[BeatmapInfo] = ...
    """
    
    :return: 
    """
    BeatmapSetInfo: Final[BeatmapSetInfo] = ...
    """
    
    :return: 
    """
    def __init__(self, file: str, beatmapId: Optional[int] = ...):
        """
        
        :param file: 
        :param beatmapId: 
        """
    @property
    def Beatmap(self) -> IBeatmap:
        """
        
        :return: 
        """
    @property
    def BeatmapInfo(self) -> IBeatmapInfo:
        """
        
        :return: 
        """
    @property
    def BeatmapLoaded(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Metadata(self) -> BeatmapMetadata:
        """
        
        :return: 
        """
    @property
    def Skin(self) -> ISkin:
        """
        
        :return: 
        """
    @property
    def Storyboard(self) -> Storyboard:
        """
        
        :return: 
        """
    @property
    def Track(self) -> Track:
        """
        
        :return: 
        """
    @property
    def TrackLoaded(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Waveform(self) -> Waveform:
        """
        
        :return: 
        """
    def BeginAsyncLoad(self) -> None:
        """"""
    def CancelAsyncLoad(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FromFileOrId(cls, fileOrId: str) -> ProcessorWorkingBeatmap:
        """
        
        :param fileOrId: 
        :return: 
        """
    def GetBackground(self) -> Texture:
        """
        
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetPanelBackground(self) -> Texture:
        """
        
        :return: 
        """
    @overload
    def GetPlayableBeatmap(self, ruleset: IRulesetInfo, mods: IReadOnlyList[Mod] = ...) -> IBeatmap:
        """
        
        :param ruleset: 
        :param mods: 
        :return: 
        """
    @overload
    def GetPlayableBeatmap(self, ruleset: IRulesetInfo, mods: IReadOnlyList[Mod], token: CancellationToken) -> IBeatmap:
        """
        
        :param ruleset: 
        :param mods: 
        :param cancellationToken: 
        :return: 
        """
    def GetStream(self, storagePath: str) -> Stream:
        """
        
        :param storagePath: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def LoadTrack(self) -> Track:
        """
        
        :return: 
        """
    def PrepareTrackForPreview(self, looping: bool, offsetFromPreviewPoint: float = ...) -> None:
        """
        
        :param looping: 
        :param offsetFromPreviewPoint: 
        """
    def ToString(self) -> str:
        """"""
    def TryTransferTrack(self, target: WorkingBeatmap) -> bool:
        """
        
        :param target: 
        :return: 
        """
class Program(Object):
    """"""
    ENDPOINT_CONFIGURATION: Final[ClassVar[EndpointConfiguration]] = ...
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
    @classmethod
    def Main(cls, args: Array[str]) -> None:
        """
        
        :param args: 
        """
    def OnExecute(self, app: CommandLineApplication, console: IConsole) -> int:
        """
        
        :param app: 
        :param console: 
        :return: 
        """
    def ToString(self) -> str:
        """"""