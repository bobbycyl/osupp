from Newtonsoft.Json.Linq import JToken
from System import Action
from System import Array
from System.Collections.Generic import Dictionary
from System.Collections.Generic import HashSet
from System.Collections.Generic import IDictionary
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IReadOnlyCollection
from System.Collections.Generic import IReadOnlyList
from System.Collections.Generic import List
from System import Enum
from System import Exception
from System import IDisposable
from System import IEquatable
from System.IO import Stream
from System.Net.Http.Headers import HttpResponseHeaders
from System.Net.Http import HttpMethod
from System.Net import HttpStatusCode
from System import Object
from System.Threading import CancellationToken
from System.Threading.Tasks import Task
from System import Type
from System import ValueType
from __future__ import annotations
from abc import ABC
from osu.Framework.IO.Network import RequestParameterType
from osu.Game.Beatmaps import IBeatmapInfo
from osu.Game.Beatmaps import IBeatmapSetInfo
from osu.Game.Localisation import Language
from osu.Game.Online.API import APIFailureHandler
from osu.Game.Online.API import APIProgressHandler
from osu.Game.Online.API import APIRequest
from osu.Game.Online.API import APIRequestCompletionState
from osu.Game.Online.API import APISuccessHandler
from osu.Game.Online.API import ArchiveDownloadRequest
from osu.Game.Online.API import IAPIProvider
from osu.Game.Online.API import OsuJsonWebRequest
from osu.Game.Online.API.Requests.Responses import APIBeatmap
from osu.Game.Online.API.Requests.Responses import APIBeatmapSet
from osu.Game.Online.API.Requests.Responses import APIChangelogBuild
from osu.Game.Online.API.Requests.Responses import APIChangelogIndex
from osu.Game.Online.API.Requests.Responses import APIChatChannel
from osu.Game.Online.API.Requests.Responses import APIKudosuHistory
from osu.Game.Online.API.Requests.Responses import APIMe
from osu.Game.Online.API.Requests.Responses import APIMenuContent
from osu.Game.Online.API.Requests.Responses import APINewsPost
from osu.Game.Online.API.Requests.Responses import APINewsSidebar
from osu.Game.Online.API.Requests.Responses import APINotificationsBundle
from osu.Game.Online.API.Requests.Responses import APIRecentActivity
from osu.Game.Online.API.Requests.Responses import APIRelation
from osu.Game.Online.API.Requests.Responses import APIScoresCollection
from osu.Game.Online.API.Requests.Responses import APISeasonalBackgrounds
from osu.Game.Online.API.Requests.Responses import APISpotlight
from osu.Game.Online.API.Requests.Responses import APITagCollection
from osu.Game.Online.API.Requests.Responses import APIUser
from osu.Game.Online.API.Requests.Responses import APIUserMostPlayedBeatmap
from osu.Game.Online.API.Requests.Responses import APIWikiPage
from osu.Game.Online.API.Requests.Responses import ChatAckResponse
from osu.Game.Online.API.Requests.Responses import CommentBundle
from osu.Game.Online.API.Requests.Responses import GetChannelResponse
from osu.Game.Online.API.Requests.Responses import GetMyFavouriteBeatmapSetsResponse
from osu.Game.Online.API.Requests.Responses import PutBeatmapSetResponse
from osu.Game.Online.API.Requests.Responses import SessionVerificationMethod
from osu.Game.Online.API.Requests.Responses import SoloScoreInfo
from osu.Game.Online.Chat import Channel
from osu.Game.Online.Chat import Message
from osu.Game.Overlays.BeatmapListing import SearchCategory
from osu.Game.Overlays.BeatmapListing import SearchExplicit
from osu.Game.Overlays.BeatmapListing import SearchExtra
from osu.Game.Overlays.BeatmapListing import SearchGeneral
from osu.Game.Overlays.BeatmapListing import SearchGenre
from osu.Game.Overlays.BeatmapListing import SearchLanguage
from osu.Game.Overlays.BeatmapListing import SearchPlayed
from osu.Game.Overlays.BeatmapListing import SortCriteria
from osu.Game.Overlays.Chat import ChatReportReason
from osu.Game.Overlays.Comments import CommentReportReason
from osu.Game.Overlays.Comments import CommentsSortCriteria
from osu.Game.Overlays.Profile import UserReportReason
from osu.Game.Overlays.Rankings import RankingsSortCriteria
from osu.Game.Overlays import SortDirection
from osu.Game.Rulesets import IRulesetInfo
from osu.Game.Rulesets.Mods import IMod
from osu.Game.Rulesets import RulesetInfo
from osu.Game.Scoring import IScoreInfo
from osu.Game.Scoring import ScoreRank
from osu.Game.Screens.Edit.Submission import BeatmapSubmissionSettings
from osu.Game.Screens.Play.Leaderboards import BeatmapLeaderboardScope
from osu.Game.Users import CountryCode
from osu.Game.Users import CountryStatistics
from osu.Game.Users import UserStatistics
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Optional
from typing import TypeVar
from typing import overload
T = TypeVar("T")
TModel = TypeVar("TModel")
class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...
class APIUploadRequest(ABC, APIRequest):
    """"""
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
    Progressed: EventType[APIProgressHandler] = ...
    """"""
    Success: EventType[APISuccessHandler] = ...
    """"""
