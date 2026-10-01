from MessagePack.Formatters import IMessagePackFormatter
from MessagePack import MessagePackReader
from MessagePack import MessagePackSerializerOptions
from MessagePack import MessagePackWriter
from System import Action
from System import Array
from System.Collections.Generic import Dictionary
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import List
from System.Collections import IDictionary
from System import DateTimeOffset
from System import Enum
from System import Exception
from System import Func
from System import Guid
from System import IDisposable
from System import IEquatable
from System.IO import Stream
from System import Int32
from System import InvalidOperationException
from System.Net.Http.Headers import HttpResponseHeaders
from System.Net.Http import HttpMethod
from System.Net import HttpStatusCode
from System import Object
from System.Reflection import MethodBase
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Threading import CancellationToken
from System.Threading.Tasks import Task
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Framework.Allocation import IDependencyActivatorRegistry
from osu.Framework.Allocation import IDependencyInjectionCandidate
from osu.Framework.Allocation import IReadOnlyDependencyContainer
from osu.Framework.Allocation import ISourceGeneratedDependencyActivator
from osu.Framework.Allocation import ISourceGeneratedLongRunningLoadCache
from osu.Framework.Bindables import Bindable
from osu.Framework.Bindables import BindableList
from osu.Framework.Bindables import IBindable
from osu.Framework.Bindables import IBindableList
from osu.Framework.Graphics import Anchor
from osu.Framework.Graphics import Axes
from osu.Framework.Graphics import BlendingParameters
from osu.Framework.Graphics.Colour import ColourInfo
from osu.Framework.Graphics import Component
from osu.Framework.Graphics.Containers import CompositeComponent
from osu.Framework.Graphics.Containers import CompositeDrawable
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
from osu.Framework.Graphics.Transforms import ITransformable
from osu.Framework.Graphics.Transforms import Transform
from osu.Framework.IO.Network import JsonWebRequest
from osu.Framework.IO.Network import RequestParameterType
from osu.Framework.IO.Network import WebRequest
from osu.Framework.Input.Events import UIEvent
from osu.Framework.Input import ISourceGeneratedHandleInputCache
from osu.Framework.Layout import InvalidationSource
from osu.Framework.Timing import FrameTimeInfo
from osu.Framework.Timing import IFrameBasedClock
from osu.Game.Configuration import OsuConfigManager
from osu.Game.Database import IHasOnlineID
from osu.Game.Localisation import Language
from osu.Game.Online.API.DummyAPIAccess import DummyLocalUserState
from osu.Game.Online.API.RegistrationRequest import RegistrationRequestErrors
from osu.Game.Online.API.RegistrationRequest.RegistrationRequestErrors import UserErrors
from osu.Game.Online.API.Requests.Responses import APIMe
from osu.Game.Online.API.Requests.Responses import APIPlayStyle
from osu.Game.Online.API.Requests.Responses import APIRelation
from osu.Game.Online.API.Requests.Responses import APITeam
from osu.Game.Online.API.Requests.Responses import APIUser
from osu.Game.Online.API.Requests.Responses.APIUser import GlobalRank
from osu.Game.Online.API.Requests.Responses.APIUser import KudosuCount
from osu.Game.Online.API.Requests.Responses.APIUser import UserCover
from osu.Game.Online.API.Requests.Responses.APIUser import UserRankHighest
from osu.Game.Online.API.Requests.Responses import APIUserAchievement
from osu.Game.Online.API.Requests.Responses import APIUserDailyChallengeStatistics
from osu.Game.Online.API.Requests.Responses import APIUserGroup
from osu.Game.Online.API.Requests.Responses import APIUserHistoryCount
from osu.Game.Online.API.Requests.Responses import APIUserMatchmakingStatistics
from osu.Game.Online.API.Requests.Responses import SessionVerificationMethod
from osu.Game.Online.Chat import IChatClient
from osu.Game.Online.Chat import Message
from osu.Game.Online import EndpointConfiguration
from osu.Game.Online import IHubClientConnector
from osu.Game.Online.Notifications.WebSocket import DummyNotificationsClient
from osu.Game.Online.Notifications.WebSocket import INotificationsClient
from osu.Game import OsuGameBase
from osu.Game.Rulesets.Mods import Mod
from osu.Game.Rulesets import Ruleset
from osu.Game.Users import Badge
from osu.Game.Users import CountryCode
from osu.Game.Users import IUser
from osu.Game.Users import TournamentBanner
from osu.Game.Users import UserStatistics
from osuTK import Vector2
from typing import Callable
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
class APIAccess(CompositeComponent, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache, IAPIProvider):
    """"""
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    def __init__(self, game: OsuGameBase, config: OsuConfigManager, endpoints: EndpointConfiguration, versionHash: str):
        """
        
        :param game: 
        :param config: 
        :param endpoints: 
        :param versionHash: 
        """
    @property
    def APIVersion(self) -> int:
        """
        
        :return: 
        """
    @property
    def AcceptsFocus(self) -> bool:
        """"""
    @property
    def AccessToken(self) -> str:
        """
        
        :return: 
        """
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
    @property
    def AutoSizeDuration(self) -> float:
        """"""
    @property
    def AutoSizeEasing(self) -> Easing:
        """"""
    @property
    def Blending(self) -> BlendingParameters:
        """"""
    @Blending.setter
    def Blending(self, value: BlendingParameters) -> None: ...
    @property
    def BorderColour(self) -> ColourInfo:
        """"""
    @property
    def BorderThickness(self) -> float:
        """"""
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
    def ChildMaskingBounds(self) -> RectangleF:
        """"""
    @property
    def ChildOffset(self) -> Vector2:
        """"""
    @property
    def ChildSize(self) -> Vector2:
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
    def CornerExponent(self) -> float:
        """"""
    @property
    def CornerRadius(self) -> float:
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
    @property
    def Endpoints(self) -> EndpointConfiguration:
        """
        
        :return: 
        """
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
    def IsDragged(self) -> bool:
        """"""
    @property
    def IsHovered(self) -> bool:
        """"""
    @property
    def IsLoaded(self) -> bool:
        """"""
    @property
    def IsLoggedIn(self) -> bool:
        """
        
        :return: 
        """
    @property
    def IsPresent(self) -> bool:
        """"""
    @property
    def IsProxy(self) -> bool:
        """"""
    @property
    def Language(self) -> Language:
        """
        
        :return: 
        """
    @property
    def LastLoginError(self) -> Exception:
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
    def LocalUser(self) -> IBindable[APIUser]:
        """
        
        :return: 
        """
    @property
    def LocalUserState(self) -> ILocalUserState:
        """
        
        :return: 
        """
    @property
    def Margin(self) -> MarginPadding:
        """"""
    @Margin.setter
    def Margin(self, value: MarginPadding) -> None: ...
    @property
    def Masking(self) -> bool:
        """"""
    @property
    def MaskingSmoothness(self) -> float:
        """"""
    @property
    def NotificationsClient(self) -> INotificationsClient:
        """
        
        :return: 
        """
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
    @property
    def Parent(self) -> CompositeDrawable:
        """"""
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
    def ProvidedUsername(self) -> str:
        """
        
        :return: 
        """
    @property
    def RelativeAnchorPosition(self) -> Vector2:
        """"""
    @RelativeAnchorPosition.setter
    def RelativeAnchorPosition(self, value: Vector2) -> None: ...
    @property
    def RelativeChildOffset(self) -> Vector2:
        """"""
    @property
    def RelativeChildSize(self) -> Vector2:
        """"""
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
    def SecondFactorCode(self) -> str:
        """
        
        :return: 
        """
    @property
    def SessionIdentifier(self) -> Guid:
        """
        
        :return: 
        """
    @property
    def SessionVerificationMethod(self) -> Optional[SessionVerificationMethod]:
        """
        
        :return: 
        """
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
    def State(self) -> IBindable[APIState]:
        """
        
        :return: 
        """
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
    def AddTransform(self, transform: Transform, customTransformID: Optional[int] = ...) -> None:
        """"""
    def ApplyTransformsAt(self, time: float, propagateChildren: bool = ...) -> None:
        """"""
    def AuthenticateSecondFactor(self, code: str) -> None:
        """
        
        :param code: 
        """
    def BeginAbsoluteSequence(self, newTransformStartTime: float, recursive: bool = ...) -> IDisposable:
        """"""
    def BeginDelayedSequence(self, delay: float, recursive: bool = ...) -> IDisposable:
        """"""
    def ClearTransforms(self, propagateChildren: bool = ..., targetMember: str = ...) -> None:
        """"""
    def ClearTransformsAfter(self, time: float, propagateChildren: bool = ..., targetMember: str = ...) -> None:
        """"""
    def ComputeMaskingBounds(self) -> RectangleF:
        """"""
    def Contains(self, screenSpacePos: Vector2) -> bool:
        """"""
    def CreateAccount(self, email: str, username: str, password: str) -> RegistrationRequest.RegistrationRequestErrors:
        """
        
        :param email: 
        :param username: 
        :param password: 
        :return: 
        """
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
    def GetChatClient(self) -> IChatClient:
        """
        
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetHubConnector(self, clientName: str, endpoint: str) -> IHubClientConnector:
        """
        
        :param clientName: 
        :param endpoint: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def Hide(self) -> None:
        """"""
    def Invalidate(self, invalidation: Invalidation = ..., source: InvalidationSource = ...) -> bool:
        """"""
    def Login(self, username: str, password: str) -> None:
        """
        
        :param username: 
        :param password: 
        """
    def Logout(self) -> None:
        """"""
    def Perform(self, request: APIRequest) -> None:
        """
        
        :param request: 
        """
    def PerformAsync(self, request: APIRequest) -> Task:
        """
        
        :param request: 
        :return: 
        """
    def Queue(self, request: APIRequest) -> None:
        """
        
        :param request: 
        """
    def ReceivePositionalInputAt(self, screenSpacePos: Vector2) -> bool:
        """"""
    def RegisterForDependencyActivation(self, registry: IDependencyActivatorRegistry) -> None:
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
    def __contains__(self, screenSpacePos: Vector2) -> bool:
        """"""
    OnLoadComplete: EventType[Action[Drawable]] = ...
    """"""
    OnUpdate: EventType[Action[Drawable]] = ...
    """"""
