from System import Array
from System.Collections.Generic import Dictionary
from System.Collections import IDictionary
from System import Exception
from System.IO import Stream
from System import Object
from System.Reflection import MethodBase
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Game.Beatmaps import BeatmapManager
from osu.Game.Beatmaps import IBeatmap
from osu.Game.Beatmaps import WorkingBeatmap
from osu.Game.Online.API import APIMod
from osu.Game.Online.API.Requests.Responses import SoloScoreInfo
from osu.Game.Online.Rooms import MultiplayerScore
from osu.Game.Rulesets import IRulesetStore
from osu.Game.Rulesets.Scoring import HitResult
from osu.Game.Rulesets.Scoring import ScoreProcessor
from osu.Game.Rulesets.Scoring import ScoringMode
from osu.Game.Scoring import Score
from osu.Game.Scoring import ScoreInfo
from osu.Game.Scoring import ScoreRank
from typing import ClassVar
from typing import Final
from typing import Optional
from typing import overload
class DatabasedLegacyScoreDecoder(LegacyScoreDecoder):
    """"""
    def __init__(self, rulesets: IRulesetStore, beatmaps: BeatmapManager):
        """
        
        :param rulesets: 
        :param beatmaps: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Parse(self, stream: Stream) -> Score:
        """
        
        :param stream: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class LegacyReplaySoloScoreInfo(Object):
    """"""
    ClientVersion: Final[str] = ...
    """
    
    :return: 
    """
    Rank: Final[Optional[ScoreRank]] = ...
    """
    
    :return: 
    """
    UserID: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def MaximumStatistics(self) -> Dictionary[HitResult, int]:
        """
        
        :return: 
        """
    @MaximumStatistics.setter
    def MaximumStatistics(self, value: Dictionary[HitResult, int]) -> None: ...
    @property
    def Mods(self) -> Array[APIMod]:
        """
        
        :return: 
        """
    @Mods.setter
    def Mods(self, value: Array[APIMod]) -> None: ...
    @property
    def OnlineID(self) -> int:
        """
        
        :return: 
        """
    @OnlineID.setter
    def OnlineID(self, value: int) -> None: ...
    @property
    def Pauses(self) -> Array[int]:
        """
        
        :return: 
        """
    @Pauses.setter
    def Pauses(self, value: Array[int]) -> None: ...
    @property
    def Statistics(self) -> Dictionary[HitResult, int]:
        """
        
        :return: 
        """
    @Statistics.setter
    def Statistics(self, value: Dictionary[HitResult, int]) -> None: ...
    @property
    def TotalScoreWithoutMods(self) -> Optional[int]:
        """
        
        :return: 
        """
    @TotalScoreWithoutMods.setter
    def TotalScoreWithoutMods(self, value: Optional[int]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FromScore(cls, score: ScoreInfo) -> LegacyReplaySoloScoreInfo:
        """
        
        :param score: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class LegacyScoreDecoder(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Parse(self, stream: Stream) -> Score:
        """
        
        :param stream: 
        :return: 
        """
    @classmethod
    def PopulateMaximumStatistics(cls, score: ScoreInfo, workingBeatmap: WorkingBeatmap) -> None:
        """
        
        :param score: 
        :param workingBeatmap: 
        """
    @classmethod
    def PopulateTotalScoreWithoutMods(cls, score: ScoreInfo) -> None:
        """
        
        :param score: 
        """
    def ToString(self) -> str:
        """"""
    class BeatmapNotFoundException(Exception, ISerializable):
        """"""
        def __init__(self, hash: str):
            """"""
        @property
        def Data(self) -> IDictionary:
            """"""
        @property
        def HResult(self) -> int:
            """"""
        @HResult.setter
        def HResult(self, value: int) -> None: ...
        @property
        def Hash(self) -> str:
            """"""
        @property
        def HelpLink(self) -> str:
            """"""
        @HelpLink.setter
        def HelpLink(self, value: str) -> None: ...
        @property
        def InnerException(self) -> Exception:
            """"""
        @property
        def Message(self) -> str:
            """"""
        @property
        def Source(self) -> str:
            """"""
        @Source.setter
        def Source(self, value: str) -> None: ...
        @property
        def StackTrace(self) -> str:
            """"""
        @property
        def TargetSite(self) -> MethodBase:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetBaseException(self) -> Exception:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
class LegacyScoreEncoder(Object):
    """"""
    FIRST_LAZER_VERSION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    LATEST_VERSION: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    def __init__(self, score: Score, beatmap: IBeatmap):
        """
        
        :param score: 
        :param beatmap: 
        """
    def Encode(self, stream: Stream, leaveOpen: bool = ...) -> None:
        """
        
        :param stream: 
        :param leaveOpen: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class ScoreInfoExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetCount100(cls, scoreInfo: ScoreInfo) -> Optional[int]:
        """
        
        :param scoreInfo: 
        :return: 
        """
    @classmethod
    def GetCount300(cls, scoreInfo: ScoreInfo) -> Optional[int]:
        """
        
        :param scoreInfo: 
        :return: 
        """
    @classmethod
    def GetCount50(cls, scoreInfo: ScoreInfo) -> Optional[int]:
        """
        
        :param scoreInfo: 
        :return: 
        """
    @classmethod
    def GetCountGeki(cls, scoreInfo: ScoreInfo) -> Optional[int]:
        """
        
        :param scoreInfo: 
        :return: 
        """
    @classmethod
    def GetCountKatu(cls, scoreInfo: ScoreInfo) -> Optional[int]:
        """
        
        :param scoreInfo: 
        :return: 
        """
    @classmethod
    def GetCountMiss(cls, scoreInfo: ScoreInfo) -> Optional[int]:
        """
        
        :param scoreInfo: 
        :return: 
        """
    @classmethod
    @overload
    def GetDisplayScore(cls, soloScoreInfo: SoloScoreInfo, mode: ScoringMode) -> int:
        """
        
        :param soloScoreInfo: 
        :param mode: 
        :return: 
        """
    @classmethod
    @overload
    def GetDisplayScore(cls, multiplayerScore: MultiplayerScore, mode: ScoringMode) -> int:
        """
        
        :param multiplayerScore: 
        :param mode: 
        :return: 
        """
    @classmethod
    @overload
    def GetDisplayScore(cls, scoreProcessor: ScoreProcessor, mode: ScoringMode) -> int:
        """
        
        :param scoreProcessor: 
        :param mode: 
        :return: 
        """
    @classmethod
    @overload
    def GetDisplayScore(cls, scoreInfo: ScoreInfo, mode: ScoringMode) -> int:
        """
        
        :param scoreInfo: 
        :param mode: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def SetCount100(cls, scoreInfo: ScoreInfo, value: int) -> None:
        """
        
        :param scoreInfo: 
        :param value: 
        """
    @classmethod
    def SetCount300(cls, scoreInfo: ScoreInfo, value: int) -> None:
        """
        
        :param scoreInfo: 
        :param value: 
        """
    @classmethod
    def SetCount50(cls, scoreInfo: ScoreInfo, value: int) -> None:
        """
        
        :param scoreInfo: 
        :param value: 
        """
    @classmethod
    def SetCountGeki(cls, scoreInfo: ScoreInfo, value: int) -> None:
        """
        
        :param scoreInfo: 
        :param value: 
        """
    @classmethod
    def SetCountKatu(cls, scoreInfo: ScoreInfo, value: int) -> None:
        """
        
        :param scoreInfo: 
        :param value: 
        """
    @classmethod
    def SetCountMiss(cls, scoreInfo: ScoreInfo, value: int) -> None:
        """
        
        :param scoreInfo: 
        :param value: 
        """
    def ToString(self) -> str:
        """"""