class AddBeatmapTagRequest(APIRequest):
    """"""
    def __init__(self, beatmapID: int, tagID: int):
        """
        
        :param beatmapID: 
        :param tagID: 
        """
    @property
    def BeatmapID(self) -> int:
        """
        
        :return: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def TagID(self) -> int:
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
class AddFriendRequest(APIRequest[AddFriendResponse]):
    """"""
    TargetId: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self, targetId: int):
        """
        
        :param targetId: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> AddFriendResponse:
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
    Success: EventType[APISuccessHandler[AddFriendResponse]] = ...
    """"""
class AddFriendResponse(Object):
    """"""
    UserRelation: Final[APIRelation] = ...
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
class BeatmapApproval(Enum):
    """"""
    Ranked: BeatmapApproval = ...
    """"""
    Approved: BeatmapApproval = ...
    """"""
    Qualified: BeatmapApproval = ...
    """"""
    Loved: BeatmapApproval = ...
    """"""
class BeatmapFavouriteAction(Enum):
    """"""
    Favourite: BeatmapFavouriteAction = ...
    """"""
    UnFavourite: BeatmapFavouriteAction = ...
    """"""
class BeatmapSetLookupType(Enum):
    """"""
    SetId: BeatmapSetLookupType = ...
    """"""
    BeatmapId: BeatmapSetLookupType = ...
    """"""
class BeatmapSetType(Enum):
    """"""
    Favourite: BeatmapSetType = ...
    """"""
    Ranked: BeatmapSetType = ...
    """"""
    Loved: BeatmapSetType = ...
    """"""
    Pending: BeatmapSetType = ...
    """"""
    Guest: BeatmapSetType = ...
    """"""
    Graveyard: BeatmapSetType = ...
    """"""
    Nominated: BeatmapSetType = ...
    """"""
class BeatmapSubmissionTarget(Enum):
    """"""
    WIP: BeatmapSubmissionTarget = ...
    """"""
    Pending: BeatmapSubmissionTarget = ...
    """"""
class BlockUserRequest(APIRequest):
    """"""
    TargetId: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self, targetId: int):
        """
        
        :param targetId: 
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
class ChatAckRequest(APIRequest[ChatAckResponse]):
    """"""
    SinceMessageId: Final[Optional[int]] = ...
    """
    
    :return: 
    """
    SinceSilenceId: Final[Optional[int]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> ChatAckResponse:
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
    Success: EventType[APISuccessHandler[ChatAckResponse]] = ...
    """"""
class ChatReportRequest(APIRequest):
    """"""
    Comment: Final[str] = ...
    """
    
    :return: 
    """
    MessageId: Final[Optional[int]] = ...
    """
    
    :return: 
    """
    Reason: Final[ChatReportReason] = ...
    """
    
    :return: 
    """
    def __init__(self, id: Optional[int], reason: ChatReportReason, comment: str):
        """
        
        :param id: 
        :param reason: 
        :param comment: 
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
class ClosePlaylistRequest(APIRequest):
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
class CommentDeleteRequest(APIRequest[CommentBundle]):
    """"""
    CommentId: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self, id: int):
        """
        
        :param id: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> CommentBundle:
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
    Success: EventType[APISuccessHandler[CommentBundle]] = ...
    """"""
class CommentPostRequest(APIRequest[CommentBundle]):
    """"""
    Commentable: Final[CommentableType] = ...
    """
    
    :return: 
    """
    CommentableId: Final[int] = ...
    """
    
    :return: 
    """
    Message: Final[str] = ...
    """
    
    :return: 
    """
    ParentCommentId: Final[Optional[int]] = ...
    """
    
    :return: 
    """
    def __init__(self, commentable: CommentableType, commentableId: int, message: str, parentCommentId: Optional[int] = ...):
        """
        
        :param commentable: 
        :param commentableId: 
        :param message: 
        :param parentCommentId: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> CommentBundle:
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
    Success: EventType[APISuccessHandler[CommentBundle]] = ...
    """"""
class CommentReportRequest(APIRequest):
    """"""
    Comment: Final[str] = ...
    """
    
    :return: 
    """
    CommentID: Final[int] = ...
    """
    
    :return: 
    """
    Reason: Final[CommentReportReason] = ...
    """
    
    :return: 
    """
    def __init__(self, commentID: int, reason: CommentReportReason, comment: str):
        """
        
        :param commentID: 
        :param reason: 
        :param comment: 
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
class CommentVoteAction(Enum):
    """"""
    Vote: CommentVoteAction = ...
    """"""
    UnVote: CommentVoteAction = ...
    """"""
class CommentVoteRequest(APIRequest[CommentBundle]):
    """"""
    def __init__(self, id: int, action: CommentVoteAction):
        """
        
        :param id: 
        :param action: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> CommentBundle:
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
    Success: EventType[APISuccessHandler[CommentBundle]] = ...
    """"""