class APIDownloadRequest(ABC, APIRequest):
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
    Success: EventType[APISuccessHandler[str]] = ...
    """"""
class APIException(InvalidOperationException, ISerializable):
    """"""
    def __init__(self, message: str, innerException: Exception, statusCode: Optional[HttpStatusCode] = ...):
        """
        
        :param message: 
        :param innerException: 
        :param statusCode: 
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
    def StatusCode(self) -> Optional[HttpStatusCode]:
        """
        
        :return: 
        """
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
APIFailureHandler: Callable[[Exception], None] = ...
"""

:param e: 
"""
class APIMessagesRequest(ABC, APIRequest[List[Message]]):
    """"""
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
class APIMod(Object, IEquatable[APIMod]):
    """"""
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, mod: Mod):
        """
        
        :param mod: 
        """
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @Acronym.setter
    def Acronym(self, value: str) -> None: ...
    @property
    def Settings(self) -> Dictionary[str, object]:
        """
        
        :return: 
        """
    @Settings.setter
    def Settings(self, value: Dictionary[str, object]) -> None: ...
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: APIMod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ShouldSerializeSettings(self) -> bool:
        """
        
        :return: 
        """
    def ToMod(self, ruleset: Ruleset) -> Mod:
        """
        
        :param ruleset: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
