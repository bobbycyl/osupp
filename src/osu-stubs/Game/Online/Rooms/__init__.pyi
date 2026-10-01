from Newtonsoft.Json.Linq import JToken
from System import Array
from System.Collections.Generic import Dictionary
from System.Collections.Generic import IDictionary
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IReadOnlyCollection
from System.Collections.Generic import IReadOnlyList
from System.Collections.Generic import List
from System.ComponentModel import INotifyPropertyChanged
from System.ComponentModel import PropertyChangedEventHandler
from System import DateTimeOffset
from System import Enum
from System import Exception
from System import IEquatable
from System import Object
from System import TimeSpan
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Framework.Bindables import IBindable
from osu.Game.Beatmaps import BeatmapInfo
from osu.Game.Beatmaps import IBeatmapInfo
from osu.Game.Online.API import APIFailureHandler
from osu.Game.Online.API import APIMod
from osu.Game.Online.API import APIRequest
from osu.Game.Online.API import APIRequestCompletionState
from osu.Game.Online.API import APISuccessHandler
from osu.Game.Online.API import IAPIProvider
from osu.Game.Online.API.Requests import Cursor
from osu.Game.Online.API.Requests import ResponseWithCursor
from osu.Game.Online.API.Requests.Responses import APIUser
from osu.Game.Online.API.Requests.Responses import APIUserScoreAggregate
from osu.Game.Online.API.Requests.Responses import SoloScoreInfo
from osu.Game.Online import DownloadState
from osu.Game.Online.Multiplayer import MultiplayerRoom
from osu.Game.Online.Multiplayer import QueueMode
from osu.Game.Online.Rooms.Room import RoomDifficultyRange
from osu.Game.Online.Rooms.Room import RoomPlaylistItemStats
from osu.Game.Rulesets import RulesetStore
from osu.Game.Rulesets.Scoring import HitResult
from osu.Game.Scoring import ScoreInfo
from osu.Game.Scoring import ScoreManager
from osu.Game.Scoring import ScoreRank
from osu.Game.Screens.OnlinePlay.Lounge.Components import LoungeFilterCriteria
from osu.Game.Utils import Optional
from typing import Final
from typing import Generic
from typing import Optional
from typing import TypeVar
from typing import overload
T = TypeVar("T")
class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...
class APICreatedRoom(Room, INotifyPropertyChanged):
    """"""
    def __init__(self):
        """"""
    @property
    def AutoSkip(self) -> bool:
        """
        
        :return: 
        """
    @AutoSkip.setter
    def AutoSkip(self, value: bool) -> None: ...
    @property
    def AutoStartDuration(self) -> TimeSpan:
        """
        
        :return: 
        """
    @AutoStartDuration.setter
    def AutoStartDuration(self, value: TimeSpan) -> None: ...
    @property
    def Availability(self) -> RoomAvailability:
        """
        
        :return: 
        """
    @Availability.setter
    def Availability(self, value: RoomAvailability) -> None: ...
    @property
    def Category(self) -> RoomCategory:
        """
        
        :return: 
        """
    @Category.setter
    def Category(self, value: RoomCategory) -> None: ...
    @property
    def ChannelId(self) -> int:
        """
        
        :return: 
        """
    @ChannelId.setter
    def ChannelId(self, value: int) -> None: ...
    @property
    def CurrentPlaylistItem(self) -> PlaylistItem:
        """
        
        :return: 
        """
    @CurrentPlaylistItem.setter
    def CurrentPlaylistItem(self, value: PlaylistItem) -> None: ...
    @property
    def DifficultyRange(self) -> Room.RoomDifficultyRange:
        """
        
        :return: 
        """
    @DifficultyRange.setter
    def DifficultyRange(self, value: Room.RoomDifficultyRange) -> None: ...
    @property
    def Duration(self) -> Optional[TimeSpan]:
        """
        
        :return: 
        """
    @Duration.setter
    def Duration(self, value: Optional[TimeSpan]) -> None: ...
    @property
    def EndDate(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @EndDate.setter
    def EndDate(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def Error(self) -> str:
        """
        
        :return: 
        """
    @Error.setter
    def Error(self, value: str) -> None: ...
    @property
    def HasEnded(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasPassword(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Host(self) -> APIUser:
        """
        
        :return: 
        """
    @Host.setter
    def Host(self, value: APIUser) -> None: ...
    @property
    def MaxAttempts(self) -> Optional[int]:
        """
        
        :return: 
        """
    @MaxAttempts.setter
    def MaxAttempts(self, value: Optional[int]) -> None: ...
    @property
    def MaxParticipants(self) -> Optional[int]:
        """
        
        :return: 
        """
    @MaxParticipants.setter
    def MaxParticipants(self, value: Optional[int]) -> None: ...
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def ParticipantCount(self) -> int:
        """
        
        :return: 
        """
    @ParticipantCount.setter
    def ParticipantCount(self, value: int) -> None: ...
    @property
    def Password(self) -> str:
        """
        
        :return: 
        """
    @Password.setter
    def Password(self, value: str) -> None: ...
    @property
    def Pinned(self) -> bool:
        """
        
        :return: 
        """
    @Pinned.setter
    def Pinned(self, value: bool) -> None: ...
    @property
    def Playlist(self) -> IReadOnlyList[PlaylistItem]:
        """
        
        :return: 
        """
    @Playlist.setter
    def Playlist(self, value: IReadOnlyList[PlaylistItem]) -> None: ...
    @property
    def PlaylistItemStats(self) -> Room.RoomPlaylistItemStats:
        """
        
        :return: 
        """
    @PlaylistItemStats.setter
    def PlaylistItemStats(self, value: Room.RoomPlaylistItemStats) -> None: ...
    @property
    def QueueMode(self) -> QueueMode:
        """
        
        :return: 
        """
    @QueueMode.setter
    def QueueMode(self, value: QueueMode) -> None: ...
    @property
    def RecentParticipants(self) -> IReadOnlyList[APIUser]:
        """
        
        :return: 
        """
    @RecentParticipants.setter
    def RecentParticipants(self, value: IReadOnlyList[APIUser]) -> None: ...
    @property
    def RoomID(self) -> Optional[int]:
        """
        
        :return: 
        """
    @RoomID.setter
    def RoomID(self, value: Optional[int]) -> None: ...
    @property
    def StartDate(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @StartDate.setter
    def StartDate(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def Status(self) -> RoomStatus:
        """
        
        :return: 
        """
    @Status.setter
    def Status(self, value: RoomStatus) -> None: ...
    @property
    def Type(self) -> MatchType:
        """
        
        :return: 
        """
    @Type.setter
    def Type(self, value: MatchType) -> None: ...
    @property
    def UserScore(self) -> PlaylistAggregateScore:
        """
        
        :return: 
        """
    @UserScore.setter
    def UserScore(self, value: PlaylistAggregateScore) -> None: ...
    def CopyFrom(self, other: Room) -> None:
        """
        
        :param other: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    PropertyChanged: EventType[PropertyChangedEventHandler] = ...
    """"""
class APILeaderboard(Object):
    """"""
    Leaderboard: Final[List[APIUserScoreAggregate]] = ...
    """
    
    :return: 
    """
    UserScore: Final[APIUserScoreAggregate] = ...
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
class APIScoreToken(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def ID(self) -> int:
        """
        
        :return: 
        """
    @ID.setter
    def ID(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class BeatmapAvailability(Object, IEquatable[BeatmapAvailability]):
    """"""
    DownloadProgress: Final[Optional[float]] = ...
    """
    
    :return: 
    """
    State: Final[DownloadState] = ...
    """
    
    :return: 
    """
    def __init__(self, state: DownloadState, downloadProgress: Optional[float] = ...):
        """
        
        :param state: 
        :param downloadProgress: 
        """
    @classmethod
    def Downloading(cls, progress: float) -> BeatmapAvailability:
        """
        
        :param progress: 
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: BeatmapAvailability) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Importing(cls) -> BeatmapAvailability:
        """
        
        :return: 
        """
    @classmethod
    def LocallyAvailable(cls) -> BeatmapAvailability:
        """
        
        :return: 
        """
    @classmethod
    def NotDownloaded(cls) -> BeatmapAvailability:
        """
        
        :return: 
        """
    def ToString(self) -> str:
        """"""
    @classmethod
    def Unknown(cls) -> BeatmapAvailability:
        """
        
        :return: 
        """
class CreateRoomRequest(APIRequest[APICreatedRoom]):
    """"""
    Room: Final[Room] = ...
    """
    
    :return: 
    """
    def __init__(self, room: Room):
        """
        
        :param room: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> APICreatedRoom:
        """
        
        :return: 
        """
    def AttachAPI(self, apiAccess: IAPIProvider) -> None:
        """
        
        :param apiAccess: 
        """
    def Cancel(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Fail(self, e: Exception) -> None:
        """
        
        :param e: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Perform(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    Failure: EventType[APIFailureHandler] = ...
    """"""
    Success: EventType[APISuccessHandler[APICreatedRoom]] = ...
    """"""
class CreateRoomScoreRequest(APIRequest[APIScoreToken]):
    """"""
    def __init__(self, roomId: int, playlistItemId: int, beatmapInfo: BeatmapInfo, rulesetId: int, versionHash: str):
        """
        
        :param roomId: 
        :param playlistItemId: 
        :param beatmapInfo: 
        :param rulesetId: 
        :param versionHash: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> APIScoreToken:
        """
        
        :return: 
        """
    def AttachAPI(self, apiAccess: IAPIProvider) -> None:
        """
        
        :param apiAccess: 
        """
    def Cancel(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Fail(self, e: Exception) -> None:
        """
        
        :param e: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Perform(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    Failure: EventType[APIFailureHandler] = ...
    """"""
    Success: EventType[APISuccessHandler[APIScoreToken]] = ...
    """"""
class GetRoomLeaderboardRequest(APIRequest[APILeaderboard]):
    """"""
    def __init__(self, roomId: int):
        """
        
        :param roomId: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> APILeaderboard:
        """
        
        :return: 
        """
    def AttachAPI(self, apiAccess: IAPIProvider) -> None:
        """
        
        :param apiAccess: 
        """
    def Cancel(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Fail(self, e: Exception) -> None:
        """
        
        :param e: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Perform(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    Failure: EventType[APIFailureHandler] = ...
    """"""
    Success: EventType[APISuccessHandler[APILeaderboard]] = ...
    """"""
class GetRoomRequest(APIRequest[Room]):
    """"""
    RoomId: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self, roomId: int):
        """
        
        :param roomId: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> Room:
        """
        
        :return: 
        """
    def AttachAPI(self, apiAccess: IAPIProvider) -> None:
        """
        
        :param apiAccess: 
        """
    def Cancel(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Fail(self, e: Exception) -> None:
        """
        
        :param e: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Perform(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    Failure: EventType[APIFailureHandler] = ...
    """"""
    Success: EventType[APISuccessHandler[Room]] = ...
    """"""
class GetRoomsRequest(APIRequest[List[Room]]):
    """"""
    def __init__(self, filterCriteria: LoungeFilterCriteria):
        """
        
        :param filterCriteria: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> List[Room]:
        """
        
        :return: 
        """
    def AttachAPI(self, apiAccess: IAPIProvider) -> None:
        """
        
        :param apiAccess: 
        """
    def Cancel(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Fail(self, e: Exception) -> None:
        """
        
        :param e: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Perform(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    Failure: EventType[APIFailureHandler] = ...
    """"""
    Success: EventType[APISuccessHandler[List[Room]]] = ...
    """"""
class IndexPlaylistScoresRequest(APIRequest[IndexedMultiplayerScores]):
    """"""
    Cursor: Final[Cursor] = ...
    """
    
    :return: 
    """
    IndexParams: Final[IndexScoresParams] = ...
    """
    
    :return: 
    """
    PlaylistItemId: Final[int] = ...
    """
    
    :return: 
    """
    RoomId: Final[int] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, roomId: int, playlistItemId: int):
        """
        
        :param roomId: 
        :param playlistItemId: 
        """
    @overload
    def __init__(self, roomId: int, playlistItemId: int, cursor: Cursor, indexParams: IndexScoresParams):
        """
        
        :param roomId: 
        :param playlistItemId: 
        :param cursor: 
        :param indexParams: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> IndexedMultiplayerScores:
        """
        
        :return: 
        """
    def AttachAPI(self, apiAccess: IAPIProvider) -> None:
        """
        
        :param apiAccess: 
        """
    def Cancel(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Fail(self, e: Exception) -> None:
        """
        
        :param e: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Perform(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    Failure: EventType[APIFailureHandler] = ...
    """"""
    Success: EventType[APISuccessHandler[IndexedMultiplayerScores]] = ...
    """"""
class IndexScoresParams(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Properties(self) -> IDictionary[str, JToken]:
        """
        
        :return: 
        """
    @Properties.setter
    def Properties(self, value: IDictionary[str, JToken]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class IndexedMultiplayerScores(MultiplayerScores):
    """"""
    Cursor: Final[Cursor] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def Params(self) -> IndexScoresParams:
        """
        
        :return: 
        """
    @Params.setter
    def Params(self, value: IndexScoresParams) -> None: ...
    @property
    def Scores(self) -> List[MultiplayerScore]:
        """
        
        :return: 
        """
    @Scores.setter
    def Scores(self, value: List[MultiplayerScore]) -> None: ...
    @property
    def TotalScores(self) -> Optional[int]:
        """
        
        :return: 
        """
    @TotalScores.setter
    def TotalScores(self, value: Optional[int]) -> None: ...
    @property
    def UserScore(self) -> MultiplayerScore:
        """
        
        :return: 
        """
    @UserScore.setter
    def UserScore(self, value: MultiplayerScore) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class ItemAttemptsCount(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Attempts(self) -> int:
        """
        
        :return: 
        """
    @Attempts.setter
    def Attempts(self, value: int) -> None: ...
    @property
    def Passed(self) -> bool:
        """
        
        :return: 
        """
    @Passed.setter
    def Passed(self, value: bool) -> None: ...
    @property
    def PlaylistItemID(self) -> int:
        """
        
        :return: 
        """
    @PlaylistItemID.setter
    def PlaylistItemID(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class JoinRoomRequest(APIRequest[Room]):
    """"""
    Password: Final[str] = ...
    """
    
    :return: 
    """
    Room: Final[Room] = ...
    """
    
    :return: 
    """
    def __init__(self, room: Room, password: str):
        """
        
        :param room: 
        :param password: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> Room:
        """
        
        :return: 
        """
    def AttachAPI(self, apiAccess: IAPIProvider) -> None:
        """
        
        :param apiAccess: 
        """
    def Cancel(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Fail(self, e: Exception) -> None:
        """
        
        :param e: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Perform(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    Failure: EventType[APIFailureHandler] = ...
    """"""
    Success: EventType[APISuccessHandler[Room]] = ...
    """"""
class MatchType(Enum):
    """"""
    Playlists: MatchType = ...
    """"""
    HeadToHead: MatchType = ...
    """"""
    TeamVersus: MatchType = ...
    """"""
    Matchmaking: MatchType = ...
    """"""
    RankedPlay: MatchType = ...
    """"""
class MatchTypeExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsMatchmakingType(cls, type: MatchType) -> bool:
        """
        
        :param type: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class MultiplayerPlaylistItem(Object, IEquatable[MultiplayerPlaylistItem]):
    """"""
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, item: PlaylistItem):
        """
        
        :param item: 
        """
    @property
    def AllowedMods(self) -> IEnumerable[APIMod]:
        """
        
        :return: 
        """
    @AllowedMods.setter
    def AllowedMods(self, value: IEnumerable[APIMod]) -> None: ...
    @property
    def BeatmapChecksum(self) -> str:
        """
        
        :return: 
        """
    @BeatmapChecksum.setter
    def BeatmapChecksum(self, value: str) -> None: ...
    @property
    def BeatmapID(self) -> int:
        """
        
        :return: 
        """
    @BeatmapID.setter
    def BeatmapID(self, value: int) -> None: ...
    @property
    def Expired(self) -> bool:
        """
        
        :return: 
        """
    @Expired.setter
    def Expired(self, value: bool) -> None: ...
    @property
    def Freestyle(self) -> bool:
        """
        
        :return: 
        """
    @Freestyle.setter
    def Freestyle(self, value: bool) -> None: ...
    @property
    def ID(self) -> int:
        """
        
        :return: 
        """
    @ID.setter
    def ID(self, value: int) -> None: ...
    @property
    def OwnerID(self) -> int:
        """
        
        :return: 
        """
    @OwnerID.setter
    def OwnerID(self, value: int) -> None: ...
    @property
    def PlayedAt(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @PlayedAt.setter
    def PlayedAt(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def PlaylistOrder(self) -> int:
        """
        
        :return: 
        """
    @PlaylistOrder.setter
    def PlaylistOrder(self, value: int) -> None: ...
    @property
    def RequiredMods(self) -> IEnumerable[APIMod]:
        """
        
        :return: 
        """
    @RequiredMods.setter
    def RequiredMods(self, value: IEnumerable[APIMod]) -> None: ...
    @property
    def RulesetID(self) -> int:
        """
        
        :return: 
        """
    @RulesetID.setter
    def RulesetID(self, value: int) -> None: ...
    @property
    def StarRating(self) -> float:
        """
        
        :return: 
        """
    @StarRating.setter
    def StarRating(self, value: float) -> None: ...
    def Clone(self) -> MultiplayerPlaylistItem:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: MultiplayerPlaylistItem) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class MultiplayerScore(Object):
    """"""
    MaximumStatistics: Final[Dictionary[HitResult, int]] = ...
    """
    
    :return: 
    """
    Statistics: Final[Dictionary[HitResult, int]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def Accuracy(self) -> float:
        """
        
        :return: 
        """
    @Accuracy.setter
    def Accuracy(self, value: float) -> None: ...
    @property
    def BeatmapId(self) -> int:
        """
        
        :return: 
        """
    @BeatmapId.setter
    def BeatmapId(self, value: int) -> None: ...
    @property
    def EndedAt(self) -> DateTimeOffset:
        """
        
        :return: 
        """
    @EndedAt.setter
    def EndedAt(self, value: DateTimeOffset) -> None: ...
    @property
    def HasReplay(self) -> bool:
        """
        
        :return: 
        """
    @HasReplay.setter
    def HasReplay(self, value: bool) -> None: ...
    @property
    def ID(self) -> int:
        """
        
        :return: 
        """
    @ID.setter
    def ID(self, value: int) -> None: ...
    @property
    def MaxCombo(self) -> int:
        """
        
        :return: 
        """
    @MaxCombo.setter
    def MaxCombo(self, value: int) -> None: ...
    @property
    def Mods(self) -> Array[APIMod]:
        """
        
        :return: 
        """
    @Mods.setter
    def Mods(self, value: Array[APIMod]) -> None: ...
    @property
    def PP(self) -> Optional[float]:
        """
        
        :return: 
        """
    @PP.setter
    def PP(self, value: Optional[float]) -> None: ...
    @property
    def Passed(self) -> bool:
        """
        
        :return: 
        """
    @Passed.setter
    def Passed(self, value: bool) -> None: ...
    @property
    def Position(self) -> Optional[int]:
        """
        
        :return: 
        """
    @Position.setter
    def Position(self, value: Optional[int]) -> None: ...
    @property
    def Rank(self) -> ScoreRank:
        """
        
        :return: 
        """
    @Rank.setter
    def Rank(self, value: ScoreRank) -> None: ...
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @Ranked.setter
    def Ranked(self, value: bool) -> None: ...
    @property
    def RulesetId(self) -> int:
        """
        
        :return: 
        """
    @RulesetId.setter
    def RulesetId(self, value: int) -> None: ...
    @property
    def ScoresAround(self) -> MultiplayerScoresAround:
        """
        
        :return: 
        """
    @ScoresAround.setter
    def ScoresAround(self, value: MultiplayerScoresAround) -> None: ...
    @property
    def TotalScore(self) -> int:
        """
        
        :return: 
        """
    @TotalScore.setter
    def TotalScore(self, value: int) -> None: ...
    @property
    def User(self) -> APIUser:
        """
        
        :return: 
        """
    @User.setter
    def User(self, value: APIUser) -> None: ...
    def CreateScoreInfo(self, scoreManager: ScoreManager, rulesets: RulesetStore, beatmap: BeatmapInfo) -> ScoreInfo:
        """
        
        :param scoreManager: 
        :param rulesets: 
        :param beatmap: 
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class MultiplayerScores(ResponseWithCursor):
    """"""
    Cursor: Final[Cursor] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def Params(self) -> IndexScoresParams:
        """
        
        :return: 
        """
    @Params.setter
    def Params(self, value: IndexScoresParams) -> None: ...
    @property
    def Scores(self) -> List[MultiplayerScore]:
        """
        
        :return: 
        """
    @Scores.setter
    def Scores(self, value: List[MultiplayerScore]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class MultiplayerScoresAround(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Higher(self) -> MultiplayerScores:
        """
        
        :return: 
        """
    @Higher.setter
    def Higher(self, value: MultiplayerScores) -> None: ...
    @property
    def Lower(self) -> MultiplayerScores:
        """
        
        :return: 
        """
    @Lower.setter
    def Lower(self, value: MultiplayerScores) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class PartRoomRequest(APIRequest):
    """"""
    def __init__(self, room: Room):
        """
        
        :param room: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    def AttachAPI(self, apiAccess: IAPIProvider) -> None:
        """
        
        :param apiAccess: 
        """
    def Cancel(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Fail(self, e: Exception) -> None:
        """
        
        :param e: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Perform(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    Failure: EventType[APIFailureHandler] = ...
    """"""
    Success: EventType[APISuccessHandler] = ...
    """"""
class PlaylistAggregateScore(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def PlaylistItemAttempts(self) -> Array[ItemAttemptsCount]:
        """
        
        :return: 
        """
    @PlaylistItemAttempts.setter
    def PlaylistItemAttempts(self, value: Array[ItemAttemptsCount]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class PlaylistExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetCurrentItem(cls, playlist: IReadOnlyCollection[PlaylistItem]) -> PlaylistItem:
        """
        
        :param playlist: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetHistoricalItems(cls, playlist: IEnumerable[PlaylistItem]) -> IEnumerable[PlaylistItem]:
        """
        
        :param playlist: 
        :return: 
        """
    @classmethod
    def GetTotalDuration(cls, playlist: IReadOnlyList[PlaylistItem], rulesetStore: RulesetStore) -> str:
        """
        
        :param playlist: 
        :param rulesetStore: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetUpcomingItems(cls, playlist: IEnumerable[PlaylistItem]) -> IEnumerable[PlaylistItem]:
        """
        
        :param playlist: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class PlaylistItem(Object, IEquatable[PlaylistItem]):
    """"""
    @overload
    def __init__(self, beatmap: IBeatmapInfo):
        """
        
        :param beatmap: 
        """
    @overload
    def __init__(self, item: MultiplayerPlaylistItem):
        """
        
        :param item: 
        """
    @property
    def AllowedMods(self) -> Array[APIMod]:
        """
        
        :return: 
        """
    @AllowedMods.setter
    def AllowedMods(self, value: Array[APIMod]) -> None: ...
    @property
    def Beatmap(self) -> IBeatmapInfo:
        """
        
        :return: 
        """
    @property
    def Completed(self) -> IBindable[bool]:
        """
        
        :return: 
        """
    @property
    def Expired(self) -> bool:
        """
        
        :return: 
        """
    @Expired.setter
    def Expired(self, value: bool) -> None: ...
    @property
    def Freestyle(self) -> bool:
        """
        
        :return: 
        """
    @Freestyle.setter
    def Freestyle(self, value: bool) -> None: ...
    @property
    def ID(self) -> int:
        """
        
        :return: 
        """
    @ID.setter
    def ID(self, value: int) -> None: ...
    @property
    def OwnerID(self) -> int:
        """
        
        :return: 
        """
    @OwnerID.setter
    def OwnerID(self, value: int) -> None: ...
    @property
    def PlayedAt(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @PlayedAt.setter
    def PlayedAt(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def PlaylistOrder(self) -> Optional[int]:
        """
        
        :return: 
        """
    @PlaylistOrder.setter
    def PlaylistOrder(self, value: Optional[int]) -> None: ...
    @property
    def RequiredMods(self) -> Array[APIMod]:
        """
        
        :return: 
        """
    @RequiredMods.setter
    def RequiredMods(self, value: Array[APIMod]) -> None: ...
    @property
    def RulesetID(self) -> int:
        """
        
        :return: 
        """
    @RulesetID.setter
    def RulesetID(self, value: int) -> None: ...
    @property
    def Valid(self) -> IBindable[bool]:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: PlaylistItem) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MarkCompleted(self) -> None:
        """"""
    def MarkInvalid(self) -> None:
        """"""
    def ShouldSerializeID(self) -> bool:
        """
        
        :return: 
        """
    def ShouldSerializeapiBeatmap(self) -> bool:
        """
        
        :return: 
        """
    def ToString(self) -> str:
        """"""
    def With(self, id: Optional[int] = ..., beatmap: Optional[IBeatmapInfo] = ..., playlistOrder: Optional[Optional[int]] = ..., ruleset: Optional[int] = ...) -> PlaylistItem:
        """
        
        :param id: 
        :param beatmap: 
        :param playlistOrder: 
        :param ruleset: 
        :return: 
        """
class Room(Object, INotifyPropertyChanged):
    """"""
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, room: MultiplayerRoom):
        """
        
        :param room: 
        """
    @property
    def AutoSkip(self) -> bool:
        """
        
        :return: 
        """
    @AutoSkip.setter
    def AutoSkip(self, value: bool) -> None: ...
    @property
    def AutoStartDuration(self) -> TimeSpan:
        """
        
        :return: 
        """
    @AutoStartDuration.setter
    def AutoStartDuration(self, value: TimeSpan) -> None: ...
    @property
    def Availability(self) -> RoomAvailability:
        """
        
        :return: 
        """
    @Availability.setter
    def Availability(self, value: RoomAvailability) -> None: ...
    @property
    def Category(self) -> RoomCategory:
        """
        
        :return: 
        """
    @Category.setter
    def Category(self, value: RoomCategory) -> None: ...
    @property
    def ChannelId(self) -> int:
        """
        
        :return: 
        """
    @ChannelId.setter
    def ChannelId(self, value: int) -> None: ...
    @property
    def CurrentPlaylistItem(self) -> PlaylistItem:
        """
        
        :return: 
        """
    @CurrentPlaylistItem.setter
    def CurrentPlaylistItem(self, value: PlaylistItem) -> None: ...
    @property
    def DifficultyRange(self) -> Room.RoomDifficultyRange:
        """
        
        :return: 
        """
    @DifficultyRange.setter
    def DifficultyRange(self, value: Room.RoomDifficultyRange) -> None: ...
    @property
    def Duration(self) -> Optional[TimeSpan]:
        """
        
        :return: 
        """
    @Duration.setter
    def Duration(self, value: Optional[TimeSpan]) -> None: ...
    @property
    def EndDate(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @EndDate.setter
    def EndDate(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def HasEnded(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasPassword(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Host(self) -> APIUser:
        """
        
        :return: 
        """
    @Host.setter
    def Host(self, value: APIUser) -> None: ...
    @property
    def MaxAttempts(self) -> Optional[int]:
        """
        
        :return: 
        """
    @MaxAttempts.setter
    def MaxAttempts(self, value: Optional[int]) -> None: ...
    @property
    def MaxParticipants(self) -> Optional[int]:
        """
        
        :return: 
        """
    @MaxParticipants.setter
    def MaxParticipants(self, value: Optional[int]) -> None: ...
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def ParticipantCount(self) -> int:
        """
        
        :return: 
        """
    @ParticipantCount.setter
    def ParticipantCount(self, value: int) -> None: ...
    @property
    def Password(self) -> str:
        """
        
        :return: 
        """
    @Password.setter
    def Password(self, value: str) -> None: ...
    @property
    def Pinned(self) -> bool:
        """
        
        :return: 
        """
    @Pinned.setter
    def Pinned(self, value: bool) -> None: ...
    @property
    def Playlist(self) -> IReadOnlyList[PlaylistItem]:
        """
        
        :return: 
        """
    @Playlist.setter
    def Playlist(self, value: IReadOnlyList[PlaylistItem]) -> None: ...
    @property
    def PlaylistItemStats(self) -> Room.RoomPlaylistItemStats:
        """
        
        :return: 
        """
    @PlaylistItemStats.setter
    def PlaylistItemStats(self, value: Room.RoomPlaylistItemStats) -> None: ...
    @property
    def QueueMode(self) -> QueueMode:
        """
        
        :return: 
        """
    @QueueMode.setter
    def QueueMode(self, value: QueueMode) -> None: ...
    @property
    def RecentParticipants(self) -> IReadOnlyList[APIUser]:
        """
        
        :return: 
        """
    @RecentParticipants.setter
    def RecentParticipants(self, value: IReadOnlyList[APIUser]) -> None: ...
    @property
    def RoomID(self) -> Optional[int]:
        """
        
        :return: 
        """
    @RoomID.setter
    def RoomID(self, value: Optional[int]) -> None: ...
    @property
    def StartDate(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @StartDate.setter
    def StartDate(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def Status(self) -> RoomStatus:
        """
        
        :return: 
        """
    @Status.setter
    def Status(self, value: RoomStatus) -> None: ...
    @property
    def Type(self) -> MatchType:
        """
        
        :return: 
        """
    @Type.setter
    def Type(self, value: MatchType) -> None: ...
    @property
    def UserScore(self) -> PlaylistAggregateScore:
        """
        
        :return: 
        """
    @UserScore.setter
    def UserScore(self, value: PlaylistAggregateScore) -> None: ...
    def CopyFrom(self, other: Room) -> None:
        """
        
        :param other: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    PropertyChanged: EventType[PropertyChangedEventHandler] = ...
    """"""
    class RoomDifficultyRange(Object):
        """"""
        Max: Final[float] = ...
        """"""
        Min: Final[float] = ...
        """"""
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
    class RoomPlaylistItemStats(Object):
        """"""
        CountActive: Final[int] = ...
        """"""
        CountTotal: Final[int] = ...
        """"""
        RulesetIDs: Final[Array[int]] = ...
        """"""
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
class RoomAvailability(Enum):
    """"""
    Public: RoomAvailability = ...
    """"""
    FriendsOnly: RoomAvailability = ...
    """"""
    InviteOnly: RoomAvailability = ...
    """"""
class RoomCategory(Enum):
    """"""
    Normal: RoomCategory = ...
    """"""
    Spotlight: RoomCategory = ...
    """"""
    FeaturedArtist: RoomCategory = ...
    """"""
    DailyChallenge: RoomCategory = ...
    """"""
class RoomExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetOnlineURL(cls, room: Room, api: IAPIProvider) -> str:
        """
        
        :param room: 
        :param api: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class RoomStatus(Enum):
    """"""
    Idle: RoomStatus = ...
    """"""
    Playing: RoomStatus = ...
    """"""
class ShowPlaylistScoreRequest(APIRequest[MultiplayerScore]):
    """"""
    def __init__(self, roomId: int, playlistItemId: int, scoreId: int):
        """
        
        :param roomId: 
        :param playlistItemId: 
        :param scoreId: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> MultiplayerScore:
        """
        
        :return: 
        """
    def AttachAPI(self, apiAccess: IAPIProvider) -> None:
        """
        
        :param apiAccess: 
        """
    def Cancel(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Fail(self, e: Exception) -> None:
        """
        
        :param e: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Perform(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    Failure: EventType[APIFailureHandler] = ...
    """"""
    Success: EventType[APISuccessHandler[MultiplayerScore]] = ...
    """"""
class ShowPlaylistUserScoreRequest(APIRequest[MultiplayerScore]):
    """"""
    def __init__(self, roomId: int, playlistItemId: int, userId: int):
        """
        
        :param roomId: 
        :param playlistItemId: 
        :param userId: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> MultiplayerScore:
        """
        
        :return: 
        """
    def AttachAPI(self, apiAccess: IAPIProvider) -> None:
        """
        
        :param apiAccess: 
        """
    def Cancel(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Fail(self, e: Exception) -> None:
        """
        
        :param e: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Perform(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    Failure: EventType[APIFailureHandler] = ...
    """"""
    Success: EventType[APISuccessHandler[MultiplayerScore]] = ...
    """"""
class SubmitRoomScoreRequest(SubmitScoreRequest):
    """"""
    Score: Final[SoloScoreInfo] = ...
    """
    
    :return: 
    """
    def __init__(self, scoreInfo: ScoreInfo, scoreId: int, roomId: int, playlistItemId: int):
        """
        
        :param scoreInfo: 
        :param scoreId: 
        :param roomId: 
        :param playlistItemId: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> MultiplayerScore:
        """
        
        :return: 
        """
    def AttachAPI(self, apiAccess: IAPIProvider) -> None:
        """
        
        :param apiAccess: 
        """
    def Cancel(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Fail(self, e: Exception) -> None:
        """
        
        :param e: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Perform(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    Failure: EventType[APIFailureHandler] = ...
    """"""
    Success: EventType[APISuccessHandler[MultiplayerScore]] = ...
    """"""
class SubmitScoreRequest(ABC, APIRequest[MultiplayerScore]):
    """"""
    Score: Final[SoloScoreInfo] = ...
    """
    
    :return: 
    """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> MultiplayerScore:
        """
        
        :return: 
        """
    def AttachAPI(self, apiAccess: IAPIProvider) -> None:
        """
        
        :param apiAccess: 
        """
    def Cancel(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Fail(self, e: Exception) -> None:
        """
        
        :param e: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Perform(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    Failure: EventType[APIFailureHandler] = ...
    """"""
    Success: EventType[APISuccessHandler[MultiplayerScore]] = ...
    """"""