class CommentableType(Enum):
    """"""
    Build: CommentableType = ...
    """"""
    Beatmapset: CommentableType = ...
    """"""
    NewsPost: CommentableType = ...
    """"""
class CreateChannelRequest(APIRequest[APIChatChannel]):
    """"""
    Channel: Final[Channel] = ...
    """
    
    :return: 
    """
    def __init__(self, channel: Channel):
        """
        
        :param channel: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> APIChatChannel:
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
    Success: EventType[APISuccessHandler[APIChatChannel]] = ...
    """"""
class CreateNewPrivateMessageRequest(APIRequest[CreateNewPrivateMessageResponse]):
    """"""
    def __init__(self, user: APIUser, message: Message):
        """
        
        :param user: 
        :param message: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> CreateNewPrivateMessageResponse:
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
    Success: EventType[APISuccessHandler[CreateNewPrivateMessageResponse]] = ...
    """"""
class CreateNewPrivateMessageResponse(Object):
    """"""
    ChannelID: Final[int] = ...
    """
    
    :return: 
    """
    Message: Final[Message] = ...
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
class Cursor(Object):
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
class DeleteFriendRequest(APIRequest):
    """"""
    TargetId: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self, targetId: int):
        """
        
        :param targetId: 
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
class DownloadBeatmapSetRequest(ArchiveDownloadRequest[IBeatmapSetInfo]):
    """"""
    Model: Final[IBeatmapSetInfo] = ...
    """
    
    :return: 
    """
    def __init__(self, set: IBeatmapSetInfo, noVideo: bool):
        """
        
        :param set: 
        :param noVideo: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Progress(self) -> float:
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
    DownloadProgressed: EventType[Action[float]] = ...
    """"""
    Failure: EventType[APIFailureHandler] = ...
    """"""
    Progressed: EventType[APIProgressHandler] = ...
    """"""
    Success: EventType[APISuccessHandler[str]] = ...
    """"""
class DownloadReplayRequest(ArchiveDownloadRequest[IScoreInfo]):
    """"""
    Model: Final[IScoreInfo] = ...
    """
    
    :return: 
    """
    def __init__(self, score: IScoreInfo):
        """
        
        :param score: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Progress(self) -> float:
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
    DownloadProgressed: EventType[Action[float]] = ...
    """"""
    Failure: EventType[APIFailureHandler] = ...
    """"""
    Progressed: EventType[APIProgressHandler] = ...
    """"""
    Success: EventType[APISuccessHandler[str]] = ...
    """"""
class GetBeatmapRequest(APIRequest[APIBeatmap]):
    """"""
    Filename: Final[str] = ...
    """
    
    :return: 
    """
    MD5Hash: Final[str] = ...
    """
    
    :return: 
    """
    OnlineID: Final[int] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, beatmapInfo: IBeatmapInfo):
        """
        
        :param beatmapInfo: 
        """
    @overload
    def __init__(self, onlineId: int = ..., md5Hash: str = ..., filename: str = ...):
        """
        
        :param onlineId: 
        :param md5Hash: 
        :param filename: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> APIBeatmap:
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
    Success: EventType[APISuccessHandler[APIBeatmap]] = ...
    """"""
class GetBeatmapSetRequest(APIRequest[APIBeatmapSet]):
    """"""
    ID: Final[int] = ...
    """
    
    :return: 
    """
    Type: Final[BeatmapSetLookupType] = ...
    """
    
    :return: 
    """
    def __init__(self, id: int, type: BeatmapSetLookupType = ...):
        """
        
        :param id: 
        :param type: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> APIBeatmapSet:
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
    Success: EventType[APISuccessHandler[APIBeatmapSet]] = ...
    """"""
class GetBeatmapsRequest(APIRequest[GetBeatmapsResponse]):
    """"""
    BeatmapIds: Final[IReadOnlyList[int]] = ...
    """
    
    :return: 
    """
    def __init__(self, beatmapIds: Array[int]):
        """
        
        :param beatmapIds: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> GetBeatmapsResponse:
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
    Success: EventType[APISuccessHandler[GetBeatmapsResponse]] = ...
    """"""
class GetBeatmapsResponse(ResponseWithCursor):
    """"""
    Beatmaps: Final[List[APIBeatmap]] = ...
    """
    
    :return: 
    """
    Cursor: Final[Cursor] = ...
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
class GetBlocksRequest(APIRequest[List[APIRelation]]):
    """"""
    def __init__(self):
        """"""
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> List[APIRelation]:
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
    Success: EventType[APISuccessHandler[List[APIRelation]]] = ...
    """"""
class GetChangelogBuildRequest(APIRequest[APIChangelogBuild]):
    """"""
    def __init__(self, streamName: str, buildVersion: str):
        """
        
        :param streamName: 
        :param buildVersion: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> APIChangelogBuild:
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
    Success: EventType[APISuccessHandler[APIChangelogBuild]] = ...
    """"""
class GetChangelogRequest(APIRequest[APIChangelogIndex]):
    """"""
    def __init__(self):
        """"""
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> APIChangelogIndex:
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
    Success: EventType[APISuccessHandler[APIChangelogIndex]] = ...
    """"""
class GetChannelRequest(APIRequest[GetChannelResponse]):
    """"""
    def __init__(self, channelId: int):
        """
        
        :param channelId: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> GetChannelResponse:
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
    Success: EventType[APISuccessHandler[GetChannelResponse]] = ...
    """"""