APIProgressHandler: Callable[[int, int], None] = ...
"""

:param current: 
:param total: 
"""
class APIRequest(ABC, Generic[T], APIRequest):
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
class APIRequest(ABC, Object):
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
class APIRequestCompletionState(Enum):
    """"""
    Waiting: APIRequestCompletionState = ...
    """"""
    Completed: APIRequestCompletionState = ...
    """"""
    Failed: APIRequestCompletionState = ...
    """"""
class APIState(Enum):
    """"""
    Offline: APIState = ...
    """"""
    Failing: APIState = ...
    """"""
    RequiresSecondFactorAuth: APIState = ...
    """"""
    Connecting: APIState = ...
    """"""
    Online: APIState = ...
    """"""
APISuccessHandler: Callable[[], None] = ...
""""""
APISuccessHandler: Callable[[T], None] = ...
"""

:param content: 
"""
class ArchiveDownloadRequest(ABC, Generic[TModel], APIDownloadRequest):
    """"""
    Model: Final[TModel] = ...
    """
    
    :return: 
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
class DummyAPIAccess(Component, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache, IAPIProvider):
    """"""
    DUMMY_USER_ID: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    HandleRequest: Final[Func[APIRequest, bool]] = ...
    """
    
    :return: 
    """
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    def __init__(self):
        """"""
    @property
    def APIVersion(self) -> int:
        """
        
        :return: 
        """
    @property
    def AcceptsFocus(self) -> bool:
        """"""
    @property
    def AccessToken(self) -> str:
        """
        
        :return: 
        """
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
    def Endpoints(self) -> EndpointConfiguration:
        """
        
        :return: 
        """
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
    def IsDragged(self) -> bool:
        """"""
    @property
    def IsHovered(self) -> bool:
        """"""
    @property
    def IsLoaded(self) -> bool:
        """"""
    @property
    def IsLoggedIn(self) -> bool:
        """
        
        :return: 
        """
    @property
    def IsPresent(self) -> bool:
        """"""
    @property
    def IsProxy(self) -> bool:
        """"""
    @property
    def Language(self) -> Language:
        """
        
        :return: 
        """
    @property
    def LastLoginError(self) -> Exception:
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
    def LocalUser(self) -> Bindable[APIUser]:
        """
        
        :return: 
        """
    @property
    def LocalUserState(self) -> DummyAPIAccess.DummyLocalUserState:
        """
        
        :return: 
        """
    @property
    def Margin(self) -> MarginPadding:
        """"""
    @Margin.setter
    def Margin(self, value: MarginPadding) -> None: ...
    @property
    def NotificationsClient(self) -> DummyNotificationsClient:
        """
        
        :return: 
        """
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
    def PropagateNonPositionalInputSubTree(self) -> bool:
        """"""
    @property
    def PropagatePositionalInputSubTree(self) -> bool:
        """"""
    @property
    def ProvidedUsername(self) -> str:
        """
        
        :return: 
        """
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
    def SessionIdentifier(self) -> Guid:
        """
        
        :return: 
        """
    @property
    def SessionVerificationMethod(self) -> Optional[SessionVerificationMethod]:
        """
        
        :return: 
        """
    @SessionVerificationMethod.setter
    def SessionVerificationMethod(self, value: Optional[SessionVerificationMethod]) -> None: ...
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
    def State(self) -> IBindable[APIState]:
        """
        
        :return: 
        """
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
    def AddTransform(self, transform: Transform, customTransformID: Optional[int] = ...) -> None:
        """"""
    def ApplyTransformsAt(self, time: float, propagateChildren: bool = ...) -> None:
        """"""
    def AuthenticateSecondFactor(self, code: str) -> None:
        """
        
        :param code: 
        """
    def BeginAbsoluteSequence(self, newTransformStartTime: float, recursive: bool = ...) -> IDisposable:
        """"""
    def BeginDelayedSequence(self, delay: float, recursive: bool = ...) -> IDisposable:
        """"""
    def ClearTransforms(self, propagateChildren: bool = ..., targetMember: str = ...) -> None:
        """"""
    def ClearTransformsAfter(self, time: float, propagateChildren: bool = ..., targetMember: str = ...) -> None:
        """"""
    def ComputeMaskingBounds(self) -> RectangleF:
        """"""
    def Contains(self, screenSpacePos: Vector2) -> bool:
        """"""
    def CreateAccount(self, email: str, username: str, password: str) -> RegistrationRequest.RegistrationRequestErrors:
        """
        
        :param email: 
        :param username: 
        :param password: 
        :return: 
        """
    def CreateProxy(self) -> Drawable:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Expire(self, calculateLifetimeStart: bool = ...) -> None:
        """"""
    def FailNextLogin(self) -> None:
        """"""
    def FinishTransforms(self, propagateChildren: bool = ..., targetMember: str = ...) -> None:
        """"""
    def GetChatClient(self) -> IChatClient:
        """
        
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetHubConnector(self, clientName: str, endpoint: str) -> IHubClientConnector:
        """
        
        :param clientName: 
        :param endpoint: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def Hide(self) -> None:
        """"""
    def Invalidate(self, invalidation: Invalidation = ..., source: InvalidationSource = ...) -> bool:
        """"""
    def Login(self, username: str, password: str) -> None:
        """
        
        :param username: 
        :param password: 
        """
    def Logout(self) -> None:
        """"""
    def PauseOnConnectingNextLogin(self) -> None:
        """"""
    def Perform(self, request: APIRequest) -> None:
        """
        
        :param request: 
        """
    def PerformAsync(self, request: APIRequest) -> Task:
        """
        
        :param request: 
        :return: 
        """
    def Queue(self, request: APIRequest) -> None:
        """
        
        :param request: 
        """
    def ReceivePositionalInputAt(self, screenSpacePos: Vector2) -> bool:
        """"""
    def RegisterForDependencyActivation(self, registry: IDependencyActivatorRegistry) -> None:
        """"""
    def RemoveTransform(self, toRemove: Transform) -> None:
        """"""
    def SetState(self, newState: APIState) -> None:
        """
        
        :param newState: 
        """
    def Show(self) -> None:
        """"""
    def SkipSecondFactor(self) -> None:
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
    def UpdateLocalBlocks(self) -> None:
        """"""
    def UpdateLocalFriends(self) -> None:
        """"""
    def UpdateSubTree(self) -> bool:
        """"""
    def UpdateSubTreeMasking(self) -> bool:
        """"""
    def WithEffect(self, effect: IEffect[T], initializationAction: Action[T] = ...) -> T:
        """"""
    def __contains__(self, screenSpacePos: Vector2) -> bool:
        """"""
    OnLoadComplete: EventType[Action[Drawable]] = ...
    """"""
    OnUpdate: EventType[Action[Drawable]] = ...
    """"""
    class DummyLocalUserState(Object, ILocalUserState):
        """"""
        def __init__(self):
            """"""
        @property
        def Blocks(self) -> BindableList[APIRelation]:
            """
            
            :return: 
            """
        @property
        def FavouriteBeatmapSets(self) -> BindableList[int]:
            """
            
            :return: 
            """
        @property
        def Friends(self) -> BindableList[APIRelation]:
            """
            
            :return: 
            """
        @property
        def User(self) -> Bindable[APIUser]:
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
        def UpdateBlocks(self) -> None:
            """"""
        def UpdateFavouriteBeatmapSets(self) -> None:
            """"""
        def UpdateFriends(self) -> None:
            """"""
class GuestUser(APIUser, IEquatable[APIUser], IEquatable[IUser], IHasOnlineID[Int32], IUser):
    """"""
    Achievements: Final[Array[APIUserAchievement]] = ...
    """
    
    :return: 
    """
    Active: Final[bool] = ...
    """
    
    :return: 
    """
    AvatarUrl: Final[str] = ...
    """
    
    :return: 
    """
    Badges: Final[Array[Badge]] = ...
    """
    
    :return: 
    """
    BeatmapPlayCountsCount: Final[int] = ...
    """
    
    :return: 
    """
    Colour: Final[str] = ...
    """
    
    :return: 
    """
    CommentsCount: Final[int] = ...
    """
    
    :return: 
    """
    Cover: Final[APIUser.UserCover] = ...
    """
    
    :return: 
    """
    DailyChallengeStatistics: Final[APIUserDailyChallengeStatistics] = ...
    """
    
    :return: 
    """
    Discord: Final[str] = ...
    """
    
    :return: 
    """
    FavouriteBeatmapsetCount: Final[int] = ...
    """
    
    :return: 
    """
    FollowerCount: Final[int] = ...
    """
    
    :return: 
    """
    GraveyardBeatmapsetCount: Final[int] = ...
    """
    
    :return: 
    """
    Groups: Final[Array[APIUserGroup]] = ...
    """
    
    :return: 
    """
    GuestBeatmapsetCount: Final[int] = ...
    """
    
    :return: 
    """
    Interests: Final[str] = ...
    """
    
    :return: 
    """
    IsAdmin: Final[bool] = ...
    """
    
    :return: 
    """
    IsBNG: Final[bool] = ...
    """
    
    :return: 
    """
    IsGMT: Final[bool] = ...
    """
    
    :return: 
    """
    IsQAT: Final[bool] = ...
    """
    
    :return: 
    """
    IsSupporter: Final[bool] = ...
    """
    
    :return: 
    """
    JoinDate: Final[DateTimeOffset] = ...
    """
    
    :return: 
    """
    Kudosu: Final[APIUser.KudosuCount] = ...
    """
    
    :return: 
    """
    LastVisit: Final[Optional[DateTimeOffset]] = ...
    """
    
    :return: 
    """
    Location: Final[str] = ...
    """
    
    :return: 
    """
    LovedBeatmapsetCount: Final[int] = ...
    """
    
    :return: 
    """
    MappingFollowerCount: Final[int] = ...
    """
    
    :return: 
    """
    MatchmakingStatistics: Final[Array[APIUserMatchmakingStatistics]] = ...
    """
    
    :return: 
    """
    MonthlyPlayCounts: Final[Array[APIUserHistoryCount]] = ...
    """
    
    :return: 
    """
    NominatedBeatmapsetCount: Final[int] = ...
    """
    
    :return: 
    """
    Occupation: Final[str] = ...
    """
    
    :return: 
    """
    PMFriendsOnly: Final[bool] = ...
    """
    
    :return: 
    """
    PendingBeatmapsetCount: Final[int] = ...
    """
    
    :return: 
    """
    PlayMode: Final[str] = ...
    """
    
    :return: 
    """
    PlayStyles: Final[Array[APIPlayStyle]] = ...
    """
    
    :return: 
    """
    PostCount: Final[int] = ...
    """
    
    :return: 
    """
    PreviousUsernames: Final[Array[str]] = ...
    """
    
    :return: 
    """
    ProfileHue: Final[Optional[int]] = ...
    """
    
    :return: 
    """
    ProfileOrder: Final[Array[str]] = ...
    """
    
    :return: 
    """
    RankHighest: Final[APIUser.UserRankHighest] = ...
    """
    
    :return: 
    """
    RankedBeatmapsetCount: Final[int] = ...
    """
    
    :return: 
    """
    ReplaysWatchedCounts: Final[Array[APIUserHistoryCount]] = ...
    """
    
    :return: 
    """
    ScoresBestCount: Final[int] = ...
    """
    
    :return: 
    """
    ScoresFirstCount: Final[int] = ...
    """
    
    :return: 
    """
    ScoresPinnedCount: Final[int] = ...
    """
    
    :return: 
    """
    ScoresRecentCount: Final[int] = ...
    """
    
    :return: 
    """
    SupportLevel: Final[int] = ...
    """
    
    :return: 
    """
    Title: Final[str] = ...
    """
    
    :return: 
    """
    TournamentBanners: Final[Array[TournamentBanner]] = ...
    """
    
    :return: 
    """
    Twitter: Final[str] = ...
    """
    
    :return: 
    """
    WasRecentlyOnline: Final[bool] = ...
    """
    
    :return: 
    """
    Website: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def CountryCode(self) -> CountryCode:
        """
        
        :return: 
        """
    @CountryCode.setter
    def CountryCode(self, value: CountryCode) -> None: ...
    @property
    def CoverUrl(self) -> str:
        """
        
        :return: 
        """
    @CoverUrl.setter
    def CoverUrl(self, value: str) -> None: ...
    @property
    def Id(self) -> int:
        """
        
        :return: 
        """
    @Id.setter
    def Id(self, value: int) -> None: ...
    @property
    def IsBot(self) -> bool:
        """
        
        :return: 
        """
    @IsBot.setter
    def IsBot(self, value: bool) -> None: ...
    @property
    def OnlineID(self) -> int:
        """
        
        :return: 
        """
    @property
    def Rank(self) -> APIUser.GlobalRank:
        """
        
        :return: 
        """
    @Rank.setter
    def Rank(self, value: APIUser.GlobalRank) -> None: ...
    @property
    def RulesetsStatistics(self) -> Dictionary[str, UserStatistics]:
        """
        
        :return: 
        """
    @RulesetsStatistics.setter
    def RulesetsStatistics(self, value: Dictionary[str, UserStatistics]) -> None: ...
    @property
    def Statistics(self) -> UserStatistics:
        """
        
        :return: 
        """
    @Statistics.setter
    def Statistics(self, value: UserStatistics) -> None: ...
    @property
    def Team(self) -> APITeam:
        """
        
        :return: 
        """
    @Team.setter
    def Team(self, value: APITeam) -> None: ...
    @property
    def Username(self) -> str:
        """
        
        :return: 
        """
    @Username.setter
    def Username(self, value: str) -> None: ...
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: APIUser) -> bool:
        """"""
    @overload
    def Equals(self, other: IUser) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class IAPIProvider:
    """"""
    @property
    def APIVersion(self) -> int:
        """
        
        :return: 
        """
    @property
    def AccessToken(self) -> str:
        """
        
        :return: 
        """
    @property
    def Endpoints(self) -> EndpointConfiguration:
        """
        
        :return: 
        """
    @property
    def IsLoggedIn(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Language(self) -> Language:
        """
        
        :return: 
        """
    @property
    def LastLoginError(self) -> Exception:
        """
        
        :return: 
        """
    @property
    def LocalUser(self) -> IBindable[APIUser]:
        """
        
        :return: 
        """
    @property
    def LocalUserState(self) -> ILocalUserState:
        """
        
        :return: 
        """
    @property
    def NotificationsClient(self) -> INotificationsClient:
        """
        
        :return: 
        """
    @property
    def ProvidedUsername(self) -> str:
        """
        
        :return: 
        """
    @property
    def SessionIdentifier(self) -> Guid:
        """
        
        :return: 
        """
    @property
    def SessionVerificationMethod(self) -> Optional[SessionVerificationMethod]:
        """
        
        :return: 
        """
    @property
    def State(self) -> IBindable[APIState]:
        """
        
        :return: 
        """
    def AuthenticateSecondFactor(self, code: str) -> None:
        """
        
        :param code: 
        """
    def CreateAccount(self, email: str, username: str, password: str) -> RegistrationRequest.RegistrationRequestErrors:
        """
        
        :param email: 
        :param username: 
        :param password: 
        :return: 
        """
    def GetChatClient(self) -> IChatClient:
        """
        
        :return: 
        """
    def GetHubConnector(self, clientName: str, endpoint: str) -> IHubClientConnector:
        """
        
        :param clientName: 
        :param endpoint: 
        :return: 
        """
    def Login(self, username: str, password: str) -> None:
        """
        
        :param username: 
        :param password: 
        """
    def Logout(self) -> None:
        """"""
    def Perform(self, request: APIRequest) -> None:
        """
        
        :param request: 
        """
    def PerformAsync(self, request: APIRequest) -> Task:
        """
        
        :param request: 
        :return: 
        """
    def Queue(self, request: APIRequest) -> None:
        """
        
        :param request: 
        """
class ILocalUserState:
    """"""
    @property
    def Blocks(self) -> IBindableList[APIRelation]:
        """
        
        :return: 
        """
    @property
    def FavouriteBeatmapSets(self) -> IBindableList[int]:
        """
        
        :return: 
        """
    @property
    def Friends(self) -> IBindableList[APIRelation]:
        """
        
        :return: 
        """
    @property
    def User(self) -> IBindable[APIUser]:
        """
        
        :return: 
        """
    def UpdateBlocks(self) -> None:
        """"""
    def UpdateFavouriteBeatmapSets(self) -> None:
        """"""
    def UpdateFriends(self) -> None:
        """"""
class LocalUserState(Component, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache, ILocalUserState):
    """"""
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    def __init__(self, api: IAPIProvider, config: OsuConfigManager):
        """
        
        :param api: 
        :param config: 
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
    def Blocks(self) -> IBindableList[APIRelation]:
        """
        
        :return: 
        """
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
    def FavouriteBeatmapSets(self) -> IBindableList[int]:
        """
        
        :return: 
        """
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
    def Friends(self) -> IBindableList[APIRelation]:
        """
        
        :return: 
        """
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
    def IsDragged(self) -> bool:
        """"""
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
    def User(self) -> IBindable[APIUser]:
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
    def AddTransform(self, transform: Transform, customTransformID: Optional[int] = ...) -> None:
        """"""
    def ApplyTransformsAt(self, time: float, propagateChildren: bool = ...) -> None:
        """"""
    def BeginAbsoluteSequence(self, newTransformStartTime: float, recursive: bool = ...) -> IDisposable:
        """"""
    def BeginDelayedSequence(self, delay: float, recursive: bool = ...) -> IDisposable:
        """"""
    def ClearLocalUser(self) -> None:
        """"""
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
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Expire(self, calculateLifetimeStart: bool = ...) -> None:
        """"""
    def FinishTransforms(self, propagateChildren: bool = ..., targetMember: str = ...) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Hide(self) -> None:
        """"""
    def Invalidate(self, invalidation: Invalidation = ..., source: InvalidationSource = ...) -> bool:
        """"""
    def ReceivePositionalInputAt(self, screenSpacePos: Vector2) -> bool:
        """"""
    def RegisterForDependencyActivation(self, registry: IDependencyActivatorRegistry) -> None:
        """"""
    def RemoveTransform(self, toRemove: Transform) -> None:
        """"""
    def SetLocalUser(self, me: APIMe) -> None:
        """
        
        :param me: 
        """
    def SetPlaceholderLocalUser(self, username: str) -> None:
        """
        
        :param username: 
        """
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
    def UpdateBlocks(self) -> None:
        """"""
    def UpdateFavouriteBeatmapSets(self) -> None:
        """"""
    def UpdateFriends(self) -> None:
        """"""
    def UpdateSubTree(self) -> bool:
        """"""
    def UpdateSubTreeMasking(self) -> bool:
        """"""
    def WithEffect(self, effect: IEffect[T], initializationAction: Action[T] = ...) -> T:
        """"""
    def __contains__(self, screenSpacePos: Vector2) -> bool:
        """"""
    OnLoadComplete: EventType[Action[Drawable]] = ...
    """"""
    OnUpdate: EventType[Action[Drawable]] = ...
    """"""
