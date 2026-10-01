from Microsoft.AspNetCore.SignalR import HubException
from System import Action
from System import Array
from System.Collections.Generic import ICollection
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IList
from System.Collections.Generic import IReadOnlyCollection
from System.Collections.Generic import IReadOnlyList
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System import Enum
from System import Exception
from System import Func
from System import IDisposable
from System import IEquatable
from System import Object
from System import Predicate
from System.Reflection import MethodBase
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Threading.Tasks import Task
from System import TimeSpan
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Framework.Allocation import IDependencyActivatorRegistry
from osu.Framework.Allocation import IDependencyInjectionCandidate
from osu.Framework.Allocation import IReadOnlyDependencyContainer
from osu.Framework.Allocation import ISourceGeneratedDependencyActivator
from osu.Framework.Allocation import ISourceGeneratedLongRunningLoadCache
from osu.Framework.Bindables import IBindable
from osu.Framework.Bindables import IBindableList
from osu.Framework.Graphics import Anchor
from osu.Framework.Graphics import Axes
from osu.Framework.Graphics import BlendingParameters
from osu.Framework.Graphics.Colour import ColourInfo
from osu.Framework.Graphics import Component
from osu.Framework.Graphics.Containers import CompositeDrawable
from osu.Framework.Graphics.Containers import Container
from osu.Framework.Graphics.Containers.Container import Enumerator
from osu.Framework.Graphics.Containers import IContainer
from osu.Framework.Graphics.Containers import IContainerCollection
from osu.Framework.Graphics.Containers import IContainerEnumerable
from osu.Framework.Graphics import DrawColourInfo
from osu.Framework.Graphics import DrawInfo
from osu.Framework.Graphics import Drawable
from osu.Framework.Graphics import Easing
from osu.Framework.Graphics.Effects import EdgeEffectParameters
from osu.Framework.Graphics.Effects import IEffect
from osu.Framework.Graphics import FillMode
from osu.Framework.Graphics import IDrawable
from osu.Framework.Graphics import Invalidation
from osu.Framework.Graphics import LoadState
from osu.Framework.Graphics import MarginPadding
from osu.Framework.Graphics.Primitives import Quad
from osu.Framework.Graphics.Primitives import RectangleF
from osu.Framework.Graphics.Sprites import IconUsage
from osu.Framework.Graphics.Transforms import ITransformable
from osu.Framework.Graphics.Transforms import Transform
from osu.Framework.Input.Events import UIEvent
from osu.Framework.Input import ISourceGeneratedHandleInputCache
from osu.Framework.Layout import InvalidationSource
from osu.Framework.Localisation import LocalisableString
from osu.Framework.Timing import FrameTimeInfo
from osu.Framework.Timing import IFrameBasedClock
from osu.Game.Online.API import APIMod
from osu.Game.Online.API.Requests.Responses import APIUser
from osu.Game.Online import EndpointConfiguration
from osu.Game.Online import IStatefulUserHubClient
from osu.Game.Online.Matchmaking import IMatchmakingClient
from osu.Game.Online.Matchmaking import IMatchmakingServer
from osu.Game.Online.Matchmaking import MatchmakingDuelIssuedParams
from osu.Game.Online.Matchmaking import MatchmakingLobbyStatus
from osu.Game.Online.Matchmaking import MatchmakingPool
from osu.Game.Online.Matchmaking import MatchmakingPoolType
from osu.Game.Online.Matchmaking import MatchmakingQueueStatus
from osu.Game.Online.Matchmaking import MatchmakingRoomInvitationParams
from osu.Game.Online.Matchmaking.Requests import MatchmakingAcceptDuelRequest
from osu.Game.Online.Matchmaking.Requests import MatchmakingIssueDuelRequest
from osu.Game.Online.Matchmaking.Requests import MatchmakingJoinLobbyRequest
from osu.Game.Online.Matchmaking.Responses import MatchmakingAcceptDuelResponse
from osu.Game.Online.Matchmaking.Responses import MatchmakingIssueDuelResponse
from osu.Game.Online.Matchmaking.Responses import MatchmakingJoinLobbyResponse
from osu.Game.Online.Multiplayer.MatchTypes.RankedPlay import RankedPlayCardItem
from osu.Game.Online.RankedPlay import IRankedPlayClient
from osu.Game.Online.RankedPlay import IRankedPlayServer
from osu.Game.Online.Rooms import BeatmapAvailability
from osu.Game.Online.Rooms import MatchType
from osu.Game.Online.Rooms import MultiplayerPlaylistItem
from osu.Game.Online.Rooms import Room
from osu.Game.Overlays.Notifications import Notification
from osu.Game.Overlays.Notifications import SimpleNotification
from osu.Game.Overlays.Notifications import UserAvatarNotification
from osu.Game.Rulesets.Mods import Mod
from osu.Game.Screens.OnlinePlay.Matchmaking.RankedPlay import RankedPlayCardWithPlaylistItem
from osu.Game.Utils import Optional
from osuTK import Vector2
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Iterator
from typing import Optional
from typing import TypeVar
from typing import overload
T = TypeVar("T")
class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...
class ChangeSlotRequest(MatchUserRequest):
    """"""
    def __init__(self):
        """"""
    @property
    def SlotID(self) -> int:
        """
        
        :return: 
        """
    @SlotID.setter
    def SlotID(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class ForceGameplayStartCountdown(MultiplayerCountdown):
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
    @property
    def IsExclusive(self) -> bool:
        """
        
        :return: 
        """
    @property
    def TimeRemaining(self) -> TimeSpan:
        """
        
        :return: 
        """
    @TimeRemaining.setter
    def TimeRemaining(self, value: TimeSpan) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class GameplayAbortReason(Enum):
    """"""
    LoadTookTooLong: GameplayAbortReason = ...
    """"""
    HostAbortedTheMatch: GameplayAbortReason = ...
    """"""
class IMultiplayerClient(IStatefulUserHubClient):
    """"""
    def DisconnectRequested(self) -> Task:
        """
        
        :return: 
        """
    def GameplayAborted(self, reason: GameplayAbortReason) -> Task:
        """
        
        :param reason: 
        :return: 
        """
    def GameplayStarted(self) -> Task:
        """
        
        :return: 
        """
    def HostChanged(self, userId: int) -> Task:
        """
        
        :param userId: 
        :return: 
        """
    def Invited(self, invitedBy: int, roomID: int, password: str) -> Task:
        """
        
        :param invitedBy: 
        :param roomID: 
        :param password: 
        :return: 
        """
    def LoadRequested(self) -> Task:
        """
        
        :return: 
        """
    def MatchEvent(self, e: MatchServerEvent) -> Task:
        """
        
        :param e: 
        :return: 
        """
    def MatchRoomStateChanged(self, state: MatchRoomState) -> Task:
        """
        
        :param state: 
        :return: 
        """
    def MatchUserStateChanged(self, userId: int, state: MatchUserState) -> Task:
        """
        
        :param userId: 
        :param state: 
        :return: 
        """
    def PlaylistItemAdded(self, item: MultiplayerPlaylistItem) -> Task:
        """
        
        :param item: 
        :return: 
        """
    def PlaylistItemChanged(self, item: MultiplayerPlaylistItem) -> Task:
        """
        
        :param item: 
        :return: 
        """
    def PlaylistItemRemoved(self, playlistItemId: int) -> Task:
        """
        
        :param playlistItemId: 
        :return: 
        """
    def ResultsReady(self) -> Task:
        """
        
        :return: 
        """
    def RoomStateChanged(self, state: MultiplayerRoomState) -> Task:
        """
        
        :param state: 
        :return: 
        """
    def ServerShuttingDown(self) -> Task:
        """
        
        :return: 
        """
    def SettingsChanged(self, newSettings: MultiplayerRoomSettings) -> Task:
        """
        
        :param newSettings: 
        :return: 
        """
    def UserBeatmapAvailabilityChanged(self, userId: int, beatmapAvailability: BeatmapAvailability) -> Task:
        """
        
        :param userId: 
        :param beatmapAvailability: 
        :return: 
        """
    def UserJoined(self, user: MultiplayerRoomUser) -> Task:
        """
        
        :param user: 
        :return: 
        """
    def UserKicked(self, user: MultiplayerRoomUser) -> Task:
        """
        
        :param user: 
        :return: 
        """
    def UserLeft(self, user: MultiplayerRoomUser) -> Task:
        """
        
        :param user: 
        :return: 
        """
    def UserModsChanged(self, userId: int, mods: IEnumerable[APIMod]) -> Task:
        """
        
        :param userId: 
        :param mods: 
        :return: 
        """
    def UserStateChanged(self, userId: int, state: MultiplayerUserState) -> Task:
        """
        
        :param userId: 
        :param state: 
        :return: 
        """
    def UserStyleChanged(self, userId: int, beatmapId: Optional[int], rulesetId: Optional[int]) -> Task:
        """
        
        :param userId: 
        :param beatmapId: 
        :param rulesetId: 
        :return: 
        """
    def UserVotedToSkipIntro(self, userId: int, voted: bool) -> Task:
        """
        
        :param userId: 
        :param voted: 
        :return: 
        """
    def VoteToSkipIntroPassed(self) -> Task:
        """
        
        :return: 
        """
class IMultiplayerLoungeServer:
    """"""
    def CreateRoom(self, room: MultiplayerRoom) -> Task[MultiplayerRoom]:
        """
        
        :param room: 
        :return: 
        """
    def JoinRoom(self, roomId: int) -> Task[MultiplayerRoom]:
        """
        
        :param roomId: 
        :return: 
        """
    def JoinRoomWithPassword(self, roomId: int, password: str) -> Task[MultiplayerRoom]:
        """
        
        :param roomId: 
        :param password: 
        :return: 
        """
class IMultiplayerRoomServer:
    """"""
    def AbortGameplay(self) -> Task:
        """
        
        :return: 
        """
    def AbortMatch(self) -> Task:
        """
        
        :return: 
        """
    def AddPlaylistItem(self, item: MultiplayerPlaylistItem) -> Task:
        """
        
        :param item: 
        :return: 
        """
    def ChangeBeatmapAvailability(self, newBeatmapAvailability: BeatmapAvailability) -> Task:
        """
        
        :param newBeatmapAvailability: 
        :return: 
        """
    def ChangeSettings(self, settings: MultiplayerRoomSettings) -> Task:
        """
        
        :param settings: 
        :return: 
        """
    def ChangeState(self, newState: MultiplayerUserState) -> Task:
        """
        
        :param newState: 
        :return: 
        """
    def ChangeUserMods(self, newMods: IEnumerable[APIMod]) -> Task:
        """
        
        :param newMods: 
        :return: 
        """
    def ChangeUserStyle(self, beatmapId: Optional[int], rulesetId: Optional[int]) -> Task:
        """
        
        :param beatmapId: 
        :param rulesetId: 
        :return: 
        """
    def EditPlaylistItem(self, item: MultiplayerPlaylistItem) -> Task:
        """
        
        :param item: 
        :return: 
        """
    def InvitePlayer(self, userId: int) -> Task:
        """
        
        :param userId: 
        :return: 
        """
    def KickUser(self, userId: int) -> Task:
        """
        
        :param userId: 
        :return: 
        """
    def LeaveRoom(self) -> Task:
        """
        
        :return: 
        """
    def RemovePlaylistItem(self, playlistItemId: int) -> Task:
        """
        
        :param playlistItemId: 
        :return: 
        """
    def SendMatchRequest(self, request: MatchUserRequest) -> Task:
        """
        
        :param request: 
        :return: 
        """
    def StartMatch(self) -> Task:
        """
        
        :return: 
        """
    def TransferHost(self, userId: int) -> Task:
        """
        
        :param userId: 
        :return: 
        """
    def VoteToSkipIntro(self) -> Task:
        """
        
        :return: 
        """
class IMultiplayerServer(IMultiplayerLoungeServer, IMultiplayerRoomServer):
    """"""
    def AbortGameplay(self) -> Task:
        """
        
        :return: 
        """
    def AbortMatch(self) -> Task:
        """
        
        :return: 
        """
    def AddPlaylistItem(self, item: MultiplayerPlaylistItem) -> Task:
        """
        
        :param item: 
        :return: 
        """
    def ChangeBeatmapAvailability(self, newBeatmapAvailability: BeatmapAvailability) -> Task:
        """
        
        :param newBeatmapAvailability: 
        :return: 
        """
    def ChangeSettings(self, settings: MultiplayerRoomSettings) -> Task:
        """
        
        :param settings: 
        :return: 
        """
    def ChangeState(self, newState: MultiplayerUserState) -> Task:
        """
        
        :param newState: 
        :return: 
        """
    def ChangeUserMods(self, newMods: IEnumerable[APIMod]) -> Task:
        """
        
        :param newMods: 
        :return: 
        """
    def ChangeUserStyle(self, beatmapId: Optional[int], rulesetId: Optional[int]) -> Task:
        """
        
        :param beatmapId: 
        :param rulesetId: 
        :return: 
        """
    def CreateRoom(self, room: MultiplayerRoom) -> Task[MultiplayerRoom]:
        """
        
        :param room: 
        :return: 
        """
    def EditPlaylistItem(self, item: MultiplayerPlaylistItem) -> Task:
        """
        
        :param item: 
        :return: 
        """
    def InvitePlayer(self, userId: int) -> Task:
        """
        
        :param userId: 
        :return: 
        """
    def JoinRoom(self, roomId: int) -> Task[MultiplayerRoom]:
        """
        
        :param roomId: 
        :return: 
        """
    def JoinRoomWithPassword(self, roomId: int, password: str) -> Task[MultiplayerRoom]:
        """
        
        :param roomId: 
        :param password: 
        :return: 
        """
    def KickUser(self, userId: int) -> Task:
        """
        
        :param userId: 
        :return: 
        """
    def LeaveRoom(self) -> Task:
        """
        
        :return: 
        """
    def RemovePlaylistItem(self, playlistItemId: int) -> Task:
        """
        
        :param playlistItemId: 
        :return: 
        """
    def SendMatchRequest(self, request: MatchUserRequest) -> Task:
        """
        
        :param request: 
        :return: 
        """
    def StartMatch(self) -> Task:
        """
        
        :return: 
        """
    def TransferHost(self, userId: int) -> Task:
        """
        
        :param userId: 
        :return: 
        """
    def VoteToSkipIntro(self) -> Task:
        """
        
        :return: 
        """
class InvalidPasswordException(HubException, ISerializable):
    """"""
    def __init__(self):
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
class InvalidStateChangeException(HubException, ISerializable):
    """"""
    def __init__(self, oldState: MultiplayerUserState, newState: MultiplayerUserState):
        """
        
        :param oldState: 
        :param newState: 
        """
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @HResult.setter
    def HResult(self, value: int) -> None: ...
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
class InvalidStateException(HubException, ISerializable):
    """"""
    def __init__(self, message: str):
        """
        
        :param message: 
        """
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @HResult.setter
    def HResult(self, value: int) -> None: ...
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
class MatchRoomState(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class MatchServerEvent(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class MatchStartCountdown(MultiplayerCountdown):
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
    @property
    def IsExclusive(self) -> bool:
        """
        
        :return: 
        """
    @property
    def TimeRemaining(self) -> TimeSpan:
        """
        
        :return: 
        """
    @TimeRemaining.setter
    def TimeRemaining(self, value: TimeSpan) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class MatchUserRequest(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class MatchUserState(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class MultiplayerClient(ABC, Component, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache, IMatchmakingClient, IMatchmakingServer, IMultiplayerClient, IMultiplayerRoomServer, IRankedPlayClient, IRankedPlayServer, IStatefulUserHubClient):
    """"""
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    @property
    def AcceptsFocus(self) -> bool:
        """"""
    @property
    def Alpha(self) -> float:
        """"""
    @Alpha.setter
    def Alpha(self, value: float) -> None: ...
    @property
    def AlwaysPresent(self) -> bool:
        """"""
    @AlwaysPresent.setter
    def AlwaysPresent(self, value: bool) -> None: ...
    @property
    def Anchor(self) -> Anchor:
        """"""
    @Anchor.setter
    def Anchor(self, value: Anchor) -> None: ...
    @property
    def AnchorPosition(self) -> Vector2:
        """"""
    @property
    def Blending(self) -> BlendingParameters:
        """"""
    @Blending.setter
    def Blending(self, value: BlendingParameters) -> None: ...
    @property
    def BoundingBox(self) -> RectangleF:
        """"""
    @property
    def BypassAutoSizeAxes(self) -> Axes:
        """"""
    @BypassAutoSizeAxes.setter
    def BypassAutoSizeAxes(self, value: Axes) -> None: ...
    @property
    def ChangeFocusOnClick(self) -> bool:
        """"""
    @property
    def Clock(self) -> IFrameBasedClock:
        """"""
    @Clock.setter
    def Clock(self, value: IFrameBasedClock) -> None: ...
    @property
    def Colour(self) -> ColourInfo:
        """"""
    @Colour.setter
    def Colour(self, value: ColourInfo) -> None: ...
    @property
    def CurrentMatchPlayingUserIds(self) -> IBindableList[int]:
        """
        
        :return: 
        """
    @property
    def Depth(self) -> float:
        """"""
    @Depth.setter
    def Depth(self, value: float) -> None: ...
    @property
    def DisposeOnDeathRemoval(self) -> bool:
        """"""
    @property
    def DragBlocksClick(self) -> bool:
        """"""
    @property
    def DrawColourInfo(self) -> DrawColourInfo:
        """"""
    @property
    def DrawHeight(self) -> float:
        """"""
    @property
    def DrawInfo(self) -> DrawInfo:
        """"""
    @property
    def DrawPosition(self) -> Vector2:
        """"""
    @property
    def DrawRectangle(self) -> RectangleF:
        """"""
    @property
    def DrawSize(self) -> Vector2:
        """"""
    @property
    def DrawWidth(self) -> float:
        """"""
    @property
    def FillAspectRatio(self) -> float:
        """"""
    @FillAspectRatio.setter
    def FillAspectRatio(self, value: float) -> None: ...
    @property
    def FillMode(self) -> FillMode:
        """"""
    @FillMode.setter
    def FillMode(self, value: FillMode) -> None: ...
    @property
    def HandleNonPositionalInput(self) -> bool:
        """"""
    @property
    def HandlePositionalInput(self) -> bool:
        """"""
    @property
    def HasFocus(self) -> bool:
        """"""
    @property
    def HasProxy(self) -> bool:
        """"""
    @property
    def Height(self) -> float:
        """"""
    @Height.setter
    def Height(self, value: float) -> None: ...
    @property
    def InvalidationFromParentSize(self) -> Invalidation:
        """"""
    @property
    def InvalidationID(self) -> int:
        """"""
    @property
    def IsAlive(self) -> bool:
        """"""
    @property
    def IsConnected(self) -> IBindable[bool]:
        """
        
        :return: 
        """
    @property
    def IsDragged(self) -> bool:
        """"""
    @property
    def IsHost(self) -> bool:
        """
        
        :return: 
        """
    @property
    def IsHovered(self) -> bool:
        """"""
    @property
    def IsLoaded(self) -> bool:
        """"""
    @property
    def IsPresent(self) -> bool:
        """"""
    @property
    def IsProxy(self) -> bool:
        """"""
    @property
    def IsReferee(self) -> bool:
        """
        
        :return: 
        """
    @property
    def LatestTransformEndTime(self) -> float:
        """"""
    @property
    def LayoutRectangle(self) -> RectangleF:
        """"""
    @property
    def LayoutSize(self) -> Vector2:
        """"""
    @property
    def LifetimeEnd(self) -> float:
        """"""
    @LifetimeEnd.setter
    def LifetimeEnd(self, value: float) -> None: ...
    @property
    def LifetimeStart(self) -> float:
        """"""
    @LifetimeStart.setter
    def LifetimeStart(self, value: float) -> None: ...
    @property
    def LoadState(self) -> LoadState:
        """"""
    @property
    def LocalUser(self) -> MultiplayerRoomUser:
        """
        
        :return: 
        """
    @property
    def Margin(self) -> MarginPadding:
        """"""
    @Margin.setter
    def Margin(self, value: MarginPadding) -> None: ...
    @property
    def Origin(self) -> Anchor:
        """"""
    @Origin.setter
    def Origin(self, value: Anchor) -> None: ...
    @property
    def OriginPosition(self) -> Vector2:
        """"""
    @OriginPosition.setter
    def OriginPosition(self, value: Vector2) -> None: ...
    @property
    def Parent(self) -> CompositeDrawable:
        """"""
    @property
    def Position(self) -> Vector2:
        """"""
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
    @property
    def PostNotification(self) -> Action[Notification]:
        """
        
        :return: 
        """
    @PostNotification.setter
    def PostNotification(self, value: Action[Notification]) -> None: ...
    @property
    def PresentMatch(self) -> Action[Room, str]:
        """
        
        :return: 
        """
    @PresentMatch.setter
    def PresentMatch(self, value: Action[Room, str]) -> None: ...
    @property
    def PropagateNonPositionalInputSubTree(self) -> bool:
        """"""
    @property
    def PropagatePositionalInputSubTree(self) -> bool:
        """"""
    @property
    def RelativeAnchorPosition(self) -> Vector2:
        """"""
    @RelativeAnchorPosition.setter
    def RelativeAnchorPosition(self, value: Vector2) -> None: ...
    @property
    def RelativeOriginPosition(self) -> Vector2:
        """"""
    @property
    def RelativePositionAxes(self) -> Axes:
        """"""
    @RelativePositionAxes.setter
    def RelativePositionAxes(self, value: Axes) -> None: ...
    @property
    def RelativeSizeAxes(self) -> Axes:
        """"""
    @RelativeSizeAxes.setter
    def RelativeSizeAxes(self, value: Axes) -> None: ...
    @property
    def RemoveCompletedTransforms(self) -> bool:
        """"""
    @property
    def RemoveWhenNotAlive(self) -> bool:
        """"""
    @property
    def RequestsFocus(self) -> bool:
        """"""
    @property
    def Room(self) -> MultiplayerRoom:
        """
        
        :return: 
        """
    @property
    def Rotation(self) -> float:
        """"""
    @Rotation.setter
    def Rotation(self, value: float) -> None: ...
    @property
    def Scale(self) -> Vector2:
        """"""
    @Scale.setter
    def Scale(self, value: Vector2) -> None: ...
    @property
    def ScreenSpaceDrawQuad(self) -> Quad:
        """"""
    @property
    def Shear(self) -> Vector2:
        """"""
    @Shear.setter
    def Shear(self, value: Vector2) -> None: ...
    @property
    def Size(self) -> Vector2:
        """"""
    @Size.setter
    def Size(self, value: Vector2) -> None: ...
    @property
    def Time(self) -> FrameTimeInfo:
        """"""
    @property
    def TransformStartTime(self) -> float:
        """"""
    @property
    def Transforms(self) -> IEnumerable[Transform]:
        """"""
    @property
    def Width(self) -> float:
        """"""
    @Width.setter
    def Width(self, value: float) -> None: ...
    @property
    def X(self) -> float:
        """"""
    @X.setter
    def X(self, value: float) -> None: ...
    @property
    def Y(self) -> float:
        """"""
    @Y.setter
    def Y(self, value: float) -> None: ...
    def AbortGameplay(self) -> Task:
        """
        
        :return: 
        """
    def AbortMatch(self) -> Task:
        """
        
        :return: 
        """
    def AddPlaylistItem(self, item: MultiplayerPlaylistItem) -> Task:
        """
        
        :param item: 
        :return: 
        """
    def AddTransform(self, transform: Transform, customTransformID: Optional[int] = ...) -> None:
        """"""
    def ApplyTransformsAt(self, time: float, propagateChildren: bool = ...) -> None:
        """"""
    def BeginAbsoluteSequence(self, newTransformStartTime: float, recursive: bool = ...) -> IDisposable:
        """"""
    def BeginDelayedSequence(self, delay: float, recursive: bool = ...) -> IDisposable:
        """"""
    def ChangeBeatmapAvailability(self, newBeatmapAvailability: BeatmapAvailability) -> Task:
        """
        
        :param newBeatmapAvailability: 
        :return: 
        """
    @overload
    def ChangeSettings(self, settings: MultiplayerRoomSettings) -> Task:
        """
        
        :param settings: 
        :return: 
        """
    @overload
    def ChangeSettings(self, name: Optional[str] = ..., password: Optional[str] = ..., matchType: Optional[MatchType] = ..., queueMode: Optional[QueueMode] = ..., autoStartDuration: Optional[TimeSpan] = ..., autoSkip: Optional[bool] = ..., maxParticipants: Optional[Optional[int]] = ...) -> Task:
        """
        
        :param name: 
        :param password: 
        :param matchType: 
        :param queueMode: 
        :param autoStartDuration: 
        :param autoSkip: 
        :param maxParticipants: 
        :return: 
        """
    def ChangeState(self, newState: MultiplayerUserState) -> Task:
        """
        
        :param newState: 
        :return: 
        """
    @overload
    def ChangeUserMods(self, newMods: IEnumerable[APIMod]) -> Task:
        """
        
        :param newMods: 
        :return: 
        """
    @overload
    def ChangeUserMods(self, newMods: IEnumerable[Mod]) -> Task:
        """
        
        :param newMods: 
        :return: 
        """
    def ChangeUserStyle(self, beatmapId: Optional[int], rulesetId: Optional[int]) -> Task:
        """
        
        :param beatmapId: 
        :param rulesetId: 
        :return: 
        """
    def ClearTransforms(self, propagateChildren: bool = ..., targetMember: str = ...) -> None:
        """"""
    def ClearTransformsAfter(self, time: float, propagateChildren: bool = ..., targetMember: str = ...) -> None:
        """"""
    def ComputeMaskingBounds(self) -> RectangleF:
        """"""
    def Contains(self, screenSpacePos: Vector2) -> bool:
        """"""
    def CreateProxy(self) -> Drawable:
        """"""
    def CreateRoom(self, room: Room) -> Task:
        """
        
        :param room: 
        :return: 
        """
    def DiscardCards(self, cards: Array[RankedPlayCardItem]) -> Task:
        """
        
        :param cards: 
        :return: 
        """
    def DisconnectRequested(self) -> Task:
        """
        
        :return: 
        """
    def Dispose(self) -> None:
        """"""
    def EditPlaylistItem(self, item: MultiplayerPlaylistItem) -> Task:
        """
        
        :param item: 
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def Expire(self, calculateLifetimeStart: bool = ...) -> None:
        """"""
    def FinishTransforms(self, propagateChildren: bool = ..., targetMember: str = ...) -> None:
        """"""
    def GameplayAborted(self, reason: GameplayAbortReason) -> Task:
        """
        
        :param reason: 
        :return: 
        """
    def GameplayStarted(self) -> Task:
        """
        
        :return: 
        """
    def GetCardWithPlaylistItem(self, card: RankedPlayCardItem) -> RankedPlayCardWithPlaylistItem:
        """
        
        :param card: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetMatchmakingPoolsOfType(self, type: MatchmakingPoolType) -> Task[Array[MatchmakingPool]]:
        """
        
        :param type: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def Hide(self) -> None:
        """"""
    def HostChanged(self, userId: int) -> Task:
        """
        
        :param userId: 
        :return: 
        """
    def Invalidate(self, invalidation: Invalidation = ..., source: InvalidationSource = ...) -> bool:
        """"""
    def InvitePlayer(self, userId: int) -> Task:
        """
        
        :param userId: 
        :return: 
        """
    def Invited(self, invitedBy: int, roomID: int, password: str) -> Task:
        """
        
        :param invitedBy: 
        :param roomID: 
        :param password: 
        :return: 
        """
    def JoinRoom(self, room: Room, password: str = ...) -> Task:
        """
        
        :param room: 
        :param password: 
        :return: 
        """
    def KickUser(self, userId: int) -> Task:
        """
        
        :param userId: 
        :return: 
        """
    def LeaveRoom(self) -> Task:
        """
        
        :return: 
        """
    def LoadRequested(self) -> Task:
        """
        
        :return: 
        """
    def MatchEvent(self, e: MatchServerEvent) -> Task:
        """
        
        :param e: 
        :return: 
        """
    def MatchRoomStateChanged(self, state: MatchRoomState) -> Task:
        """
        
        :param state: 
        :return: 
        """
    def MatchUserStateChanged(self, userId: int, state: MatchUserState) -> Task:
        """
        
        :param userId: 
        :param state: 
        :return: 
        """
    def MatchmakingAcceptDuel(self, request: MatchmakingAcceptDuelRequest) -> Task[MatchmakingAcceptDuelResponse]:
        """
        
        :param request: 
        :return: 
        """
    def MatchmakingAcceptInvitation(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingDeclineInvitation(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingDuelIssued(self, issue: MatchmakingDuelIssuedParams) -> Task:
        """
        
        :param issue: 
        :return: 
        """
    def MatchmakingIssueDuel(self, request: MatchmakingIssueDuelRequest) -> Task[MatchmakingIssueDuelResponse]:
        """
        
        :param request: 
        :return: 
        """
    def MatchmakingItemDeselected(self, userId: int, playlistItemId: int) -> Task:
        """
        
        :param userId: 
        :param playlistItemId: 
        :return: 
        """
    def MatchmakingItemSelected(self, userId: int, playlistItemId: int) -> Task:
        """
        
        :param userId: 
        :param playlistItemId: 
        :return: 
        """
    def MatchmakingJoinLobbyWithParams(self, request: MatchmakingJoinLobbyRequest) -> Task[MatchmakingJoinLobbyResponse]:
        """
        
        :param request: 
        :return: 
        """
    def MatchmakingJoinQueue(self, poolId: int) -> Task:
        """
        
        :param poolId: 
        :return: 
        """
    def MatchmakingLeaveLobby(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingLeaveQueue(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingLobbyStatusChanged(self, status: MatchmakingLobbyStatus) -> Task:
        """
        
        :param status: 
        :return: 
        """
    def MatchmakingQueueJoined(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingQueueLeft(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingQueueStatusChanged(self, status: MatchmakingQueueStatus) -> Task:
        """
        
        :param status: 
        :return: 
        """
    def MatchmakingRoomInvited(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingRoomInvitedWithParams(self, invitation: MatchmakingRoomInvitationParams) -> Task:
        """
        
        :param invitation: 
        :return: 
        """
    def MatchmakingRoomReady(self, roomId: int, password: str) -> Task:
        """
        
        :param roomId: 
        :param password: 
        :return: 
        """
    def MatchmakingSkipToNextStage(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingToggleSelection(self, playlistItemId: int) -> Task:
        """
        
        :param playlistItemId: 
        :return: 
        """
    def PlayCard(self, card: RankedPlayCardItem) -> Task:
        """
        
        :param card: 
        :return: 
        """
    def PlaylistItemAdded(self, item: MultiplayerPlaylistItem) -> Task:
        """
        
        :param item: 
        :return: 
        """
    def PlaylistItemChanged(self, item: MultiplayerPlaylistItem) -> Task:
        """
        
        :param item: 
        :return: 
        """
    def PlaylistItemRemoved(self, playlistItemId: int) -> Task:
        """
        
        :param playlistItemId: 
        :return: 
        """
    def RankedPlayCardAdded(self, userId: int, card: RankedPlayCardItem) -> Task:
        """
        
        :param userId: 
        :param card: 
        :return: 
        """
    def RankedPlayCardPlayed(self, card: RankedPlayCardItem) -> Task:
        """
        
        :param card: 
        :return: 
        """
    def RankedPlayCardRemoved(self, userId: int, card: RankedPlayCardItem) -> Task:
        """
        
        :param userId: 
        :param card: 
        :return: 
        """
    def RankedPlayCardRevealed(self, card: RankedPlayCardItem, item: MultiplayerPlaylistItem) -> Task:
        """
        
        :param card: 
        :param item: 
        :return: 
        """
    def ReceivePositionalInputAt(self, screenSpacePos: Vector2) -> bool:
        """"""
    def Reconnect(self) -> Task:
        """
        
        :return: 
        """
    def RegisterForDependencyActivation(self, registry: IDependencyActivatorRegistry) -> None:
        """"""
    def RemovePlaylistItem(self, playlistItemId: int) -> Task:
        """
        
        :param playlistItemId: 
        :return: 
        """
    def RemoveTransform(self, toRemove: Transform) -> None:
        """"""
    def ResultsReady(self) -> Task:
        """
        
        :return: 
        """
    def RoomStateChanged(self, state: MultiplayerRoomState) -> Task:
        """
        
        :param state: 
        :return: 
        """
    def SendMatchRequest(self, request: MatchUserRequest) -> Task:
        """
        
        :param request: 
        :return: 
        """
    def ServerShuttingDown(self) -> Task:
        """
        
        :return: 
        """
    def SettingsChanged(self, newSettings: MultiplayerRoomSettings) -> Task:
        """
        
        :param newSettings: 
        :return: 
        """
    def Show(self) -> None:
        """"""
    def StartMatch(self) -> Task:
        """
        
        :return: 
        """
    @overload
    def ToLocalSpace(self, screenSpaceQuad: Quad) -> Quad:
        """"""
    @overload
    def ToLocalSpace(self, screenSpacePos: Vector2) -> Vector2:
        """"""
    @overload
    def ToParentSpace(self, input: RectangleF) -> Quad:
        """"""
    @overload
    def ToParentSpace(self, input: Vector2) -> Vector2:
        """"""
    @overload
    def ToScreenSpace(self, input: RectangleF) -> Quad:
        """"""
    @overload
    def ToScreenSpace(self, input: Vector2) -> Vector2:
        """"""
    @overload
    def ToSpaceOfOtherDrawable(self, input: RectangleF, other: IDrawable) -> Quad:
        """"""
    @overload
    def ToSpaceOfOtherDrawable(self, input: Vector2, other: IDrawable) -> Vector2:
        """"""
    def ToString(self) -> str:
        """"""
    def ToggleReady(self) -> Task:
        """
        
        :return: 
        """
    def ToggleSpectate(self) -> Task:
        """
        
        :return: 
        """
    def TransferHost(self, userId: int) -> Task:
        """
        
        :param userId: 
        :return: 
        """
    def TransformsForTargetMember(self, targetMember: str) -> IEnumerable[Transform]:
        """"""
    def TriggerClick(self) -> bool:
        """"""
    def TriggerEvent(self, e: UIEvent) -> bool:
        """"""
    def UpdateSubTree(self) -> bool:
        """"""
    def UpdateSubTreeMasking(self) -> bool:
        """"""
    def UserBeatmapAvailabilityChanged(self, userId: int, beatmapAvailability: BeatmapAvailability) -> Task:
        """
        
        :param userId: 
        :param beatmapAvailability: 
        :return: 
        """
    def UserJoined(self, user: MultiplayerRoomUser) -> Task:
        """
        
        :param user: 
        :return: 
        """
    def UserKicked(self, user: MultiplayerRoomUser) -> Task:
        """
        
        :param user: 
        :return: 
        """
    def UserLeft(self, user: MultiplayerRoomUser) -> Task:
        """
        
        :param user: 
        :return: 
        """
    def UserModsChanged(self, userId: int, mods: IEnumerable[APIMod]) -> Task:
        """
        
        :param userId: 
        :param mods: 
        :return: 
        """
    def UserStateChanged(self, userId: int, state: MultiplayerUserState) -> Task:
        """
        
        :param userId: 
        :param state: 
        :return: 
        """
    def UserStyleChanged(self, userId: int, beatmapId: Optional[int], rulesetId: Optional[int]) -> Task:
        """
        
        :param userId: 
        :param beatmapId: 
        :param rulesetId: 
        :return: 
        """
    def UserVotedToSkipIntro(self, userId: int, voted: bool) -> Task:
        """
        
        :param userId: 
        :param voted: 
        :return: 
        """
    def VoteToSkipIntro(self) -> Task:
        """
        
        :return: 
        """
    def VoteToSkipIntroPassed(self) -> Task:
        """
        
        :return: 
        """
    def WithEffect(self, effect: IEffect[T], initializationAction: Action[T] = ...) -> T:
        """"""
    def __contains__(self, screenSpacePos: Vector2) -> bool:
        """"""
    BeatmapAvailabilityChanged: EventType[Action[MultiplayerRoomUser, BeatmapAvailability]] = ...
    """"""
    CountdownStarted: EventType[Action[MultiplayerCountdown]] = ...
    """"""
    CountdownStopped: EventType[Action[MultiplayerCountdown]] = ...
    """"""
    Disconnecting: EventType[Action] = ...
    """"""
    GameplayAborted: EventType[Action[GameplayAbortReason]] = ...
    """"""
    GameplayStarted: EventType[Action] = ...
    """"""
    HostChanged: EventType[Action[MultiplayerRoomUser]] = ...
    """"""
    ItemAdded: EventType[Action[MultiplayerPlaylistItem]] = ...
    """"""
    ItemChanged: EventType[Action[MultiplayerPlaylistItem]] = ...
    """"""
    ItemRemoved: EventType[Action[int]] = ...
    """"""
    LoadRequested: EventType[Action] = ...
    """"""
    MatchEvent: EventType[Action[MatchServerEvent]] = ...
    """"""
    MatchRoomStateChanged: EventType[Action[MatchRoomState]] = ...
    """"""
    MatchmakingDuelIssued: EventType[Action[MatchmakingDuelIssuedParams]] = ...
    """"""
    MatchmakingItemDeselected: EventType[Action[int, int]] = ...
    """"""
    MatchmakingItemSelected: EventType[Action[int, int]] = ...
    """"""
    MatchmakingLobbyStatusChanged: EventType[Action[MatchmakingLobbyStatus]] = ...
    """"""
    MatchmakingQueueJoined: EventType[Action] = ...
    """"""
    MatchmakingQueueLeft: EventType[Action] = ...
    """"""
    MatchmakingQueueStatusChanged: EventType[Action[MatchmakingQueueStatus]] = ...
    """"""
    MatchmakingRoomInvited: EventType[Action[MatchmakingRoomInvitationParams]] = ...
    """"""
    MatchmakingRoomReady: EventType[Action[int, str]] = ...
    """"""
    OnLoadComplete: EventType[Action[Drawable]] = ...
    """"""
    OnUpdate: EventType[Action[Drawable]] = ...
    """"""
    RankedPlayCardAdded: EventType[Action[int, RankedPlayCardWithPlaylistItem]] = ...
    """"""
    RankedPlayCardPlayed: EventType[Action[RankedPlayCardWithPlaylistItem]] = ...
    """"""
    RankedPlayCardRemoved: EventType[Action[int, RankedPlayCardWithPlaylistItem]] = ...
    """"""
    ResultsReady: EventType[Action] = ...
    """"""
    RoomUpdated: EventType[Action] = ...
    """"""
    SettingsChanged: EventType[Action[MultiplayerRoomSettings]] = ...
    """"""
    UserJoined: EventType[Action[MultiplayerRoomUser]] = ...
    """"""
    UserKicked: EventType[Action[MultiplayerRoomUser]] = ...
    """"""
    UserLeft: EventType[Action[MultiplayerRoomUser]] = ...
    """"""
    UserModsChanged: EventType[Action[MultiplayerRoomUser]] = ...
    """"""
    UserStateChanged: EventType[Action[MultiplayerRoomUser, MultiplayerUserState]] = ...
    """"""
    UserStyleChanged: EventType[Action[MultiplayerRoomUser]] = ...
    """"""
    UserVotedToSkipIntro: EventType[Action[int, bool]] = ...
    """"""
    VoteToSkipIntroPassed: EventType[Action] = ...
    """"""
class MultiplayerClientExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FireAndForget(cls, task: Task, onSuccess: Action = ..., onError: Action[Exception] = ...) -> None:
        """
        
        :param task: 
        :param onSuccess: 
        :param onError: 
        """
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetHubExceptionMessage(cls, exception: Exception) -> str:
        """
        
        :param exception: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ReconnectWhenReady(cls, client: IStatefulUserHubClient, isConnected: IBindable[bool], readyFunction: Func[bool], reconnectFunction: Func[Task]) -> None:
        """
        
        :param client: 
        :param isConnected: 
        :param readyFunction: 
        :param reconnectFunction: 
        """
    def ToString(self) -> str:
        """"""
class MultiplayerCountdown(ABC, Object):
    """"""
    @property
    def ID(self) -> int:
        """
        
        :return: 
        """
    @ID.setter
    def ID(self, value: int) -> None: ...
    @property
    def IsExclusive(self) -> bool:
        """
        
        :return: 
        """
    @property
    def TimeRemaining(self) -> TimeSpan:
        """
        
        :return: 
        """
    @TimeRemaining.setter
    def TimeRemaining(self, value: TimeSpan) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class MultiplayerInvitationNotification(UserAvatarNotification, ICollection[Drawable], IEnumerable[Drawable], IReadOnlyCollection[Drawable], IReadOnlyList[Drawable], IEnumerable, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, IContainer, IContainerCollection[Drawable], IContainerEnumerable[Drawable], ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
    """"""
    Activated: Final[Func[bool]] = ...
    """
    
    :return: 
    """
    MainContent: Final[Container] = ...
    """
    
    :return: 
    """
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    def __init__(self, user: APIUser, room: Room):
        """
        
        :param user: 
        :param room: 
        """
    @property
    def AcceptsFocus(self) -> bool:
        """"""
    @property
    def AliveChildren(self) -> IReadOnlyList[Drawable]:
        """"""
    @property
    def Alpha(self) -> float:
        """"""
    @Alpha.setter
    def Alpha(self, value: float) -> None: ...
    @property
    def AlwaysPresent(self) -> bool:
        """"""
    @AlwaysPresent.setter
    def AlwaysPresent(self, value: bool) -> None: ...
    @property
    def Anchor(self) -> Anchor:
        """"""
    @Anchor.setter
    def Anchor(self, value: Anchor) -> None: ...
    @property
    def AnchorPosition(self) -> Vector2:
        """"""
    @property
    def AutoSizeAxes(self) -> Axes:
        """"""
    @AutoSizeAxes.setter
    def AutoSizeAxes(self, value: Axes) -> None: ...
    @property
    def AutoSizeDuration(self) -> float:
        """"""
    @AutoSizeDuration.setter
    def AutoSizeDuration(self, value: float) -> None: ...
    @property
    def AutoSizeEasing(self) -> Easing:
        """"""
    @AutoSizeEasing.setter
    def AutoSizeEasing(self, value: Easing) -> None: ...
    @property
    def Blending(self) -> BlendingParameters:
        """"""
    @Blending.setter
    def Blending(self, value: BlendingParameters) -> None: ...
    @property
    def BorderColour(self) -> ColourInfo:
        """"""
    @BorderColour.setter
    def BorderColour(self, value: ColourInfo) -> None: ...
    @property
    def BorderThickness(self) -> float:
        """"""
    @BorderThickness.setter
    def BorderThickness(self, value: float) -> None: ...
    @property
    def BoundingBox(self) -> RectangleF:
        """"""
    @property
    def BypassAutoSizeAxes(self) -> Axes:
        """"""
    @BypassAutoSizeAxes.setter
    def BypassAutoSizeAxes(self, value: Axes) -> None: ...
    @property
    def ChangeFocusOnClick(self) -> bool:
        """"""
    @property
    def Child(self) -> Drawable:
        """"""
    @Child.setter
    def Child(self, value: Drawable) -> None: ...
    @property
    def ChildMaskingBounds(self) -> RectangleF:
        """"""
    @property
    def ChildOffset(self) -> Vector2:
        """"""
    @property
    def ChildSize(self) -> Vector2:
        """"""
    @property
    def Children(self) -> IReadOnlyList[Drawable]:
        """"""
    @Children.setter
    def Children(self, value: IReadOnlyList[Drawable]) -> None: ...
    @property
    def ChildrenEnumerable(self) -> IEnumerable[Drawable]:
        """"""
    @ChildrenEnumerable.setter
    def ChildrenEnumerable(self, value: IEnumerable[Drawable]) -> None: ...
    @property
    def Clock(self) -> IFrameBasedClock:
        """"""
    @Clock.setter
    def Clock(self, value: IFrameBasedClock) -> None: ...
    @property
    def Colour(self) -> ColourInfo:
        """"""
    @Colour.setter
    def Colour(self, value: ColourInfo) -> None: ...
    @property
    def CornerExponent(self) -> float:
        """"""
    @CornerExponent.setter
    def CornerExponent(self, value: float) -> None: ...
    @property
    def CornerRadius(self) -> float:
        """"""
    @CornerRadius.setter
    def CornerRadius(self, value: float) -> None: ...
    @property
    def Count(self) -> int:
        """"""
    @property
    def Dependencies(self) -> IReadOnlyDependencyContainer:
        """"""
    @property
    def Depth(self) -> float:
        """"""
    @Depth.setter
    def Depth(self, value: float) -> None: ...
    @property
    def DisplayOnTop(self) -> bool:
        """
        
        :return: 
        """
    @property
    def DisposeOnDeathRemoval(self) -> bool:
        """"""
    @property
    def DragBlocksClick(self) -> bool:
        """"""
    @property
    def DrawColourInfo(self) -> DrawColourInfo:
        """"""
    @property
    def DrawHeight(self) -> float:
        """"""
    @property
    def DrawInfo(self) -> DrawInfo:
        """"""
    @property
    def DrawPosition(self) -> Vector2:
        """"""
    @property
    def DrawRectangle(self) -> RectangleF:
        """"""
    @property
    def DrawSize(self) -> Vector2:
        """"""
    @property
    def DrawWidth(self) -> float:
        """"""
    @property
    def EdgeEffect(self) -> EdgeEffectParameters:
        """"""
    @EdgeEffect.setter
    def EdgeEffect(self, value: EdgeEffectParameters) -> None: ...
    @property
    def FillAspectRatio(self) -> float:
        """"""
    @FillAspectRatio.setter
    def FillAspectRatio(self, value: float) -> None: ...
    @property
    def FillMode(self) -> FillMode:
        """"""
    @FillMode.setter
    def FillMode(self, value: FillMode) -> None: ...
    @property
    def ForceLocalVertexBatch(self) -> bool:
        """"""
    @ForceLocalVertexBatch.setter
    def ForceLocalVertexBatch(self, value: bool) -> None: ...
    @property
    def ForwardToOverlay(self) -> Action:
        """
        
        :return: 
        """
    @ForwardToOverlay.setter
    def ForwardToOverlay(self, value: Action) -> None: ...
    @property
    def HandleNonPositionalInput(self) -> bool:
        """"""
    @property
    def HandlePositionalInput(self) -> bool:
        """"""
    @property
    def HasFocus(self) -> bool:
        """"""
    @property
    def HasProxy(self) -> bool:
        """"""
    @property
    def Height(self) -> float:
        """"""
    @Height.setter
    def Height(self, value: float) -> None: ...
    @property
    def Icon(self) -> IconUsage:
        """
        
        :return: 
        """
    @Icon.setter
    def Icon(self, value: IconUsage) -> None: ...
    @property
    def IconColour(self) -> ColourInfo:
        """
        
        :return: 
        """
    @IconColour.setter
    def IconColour(self, value: ColourInfo) -> None: ...
    @property
    def InvalidationFromParentSize(self) -> Invalidation:
        """"""
    @property
    def InvalidationID(self) -> int:
        """"""
    @property
    def IsAlive(self) -> bool:
        """"""
    @property
    def IsCritical(self) -> bool:
        """
        
        :return: 
        """
    @IsCritical.setter
    def IsCritical(self, value: bool) -> None: ...
    @property
    def IsDragged(self) -> bool:
        """"""
    @property
    def IsHovered(self) -> bool:
        """"""
    @property
    def IsImportant(self) -> bool:
        """
        
        :return: 
        """
    @IsImportant.setter
    def IsImportant(self, value: bool) -> None: ...
    @property
    def IsInToastTray(self) -> bool:
        """
        
        :return: 
        """
    @IsInToastTray.setter
    def IsInToastTray(self, value: bool) -> None: ...
    @property
    def IsLoaded(self) -> bool:
        """"""
    @property
    def IsPresent(self) -> bool:
        """"""
    @property
    def IsProxy(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def LatestTransformEndTime(self) -> float:
        """"""
    @property
    def LayoutRectangle(self) -> RectangleF:
        """"""
    @property
    def LayoutSize(self) -> Vector2:
        """"""
    @property
    def LifetimeEnd(self) -> float:
        """"""
    @LifetimeEnd.setter
    def LifetimeEnd(self, value: float) -> None: ...
    @property
    def LifetimeStart(self) -> float:
        """"""
    @LifetimeStart.setter
    def LifetimeStart(self, value: float) -> None: ...
    @property
    def LoadState(self) -> LoadState:
        """"""
    @property
    def Margin(self) -> MarginPadding:
        """"""
    @Margin.setter
    def Margin(self, value: MarginPadding) -> None: ...
    @property
    def Masking(self) -> bool:
        """"""
    @Masking.setter
    def Masking(self, value: bool) -> None: ...
    @property
    def MaskingSmoothness(self) -> float:
        """"""
    @MaskingSmoothness.setter
    def MaskingSmoothness(self, value: float) -> None: ...
    @property
    def Origin(self) -> Anchor:
        """"""
    @Origin.setter
    def Origin(self, value: Anchor) -> None: ...
    @property
    def OriginPosition(self) -> Vector2:
        """"""
    @OriginPosition.setter
    def OriginPosition(self, value: Vector2) -> None: ...
    @property
    def Padding(self) -> MarginPadding:
        """"""
    @Padding.setter
    def Padding(self, value: MarginPadding) -> None: ...
    @property
    def Parent(self) -> CompositeDrawable:
        """"""
    @property
    def PopInSampleName(self) -> str:
        """
        
        :return: 
        """
    @property
    def PopOutSampleName(self) -> str:
        """
        
        :return: 
        """
    @property
    def Position(self) -> Vector2:
        """"""
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
    @property
    def PropagateNonPositionalInputSubTree(self) -> bool:
        """"""
    @property
    def PropagatePositionalInputSubTree(self) -> bool:
        """"""
    @property
    def Read(self) -> bool:
        """
        
        :return: 
        """
    @Read.setter
    def Read(self, value: bool) -> None: ...
    @property
    def RelativeAnchorPosition(self) -> Vector2:
        """"""
    @RelativeAnchorPosition.setter
    def RelativeAnchorPosition(self, value: Vector2) -> None: ...
    @property
    def RelativeChildOffset(self) -> Vector2:
        """"""
    @RelativeChildOffset.setter
    def RelativeChildOffset(self, value: Vector2) -> None: ...
    @property
    def RelativeChildSize(self) -> Vector2:
        """"""
    @RelativeChildSize.setter
    def RelativeChildSize(self, value: Vector2) -> None: ...
    @property
    def RelativeOriginPosition(self) -> Vector2:
        """"""
    @property
    def RelativePositionAxes(self) -> Axes:
        """"""
    @RelativePositionAxes.setter
    def RelativePositionAxes(self, value: Axes) -> None: ...
    @property
    def RelativeSizeAxes(self) -> Axes:
        """"""
    @RelativeSizeAxes.setter
    def RelativeSizeAxes(self, value: Axes) -> None: ...
    @property
    def RelativeToAbsoluteFactor(self) -> Vector2:
        """"""
    @property
    def RemoveCompletedTransforms(self) -> bool:
        """"""
    @property
    def RemoveWhenNotAlive(self) -> bool:
        """"""
    @property
    def RequestsFocus(self) -> bool:
        """"""
    @property
    def Rotation(self) -> float:
        """"""
    @Rotation.setter
    def Rotation(self, value: float) -> None: ...
    @property
    def Scale(self) -> Vector2:
        """"""
    @Scale.setter
    def Scale(self, value: Vector2) -> None: ...
    @property
    def ScreenSpaceDrawQuad(self) -> Quad:
        """"""
    @property
    def Shear(self) -> Vector2:
        """"""
    @Shear.setter
    def Shear(self, value: Vector2) -> None: ...
    @property
    def Size(self) -> Vector2:
        """"""
    @Size.setter
    def Size(self, value: Vector2) -> None: ...
    @property
    def Text(self) -> LocalisableString:
        """
        
        :return: 
        """
    @Text.setter
    def Text(self, value: LocalisableString) -> None: ...
    @property
    def Time(self) -> FrameTimeInfo:
        """"""
    @property
    def TransformStartTime(self) -> float:
        """"""
    @property
    def Transforms(self) -> IEnumerable[Transform]:
        """"""
    @property
    def Transient(self) -> bool:
        """
        
        :return: 
        """
    @Transient.setter
    def Transient(self, value: bool) -> None: ...
    @property
    def WasClosed(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Width(self) -> float:
        """"""
    @Width.setter
    def Width(self, value: float) -> None: ...
    @property
    def X(self) -> float:
        """"""
    @X.setter
    def X(self, value: float) -> None: ...
    @property
    def Y(self) -> float:
        """"""
    @Y.setter
    def Y(self, value: float) -> None: ...
    def Add(self, drawable: Drawable) -> None:
        """"""
    def AddRange(self, range: IEnumerable[Drawable]) -> None:
        """"""
    def AddTransform(self, transform: Transform, customTransformID: Optional[int] = ...) -> None:
        """"""
    def ApplyTransformsAt(self, time: float, propagateChildren: bool = ...) -> None:
        """"""
    def BeginAbsoluteSequence(self, newTransformStartTime: float, recursive: bool = ...) -> IDisposable:
        """"""
    def BeginDelayedSequence(self, delay: float, recursive: bool = ...) -> IDisposable:
        """"""
    def ChangeChildDepth(self, child: Drawable, newDepth: float) -> None:
        """"""
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Clear(self, disposeChildren: bool) -> None:
        """"""
    def ClearTransforms(self, propagateChildren: bool = ..., targetMember: str = ...) -> None:
        """"""
    def ClearTransformsAfter(self, time: float, propagateChildren: bool = ..., targetMember: str = ...) -> None:
        """"""
    def Close(self, runFlingAnimation: bool) -> None:
        """
        
        :param runFlingAnimation: 
        """
    def ComputeMaskingBounds(self) -> RectangleF:
        """"""
    @overload
    def Contains(self, drawable: Drawable) -> bool:
        """"""
    @overload
    def Contains(self, screenSpacePos: Vector2) -> bool:
        """"""
    def CopyTo(self, array: Array[Drawable], arrayIndex: int) -> None:
        """"""
    def CreateProxy(self) -> Drawable:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Expire(self, calculateLifetimeStart: bool = ...) -> None:
        """"""
    def FinishTransforms(self, propagateChildren: bool = ..., targetMember: str = ...) -> None:
        """"""
    def GetEnumerator(self) -> Container.Enumerator[Drawable]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Hide(self) -> None:
        """"""
    def IndexOf(self, drawable: Drawable) -> int:
        """"""
    def Invalidate(self, invalidation: Invalidation = ..., source: InvalidationSource = ...) -> bool:
        """"""
    def ReceivePositionalInputAt(self, screenSpacePos: Vector2) -> bool:
        """"""
    def RegisterForDependencyActivation(self, registry: IDependencyActivatorRegistry) -> None:
        """"""
    @overload
    def Remove(self, item: Drawable) -> bool:
        """"""
    @overload
    def Remove(self, drawable: Drawable, disposeImmediately: bool) -> bool:
        """"""
    def RemoveAll(self, pred: Predicate[Drawable], disposeImmediately: bool) -> int:
        """"""
    def RemoveRange(self, range: IEnumerable[Drawable], disposeImmediately: bool) -> None:
        """"""
    def RemoveTransform(self, toRemove: Transform) -> None:
        """"""
    def Show(self) -> None:
        """"""
    @overload
    def ToLocalSpace(self, screenSpaceQuad: Quad) -> Quad:
        """"""
    @overload
    def ToLocalSpace(self, screenSpacePos: Vector2) -> Vector2:
        """"""
    @overload
    def ToParentSpace(self, input: RectangleF) -> Quad:
        """"""
    @overload
    def ToParentSpace(self, input: Vector2) -> Vector2:
        """"""
    @overload
    def ToScreenSpace(self, input: RectangleF) -> Quad:
        """"""
    @overload
    def ToScreenSpace(self, input: Vector2) -> Vector2:
        """"""
    @overload
    def ToSpaceOfOtherDrawable(self, input: RectangleF, other: IDrawable) -> Quad:
        """"""
    @overload
    def ToSpaceOfOtherDrawable(self, input: Vector2, other: IDrawable) -> Vector2:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformsForTargetMember(self, targetMember: str) -> IEnumerable[Transform]:
        """"""
    def TriggerClick(self) -> bool:
        """"""
    def TriggerEvent(self, e: UIEvent) -> bool:
        """"""
    def UpdateSubTree(self) -> bool:
        """"""
    def UpdateSubTreeMasking(self) -> bool:
        """"""
    def WithEffect(self, effect: IEffect[T], initializationAction: Action[T] = ...) -> T:
        """"""
    @overload
    def __contains__(self, drawable: Drawable) -> bool:
        """"""
    @overload
    def __contains__(self, screenSpacePos: Vector2) -> bool:
        """"""
    @overload
    def __delitem__(self, item: Drawable) -> bool:
        """"""
    @overload
    def __delitem__(self, drawable: Drawable, disposeImmediately: bool) -> bool:
        """"""
    def __getitem__(self, index: int) -> Drawable:
        """"""
    def __iter__(self) -> Iterator[Drawable]:
        """"""
    def __len__(self) -> int:
        """"""
    Closed: EventType[Action] = ...
    """"""
    OnLoadComplete: EventType[Action[Drawable]] = ...
    """"""
    OnUpdate: EventType[Action[Drawable]] = ...
    """"""
class MultiplayerRoom(Object):
    """"""
    RoomID: Final[int] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, roomId: int):
        """
        
        :param roomId: 
        """
    @overload
    def __init__(self, room: Room):
        """
        
        :param room: 
        """
    @property
    def ActiveCountdowns(self) -> IList[MultiplayerCountdown]:
        """
        
        :return: 
        """
    @ActiveCountdowns.setter
    def ActiveCountdowns(self, value: IList[MultiplayerCountdown]) -> None: ...
    @property
    def ChannelID(self) -> int:
        """
        
        :return: 
        """
    @ChannelID.setter
    def ChannelID(self, value: int) -> None: ...
    @property
    def CurrentPlaylistItem(self) -> MultiplayerPlaylistItem:
        """
        
        :return: 
        """
    @property
    def Host(self) -> MultiplayerRoomUser:
        """
        
        :return: 
        """
    @Host.setter
    def Host(self, value: MultiplayerRoomUser) -> None: ...
    @property
    def MatchState(self) -> MatchRoomState:
        """
        
        :return: 
        """
    @MatchState.setter
    def MatchState(self, value: MatchRoomState) -> None: ...
    @property
    def Playlist(self) -> IList[MultiplayerPlaylistItem]:
        """
        
        :return: 
        """
    @Playlist.setter
    def Playlist(self, value: IList[MultiplayerPlaylistItem]) -> None: ...
    @property
    def Settings(self) -> MultiplayerRoomSettings:
        """
        
        :return: 
        """
    @Settings.setter
    def Settings(self, value: MultiplayerRoomSettings) -> None: ...
    @property
    def State(self) -> MultiplayerRoomState:
        """
        
        :return: 
        """
    @State.setter
    def State(self, value: MultiplayerRoomState) -> None: ...
    @property
    def Users(self) -> IList[MultiplayerRoomUser]:
        """
        
        :return: 
        """
    @Users.setter
    def Users(self, value: IList[MultiplayerRoomUser]) -> None: ...
    def CanAddPlaylistItems(self, user: MultiplayerRoomUser) -> bool:
        """
        
        :param user: 
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
class MultiplayerRoomExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetCurrentItem(cls, room: MultiplayerRoom) -> MultiplayerPlaylistItem:
        """
        
        :param room: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetHistoricalItems(cls, room: MultiplayerRoom) -> IEnumerable[MultiplayerPlaylistItem]:
        """
        
        :param room: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetUpcomingItems(cls, room: MultiplayerRoom) -> IEnumerable[MultiplayerPlaylistItem]:
        """
        
        :param room: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class MultiplayerRoomSettings(Object, IEquatable[MultiplayerRoomSettings]):
    """"""
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, room: Room):
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
    def AutoStartEnabled(self) -> bool:
        """
        
        :return: 
        """
    @property
    def MatchType(self) -> MatchType:
        """
        
        :return: 
        """
    @MatchType.setter
    def MatchType(self, value: MatchType) -> None: ...
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
    def Password(self) -> str:
        """
        
        :return: 
        """
    @Password.setter
    def Password(self, value: str) -> None: ...
    @property
    def PlaylistItemId(self) -> int:
        """
        
        :return: 
        """
    @PlaylistItemId.setter
    def PlaylistItemId(self, value: int) -> None: ...
    @property
    def QueueMode(self) -> QueueMode:
        """
        
        :return: 
        """
    @QueueMode.setter
    def QueueMode(self, value: QueueMode) -> None: ...
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: MultiplayerRoomSettings) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class MultiplayerRoomState(Enum):
    """"""
    Open: MultiplayerRoomState = ...
    """"""
    WaitingForLoad: MultiplayerRoomState = ...
    """"""
    Playing: MultiplayerRoomState = ...
    """"""
    Closed: MultiplayerRoomState = ...
    """"""
class MultiplayerRoomUser(Object, IEquatable[MultiplayerRoomUser]):
    """"""
    BeatmapId: Final[Optional[int]] = ...
    """
    
    :return: 
    """
    Role: Final[MultiplayerRoomUserRole] = ...
    """
    
    :return: 
    """
    RulesetId: Final[Optional[int]] = ...
    """
    
    :return: 
    """
    UserID: Final[int] = ...
    """
    
    :return: 
    """
    VotedToSkipIntro: Final[bool] = ...
    """
    
    :return: 
    """
    def __init__(self, userId: int):
        """
        
        :param userId: 
        """
    @property
    def BeatmapAvailability(self) -> BeatmapAvailability:
        """
        
        :return: 
        """
    @BeatmapAvailability.setter
    def BeatmapAvailability(self, value: BeatmapAvailability) -> None: ...
    @property
    def MatchState(self) -> MatchUserState:
        """
        
        :return: 
        """
    @MatchState.setter
    def MatchState(self, value: MatchUserState) -> None: ...
    @property
    def Mods(self) -> IEnumerable[APIMod]:
        """
        
        :return: 
        """
    @Mods.setter
    def Mods(self, value: IEnumerable[APIMod]) -> None: ...
    @property
    def State(self) -> MultiplayerUserState:
        """
        
        :return: 
        """
    @State.setter
    def State(self, value: MultiplayerUserState) -> None: ...
    @property
    def User(self) -> APIUser:
        """
        
        :return: 
        """
    @User.setter
    def User(self, value: APIUser) -> None: ...
    def CanStartGameplay(self) -> bool:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: MultiplayerRoomUser) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class MultiplayerRoomUserRole(Enum):
    """"""
    Player: MultiplayerRoomUserRole = ...
    """"""
    Referee: MultiplayerRoomUserRole = ...
    """"""
class MultiplayerUserState(Enum):
    """"""
    Idle: MultiplayerUserState = ...
    """"""
    Ready: MultiplayerUserState = ...
    """"""
    WaitingForLoad: MultiplayerUserState = ...
    """"""
    Loaded: MultiplayerUserState = ...
    """"""
    ReadyForGameplay: MultiplayerUserState = ...
    """"""
    Playing: MultiplayerUserState = ...
    """"""
    FinishedPlay: MultiplayerUserState = ...
    """"""
    Results: MultiplayerUserState = ...
    """"""
    Spectating: MultiplayerUserState = ...
    """"""
class NotHostException(HubException, ISerializable):
    """"""
    def __init__(self):
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
class NotJoinedRoomException(HubException, ISerializable):
    """"""
    def __init__(self):
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
class OnlineMultiplayerClient(MultiplayerClient, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache, IMatchmakingClient, IMatchmakingServer, IMultiplayerClient, IMultiplayerRoomServer, IRankedPlayClient, IRankedPlayServer, IStatefulUserHubClient):
    """"""
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    def __init__(self, endpoints: EndpointConfiguration):
        """
        
        :param endpoints: 
        """
    @property
    def AcceptsFocus(self) -> bool:
        """"""
    @property
    def Alpha(self) -> float:
        """"""
    @Alpha.setter
    def Alpha(self, value: float) -> None: ...
    @property
    def AlwaysPresent(self) -> bool:
        """"""
    @AlwaysPresent.setter
    def AlwaysPresent(self, value: bool) -> None: ...
    @property
    def Anchor(self) -> Anchor:
        """"""
    @Anchor.setter
    def Anchor(self, value: Anchor) -> None: ...
    @property
    def AnchorPosition(self) -> Vector2:
        """"""
    @property
    def Blending(self) -> BlendingParameters:
        """"""
    @Blending.setter
    def Blending(self, value: BlendingParameters) -> None: ...
    @property
    def BoundingBox(self) -> RectangleF:
        """"""
    @property
    def BypassAutoSizeAxes(self) -> Axes:
        """"""
    @BypassAutoSizeAxes.setter
    def BypassAutoSizeAxes(self, value: Axes) -> None: ...
    @property
    def ChangeFocusOnClick(self) -> bool:
        """"""
    @property
    def Clock(self) -> IFrameBasedClock:
        """"""
    @Clock.setter
    def Clock(self, value: IFrameBasedClock) -> None: ...
    @property
    def Colour(self) -> ColourInfo:
        """"""
    @Colour.setter
    def Colour(self, value: ColourInfo) -> None: ...
    @property
    def CurrentMatchPlayingUserIds(self) -> IBindableList[int]:
        """
        
        :return: 
        """
    @property
    def Depth(self) -> float:
        """"""
    @Depth.setter
    def Depth(self, value: float) -> None: ...
    @property
    def DisposeOnDeathRemoval(self) -> bool:
        """"""
    @property
    def DragBlocksClick(self) -> bool:
        """"""
    @property
    def DrawColourInfo(self) -> DrawColourInfo:
        """"""
    @property
    def DrawHeight(self) -> float:
        """"""
    @property
    def DrawInfo(self) -> DrawInfo:
        """"""
    @property
    def DrawPosition(self) -> Vector2:
        """"""
    @property
    def DrawRectangle(self) -> RectangleF:
        """"""
    @property
    def DrawSize(self) -> Vector2:
        """"""
    @property
    def DrawWidth(self) -> float:
        """"""
    @property
    def FillAspectRatio(self) -> float:
        """"""
    @FillAspectRatio.setter
    def FillAspectRatio(self, value: float) -> None: ...
    @property
    def FillMode(self) -> FillMode:
        """"""
    @FillMode.setter
    def FillMode(self, value: FillMode) -> None: ...
    @property
    def HandleNonPositionalInput(self) -> bool:
        """"""
    @property
    def HandlePositionalInput(self) -> bool:
        """"""
    @property
    def HasFocus(self) -> bool:
        """"""
    @property
    def HasProxy(self) -> bool:
        """"""
    @property
    def Height(self) -> float:
        """"""
    @Height.setter
    def Height(self, value: float) -> None: ...
    @property
    def InvalidationFromParentSize(self) -> Invalidation:
        """"""
    @property
    def InvalidationID(self) -> int:
        """"""
    @property
    def IsAlive(self) -> bool:
        """"""
    @property
    def IsConnected(self) -> IBindable[bool]:
        """
        
        :return: 
        """
    @property
    def IsDragged(self) -> bool:
        """"""
    @property
    def IsHost(self) -> bool:
        """
        
        :return: 
        """
    @property
    def IsHovered(self) -> bool:
        """"""
    @property
    def IsLoaded(self) -> bool:
        """"""
    @property
    def IsPresent(self) -> bool:
        """"""
    @property
    def IsProxy(self) -> bool:
        """"""
    @property
    def IsReferee(self) -> bool:
        """
        
        :return: 
        """
    @property
    def LatestTransformEndTime(self) -> float:
        """"""
    @property
    def LayoutRectangle(self) -> RectangleF:
        """"""
    @property
    def LayoutSize(self) -> Vector2:
        """"""
    @property
    def LifetimeEnd(self) -> float:
        """"""
    @LifetimeEnd.setter
    def LifetimeEnd(self, value: float) -> None: ...
    @property
    def LifetimeStart(self) -> float:
        """"""
    @LifetimeStart.setter
    def LifetimeStart(self, value: float) -> None: ...
    @property
    def LoadState(self) -> LoadState:
        """"""
    @property
    def LocalUser(self) -> MultiplayerRoomUser:
        """
        
        :return: 
        """
    @property
    def Margin(self) -> MarginPadding:
        """"""
    @Margin.setter
    def Margin(self, value: MarginPadding) -> None: ...
    @property
    def Origin(self) -> Anchor:
        """"""
    @Origin.setter
    def Origin(self, value: Anchor) -> None: ...
    @property
    def OriginPosition(self) -> Vector2:
        """"""
    @OriginPosition.setter
    def OriginPosition(self, value: Vector2) -> None: ...
    @property
    def Parent(self) -> CompositeDrawable:
        """"""
    @property
    def Position(self) -> Vector2:
        """"""
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
    @property
    def PostNotification(self) -> Action[Notification]:
        """
        
        :return: 
        """
    @PostNotification.setter
    def PostNotification(self, value: Action[Notification]) -> None: ...
    @property
    def PresentMatch(self) -> Action[Room, str]:
        """
        
        :return: 
        """
    @PresentMatch.setter
    def PresentMatch(self, value: Action[Room, str]) -> None: ...
    @property
    def PropagateNonPositionalInputSubTree(self) -> bool:
        """"""
    @property
    def PropagatePositionalInputSubTree(self) -> bool:
        """"""
    @property
    def RelativeAnchorPosition(self) -> Vector2:
        """"""
    @RelativeAnchorPosition.setter
    def RelativeAnchorPosition(self, value: Vector2) -> None: ...
    @property
    def RelativeOriginPosition(self) -> Vector2:
        """"""
    @property
    def RelativePositionAxes(self) -> Axes:
        """"""
    @RelativePositionAxes.setter
    def RelativePositionAxes(self, value: Axes) -> None: ...
    @property
    def RelativeSizeAxes(self) -> Axes:
        """"""
    @RelativeSizeAxes.setter
    def RelativeSizeAxes(self, value: Axes) -> None: ...
    @property
    def RemoveCompletedTransforms(self) -> bool:
        """"""
    @property
    def RemoveWhenNotAlive(self) -> bool:
        """"""
    @property
    def RequestsFocus(self) -> bool:
        """"""
    @property
    def Room(self) -> MultiplayerRoom:
        """
        
        :return: 
        """
    @property
    def Rotation(self) -> float:
        """"""
    @Rotation.setter
    def Rotation(self, value: float) -> None: ...
    @property
    def Scale(self) -> Vector2:
        """"""
    @Scale.setter
    def Scale(self, value: Vector2) -> None: ...
    @property
    def ScreenSpaceDrawQuad(self) -> Quad:
        """"""
    @property
    def Shear(self) -> Vector2:
        """"""
    @Shear.setter
    def Shear(self, value: Vector2) -> None: ...
    @property
    def Size(self) -> Vector2:
        """"""
    @Size.setter
    def Size(self, value: Vector2) -> None: ...
    @property
    def Time(self) -> FrameTimeInfo:
        """"""
    @property
    def TransformStartTime(self) -> float:
        """"""
    @property
    def Transforms(self) -> IEnumerable[Transform]:
        """"""
    @property
    def Width(self) -> float:
        """"""
    @Width.setter
    def Width(self, value: float) -> None: ...
    @property
    def X(self) -> float:
        """"""
    @X.setter
    def X(self, value: float) -> None: ...
    @property
    def Y(self) -> float:
        """"""
    @Y.setter
    def Y(self, value: float) -> None: ...
    def AbortGameplay(self) -> Task:
        """
        
        :return: 
        """
    def AbortMatch(self) -> Task:
        """
        
        :return: 
        """
    def AddPlaylistItem(self, item: MultiplayerPlaylistItem) -> Task:
        """
        
        :param item: 
        :return: 
        """
    def AddTransform(self, transform: Transform, customTransformID: Optional[int] = ...) -> None:
        """"""
    def ApplyTransformsAt(self, time: float, propagateChildren: bool = ...) -> None:
        """"""
    def BeginAbsoluteSequence(self, newTransformStartTime: float, recursive: bool = ...) -> IDisposable:
        """"""
    def BeginDelayedSequence(self, delay: float, recursive: bool = ...) -> IDisposable:
        """"""
    def ChangeBeatmapAvailability(self, newBeatmapAvailability: BeatmapAvailability) -> Task:
        """
        
        :param newBeatmapAvailability: 
        :return: 
        """
    @overload
    def ChangeSettings(self, settings: MultiplayerRoomSettings) -> Task:
        """
        
        :param settings: 
        :return: 
        """
    @overload
    def ChangeSettings(self, name: Optional[str] = ..., password: Optional[str] = ..., matchType: Optional[MatchType] = ..., queueMode: Optional[QueueMode] = ..., autoStartDuration: Optional[TimeSpan] = ..., autoSkip: Optional[bool] = ..., maxParticipants: Optional[Optional[int]] = ...) -> Task:
        """
        
        :param name: 
        :param password: 
        :param matchType: 
        :param queueMode: 
        :param autoStartDuration: 
        :param autoSkip: 
        :param maxParticipants: 
        :return: 
        """
    def ChangeState(self, newState: MultiplayerUserState) -> Task:
        """
        
        :param newState: 
        :return: 
        """
    @overload
    def ChangeUserMods(self, newMods: IEnumerable[APIMod]) -> Task:
        """
        
        :param newMods: 
        :return: 
        """
    @overload
    def ChangeUserMods(self, newMods: IEnumerable[Mod]) -> Task:
        """
        
        :param newMods: 
        :return: 
        """
    def ChangeUserStyle(self, beatmapId: Optional[int], rulesetId: Optional[int]) -> Task:
        """
        
        :param beatmapId: 
        :param rulesetId: 
        :return: 
        """
    def ClearTransforms(self, propagateChildren: bool = ..., targetMember: str = ...) -> None:
        """"""
    def ClearTransformsAfter(self, time: float, propagateChildren: bool = ..., targetMember: str = ...) -> None:
        """"""
    def ComputeMaskingBounds(self) -> RectangleF:
        """"""
    def Contains(self, screenSpacePos: Vector2) -> bool:
        """"""
    def CreateProxy(self) -> Drawable:
        """"""
    def CreateRoom(self, room: Room) -> Task:
        """
        
        :param room: 
        :return: 
        """
    def DiscardCards(self, cards: Array[RankedPlayCardItem]) -> Task:
        """
        
        :param cards: 
        :return: 
        """
    def DisconnectRequested(self) -> Task:
        """
        
        :return: 
        """
    def Dispose(self) -> None:
        """"""
    def EditPlaylistItem(self, item: MultiplayerPlaylistItem) -> Task:
        """
        
        :param item: 
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def Expire(self, calculateLifetimeStart: bool = ...) -> None:
        """"""
    def FinishTransforms(self, propagateChildren: bool = ..., targetMember: str = ...) -> None:
        """"""
    def GameplayAborted(self, reason: GameplayAbortReason) -> Task:
        """
        
        :param reason: 
        :return: 
        """
    def GameplayStarted(self) -> Task:
        """
        
        :return: 
        """
    def GetCardWithPlaylistItem(self, card: RankedPlayCardItem) -> RankedPlayCardWithPlaylistItem:
        """
        
        :param card: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetMatchmakingPoolsOfType(self, type: MatchmakingPoolType) -> Task[Array[MatchmakingPool]]:
        """
        
        :param type: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def Hide(self) -> None:
        """"""
    def HostChanged(self, userId: int) -> Task:
        """
        
        :param userId: 
        :return: 
        """
    def Invalidate(self, invalidation: Invalidation = ..., source: InvalidationSource = ...) -> bool:
        """"""
    def InvitePlayer(self, userId: int) -> Task:
        """
        
        :param userId: 
        :return: 
        """
    def Invited(self, invitedBy: int, roomID: int, password: str) -> Task:
        """
        
        :param invitedBy: 
        :param roomID: 
        :param password: 
        :return: 
        """
    def JoinRoom(self, room: Room, password: str = ...) -> Task:
        """
        
        :param room: 
        :param password: 
        :return: 
        """
    def KickUser(self, userId: int) -> Task:
        """
        
        :param userId: 
        :return: 
        """
    def LeaveRoom(self) -> Task:
        """
        
        :return: 
        """
    def LoadRequested(self) -> Task:
        """
        
        :return: 
        """
    def MatchEvent(self, e: MatchServerEvent) -> Task:
        """
        
        :param e: 
        :return: 
        """
    def MatchRoomStateChanged(self, state: MatchRoomState) -> Task:
        """
        
        :param state: 
        :return: 
        """
    def MatchUserStateChanged(self, userId: int, state: MatchUserState) -> Task:
        """
        
        :param userId: 
        :param state: 
        :return: 
        """
    def MatchmakingAcceptDuel(self, request: MatchmakingAcceptDuelRequest) -> Task[MatchmakingAcceptDuelResponse]:
        """
        
        :param request: 
        :return: 
        """
    def MatchmakingAcceptInvitation(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingDeclineInvitation(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingDuelIssued(self, issue: MatchmakingDuelIssuedParams) -> Task:
        """
        
        :param issue: 
        :return: 
        """
    def MatchmakingIssueDuel(self, request: MatchmakingIssueDuelRequest) -> Task[MatchmakingIssueDuelResponse]:
        """
        
        :param request: 
        :return: 
        """
    def MatchmakingItemDeselected(self, userId: int, playlistItemId: int) -> Task:
        """
        
        :param userId: 
        :param playlistItemId: 
        :return: 
        """
    def MatchmakingItemSelected(self, userId: int, playlistItemId: int) -> Task:
        """
        
        :param userId: 
        :param playlistItemId: 
        :return: 
        """
    def MatchmakingJoinLobbyWithParams(self, request: MatchmakingJoinLobbyRequest) -> Task[MatchmakingJoinLobbyResponse]:
        """
        
        :param request: 
        :return: 
        """
    def MatchmakingJoinQueue(self, poolId: int) -> Task:
        """
        
        :param poolId: 
        :return: 
        """
    def MatchmakingLeaveLobby(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingLeaveQueue(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingLobbyStatusChanged(self, status: MatchmakingLobbyStatus) -> Task:
        """
        
        :param status: 
        :return: 
        """
    def MatchmakingQueueJoined(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingQueueLeft(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingQueueStatusChanged(self, status: MatchmakingQueueStatus) -> Task:
        """
        
        :param status: 
        :return: 
        """
    def MatchmakingRoomInvited(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingRoomInvitedWithParams(self, invitation: MatchmakingRoomInvitationParams) -> Task:
        """
        
        :param invitation: 
        :return: 
        """
    def MatchmakingRoomReady(self, roomId: int, password: str) -> Task:
        """
        
        :param roomId: 
        :param password: 
        :return: 
        """
    def MatchmakingSkipToNextStage(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingToggleSelection(self, playlistItemId: int) -> Task:
        """
        
        :param playlistItemId: 
        :return: 
        """
    def PlayCard(self, card: RankedPlayCardItem) -> Task:
        """
        
        :param card: 
        :return: 
        """
    def PlaylistItemAdded(self, item: MultiplayerPlaylistItem) -> Task:
        """
        
        :param item: 
        :return: 
        """
    def PlaylistItemChanged(self, item: MultiplayerPlaylistItem) -> Task:
        """
        
        :param item: 
        :return: 
        """
    def PlaylistItemRemoved(self, playlistItemId: int) -> Task:
        """
        
        :param playlistItemId: 
        :return: 
        """
    def RankedPlayCardAdded(self, userId: int, card: RankedPlayCardItem) -> Task:
        """
        
        :param userId: 
        :param card: 
        :return: 
        """
    def RankedPlayCardPlayed(self, card: RankedPlayCardItem) -> Task:
        """
        
        :param card: 
        :return: 
        """
    def RankedPlayCardRemoved(self, userId: int, card: RankedPlayCardItem) -> Task:
        """
        
        :param userId: 
        :param card: 
        :return: 
        """
    def RankedPlayCardRevealed(self, card: RankedPlayCardItem, item: MultiplayerPlaylistItem) -> Task:
        """
        
        :param card: 
        :param item: 
        :return: 
        """
    def ReceivePositionalInputAt(self, screenSpacePos: Vector2) -> bool:
        """"""
    def Reconnect(self) -> Task:
        """
        
        :return: 
        """
    def RegisterForDependencyActivation(self, registry: IDependencyActivatorRegistry) -> None:
        """"""
    def RemovePlaylistItem(self, playlistItemId: int) -> Task:
        """
        
        :param playlistItemId: 
        :return: 
        """
    def RemoveTransform(self, toRemove: Transform) -> None:
        """"""
    def ResultsReady(self) -> Task:
        """
        
        :return: 
        """
    def RoomStateChanged(self, state: MultiplayerRoomState) -> Task:
        """
        
        :param state: 
        :return: 
        """
    def SendMatchRequest(self, request: MatchUserRequest) -> Task:
        """
        
        :param request: 
        :return: 
        """
    def ServerShuttingDown(self) -> Task:
        """
        
        :return: 
        """
    def SettingsChanged(self, newSettings: MultiplayerRoomSettings) -> Task:
        """
        
        :param newSettings: 
        :return: 
        """
    def Show(self) -> None:
        """"""
    def StartMatch(self) -> Task:
        """
        
        :return: 
        """
    @overload
    def ToLocalSpace(self, screenSpaceQuad: Quad) -> Quad:
        """"""
    @overload
    def ToLocalSpace(self, screenSpacePos: Vector2) -> Vector2:
        """"""
    @overload
    def ToParentSpace(self, input: RectangleF) -> Quad:
        """"""
    @overload
    def ToParentSpace(self, input: Vector2) -> Vector2:
        """"""
    @overload
    def ToScreenSpace(self, input: RectangleF) -> Quad:
        """"""
    @overload
    def ToScreenSpace(self, input: Vector2) -> Vector2:
        """"""
    @overload
    def ToSpaceOfOtherDrawable(self, input: RectangleF, other: IDrawable) -> Quad:
        """"""
    @overload
    def ToSpaceOfOtherDrawable(self, input: Vector2, other: IDrawable) -> Vector2:
        """"""
    def ToString(self) -> str:
        """"""
    def ToggleReady(self) -> Task:
        """
        
        :return: 
        """
    def ToggleSpectate(self) -> Task:
        """
        
        :return: 
        """
    def TransferHost(self, userId: int) -> Task:
        """
        
        :param userId: 
        :return: 
        """
    def TransformsForTargetMember(self, targetMember: str) -> IEnumerable[Transform]:
        """"""
    def TriggerClick(self) -> bool:
        """"""
    def TriggerEvent(self, e: UIEvent) -> bool:
        """"""
    def UpdateSubTree(self) -> bool:
        """"""
    def UpdateSubTreeMasking(self) -> bool:
        """"""
    def UserBeatmapAvailabilityChanged(self, userId: int, beatmapAvailability: BeatmapAvailability) -> Task:
        """
        
        :param userId: 
        :param beatmapAvailability: 
        :return: 
        """
    def UserJoined(self, user: MultiplayerRoomUser) -> Task:
        """
        
        :param user: 
        :return: 
        """
    def UserKicked(self, user: MultiplayerRoomUser) -> Task:
        """
        
        :param user: 
        :return: 
        """
    def UserLeft(self, user: MultiplayerRoomUser) -> Task:
        """
        
        :param user: 
        :return: 
        """
    def UserModsChanged(self, userId: int, mods: IEnumerable[APIMod]) -> Task:
        """
        
        :param userId: 
        :param mods: 
        :return: 
        """
    def UserStateChanged(self, userId: int, state: MultiplayerUserState) -> Task:
        """
        
        :param userId: 
        :param state: 
        :return: 
        """
    def UserStyleChanged(self, userId: int, beatmapId: Optional[int], rulesetId: Optional[int]) -> Task:
        """
        
        :param userId: 
        :param beatmapId: 
        :param rulesetId: 
        :return: 
        """
    def UserVotedToSkipIntro(self, userId: int, voted: bool) -> Task:
        """
        
        :param userId: 
        :param voted: 
        :return: 
        """
    def VoteToSkipIntro(self) -> Task:
        """
        
        :return: 
        """
    def VoteToSkipIntroPassed(self) -> Task:
        """
        
        :return: 
        """
    def WithEffect(self, effect: IEffect[T], initializationAction: Action[T] = ...) -> T:
        """"""
    def __contains__(self, screenSpacePos: Vector2) -> bool:
        """"""
    BeatmapAvailabilityChanged: EventType[Action[MultiplayerRoomUser, BeatmapAvailability]] = ...
    """"""
    CountdownStarted: EventType[Action[MultiplayerCountdown]] = ...
    """"""
    CountdownStopped: EventType[Action[MultiplayerCountdown]] = ...
    """"""
    Disconnecting: EventType[Action] = ...
    """"""
    GameplayAborted: EventType[Action[GameplayAbortReason]] = ...
    """"""
    GameplayStarted: EventType[Action] = ...
    """"""
    HostChanged: EventType[Action[MultiplayerRoomUser]] = ...
    """"""
    ItemAdded: EventType[Action[MultiplayerPlaylistItem]] = ...
    """"""
    ItemChanged: EventType[Action[MultiplayerPlaylistItem]] = ...
    """"""
    ItemRemoved: EventType[Action[int]] = ...
    """"""
    LoadRequested: EventType[Action] = ...
    """"""
    MatchEvent: EventType[Action[MatchServerEvent]] = ...
    """"""
    MatchRoomStateChanged: EventType[Action[MatchRoomState]] = ...
    """"""
    MatchmakingDuelIssued: EventType[Action[MatchmakingDuelIssuedParams]] = ...
    """"""
    MatchmakingItemDeselected: EventType[Action[int, int]] = ...
    """"""
    MatchmakingItemSelected: EventType[Action[int, int]] = ...
    """"""
    MatchmakingLobbyStatusChanged: EventType[Action[MatchmakingLobbyStatus]] = ...
    """"""
    MatchmakingQueueJoined: EventType[Action] = ...
    """"""
    MatchmakingQueueLeft: EventType[Action] = ...
    """"""
    MatchmakingQueueStatusChanged: EventType[Action[MatchmakingQueueStatus]] = ...
    """"""
    MatchmakingRoomInvited: EventType[Action[MatchmakingRoomInvitationParams]] = ...
    """"""
    MatchmakingRoomReady: EventType[Action[int, str]] = ...
    """"""
    OnLoadComplete: EventType[Action[Drawable]] = ...
    """"""
    OnUpdate: EventType[Action[Drawable]] = ...
    """"""
    RankedPlayCardAdded: EventType[Action[int, RankedPlayCardWithPlaylistItem]] = ...
    """"""
    RankedPlayCardPlayed: EventType[Action[RankedPlayCardWithPlaylistItem]] = ...
    """"""
    RankedPlayCardRemoved: EventType[Action[int, RankedPlayCardWithPlaylistItem]] = ...
    """"""
    ResultsReady: EventType[Action] = ...
    """"""
    RoomUpdated: EventType[Action] = ...
    """"""
    SettingsChanged: EventType[Action[MultiplayerRoomSettings]] = ...
    """"""
    UserJoined: EventType[Action[MultiplayerRoomUser]] = ...
    """"""
    UserKicked: EventType[Action[MultiplayerRoomUser]] = ...
    """"""
    UserLeft: EventType[Action[MultiplayerRoomUser]] = ...
    """"""
    UserModsChanged: EventType[Action[MultiplayerRoomUser]] = ...
    """"""
    UserStateChanged: EventType[Action[MultiplayerRoomUser, MultiplayerUserState]] = ...
    """"""
    UserStyleChanged: EventType[Action[MultiplayerRoomUser]] = ...
    """"""
    UserVotedToSkipIntro: EventType[Action[int, bool]] = ...
    """"""
    VoteToSkipIntroPassed: EventType[Action] = ...
    """"""
class QueueMode(Enum):
    """"""
    HostOnly: QueueMode = ...
    """"""
    AllPlayers: QueueMode = ...
    """"""
    AllPlayersRoundRobin: QueueMode = ...
    """"""
class RollEvent(MatchServerEvent):
    """"""
    def __init__(self):
        """"""
    @property
    def Max(self) -> int:
        """
        
        :return: 
        """
    @Max.setter
    def Max(self, value: int) -> None: ...
    @property
    def Result(self) -> int:
        """
        
        :return: 
        """
    @Result.setter
    def Result(self, value: int) -> None: ...
    @property
    def UserID(self) -> int:
        """
        
        :return: 
        """
    @UserID.setter
    def UserID(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class RollRequest(MatchUserRequest):
    """"""
    def __init__(self):
        """"""
    @property
    def Max(self) -> Optional[int]:
        """
        
        :return: 
        """
    @Max.setter
    def Max(self, value: Optional[int]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class ServerShutdownNotification(SimpleNotification, ICollection[Drawable], IEnumerable[Drawable], IReadOnlyCollection[Drawable], IReadOnlyList[Drawable], IEnumerable, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, IContainer, IContainerCollection[Drawable], IContainerEnumerable[Drawable], ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
    """"""
    Activated: Final[Func[bool]] = ...
    """
    
    :return: 
    """
    MainContent: Final[Container] = ...
    """
    
    :return: 
    """
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    def __init__(self, duration: TimeSpan):
        """
        
        :param duration: 
        """
    @property
    def AcceptsFocus(self) -> bool:
        """"""
    @property
    def AliveChildren(self) -> IReadOnlyList[Drawable]:
        """"""
    @property
    def Alpha(self) -> float:
        """"""
    @Alpha.setter
    def Alpha(self, value: float) -> None: ...
    @property
    def AlwaysPresent(self) -> bool:
        """"""
    @AlwaysPresent.setter
    def AlwaysPresent(self, value: bool) -> None: ...
    @property
    def Anchor(self) -> Anchor:
        """"""
    @Anchor.setter
    def Anchor(self, value: Anchor) -> None: ...
    @property
    def AnchorPosition(self) -> Vector2:
        """"""
    @property
    def AutoSizeAxes(self) -> Axes:
        """"""
    @AutoSizeAxes.setter
    def AutoSizeAxes(self, value: Axes) -> None: ...
    @property
    def AutoSizeDuration(self) -> float:
        """"""
    @AutoSizeDuration.setter
    def AutoSizeDuration(self, value: float) -> None: ...
    @property
    def AutoSizeEasing(self) -> Easing:
        """"""
    @AutoSizeEasing.setter
    def AutoSizeEasing(self, value: Easing) -> None: ...
    @property
    def Blending(self) -> BlendingParameters:
        """"""
    @Blending.setter
    def Blending(self, value: BlendingParameters) -> None: ...
    @property
    def BorderColour(self) -> ColourInfo:
        """"""
    @BorderColour.setter
    def BorderColour(self, value: ColourInfo) -> None: ...
    @property
    def BorderThickness(self) -> float:
        """"""
    @BorderThickness.setter
    def BorderThickness(self, value: float) -> None: ...
    @property
    def BoundingBox(self) -> RectangleF:
        """"""
    @property
    def BypassAutoSizeAxes(self) -> Axes:
        """"""
    @BypassAutoSizeAxes.setter
    def BypassAutoSizeAxes(self, value: Axes) -> None: ...
    @property
    def ChangeFocusOnClick(self) -> bool:
        """"""
    @property
    def Child(self) -> Drawable:
        """"""
    @Child.setter
    def Child(self, value: Drawable) -> None: ...
    @property
    def ChildMaskingBounds(self) -> RectangleF:
        """"""
    @property
    def ChildOffset(self) -> Vector2:
        """"""
    @property
    def ChildSize(self) -> Vector2:
        """"""
    @property
    def Children(self) -> IReadOnlyList[Drawable]:
        """"""
    @Children.setter
    def Children(self, value: IReadOnlyList[Drawable]) -> None: ...
    @property
    def ChildrenEnumerable(self) -> IEnumerable[Drawable]:
        """"""
    @ChildrenEnumerable.setter
    def ChildrenEnumerable(self, value: IEnumerable[Drawable]) -> None: ...
    @property
    def Clock(self) -> IFrameBasedClock:
        """"""
    @Clock.setter
    def Clock(self, value: IFrameBasedClock) -> None: ...
    @property
    def Colour(self) -> ColourInfo:
        """"""
    @Colour.setter
    def Colour(self, value: ColourInfo) -> None: ...
    @property
    def CornerExponent(self) -> float:
        """"""
    @CornerExponent.setter
    def CornerExponent(self, value: float) -> None: ...
    @property
    def CornerRadius(self) -> float:
        """"""
    @CornerRadius.setter
    def CornerRadius(self, value: float) -> None: ...
    @property
    def Count(self) -> int:
        """"""
    @property
    def Dependencies(self) -> IReadOnlyDependencyContainer:
        """"""
    @property
    def Depth(self) -> float:
        """"""
    @Depth.setter
    def Depth(self, value: float) -> None: ...
    @property
    def DisplayOnTop(self) -> bool:
        """
        
        :return: 
        """
    @property
    def DisposeOnDeathRemoval(self) -> bool:
        """"""
    @property
    def DragBlocksClick(self) -> bool:
        """"""
    @property
    def DrawColourInfo(self) -> DrawColourInfo:
        """"""
    @property
    def DrawHeight(self) -> float:
        """"""
    @property
    def DrawInfo(self) -> DrawInfo:
        """"""
    @property
    def DrawPosition(self) -> Vector2:
        """"""
    @property
    def DrawRectangle(self) -> RectangleF:
        """"""
    @property
    def DrawSize(self) -> Vector2:
        """"""
    @property
    def DrawWidth(self) -> float:
        """"""
    @property
    def EdgeEffect(self) -> EdgeEffectParameters:
        """"""
    @EdgeEffect.setter
    def EdgeEffect(self, value: EdgeEffectParameters) -> None: ...
    @property
    def FillAspectRatio(self) -> float:
        """"""
    @FillAspectRatio.setter
    def FillAspectRatio(self, value: float) -> None: ...
    @property
    def FillMode(self) -> FillMode:
        """"""
    @FillMode.setter
    def FillMode(self, value: FillMode) -> None: ...
    @property
    def ForceLocalVertexBatch(self) -> bool:
        """"""
    @ForceLocalVertexBatch.setter
    def ForceLocalVertexBatch(self, value: bool) -> None: ...
    @property
    def ForwardToOverlay(self) -> Action:
        """
        
        :return: 
        """
    @ForwardToOverlay.setter
    def ForwardToOverlay(self, value: Action) -> None: ...
    @property
    def HandleNonPositionalInput(self) -> bool:
        """"""
    @property
    def HandlePositionalInput(self) -> bool:
        """"""
    @property
    def HasFocus(self) -> bool:
        """"""
    @property
    def HasProxy(self) -> bool:
        """"""
    @property
    def Height(self) -> float:
        """"""
    @Height.setter
    def Height(self, value: float) -> None: ...
    @property
    def Icon(self) -> IconUsage:
        """
        
        :return: 
        """
    @Icon.setter
    def Icon(self, value: IconUsage) -> None: ...
    @property
    def IconColour(self) -> ColourInfo:
        """
        
        :return: 
        """
    @IconColour.setter
    def IconColour(self, value: ColourInfo) -> None: ...
    @property
    def InvalidationFromParentSize(self) -> Invalidation:
        """"""
    @property
    def InvalidationID(self) -> int:
        """"""
    @property
    def IsAlive(self) -> bool:
        """"""
    @property
    def IsCritical(self) -> bool:
        """
        
        :return: 
        """
    @IsCritical.setter
    def IsCritical(self, value: bool) -> None: ...
    @property
    def IsDragged(self) -> bool:
        """"""
    @property
    def IsHovered(self) -> bool:
        """"""
    @property
    def IsImportant(self) -> bool:
        """
        
        :return: 
        """
    @IsImportant.setter
    def IsImportant(self, value: bool) -> None: ...
    @property
    def IsInToastTray(self) -> bool:
        """
        
        :return: 
        """
    @IsInToastTray.setter
    def IsInToastTray(self, value: bool) -> None: ...
    @property
    def IsLoaded(self) -> bool:
        """"""
    @property
    def IsPresent(self) -> bool:
        """"""
    @property
    def IsProxy(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def LatestTransformEndTime(self) -> float:
        """"""
    @property
    def LayoutRectangle(self) -> RectangleF:
        """"""
    @property
    def LayoutSize(self) -> Vector2:
        """"""
    @property
    def LifetimeEnd(self) -> float:
        """"""
    @LifetimeEnd.setter
    def LifetimeEnd(self, value: float) -> None: ...
    @property
    def LifetimeStart(self) -> float:
        """"""
    @LifetimeStart.setter
    def LifetimeStart(self, value: float) -> None: ...
    @property
    def LoadState(self) -> LoadState:
        """"""
    @property
    def Margin(self) -> MarginPadding:
        """"""
    @Margin.setter
    def Margin(self, value: MarginPadding) -> None: ...
    @property
    def Masking(self) -> bool:
        """"""
    @Masking.setter
    def Masking(self, value: bool) -> None: ...
    @property
    def MaskingSmoothness(self) -> float:
        """"""
    @MaskingSmoothness.setter
    def MaskingSmoothness(self, value: float) -> None: ...
    @property
    def Origin(self) -> Anchor:
        """"""
    @Origin.setter
    def Origin(self, value: Anchor) -> None: ...
    @property
    def OriginPosition(self) -> Vector2:
        """"""
    @OriginPosition.setter
    def OriginPosition(self, value: Vector2) -> None: ...
    @property
    def Padding(self) -> MarginPadding:
        """"""
    @Padding.setter
    def Padding(self, value: MarginPadding) -> None: ...
    @property
    def Parent(self) -> CompositeDrawable:
        """"""
    @property
    def PopInSampleName(self) -> str:
        """
        
        :return: 
        """
    @property
    def PopOutSampleName(self) -> str:
        """
        
        :return: 
        """
    @property
    def Position(self) -> Vector2:
        """"""
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
    @property
    def PropagateNonPositionalInputSubTree(self) -> bool:
        """"""
    @property
    def PropagatePositionalInputSubTree(self) -> bool:
        """"""
    @property
    def Read(self) -> bool:
        """
        
        :return: 
        """
    @Read.setter
    def Read(self, value: bool) -> None: ...
    @property
    def RelativeAnchorPosition(self) -> Vector2:
        """"""
    @RelativeAnchorPosition.setter
    def RelativeAnchorPosition(self, value: Vector2) -> None: ...
    @property
    def RelativeChildOffset(self) -> Vector2:
        """"""
    @RelativeChildOffset.setter
    def RelativeChildOffset(self, value: Vector2) -> None: ...
    @property
    def RelativeChildSize(self) -> Vector2:
        """"""
    @RelativeChildSize.setter
    def RelativeChildSize(self, value: Vector2) -> None: ...
    @property
    def RelativeOriginPosition(self) -> Vector2:
        """"""
    @property
    def RelativePositionAxes(self) -> Axes:
        """"""
    @RelativePositionAxes.setter
    def RelativePositionAxes(self, value: Axes) -> None: ...
    @property
    def RelativeSizeAxes(self) -> Axes:
        """"""
    @RelativeSizeAxes.setter
    def RelativeSizeAxes(self, value: Axes) -> None: ...
    @property
    def RelativeToAbsoluteFactor(self) -> Vector2:
        """"""
    @property
    def RemoveCompletedTransforms(self) -> bool:
        """"""
    @property
    def RemoveWhenNotAlive(self) -> bool:
        """"""
    @property
    def RequestsFocus(self) -> bool:
        """"""
    @property
    def Rotation(self) -> float:
        """"""
    @Rotation.setter
    def Rotation(self, value: float) -> None: ...
    @property
    def Scale(self) -> Vector2:
        """"""
    @Scale.setter
    def Scale(self, value: Vector2) -> None: ...
    @property
    def ScreenSpaceDrawQuad(self) -> Quad:
        """"""
    @property
    def Shear(self) -> Vector2:
        """"""
    @Shear.setter
    def Shear(self, value: Vector2) -> None: ...
    @property
    def Size(self) -> Vector2:
        """"""
    @Size.setter
    def Size(self, value: Vector2) -> None: ...
    @property
    def Text(self) -> LocalisableString:
        """
        
        :return: 
        """
    @Text.setter
    def Text(self, value: LocalisableString) -> None: ...
    @property
    def Time(self) -> FrameTimeInfo:
        """"""
    @property
    def TransformStartTime(self) -> float:
        """"""
    @property
    def Transforms(self) -> IEnumerable[Transform]:
        """"""
    @property
    def Transient(self) -> bool:
        """
        
        :return: 
        """
    @Transient.setter
    def Transient(self, value: bool) -> None: ...
    @property
    def WasClosed(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Width(self) -> float:
        """"""
    @Width.setter
    def Width(self, value: float) -> None: ...
    @property
    def X(self) -> float:
        """"""
    @X.setter
    def X(self, value: float) -> None: ...
    @property
    def Y(self) -> float:
        """"""
    @Y.setter
    def Y(self, value: float) -> None: ...
    def Add(self, drawable: Drawable) -> None:
        """"""
    def AddRange(self, range: IEnumerable[Drawable]) -> None:
        """"""
    def AddTransform(self, transform: Transform, customTransformID: Optional[int] = ...) -> None:
        """"""
    def ApplyTransformsAt(self, time: float, propagateChildren: bool = ...) -> None:
        """"""
    def BeginAbsoluteSequence(self, newTransformStartTime: float, recursive: bool = ...) -> IDisposable:
        """"""
    def BeginDelayedSequence(self, delay: float, recursive: bool = ...) -> IDisposable:
        """"""
    def ChangeChildDepth(self, child: Drawable, newDepth: float) -> None:
        """"""
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Clear(self, disposeChildren: bool) -> None:
        """"""
    def ClearTransforms(self, propagateChildren: bool = ..., targetMember: str = ...) -> None:
        """"""
    def ClearTransformsAfter(self, time: float, propagateChildren: bool = ..., targetMember: str = ...) -> None:
        """"""
    def Close(self, runFlingAnimation: bool) -> None:
        """
        
        :param runFlingAnimation: 
        """
    def ComputeMaskingBounds(self) -> RectangleF:
        """"""
    @overload
    def Contains(self, drawable: Drawable) -> bool:
        """"""
    @overload
    def Contains(self, screenSpacePos: Vector2) -> bool:
        """"""
    def CopyTo(self, array: Array[Drawable], arrayIndex: int) -> None:
        """"""
    def CreateProxy(self) -> Drawable:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Expire(self, calculateLifetimeStart: bool = ...) -> None:
        """"""
    def FinishTransforms(self, propagateChildren: bool = ..., targetMember: str = ...) -> None:
        """"""
    def GetEnumerator(self) -> Container.Enumerator[Drawable]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Hide(self) -> None:
        """"""
    def IndexOf(self, drawable: Drawable) -> int:
        """"""
    def Invalidate(self, invalidation: Invalidation = ..., source: InvalidationSource = ...) -> bool:
        """"""
    def ReceivePositionalInputAt(self, screenSpacePos: Vector2) -> bool:
        """"""
    def RegisterForDependencyActivation(self, registry: IDependencyActivatorRegistry) -> None:
        """"""
    @overload
    def Remove(self, item: Drawable) -> bool:
        """"""
    @overload
    def Remove(self, drawable: Drawable, disposeImmediately: bool) -> bool:
        """"""
    def RemoveAll(self, pred: Predicate[Drawable], disposeImmediately: bool) -> int:
        """"""
    def RemoveRange(self, range: IEnumerable[Drawable], disposeImmediately: bool) -> None:
        """"""
    def RemoveTransform(self, toRemove: Transform) -> None:
        """"""
    def Show(self) -> None:
        """"""
    @overload
    def ToLocalSpace(self, screenSpaceQuad: Quad) -> Quad:
        """"""
    @overload
    def ToLocalSpace(self, screenSpacePos: Vector2) -> Vector2:
        """"""
    @overload
    def ToParentSpace(self, input: RectangleF) -> Quad:
        """"""
    @overload
    def ToParentSpace(self, input: Vector2) -> Vector2:
        """"""
    @overload
    def ToScreenSpace(self, input: RectangleF) -> Quad:
        """"""
    @overload
    def ToScreenSpace(self, input: Vector2) -> Vector2:
        """"""
    @overload
    def ToSpaceOfOtherDrawable(self, input: RectangleF, other: IDrawable) -> Quad:
        """"""
    @overload
    def ToSpaceOfOtherDrawable(self, input: Vector2, other: IDrawable) -> Vector2:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformsForTargetMember(self, targetMember: str) -> IEnumerable[Transform]:
        """"""
    def TriggerClick(self) -> bool:
        """"""
    def TriggerEvent(self, e: UIEvent) -> bool:
        """"""
    def UpdateSubTree(self) -> bool:
        """"""
    def UpdateSubTreeMasking(self) -> bool:
        """"""
    def WithEffect(self, effect: IEffect[T], initializationAction: Action[T] = ...) -> T:
        """"""
    @overload
    def __contains__(self, drawable: Drawable) -> bool:
        """"""
    @overload
    def __contains__(self, screenSpacePos: Vector2) -> bool:
        """"""
    @overload
    def __delitem__(self, item: Drawable) -> bool:
        """"""
    @overload
    def __delitem__(self, drawable: Drawable, disposeImmediately: bool) -> bool:
        """"""
    def __getitem__(self, index: int) -> Drawable:
        """"""
    def __iter__(self) -> Iterator[Drawable]:
        """"""
    def __len__(self) -> int:
        """"""
    Closed: EventType[Action] = ...
    """"""
    OnLoadComplete: EventType[Action[Drawable]] = ...
    """"""
    OnUpdate: EventType[Action[Drawable]] = ...
    """"""
class ServerShuttingDownCountdown(MultiplayerCountdown):
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
    @property
    def IsExclusive(self) -> bool:
        """
        
        :return: 
        """
    @property
    def TimeRemaining(self) -> TimeSpan:
        """
        
        :return: 
        """
    @TimeRemaining.setter
    def TimeRemaining(self, value: TimeSpan) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class SetLockStateRequest(MatchUserRequest):
    """"""
    def __init__(self):
        """"""
    @property
    def Locked(self) -> bool:
        """
        
        :return: 
        """
    @Locked.setter
    def Locked(self, value: bool) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class StandardMatchRoomState(MatchRoomState):
    """"""
    def __init__(self):
        """"""
    @property
    def Locked(self) -> bool:
        """
        
        :return: 
        """
    @Locked.setter
    def Locked(self, value: bool) -> None: ...
    @property
    def Slots(self) -> Optional[int]:
        """
        
        :return: 
        """
    @Slots.setter
    def Slots(self, value: Optional[int]) -> None: ...
    @classmethod
    def Create(cls, maxParticipants: Optional[int] = ...) -> StandardMatchRoomState:
        """
        
        :param maxParticipants: 
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
class UserBlockedException(HubException, ISerializable):
    """"""
    MESSAGE: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    def __init__(self):
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
class UserBlocksPMsException(HubException, ISerializable):
    """"""
    MESSAGE: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    def __init__(self):
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