class GetCommentsRequest(APIRequest[CommentBundle]):
    """"""
    def __init__(self, commentableId: int, type: CommentableType, sort: CommentsSortCriteria = ..., page: int = ..., parentId: Optional[int] = ...):
        """
        
        :param commentableId: 
        :param type: 
        :param sort: 
        :param page: 
        :param parentId: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> CommentBundle:
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
    Success: EventType[APISuccessHandler[CommentBundle]] = ...
    """"""
class GetCountriesResponse(ResponseWithCursor):
    """"""
    Countries: Final[List[CountryStatistics]] = ...
    """
    
    :return: 
    """
    Cursor: Final[Cursor] = ...
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
class GetCountryRankingsRequest(GetRankingsRequest[GetCountriesResponse]):
    """"""
    def __init__(self, ruleset: RulesetInfo, page: int = ...):
        """
        
        :param ruleset: 
        :param page: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> GetCountriesResponse:
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
    Success: EventType[APISuccessHandler[GetCountriesResponse]] = ...
    """"""
class GetFriendsRequest(APIRequest[List[APIRelation]]):
    """"""
    def __init__(self):
        """"""
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> List[APIRelation]:
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
    Success: EventType[APISuccessHandler[List[APIRelation]]] = ...
    """"""
class GetKudosuRankingsRequest(APIRequest[GetKudosuRankingsResponse]):
    """"""
    def __init__(self, page: int = ...):
        """
        
        :param page: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> GetKudosuRankingsResponse:
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
    Success: EventType[APISuccessHandler[GetKudosuRankingsResponse]] = ...
    """"""
class GetKudosuRankingsResponse(Object):
    """"""
    Users: Final[List[APIUser]] = ...
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
class GetMeRequest(APIRequest[APIMe]):
    """"""
    Ruleset: Final[IRulesetInfo] = ...
    """
    
    :return: 
    """
    def __init__(self, ruleset: IRulesetInfo = ...):
        """
        
        :param ruleset: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> APIMe:
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
    Success: EventType[APISuccessHandler[APIMe]] = ...
    """"""
class GetMenuContentRequest(OsuJsonWebRequest[APIMenuContent], IDisposable):
    """"""
    AllowRetryOnTimeout: Final[bool] = ...
    """"""
    ContentType: Final[str] = ...
    """"""
    Method: Final[HttpMethod] = ...
    """"""
    Timeout: Final[int] = ...
    """"""
    Url: Final[str] = ...
    """"""
    def __init__(self):
        """"""
    @property
    def Aborted(self) -> bool:
        """"""
    @property
    def AllowInsecureRequests(self) -> bool:
        """"""
    @AllowInsecureRequests.setter
    def AllowInsecureRequests(self, value: bool) -> None: ...
    @property
    def Completed(self) -> bool:
        """"""
    @property
    def ResponseHeaders(self) -> HttpResponseHeaders:
        """"""
    @property
    def ResponseObject(self) -> APIMenuContent:
        """"""
    @property
    def ResponseStatusCode(self) -> Optional[HttpStatusCode]:
        """"""
    @property
    def ResponseStream(self) -> Stream:
        """"""
    def Abort(self) -> None:
        """"""
    def AddFile(self, paramName: str, data: Array[int], filename: str = ...) -> None:
        """"""
    def AddHeader(self, name: str, value: str) -> None:
        """"""
    @overload
    def AddParameter(self, name: str, value: str) -> None:
        """"""
    @overload
    def AddParameter(self, name: str, value: str, type: RequestParameterType) -> None:
        """"""
    @overload
    def AddRaw(self, stream: Stream) -> None:
        """"""
    @overload
    def AddRaw(self, bytes: Array[int]) -> None:
        """"""
    @overload
    def AddRaw(self, text: str) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetResponseData(self) -> Array[int]:
        """"""
    def GetResponseString(self) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def Perform(self) -> None:
        """"""
    def PerformAsync(self, cancellationToken: CancellationToken = ...) -> Task:
        """"""
    def ToString(self) -> str:
        """"""
    DownloadProgress: EventType[Action[int, int]] = ...
    """"""
    Failed: EventType[Action[Exception]] = ...
    """"""
    Finished: EventType[Action] = ...
    """"""
    Started: EventType[Action] = ...
    """"""
    UploadProgress: EventType[Action[int, int]] = ...
    """"""
class GetMessagesRequest(APIRequest[List[Message]]):
    """"""
    Channel: Final[Channel] = ...
    """
    
    :return: 
    """
    def __init__(self, channel: Channel):
        """
        
        :param channel: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> List[Message]:
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
    Success: EventType[APISuccessHandler[List[Message]]] = ...
    """"""
class GetMyFavouriteBeatmapSetsRequest(APIRequest[GetMyFavouriteBeatmapSetsResponse]):
    """"""
    def __init__(self):
        """"""
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> GetMyFavouriteBeatmapSetsResponse:
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
    Success: EventType[APISuccessHandler[GetMyFavouriteBeatmapSetsResponse]] = ...
    """"""
class GetNewsRequest(APIRequest[GetNewsResponse]):
    """"""
    def __init__(self, year: Optional[int] = ..., cursor: Cursor = ...):
        """
        
        :param year: 
        :param cursor: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> GetNewsResponse:
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
    Success: EventType[APISuccessHandler[GetNewsResponse]] = ...
    """"""