class ModSettingsDictionaryFormatter(Object, IMessagePackFormatter, IMessagePackFormatter[Dictionary, Object]):
    """"""
    def __init__(self):
        """"""
    def Deserialize(self, reader: MessagePackReader, options: MessagePackSerializerOptions) -> Dictionary[str, object]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Serialize(self, writer: MessagePackWriter, value: Dictionary[str, object], options: MessagePackSerializerOptions) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class OAuth(Object):
    """"""
    Token: Final[Bindable[OAuthToken]] = ...
    """
    
    :return: 
    """
    @property
    def TokenString(self) -> str:
        """
        
        :return: 
        """
    @TokenString.setter
    def TokenString(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class OAuthToken(Object):
    """"""
    AccessToken: Final[str] = ...
    """
    
    :return: 
    """
    AccessTokenExpiry: Final[int] = ...
    """
    
    :return: 
    """
    RefreshToken: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def ExpiresIn(self) -> int:
        """
        
        :return: 
        """
    @ExpiresIn.setter
    def ExpiresIn(self, value: int) -> None: ...
    @property
    def IsValid(self) -> bool:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Parse(cls, value: str) -> OAuthToken:
        """
        
        :param value: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class OsuJsonWebRequest(Generic[T], JsonWebRequest[T], IDisposable):
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
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, uri: str):
        """
        
        :param uri: 
        """
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
    def ResponseObject(self) -> T:
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
class OsuWebRequest(WebRequest, IDisposable):
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
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, uri: str):
        """
        
        :param uri: 
        """
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
class RegistrationRequest(OsuWebRequest, IDisposable):
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
    class RegistrationRequestErrors(Object):
        """"""
        Message: Final[str] = ...
        """"""
        Redirect: Final[str] = ...
        """"""
        User: Final[RegistrationRequest.RegistrationRequestErrors.UserErrors] = ...
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
        class UserErrors(Object):
            """"""
            Email: Final[Array[str]] = ...
            """"""
            Password: Final[Array[str]] = ...
            """"""
            Username: Final[Array[str]] = ...
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