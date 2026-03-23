from System import Action
from System import Array
from System.Collections.Generic import Dictionary
from System.Collections.Generic import ICollection
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IReadOnlyCollection
from System.Collections.Generic import IReadOnlyList
from System.Collections import IEnumerable
from System import Func
from System import IDisposable
from System import Predicate
from System.Threading.Tasks import Task
from System import Type
from System import Version
from __future__ import annotations
from osu.Framework.Allocation import IDependencyActivatorRegistry
from osu.Framework.Allocation import IDependencyInjectionCandidate
from osu.Framework.Allocation import IReadOnlyDependencyContainer
from osu.Framework.Allocation import ISourceGeneratedDependencyActivator
from osu.Framework.Allocation import ISourceGeneratedLongRunningLoadCache
from osu.Framework.Audio import AudioManager
from osu.Framework.Audio import IHasAmplitudes
from osu.Framework.Audio.Track import ChannelAmplitudes
from osu.Framework.Bindables import Bindable
from osu.Framework.Bindables import IBindable
from osu.Framework import Game
from osu.Framework.Graphics import Anchor
from osu.Framework.Graphics import Axes
from osu.Framework.Graphics import BlendingParameters
from osu.Framework.Graphics.Colour import ColourInfo
from osu.Framework.Graphics import Component
from osu.Framework.Graphics.Containers import CompositeDrawable
from osu.Framework.Graphics.Containers.Container import Enumerator
from osu.Framework.Graphics.Containers import IContainer
from osu.Framework.Graphics.Containers import IContainerCollection
from osu.Framework.Graphics.Containers import IContainerEnumerable
from osu.Framework.Graphics.Containers import OverlayContainer
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
from osu.Framework.Graphics.Shaders import ShaderManager
from osu.Framework.Graphics.Textures import TextureStore
from osu.Framework.Graphics.Transforms import ITransformable
from osu.Framework.Graphics.Transforms import Transform
from osu.Framework.IO.Stores import FontStore
from osu.Framework.IO.Stores import ResourceStore
from osu.Framework.Input.Bindings import IKeyBindingHandler
from osu.Framework.Input.Events import KeyBindingPressEvent
from osu.Framework.Input.Events import KeyBindingReleaseEvent
from osu.Framework.Input.Events import UIEvent
from osu.Framework.Input import FrameworkAction
from osu.Framework.Input.Handlers import InputHandler
from osu.Framework.Input import IHandleGlobalKeyboardInput
from osu.Framework.Input import ISourceGeneratedHandleInputCache
from osu.Framework.Input import PlatformAction
from osu.Framework.Layout import InvalidationSource
from osu.Framework.Platform import GameHost
from osu.Framework.Platform import IWindow
from osu.Framework.Platform import Storage
from osu.Framework.Screens import IScreen
from osu.Framework.Timing import FrameTimeInfo
from osu.Framework.Timing import IFrameBasedClock
from osu.Game.Beatmaps import BeatmapInfo
from osu.Game.Beatmaps.ControlPoints import ControlPointInfo
from osu.Game.Beatmaps import IBeatSyncProvider
from osu.Game.Beatmaps import IBeatmapSetInfo
from osu.Game.Database import ICanAcceptFiles
from osu.Game.Database import ImportParameters
from osu.Game.Database import ImportTask
from osu.Game.IO import StableStorage
from osu.Game.Input.Bindings import GlobalAction
from osu.Game.Localisation import Language
from osu.Game.Online.Chat import LinkDetails
from osu.Game.Online.Chat import LinkWarnMode
from osu.Game.Online import EndpointConfiguration
from osu.Game.Online import ILinkHandler
from osu.Game.Online.Rooms import Room
from osu.Game.Overlays.BeatmapListing import SearchGenre
from osu.Game.Overlays.BeatmapListing import SearchLanguage
from osu.Game.Overlays import IOverlayManager
from osu.Game.Overlays import OverlayActivation
from osu.Game.Overlays.Settings import SettingsSubsection
from osu.Game.Overlays.Toolbar import Toolbar
from osu.Game.Rulesets.Mods import Mod
from osu.Game.Scoring import IScoreInfo
from osu.Game.Screens import IPerformFromScreenRunner
from osu.Game.Screens.Play import ILocalUserPlayInfo
from osu.Game.Screens.Play import LocalUserPlayingState
from osu.Game.Screens import ScorePresentType
from osu.Game.Skinning import SkinInfo
from osu.Game.Users import IUser
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
class OsuGame(OsuGameBase, ICollection[Drawable], IEnumerable[Drawable], IReadOnlyCollection[Drawable], IReadOnlyList[Drawable], IEnumerable, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, IHasAmplitudes, IContainer, IContainerCollection[Drawable], IContainerEnumerable[Drawable], ITransformable, IDrawable, IKeyBindingHandler, IKeyBindingHandler[FrameworkAction], IKeyBindingHandler[PlatformAction], IKeyBindingHandler[GlobalAction], IHandleGlobalKeyboardInput, ISourceGeneratedHandleInputCache, IBeatSyncProvider, ICanAcceptFiles, ILinkHandler, IOverlayManager, ILocalUserPlayInfo, IPerformFromScreenRunner):
    """"""
    AvailableMods: Final[Bindable[Dictionary, IReadOnlyList[Mod]]] = ...
    """
    
    :return: 
    """
    IPC_PIPE_NAME: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Name: Final[str] = ...
    """"""
    OverlayActivationMode: Final[IBindable[OverlayActivation]] = ...
    """
    
    :return: 
    """
    ProcessCustomClock: Final[bool] = ...
    """"""
    SCREEN_EDGE_MARGIN: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    SHEAR: Final[ClassVar[Vector2]] = ...
    """
    
    :return: 
    """
    def __init__(self, args: Array[str] = ...):
        """
        
        :param args: 
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
    def AssemblyVersion(self) -> Version:
        """
        
        :return: 
        """
    @property
    def Audio(self) -> AudioManager:
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
    def ControlPoints(self) -> ControlPointInfo:
        """
        
        :return: 
        """
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
    def CurrentAmplitudes(self) -> ChannelAmplitudes:
        """"""
    @property
    def CurrentLanguage(self) -> Bindable[Language]:
        """
        
        :return: 
        """
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
    def Fonts(self) -> FontStore:
        """"""
    @property
    def ForceLocalVertexBatch(self) -> bool:
        """"""
    @ForceLocalVertexBatch.setter
    def ForceLocalVertexBatch(self, value: bool) -> None: ...
    @property
    def HandleNonPositionalInput(self) -> bool:
        """"""
    @property
    def HandlePositionalInput(self) -> bool:
        """"""
    @property
    def HandledExtensions(self) -> IEnumerable[str]:
        """
        
        :return: 
        """
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
    def HideUnlicensedContent(self) -> bool:
        """
        
        :return: 
        """
    @property
    def InvalidationFromParentSize(self) -> Invalidation:
        """"""
    @property
    def InvalidationID(self) -> int:
        """"""
    @property
    def IsActive(self) -> IBindable[bool]:
        """"""
    @property
    def IsAlive(self) -> bool:
        """"""
    @property
    def IsDeployedBuild(self) -> bool:
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
    def IsIdle(self) -> IBindable[bool]:
        """
        
        :return: 
        """
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
    def OverlayActivationMode(self) -> IBindable[OverlayActivation]:
        """
        
        :return: 
        """
    @property
    def Padding(self) -> MarginPadding:
        """"""
    @Padding.setter
    def Padding(self, value: MarginPadding) -> None: ...
    @property
    def Parent(self) -> CompositeDrawable:
        """"""
    @property
    def PlayingState(self) -> IBindable[LocalUserPlayingState]:
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
    def Resources(self) -> ResourceStore[Array[int]]:
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
    def ScalingContainerTargetDrawSize(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def ScreenSpaceDrawQuad(self) -> Quad:
        """"""
    @property
    def Shaders(self) -> ShaderManager:
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
    def Textures(self) -> TextureStore:
        """"""
    @property
    def Time(self) -> FrameTimeInfo:
        """"""
    @property
    def Toolbar(self) -> Toolbar:
        """
        
        :return: 
        """
    @property
    def TransformStartTime(self) -> float:
        """"""
    @property
    def Transforms(self) -> IEnumerable[Transform]:
        """"""
    @property
    def UseDevelopmentServer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Version(self) -> str:
        """
        
        :return: 
        """
    @property
    def VersionHash(self) -> str:
        """
        
        :return: 
        """
    @property
    def Width(self) -> float:
        """"""
    @Width.setter
    def Width(self, value: float) -> None: ...
    @property
    def Window(self) -> IWindow:
        """"""
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
    def AddFont(self, store: ResourceStore[Array[int]], assetName: str = ..., target: FontStore = ...) -> None:
        """"""
    def AddRange(self, range: IEnumerable[Drawable]) -> None:
        """"""
    def AddTransform(self, transform: Transform, customTransformID: Optional[int] = ...) -> None:
        """"""
    def ApplyTransformsAt(self, time: float, propagateChildren: bool = ...) -> None:
        """"""
    def AttemptExit(self) -> None:
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
    def CloseAllOverlays(self, hideToolbar: bool = ...) -> None:
        """
        
        :param hideToolbar: 
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
    def CopyToClipboard(self, value: str) -> None:
        """
        
        :param value: 
        """
    def CreateEndpoints(self) -> EndpointConfiguration:
        """
        
        :return: 
        """
    def CreateProxy(self) -> Drawable:
        """"""
    def CreateSettingsSubsectionFor(self, handler: InputHandler) -> SettingsSubsection:
        """
        
        :param handler: 
        :return: 
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Exit(self) -> None:
        """"""
    def Expire(self, calculateLifetimeStart: bool = ...) -> None:
        """"""
    def FilterBeatmapSetGenre(self, genre: SearchGenre) -> None:
        """
        
        :param genre: 
        """
    def FilterBeatmapSetLanguage(self, language: SearchLanguage) -> None:
        """
        
        :param language: 
        """
    def FinishTransforms(self, propagateChildren: bool = ..., targetMember: str = ...) -> None:
        """"""
    def GetEnumerator(self) -> Container.Enumerator[Drawable]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetStorageForStableInstall(self) -> StableStorage:
        """
        
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    @overload
    def HandleLink(self, url: str) -> None:
        """
        
        :param url: 
        """
    @overload
    def HandleLink(self, link: LinkDetails) -> None:
        """
        
        :param link: 
        """
    def HandleTimestamp(self, timestamp: str) -> None:
        """
        
        :param timestamp: 
        """
    def Hide(self) -> None:
        """"""
    def HideBlockingOverlay(self, overlay: OverlayContainer) -> None:
        """
        
        :param overlay: 
        """
    @overload
    def Import(self, paths: Array[str]) -> Task:
        """
        
        :param paths: 
        :return: 
        """
    @overload
    def Import(self, imports: Array[ImportTask], parameters: ImportParameters = ...) -> Task:
        """
        
        :param tasks: 
        :param parameters: 
        :return: 
        """
    def IndexOf(self, drawable: Drawable) -> int:
        """"""
    def Invalidate(self, invalidation: Invalidation = ..., source: InvalidationSource = ...) -> bool:
        """"""
    def JoinRoom(self, id: int) -> None:
        """
        
        :param id: 
        """
    def Migrate(self, path: str) -> bool:
        """
        
        :param path: 
        :return: 
        """
    @overload
    def OnPressed(self, e: KeyBindingPressEvent[FrameworkAction]) -> bool:
        """"""
    @overload
    def OnPressed(self, e: KeyBindingPressEvent[PlatformAction]) -> bool:
        """"""
    @overload
    def OnPressed(self, e: KeyBindingPressEvent[GlobalAction]) -> bool:
        """"""
    @overload
    def OnReleased(self, e: KeyBindingReleaseEvent[FrameworkAction]) -> None:
        """"""
    @overload
    def OnReleased(self, e: KeyBindingReleaseEvent[PlatformAction]) -> None:
        """"""
    @overload
    def OnReleased(self, e: KeyBindingReleaseEvent[GlobalAction]) -> None:
        """"""
    def OpenUrlExternally(self, url: str, warnMode: LinkWarnMode = ...) -> None:
        """
        
        :param url: 
        :param warnMode: 
        """
    def PerformFromScreen(self, action: Action[IScreen], validScreens: IEnumerable[Type] = ...) -> None:
        """
        
        :param action: 
        :param validScreens: 
        """
    def PresentBeatmap(self, beatmap: IBeatmapSetInfo, difficultyCriteria: Predicate[BeatmapInfo] = ...) -> None:
        """
        
        :param beatmap: 
        :param difficultyCriteria: 
        """
    def PresentMultiplayerMatch(self, room: Room, password: str) -> None:
        """
        
        :param room: 
        :param password: 
        """
    def PresentPlaylist(self, room: Room) -> None:
        """
        
        :param room: 
        """
    def PresentScore(self, score: IScoreInfo, presentType: ScorePresentType = ...) -> None:
        """
        
        :param score: 
        :param presentType: 
        """
    def PresentSkin(self, skin: SkinInfo) -> None:
        """
        
        :param skin: 
        """
    def ReceivePositionalInputAt(self, screenSpacePos: Vector2) -> bool:
        """"""
    def RegisterBlockingOverlay(self, overlayContainer: OverlayContainer) -> IDisposable:
        """
        
        :param overlayContainer: 
        :return: 
        """
    def RegisterForDependencyActivation(self, registry: IDependencyActivatorRegistry) -> None:
        """"""
    def RegisterImportHandler(self, handler: ICanAcceptFiles) -> None:
        """
        
        :param handler: 
        """
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
    def RequestExit(self) -> None:
        """"""
    def RestartAppWhenExited(self) -> bool:
        """
        
        :return: 
        """
    def SearchBeatmapSet(self, query: str) -> None:
        """
        
        :param query: 
        """
    def SetHost(self, host: GameHost) -> None:
        """"""
    def SetupLogging(self, gameStorage: Storage, cacheStorage: Storage) -> None:
        """"""
    def Show(self) -> None:
        """"""
    def ShowBeatmap(self, beatmapId: int) -> None:
        """
        
        :param beatmapId: 
        """
    def ShowBeatmapSet(self, setId: int) -> None:
        """
        
        :param setId: 
        """
    def ShowBlockingOverlay(self, overlay: OverlayContainer) -> None:
        """
        
        :param overlay: 
        """
    def ShowChangelogBuild(self, version: str) -> None:
        """
        
        :param version: 
        """
    def ShowChangelogListing(self) -> None:
        """"""
    def ShowChannel(self, channel: str) -> None:
        """
        
        :param channel: 
        """
    def ShowUser(self, user: IUser) -> None:
        """
        
        :param user: 
        """
    def ShowWiki(self, path: str) -> None:
        """
        
        :param path: 
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
    def UnregisterImportHandler(self, handler: ICanAcceptFiles) -> None:
        """
        
        :param handler: 
        """
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
    OnLoadComplete: EventType[Action[Drawable]] = ...
    """"""
    OnUpdate: EventType[Action[Drawable]] = ...
    """"""
class OsuGameBase(Game, ICollection[Drawable], IEnumerable[Drawable], IReadOnlyCollection[Drawable], IReadOnlyList[Drawable], IEnumerable, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, IHasAmplitudes, IContainer, IContainerCollection[Drawable], IContainerEnumerable[Drawable], ITransformable, IDrawable, IKeyBindingHandler, IKeyBindingHandler[FrameworkAction], IKeyBindingHandler[PlatformAction], IHandleGlobalKeyboardInput, ISourceGeneratedHandleInputCache, IBeatSyncProvider, ICanAcceptFiles):
    """"""
    AvailableMods: Final[Bindable[Dictionary, IReadOnlyList[Mod]]] = ...
    """
    
    :return: 
    """
    CLIENT_DATABASE_FILENAME: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    GAME_NAME: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Name: Final[str] = ...
    """"""
    OSU_PROTOCOL: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    ProcessCustomClock: Final[bool] = ...
    """"""
    SAMPLE_CONCURRENCY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SAMPLE_DEBOUNCE_TIME: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SFX_STEREO_STRENGTH: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
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
    def AssemblyVersion(self) -> Version:
        """
        
        :return: 
        """
    @property
    def Audio(self) -> AudioManager:
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
        """
        
        :return: 
        """
    @Clock.setter
    def Clock(self, value: IFrameBasedClock) -> None: ...
    @property
    def Colour(self) -> ColourInfo:
        """"""
    @Colour.setter
    def Colour(self, value: ColourInfo) -> None: ...
    @property
    def ControlPoints(self) -> ControlPointInfo:
        """
        
        :return: 
        """
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
    def CurrentAmplitudes(self) -> ChannelAmplitudes:
        """"""
    @property
    def CurrentLanguage(self) -> Bindable[Language]:
        """
        
        :return: 
        """
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
    def Fonts(self) -> FontStore:
        """"""
    @property
    def ForceLocalVertexBatch(self) -> bool:
        """"""
    @ForceLocalVertexBatch.setter
    def ForceLocalVertexBatch(self, value: bool) -> None: ...
    @property
    def HandleNonPositionalInput(self) -> bool:
        """"""
    @property
    def HandlePositionalInput(self) -> bool:
        """"""
    @property
    def HandledExtensions(self) -> IEnumerable[str]:
        """
        
        :return: 
        """
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
    def IsActive(self) -> IBindable[bool]:
        """"""
    @property
    def IsAlive(self) -> bool:
        """"""
    @property
    def IsDeployedBuild(self) -> bool:
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
    def Resources(self) -> ResourceStore[Array[int]]:
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
    def Shaders(self) -> ShaderManager:
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
    def Textures(self) -> TextureStore:
        """"""
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
    def UseDevelopmentServer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Version(self) -> str:
        """
        
        :return: 
        """
    @property
    def VersionHash(self) -> str:
        """
        
        :return: 
        """
    @property
    def Width(self) -> float:
        """"""
    @Width.setter
    def Width(self, value: float) -> None: ...
    @property
    def Window(self) -> IWindow:
        """"""
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
    def AddFont(self, store: ResourceStore[Array[int]], assetName: str = ..., target: FontStore = ...) -> None:
        """"""
    def AddRange(self, range: IEnumerable[Drawable]) -> None:
        """"""
    def AddTransform(self, transform: Transform, customTransformID: Optional[int] = ...) -> None:
        """"""
    def ApplyTransformsAt(self, time: float, propagateChildren: bool = ...) -> None:
        """"""
    def AttemptExit(self) -> None:
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
    def CreateEndpoints(self) -> EndpointConfiguration:
        """
        
        :return: 
        """
    def CreateProxy(self) -> Drawable:
        """"""
    def CreateSettingsSubsectionFor(self, handler: InputHandler) -> SettingsSubsection:
        """
        
        :param handler: 
        :return: 
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Exit(self) -> None:
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
    @overload
    def Import(self, paths: Array[str]) -> Task:
        """
        
        :param paths: 
        :return: 
        """
    @overload
    def Import(self, tasks: Array[ImportTask], parameters: ImportParameters = ...) -> Task:
        """
        
        :param tasks: 
        :param parameters: 
        :return: 
        """
    def IndexOf(self, drawable: Drawable) -> int:
        """"""
    def Invalidate(self, invalidation: Invalidation = ..., source: InvalidationSource = ...) -> bool:
        """"""
    def Migrate(self, path: str) -> bool:
        """
        
        :param path: 
        :return: 
        """
    @overload
    def OnPressed(self, e: KeyBindingPressEvent[FrameworkAction]) -> bool:
        """"""
    @overload
    def OnPressed(self, e: KeyBindingPressEvent[PlatformAction]) -> bool:
        """"""
    @overload
    def OnReleased(self, e: KeyBindingReleaseEvent[FrameworkAction]) -> None:
        """"""
    @overload
    def OnReleased(self, e: KeyBindingReleaseEvent[PlatformAction]) -> None:
        """"""
    def ReceivePositionalInputAt(self, screenSpacePos: Vector2) -> bool:
        """"""
    def RegisterForDependencyActivation(self, registry: IDependencyActivatorRegistry) -> None:
        """"""
    def RegisterImportHandler(self, handler: ICanAcceptFiles) -> None:
        """
        
        :param handler: 
        """
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
    def RequestExit(self) -> None:
        """"""
    def RestartAppWhenExited(self) -> bool:
        """
        
        :return: 
        """
    def SetHost(self, host: GameHost) -> None:
        """"""
    def SetupLogging(self, gameStorage: Storage, cacheStorage: Storage) -> None:
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
    def UnregisterImportHandler(self, handler: ICanAcceptFiles) -> None:
        """
        
        :param handler: 
        """
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
    OnLoadComplete: EventType[Action[Drawable]] = ...
    """"""
    OnUpdate: EventType[Action[Drawable]] = ...
    """"""
class PerformFromMenuRunner(Component, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
    """"""
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    def __init__(self, finalAction: Action[IScreen], validScreens: IEnumerable[Type], getCurrentScreen: Func[IScreen]):
        """
        
        :param finalAction: 
        :param validScreens: 
        :param getCurrentScreen: 
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
    def Cancel(self) -> None:
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