class GetNewsResponse(ResponseWithCursor):
    """"""
    Cursor: Final[Cursor] = ...
    """
    
    :return: 
    """
    NewsPosts: Final[IEnumerable[APINewsPost]] = ...
    """
    
    :return: 
    """
    SidebarMetadata: Final[APINewsSidebar] = ...
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
class GetNotificationsRequest(APIRequest[APINotificationsBundle]):
    """"""
    def __init__(self):
        """"""
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> APINotificationsBundle:
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
    Success: EventType[APISuccessHandler[APINotificationsBundle]] = ...
    """"""
class GetRankingsRequest(ABC, Generic[TModel], APIRequest[TModel]):
    """"""
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> TModel:
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
    Success: EventType[APISuccessHandler[TModel]] = ...
    """"""
class GetScoresRequest(APIRequest[APIScoresCollection], IEquatable[GetScoresRequest]):
    """"""
    DEFAULT_SCORES_PER_REQUEST: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MAX_SCORES_PER_REQUEST: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    def __init__(self, beatmapInfo: IBeatmapInfo, ruleset: IRulesetInfo, scope: BeatmapLeaderboardScope = ..., mods: IEnumerable[IMod] = ...):
        """
        
        :param beatmapInfo: 
        :param ruleset: 
        :param scope: 
        :param mods: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> APIScoresCollection:
        """
        
        :return: 
        """
    @property
    def ScoresRequested(self) -> int:
        """
        
        :return: 
        """
    def AttachAPI(self, apiAccess: IAPIProvider) -> None:
        """
        
        :param apiAccess: 
        """
    def Cancel(self) -> None:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: GetScoresRequest) -> bool:
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
    Success: EventType[APISuccessHandler[APIScoresCollection]] = ...
    """"""
class GetSeasonalBackgroundsRequest(APIRequest[APISeasonalBackgrounds]):
    """"""
    def __init__(self):
        """"""
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> APISeasonalBackgrounds:
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
    Success: EventType[APISuccessHandler[APISeasonalBackgrounds]] = ...
    """"""
class GetSpotlightRankingsRequest(GetRankingsRequest[GetSpotlightRankingsResponse]):
    """"""
    def __init__(self, ruleset: RulesetInfo, spotlight: int, sort: RankingsSortCriteria):
        """
        
        :param ruleset: 
        :param spotlight: 
        :param sort: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> GetSpotlightRankingsResponse:
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
    Success: EventType[APISuccessHandler[GetSpotlightRankingsResponse]] = ...
    """"""
class GetSpotlightRankingsResponse(Object):
    """"""
    BeatmapSets: Final[List[APIBeatmapSet]] = ...
    """
    
    :return: 
    """
    Spotlight: Final[APISpotlight] = ...
    """
    
    :return: 
    """
    Users: Final[List[UserStatistics]] = ...
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
class GetSpotlightsRequest(APIRequest[SpotlightsCollection]):
    """"""
    def __init__(self):
        """"""
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> SpotlightsCollection:
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
    Success: EventType[APISuccessHandler[SpotlightsCollection]] = ...
    """"""
class GetTopUsersRequest(APIRequest[GetTopUsersResponse]):
    """"""
    def __init__(self):
        """"""
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> GetTopUsersResponse:
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
    Success: EventType[APISuccessHandler[GetTopUsersResponse]] = ...
    """"""
class GetTopUsersResponse(ResponseWithCursor):
    """"""
    Cursor: Final[Cursor] = ...
    """
    
    :return: 
    """
    Users: Final[List[UserStatistics]] = ...
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
class GetUpdatesRequest(APIRequest[GetUpdatesResponse]):
    """"""
    def __init__(self, sinceId: int, channel: Channel = ...):
        """
        
        :param sinceId: 
        :param channel: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> GetUpdatesResponse:
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
    Success: EventType[APISuccessHandler[GetUpdatesResponse]] = ...
    """"""
class GetUpdatesResponse(Object):
    """"""
    Messages: Final[List[Message]] = ...
    """
    
    :return: 
    """
    Presence: Final[List[Channel]] = ...
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
class GetUserBeatmapsRequest(PaginatedAPIRequest[List[APIBeatmapSet]]):
    """"""
    def __init__(self, userId: int, type: BeatmapSetType, pagination: PaginationParameters):
        """
        
        :param userId: 
        :param type: 
        :param pagination: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> List[APIBeatmapSet]:
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
    Success: EventType[APISuccessHandler[List[APIBeatmapSet]]] = ...
    """"""
