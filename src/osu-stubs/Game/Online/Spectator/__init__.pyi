from System import Action
from System import Array
from System.Collections.Generic import Dictionary
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IList
from System.Collections.Generic import IReadOnlyList
from System import DateTimeOffset
from System import Enum
from System import Func
from System import IDisposable
from System import IEquatable
from System import Int32
from System import Object
from System.Threading.Tasks import Task
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Framework.Allocation import IDependencyActivatorRegistry
from osu.Framework.Allocation import IDependencyInjectionCandidate
from osu.Framework.Allocation import ISourceGeneratedDependencyActivator
from osu.Framework.Allocation import ISourceGeneratedLongRunningLoadCache
from osu.Framework.Bindables import Bindable
from osu.Framework.Bindables import BindableDouble
from osu.Framework.Bindables import BindableInt
from osu.Framework.Bindables import BindableLong
from osu.Framework.Bindables import IBindable
from osu.Framework.Bindables import IBindableDictionary
from osu.Framework.Bindables import IBindableList
from osu.Framework.Graphics import Anchor
from osu.Framework.Graphics import Axes
from osu.Framework.Graphics import BlendingParameters
from osu.Framework.Graphics.Colour import ColourInfo
from osu.Framework.Graphics import Component
from osu.Framework.Graphics.Containers import CompositeDrawable
from osu.Framework.Graphics import DrawColourInfo
from osu.Framework.Graphics import DrawInfo
from osu.Framework.Graphics import Drawable
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
from osu.Framework.Input.Events import UIEvent
from osu.Framework.Input import ISourceGeneratedHandleInputCache
from osu.Framework.Layout import InvalidationSource
from osu.Framework.Timing import FrameTimeInfo
from osu.Framework.Timing import IClock
from osu.Framework.Timing import IFrameBasedClock
from osu.Game.Database import IHasOnlineID
from osu.Game.Online.API import APIMod
from osu.Game.Online import EndpointConfiguration
from osu.Game.Online import IStatefulUserHubClient
from osu.Game.Replays.Legacy import LegacyReplayFrame
from osu.Game.Rulesets.Mods import Mod
from osu.Game.Rulesets.Replays import ReplayFrame
from osu.Game.Rulesets.Scoring import HitResult
from osu.Game.Rulesets.Scoring import ScoreProcessor
from osu.Game.Rulesets.Scoring import ScoreProcessorStatistics
from osu.Game.Rulesets.Scoring import ScoringMode
from osu.Game.Scoring import Score
from osu.Game.Scoring import ScoreInfo
from osu.Game.Screens.Play import GameplayState
from osu.Game.Users import CountryCode
from osu.Game.Users import IUser
from osuTK import Vector2
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Optional
from typing import TypeVar
from typing import overload
T = TypeVar("T")
class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...
class FrameDataBundle(Object):
    """"""
    @overload
    def __init__(self, header: FrameHeader, frames: IList[LegacyReplayFrame]):
        """
        
        :param header: 
        :param frames: 
        """
    @overload
    def __init__(self, score: ScoreInfo, scoreProcessor: ScoreProcessor, frames: IList[LegacyReplayFrame]):
        """
        
        :param score: 
        :param scoreProcessor: 
        :param frames: 
        """
    @property
    def Frames(self) -> IList[LegacyReplayFrame]:
        """
        
        :return: 
        """
    @Frames.setter
    def Frames(self, value: IList[LegacyReplayFrame]) -> None: ...
    @property
    def Header(self) -> FrameHeader:
        """
        
        :return: 
        """
    @Header.setter
    def Header(self, value: FrameHeader) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class FrameHeader(Object):
    """"""
    @overload
    def __init__(self, score: ScoreInfo, statistics: ScoreProcessorStatistics):
        """
        
        :param score: 
        :param statistics: 
        """
    @overload
    def __init__(self, totalScore: int, accuracy: float, combo: int, maxCombo: int, statistics: Dictionary[HitResult, int], scoreProcessorStatistics: ScoreProcessorStatistics, receivedTime: DateTimeOffset, mods: Array[APIMod], totalScoreWithoutMods: Optional[int], pauses: Array[int]):
        """
        
        :param totalScore: 
        :param accuracy: 
        :param combo: 
        :param maxCombo: 
        :param statistics: 
        :param scoreProcessorStatistics: 
        :param receivedTime: 
        :param mods: 
        :param totalScoreWithoutMods: 
        :param pauses: 
        """
    @property
    def Accuracy(self) -> float:
        """
        
        :return: 
        """
    @Accuracy.setter
    def Accuracy(self, value: float) -> None: ...
    @property
    def Combo(self) -> int:
        """
        
        :return: 
        """
    @Combo.setter
    def Combo(self, value: int) -> None: ...
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
    def Pauses(self) -> Array[int]:
        """
        
        :return: 
        """
    @Pauses.setter
    def Pauses(self, value: Array[int]) -> None: ...
    @property
    def ReceivedTime(self) -> DateTimeOffset:
        """
        
        :return: 
        """
    @ReceivedTime.setter
    def ReceivedTime(self, value: DateTimeOffset) -> None: ...
    @property
    def ScoreProcessorStatistics(self) -> ScoreProcessorStatistics:
        """
        
        :return: 
        """
    @ScoreProcessorStatistics.setter
    def ScoreProcessorStatistics(self, value: ScoreProcessorStatistics) -> None: ...
    @property
    def Statistics(self) -> Dictionary[HitResult, int]:
        """
        
        :return: 
        """
    @Statistics.setter
    def Statistics(self, value: Dictionary[HitResult, int]) -> None: ...
    @property
    def TotalScore(self) -> int:
        """
        
        :return: 
        """
    @TotalScore.setter
    def TotalScore(self, value: int) -> None: ...
    @property
    def TotalScoreWithoutMods(self) -> Optional[int]:
        """
        
        :return: 
        """
    @TotalScoreWithoutMods.setter
    def TotalScoreWithoutMods(self, value: Optional[int]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class ISpectatorClient(IStatefulUserHubClient):
    """"""
    def DisconnectRequested(self) -> Task:
        """
        
        :return: 
        """
    def ServerShuttingDown(self) -> Task:
        """
        
        :return: 
        """
    def UserBeganPlaying(self, userId: int, state: SpectatorState) -> Task:
        """
        
        :param userId: 
        :param state: 
        :return: 
        """
    def UserEndedWatching(self, userId: int) -> Task:
        """
        
        :param userId: 
        :return: 
        """
    def UserFinishedPlaying(self, userId: int, state: SpectatorState) -> Task:
        """
        
        :param userId: 
        :param state: 
        :return: 
        """
    def UserScoreProcessed(self, userId: int, scoreId: int) -> Task:
        """
        
        :param userId: 
        :param scoreId: 
        :return: 
        """
    def UserSentFrames(self, userId: int, data: FrameDataBundle) -> Task:
        """
        
        :param userId: 
        :param data: 
        :return: 
        """
    def UserStartedWatching(self, user: Array[SpectatorUser]) -> Task:
        """
        
        :param user: 
        :return: 
        """
class ISpectatorServer:
    """"""
    def BeginPlaySession(self, scoreToken: Optional[int], state: SpectatorState) -> Task:
        """
        
        :param scoreToken: 
        :param state: 
        :return: 
        """
    def EndPlaySession(self, state: SpectatorState) -> Task:
        """
        
        :param state: 
        :return: 
        """
    def EndWatchingUser(self, userId: int) -> Task:
        """
        
        :param userId: 
        :return: 
        """
    def SendFrameData(self, data: FrameDataBundle) -> Task:
        """
        
        :param data: 
        :return: 
        """
    def StartWatchingUser(self, userId: int) -> Task:
        """
        
        :param userId: 
        :return: 
        """
class OnlineSpectatorClient(SpectatorClient, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache, ISpectatorClient, IStatefulUserHubClient):
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
    def WatchedUserStates(self) -> IBindableDictionary[int, SpectatorState]:
        """
        
        :return: 
        """
    @property
    def WatchingUsers(self) -> IBindableList[SpectatorUser]:
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
    def BeginPlaying(self, scoreToken: Optional[int], state: GameplayState, score: Score) -> None:
        """
        
        :param scoreToken: 
        :param state: 
        :param score: 
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
    def DisconnectRequested(self) -> Task:
        """
        
        :return: 
        """
    def Dispose(self) -> None:
        """"""
    def EndPlaying(self, state: GameplayState) -> None:
        """
        
        :param state: 
        """
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
    def HandleFrame(self, frame: ReplayFrame) -> None:
        """
        
        :param frame: 
        """
    def Hide(self) -> None:
        """"""
    def Invalidate(self, invalidation: Invalidation = ..., source: InvalidationSource = ...) -> bool:
        """"""
    def ReceivePositionalInputAt(self, screenSpacePos: Vector2) -> bool:
        """"""
    def Reconnect(self) -> Task:
        """
        
        :return: 
        """
    def RegisterForDependencyActivation(self, registry: IDependencyActivatorRegistry) -> None:
        """"""
    def RemoveTransform(self, toRemove: Transform) -> None:
        """"""
    def ServerShuttingDown(self) -> Task:
        """
        
        :return: 
        """
    def Show(self) -> None:
        """"""
    def StopWatchingUser(self, userId: int) -> None:
        """
        
        :param userId: 
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
    def UserBeganPlaying(self, userId: int, state: SpectatorState) -> Task:
        """
        
        :param userId: 
        :param state: 
        :return: 
        """
    def UserEndedWatching(self, userId: int) -> Task:
        """
        
        :param userId: 
        :return: 
        """
    def UserFinishedPlaying(self, userId: int, state: SpectatorState) -> Task:
        """
        
        :param userId: 
        :param state: 
        :return: 
        """
    def UserScoreProcessed(self, userId: int, scoreId: int) -> Task:
        """
        
        :param userId: 
        :param scoreId: 
        :return: 
        """
    def UserSentFrames(self, userId: int, data: FrameDataBundle) -> Task:
        """
        
        :param userId: 
        :param data: 
        :return: 
        """
    def UserStartedWatching(self, user: Array[SpectatorUser]) -> Task:
        """
        
        :param user: 
        :return: 
        """
    def WatchUser(self, userId: int) -> None:
        """
        
        :param userId: 
        """
    def WithEffect(self, effect: IEffect[T], initializationAction: Action[T] = ...) -> T:
        """"""
    def __contains__(self, screenSpacePos: Vector2) -> bool:
        """"""
    Disconnecting: EventType[Action] = ...
    """"""
    OnLoadComplete: EventType[Action[Drawable]] = ...
    """"""
    OnNewFrames: EventType[Action[int, FrameDataBundle]] = ...
    """"""
    OnUpdate: EventType[Action[Drawable]] = ...
    """"""
    OnUserBeganPlaying: EventType[Action[int, SpectatorState]] = ...
    """"""
    OnUserFinishedPlaying: EventType[Action[int, SpectatorState]] = ...
    """"""
    OnUserScoreProcessed: EventType[Action[int, int]] = ...
    """"""
class SpectatedUserState(Enum):
    """"""
    Idle: SpectatedUserState = ...
    """"""
    Playing: SpectatedUserState = ...
    """"""
    Paused: SpectatedUserState = ...
    """"""
    Passed: SpectatedUserState = ...
    """"""
    Failed: SpectatedUserState = ...
    """"""
    Quit: SpectatedUserState = ...
    """"""
class SpectatorClient(ABC, Component, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache, ISpectatorClient, IStatefulUserHubClient):
    """"""
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    TIME_BETWEEN_SENDS: Final[ClassVar[float]] = ...
    """
    
    :return: 
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
    def WatchedUserStates(self) -> IBindableDictionary[int, SpectatorState]:
        """
        
        :return: 
        """
    @property
    def WatchingUsers(self) -> IBindableList[SpectatorUser]:
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
    def BeginPlaying(self, scoreToken: Optional[int], state: GameplayState, score: Score) -> None:
        """
        
        :param scoreToken: 
        :param state: 
        :param score: 
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
    def DisconnectRequested(self) -> Task:
        """
        
        :return: 
        """
    def Dispose(self) -> None:
        """"""
    def EndPlaying(self, state: GameplayState) -> None:
        """
        
        :param state: 
        """
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
    def HandleFrame(self, frame: ReplayFrame) -> None:
        """
        
        :param frame: 
        """
    def Hide(self) -> None:
        """"""
    def Invalidate(self, invalidation: Invalidation = ..., source: InvalidationSource = ...) -> bool:
        """"""
    def ReceivePositionalInputAt(self, screenSpacePos: Vector2) -> bool:
        """"""
    def Reconnect(self) -> Task:
        """
        
        :return: 
        """
    def RegisterForDependencyActivation(self, registry: IDependencyActivatorRegistry) -> None:
        """"""
    def RemoveTransform(self, toRemove: Transform) -> None:
        """"""
    def ServerShuttingDown(self) -> Task:
        """
        
        :return: 
        """
    def Show(self) -> None:
        """"""
    def StopWatchingUser(self, userId: int) -> None:
        """
        
        :param userId: 
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
    def UserBeganPlaying(self, userId: int, state: SpectatorState) -> Task:
        """
        
        :param userId: 
        :param state: 
        :return: 
        """
    def UserEndedWatching(self, userId: int) -> Task:
        """
        
        :param userId: 
        :return: 
        """
    def UserFinishedPlaying(self, userId: int, state: SpectatorState) -> Task:
        """
        
        :param userId: 
        :param state: 
        :return: 
        """
    def UserScoreProcessed(self, userId: int, scoreId: int) -> Task:
        """
        
        :param userId: 
        :param scoreId: 
        :return: 
        """
    def UserSentFrames(self, userId: int, data: FrameDataBundle) -> Task:
        """
        
        :param userId: 
        :param data: 
        :return: 
        """
    def UserStartedWatching(self, user: Array[SpectatorUser]) -> Task:
        """
        
        :param user: 
        :return: 
        """
    def WatchUser(self, userId: int) -> None:
        """
        
        :param userId: 
        """
    def WithEffect(self, effect: IEffect[T], initializationAction: Action[T] = ...) -> T:
        """"""
    def __contains__(self, screenSpacePos: Vector2) -> bool:
        """"""
    Disconnecting: EventType[Action] = ...
    """"""
    OnLoadComplete: EventType[Action[Drawable]] = ...
    """"""
    OnNewFrames: EventType[Action[int, FrameDataBundle]] = ...
    """"""
    OnUpdate: EventType[Action[Drawable]] = ...
    """"""
    OnUserBeganPlaying: EventType[Action[int, SpectatorState]] = ...
    """"""
    OnUserFinishedPlaying: EventType[Action[int, SpectatorState]] = ...
    """"""
    OnUserScoreProcessed: EventType[Action[int, int]] = ...
    """"""
class SpectatorScoreProcessor(Component, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
    """"""
    Accuracy: Final[BindableDouble] = ...
    """
    
    :return: 
    """
    Combo: Final[BindableInt] = ...
    """
    
    :return: 
    """
    HighestCombo: Final[BindableInt] = ...
    """
    
    :return: 
    """
    Mode: Final[Bindable[ScoringMode]] = ...
    """
    
    :return: 
    """
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    TotalScore: Final[BindableLong] = ...
    """
    
    :return: 
    """
    def __init__(self, userId: int):
        """
        
        :param userId: 
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
    def GetDisplayScore(self) -> Func[ScoringMode, int]:
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
    def Mods(self) -> IReadOnlyList[Mod]:
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
    def ReferenceClock(self) -> IClock:
        """
        
        :return: 
        """
    @ReferenceClock.setter
    def ReferenceClock(self, value: IClock) -> None: ...
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
    def UpdateScore(self) -> None:
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
class SpectatorState(Object, IEquatable[SpectatorState]):
    """"""
    def __init__(self):
        """"""
    @property
    def BeatmapID(self) -> Optional[int]:
        """
        
        :return: 
        """
    @BeatmapID.setter
    def BeatmapID(self, value: Optional[int]) -> None: ...
    @property
    def MaximumStatistics(self) -> Dictionary[HitResult, int]:
        """
        
        :return: 
        """
    @MaximumStatistics.setter
    def MaximumStatistics(self, value: Dictionary[HitResult, int]) -> None: ...
    @property
    def Mods(self) -> IEnumerable[APIMod]:
        """
        
        :return: 
        """
    @Mods.setter
    def Mods(self, value: IEnumerable[APIMod]) -> None: ...
    @property
    def RulesetID(self) -> Optional[int]:
        """
        
        :return: 
        """
    @RulesetID.setter
    def RulesetID(self, value: Optional[int]) -> None: ...
    @property
    def State(self) -> SpectatedUserState:
        """
        
        :return: 
        """
    @State.setter
    def State(self, value: SpectatedUserState) -> None: ...
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: SpectatorState) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class SpectatorUser(Object, IEquatable[SpectatorUser], IEquatable[IUser], IHasOnlineID[Int32], IUser):
    """"""
    def __init__(self):
        """"""
    @property
    def CountryCode(self) -> CountryCode:
        """
        
        :return: 
        """
    @property
    def IsBot(self) -> bool:
        """
        
        :return: 
        """
    @property
    def OnlineID(self) -> int:
        """
        
        :return: 
        """
    @OnlineID.setter
    def OnlineID(self, value: int) -> None: ...
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
    def Equals(self, other: SpectatorUser) -> bool:
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