class GetUserKudosuHistoryRequest(PaginatedAPIRequest[List[APIKudosuHistory]]):
    """"""
    def __init__(self, userId: int, pagination: PaginationParameters):
        """
        
        :param userId: 
        :param pagination: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> List[APIKudosuHistory]:
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
    Success: EventType[APISuccessHandler[List[APIKudosuHistory]]] = ...
    """"""
class GetUserMostPlayedBeatmapsRequest(PaginatedAPIRequest[List[APIUserMostPlayedBeatmap]]):
    """"""
    def __init__(self, userId: int, pagination: PaginationParameters):
        """
        
        :param userId: 
        :param pagination: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> List[APIUserMostPlayedBeatmap]:
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
    Success: EventType[APISuccessHandler[List[APIUserMostPlayedBeatmap]]] = ...
    """"""
class GetUserRankingsRequest(GetRankingsRequest[GetTopUsersResponse]):
    """"""
    Type: Final[UserRankingsType] = ...
    """
    
    :return: 
    """
    def __init__(self, ruleset: RulesetInfo, type: UserRankingsType = ..., page: int = ..., countryCode: CountryCode = ...):
        """
        
        :param ruleset: 
        :param type: 
        :param page: 
        :param countryCode: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> GetTopUsersResponse:
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
    Success: EventType[APISuccessHandler[GetTopUsersResponse]] = ...
    """"""
class GetUserRecentActivitiesRequest(PaginatedAPIRequest[List[APIRecentActivity]]):
    """"""
    def __init__(self, userId: int, pagination: PaginationParameters):
        """
        
        :param userId: 
        :param pagination: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> List[APIRecentActivity]:
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
    Success: EventType[APISuccessHandler[List[APIRecentActivity]]] = ...
    """"""
class GetUserRequest(APIRequest[APIUser]):
    """"""
    Lookup: Final[str] = ...
    """
    
    :return: 
    """
    Ruleset: Final[IRulesetInfo] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, userId: Optional[int] = ..., ruleset: IRulesetInfo = ...):
        """
        
        :param userId: 
        :param ruleset: 
        """
    @overload
    def __init__(self, username: str, ruleset: IRulesetInfo = ...):
        """
        
        :param username: 
        :param ruleset: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> APIUser:
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
    Success: EventType[APISuccessHandler[APIUser]] = ...
    """"""
class GetUserScoresRequest(PaginatedAPIRequest[List[SoloScoreInfo]]):
    """"""
    def __init__(self, userId: int, type: ScoreType, pagination: PaginationParameters, ruleset: RulesetInfo = ...):
        """
        
        :param userId: 
        :param type: 
        :param pagination: 
        :param ruleset: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> List[SoloScoreInfo]:
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
    Success: EventType[APISuccessHandler[List[SoloScoreInfo]]] = ...
    """"""
class GetUsersRequest(APIRequest[GetUsersResponse]):
    """"""
    MAX_IDS_PER_REQUEST: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    UserIds: Final[Array[int]] = ...
    """
    
    :return: 
    """
    def __init__(self, userIds: Array[int]):
        """
        
        :param userIds: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> GetUsersResponse:
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
    Success: EventType[APISuccessHandler[GetUsersResponse]] = ...
    """"""
class GetUsersResponse(ResponseWithCursor):
    """"""
    Cursor: Final[Cursor] = ...
    """
    
    :return: 
    """
    Users: Final[List[APIUser]] = ...
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
class GetWikiRequest(APIRequest[APIWikiPage]):
    """"""
    Path: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self, path: str, language: Language = ...):
        """
        
        :param path: 
        :param language: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> APIWikiPage:
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
    Success: EventType[APISuccessHandler[APIWikiPage]] = ...
    """"""
class JoinChannelRequest(APIRequest):
    """"""
    def __init__(self, channel: Channel):
        """
        
        :param channel: 
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
class LeaveChannelRequest(APIRequest):
    """"""
    def __init__(self, channel: Channel):
        """
        
        :param channel: 
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
class ListChannelsRequest(APIRequest[List[Channel]]):
    """"""
    def __init__(self):
        """"""
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> List[Channel]:
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
    Success: EventType[APISuccessHandler[List[Channel]]] = ...
    """"""
class ListTagsRequest(APIRequest[APITagCollection]):
    """"""
    def __init__(self):
        """"""
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> APITagCollection:
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
    Success: EventType[APISuccessHandler[APITagCollection]] = ...
    """"""
class LookupUsersRequest(APIRequest[GetUsersResponse]):
    """"""
    RulesetId: Final[Optional[int]] = ...
    """
    
    :return: 
    """
    UserIds: Final[Array[int]] = ...
    """
    
    :return: 
    """
    def __init__(self, userIds: Array[int], rulesetId: Optional[int] = ...):
        """
        
        :param userIds: 
        :param rulesetId: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> GetUsersResponse:
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
    Success: EventType[APISuccessHandler[GetUsersResponse]] = ...
    """"""
class MarkChannelAsReadRequest(APIRequest):
    """"""
    Channel: Final[Channel] = ...
    """
    
    :return: 
    """
    Message: Final[Message] = ...
    """
    
    :return: 
    """
    def __init__(self, channel: Channel, message: Message):
        """
        
        :param channel: 
        :param message: 
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
class PaginatedAPIRequest(ABC, Generic[T], APIRequest[T]):
    """"""
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> T:
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
    Success: EventType[APISuccessHandler[T]] = ...
    """"""
class PaginationParameters(ValueType):
    """"""
    @overload
    def __init__(self, limit: int):
        """
        
        :param limit: 
        """
    @overload
    def __init__(self, offset: int, limit: int):
        """
        
        :param offset: 
        :param limit: 
        """
    @property
    def Limit(self) -> int:
        """
        
        :return: 
        """
    @property
    def Offset(self) -> int:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def TakeNext(self, limit: int) -> PaginationParameters:
        """
        
        :param limit: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class PatchBeatmapPackageRequest(APIUploadRequest):
    """"""
    def __init__(self, beatmapSetId: int):
        """
        
        :param beatmapSetId: 
        """
    @property
    def BeatmapSetID(self) -> int:
        """
        
        :return: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def FilesChanged(self) -> Dictionary[str, Array[int]]:
        """
        
        :return: 
        """
    @property
    def FilesDeleted(self) -> HashSet[str]:
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
    Progressed: EventType[APIProgressHandler] = ...
    """"""
    Success: EventType[APISuccessHandler] = ...
    """"""
class PostBeatmapFavouriteRequest(APIRequest):
    """"""
    Action: Final[BeatmapFavouriteAction] = ...
    """
    
    :return: 
    """
    def __init__(self, id: int, action: BeatmapFavouriteAction):
        """
        
        :param id: 
        :param action: 
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
class PostMessageRequest(APIRequest[Message]):
    """"""
    Message: Final[Message] = ...
    """
    
    :return: 
    """
    def __init__(self, message: Message):
        """
        
        :param message: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> Message:
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
    Success: EventType[APISuccessHandler[Message]] = ...
    """"""
class PutBeatmapSetRequest(APIRequest[PutBeatmapSetResponse]):
    """"""
    @property
    def BeatmapSetID(self) -> Optional[int]:
        """
        
        :return: 
        """
    @BeatmapSetID.setter
    def BeatmapSetID(self, value: Optional[int]) -> None: ...
    @property
    def BeatmapsToCreate(self) -> int:
        """
        
        :return: 
        """
    @BeatmapsToCreate.setter
    def BeatmapsToCreate(self, value: int) -> None: ...
    @property
    def BeatmapsToKeep(self) -> Array[int]:
        """
        
        :return: 
        """
    @BeatmapsToKeep.setter
    def BeatmapsToKeep(self, value: Array[int]) -> None: ...
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def NotifyOnDiscussionReplies(self) -> bool:
        """
        
        :return: 
        """
    @NotifyOnDiscussionReplies.setter
    def NotifyOnDiscussionReplies(self, value: bool) -> None: ...
    @property
    def Response(self) -> PutBeatmapSetResponse:
        """
        
        :return: 
        """
    @property
    def SubmissionTarget(self) -> BeatmapSubmissionTarget:
        """
        
        :return: 
        """
    @SubmissionTarget.setter
    def SubmissionTarget(self, value: BeatmapSubmissionTarget) -> None: ...
    def AttachAPI(self, apiAccess: IAPIProvider) -> None:
        """
        
        :param apiAccess: 
        """
    def Cancel(self) -> None:
        """"""
    @classmethod
    def CreateNew(cls, beatmapCount: int, settings: BeatmapSubmissionSettings) -> PutBeatmapSetRequest:
        """
        
        :param beatmapCount: 
        :param settings: 
        :return: 
        """
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
    @classmethod
    def UpdateExisting(cls, beatmapSetId: int, beatmapsToKeep: IEnumerable[int], beatmapsToCreate: int, settings: BeatmapSubmissionSettings) -> PutBeatmapSetRequest:
        """
        
        :param beatmapSetId: 
        :param beatmapsToKeep: 
        :param beatmapsToCreate: 
        :param settings: 
        :return: 
        """
    Failure: EventType[APIFailureHandler] = ...
    """"""
    Success: EventType[APISuccessHandler[PutBeatmapSetResponse]] = ...
    """"""
class RecentActivityType(Enum):
    """"""
    Achievement: RecentActivityType = ...
    """"""
    BeatmapPlaycount: RecentActivityType = ...
    """"""
    BeatmapsetApprove: RecentActivityType = ...
    """"""
    BeatmapsetDelete: RecentActivityType = ...
    """"""
    BeatmapsetRevive: RecentActivityType = ...
    """"""
    BeatmapsetUpdate: RecentActivityType = ...
    """"""
    BeatmapsetUpload: RecentActivityType = ...
    """"""
    Medal: RecentActivityType = ...
    """"""
    Rank: RecentActivityType = ...
    """"""
    RankLost: RecentActivityType = ...
    """"""
    UserSupportAgain: RecentActivityType = ...
    """"""
    UserSupportFirst: RecentActivityType = ...
    """"""
    UserSupportGift: RecentActivityType = ...
    """"""
    UsernameChange: RecentActivityType = ...
    """"""
class ReissueVerificationCodeRequest(APIRequest):
    """"""
    def __init__(self):
        """"""
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
class RemoveBeatmapTagRequest(APIRequest):
    """"""
    def __init__(self, beatmapID: int, tagID: int):
        """
        
        :param beatmapID: 
        :param tagID: 
        """
    @property
    def BeatmapID(self) -> int:
        """
        
        :return: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def TagID(self) -> int:
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
class ReplaceBeatmapPackageRequest(APIUploadRequest):
    """"""
    def __init__(self, beatmapSetID: int, oszPackage: Array[int]):
        """
        
        :param beatmapSetID: 
        :param oszPackage: 
        """
    @property
    def BeatmapSetID(self) -> int:
        """
        
        :return: 
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
    Progressed: EventType[APIProgressHandler] = ...
    """"""
    Success: EventType[APISuccessHandler] = ...
    """"""
class ResponseWithCursor(ABC, Object):
    """"""
    Cursor: Final[Cursor] = ...
    """
    
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
class ScoreType(Enum):
    """"""
    Best: ScoreType = ...
    """"""
    Firsts: ScoreType = ...
    """"""
    Recent: ScoreType = ...
    """"""
    Pinned: ScoreType = ...
    """"""
class SearchBeatmapSetsRequest(APIRequest[SearchBeatmapSetsResponse]):
    """"""
    def __init__(self, query: str, ruleset: RulesetInfo, cursor: Cursor = ..., general: IReadOnlyCollection[SearchGeneral] = ..., searchCategory: SearchCategory = ..., sortCriteria: SortCriteria = ..., sortDirection: SortDirection = ..., genre: SearchGenre = ..., language: SearchLanguage = ..., extra: IReadOnlyCollection[SearchExtra] = ..., ranks: IReadOnlyCollection[ScoreRank] = ..., played: SearchPlayed = ..., explicitContent: SearchExplicit = ...):
        """
        
        :param query: 
        :param ruleset: 
        :param cursor: 
        :param general: 
        :param searchCategory: 
        :param sortCriteria: 
        :param sortDirection: 
        :param genre: 
        :param language: 
        :param extra: 
        :param ranks: 
        :param played: 
        :param explicitContent: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def ExplicitContent(self) -> SearchExplicit:
        """
        
        :return: 
        """
    @property
    def Extra(self) -> IReadOnlyCollection[SearchExtra]:
        """
        
        :return: 
        """
    @property
    def General(self) -> IReadOnlyCollection[SearchGeneral]:
        """
        
        :return: 
        """
    @property
    def Genre(self) -> SearchGenre:
        """
        
        :return: 
        """
    @property
    def Language(self) -> SearchLanguage:
        """
        
        :return: 
        """
    @property
    def Played(self) -> SearchPlayed:
        """
        
        :return: 
        """
    @property
    def Ranks(self) -> IReadOnlyCollection[ScoreRank]:
        """
        
        :return: 
        """
    @property
    def Response(self) -> SearchBeatmapSetsResponse:
        """
        
        :return: 
        """
    @property
    def SearchCategory(self) -> SearchCategory:
        """
        
        :return: 
        """
    @property
    def SortCriteria(self) -> SortCriteria:
        """
        
        :return: 
        """
    @property
    def SortDirection(self) -> SortDirection:
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
    Success: EventType[APISuccessHandler[SearchBeatmapSetsResponse]] = ...
    """"""
class SearchBeatmapSetsResponse(ResponseWithCursor):
    """"""
    BeatmapSets: Final[IEnumerable[APIBeatmapSet]] = ...
    """
    
    :return: 
    """
    Cursor: Final[Cursor] = ...
    """
    
    :return: 
    """
    Total: Final[int] = ...
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
class SearchUsersRequest(APIRequest[SearchUsersResponse]):
    """"""
    Query: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self, query: str):
        """
        
        :param query: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> SearchUsersResponse:
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
    Success: EventType[APISuccessHandler[SearchUsersResponse]] = ...
    """"""
class SearchUsersResponse(Object):
    """"""
    Total: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def Users(self) -> List[APIUser]:
        """
        
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
class SpotlightsCollection(Object):
    """"""
    Spotlights: Final[List[APISpotlight]] = ...
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
class UnblockUserRequest(APIRequest):
    """"""
    TargetId: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self, targetId: int):
        """
        
        :param targetId: 
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
class UserRankingsType(Enum):
    """"""
    Performance: UserRankingsType = ...
    """"""
    Score: UserRankingsType = ...
    """"""
class UserReportRequest(APIRequest):
    """"""
    Comment: Final[str] = ...
    """
    
    :return: 
    """
    Reason: Final[UserReportReason] = ...
    """
    
    :return: 
    """
    UserID: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self, userID: int, reason: UserReportReason, comment: str):
        """
        
        :param userID: 
        :param reason: 
        :param comment: 
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
class VerificationMailFallbackRequest(APIRequest):
    """"""
    def __init__(self):
        """"""
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
class VerifySessionRequest(APIRequest):
    """"""
    VerificationKey: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self, verificationKey: str):
        """
        
        :param verificationKey: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def RequiredVerificationMethod(self) -> Optional[SessionVerificationMethod]:
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