from System import Action
from System import Array
from System.Collections.Generic import ICollection
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IReadOnlyCollection
from System.Collections.Generic import IReadOnlyList
from System.Collections import IEnumerable
from System import Enum
from System import IDisposable
from System import Predicate
from System import Type
from System import ValueTuple
from __future__ import annotations
from osu.Framework.Allocation import IDependencyActivatorRegistry
from osu.Framework.Allocation import IDependencyInjectionCandidate
from osu.Framework.Allocation import IReadOnlyDependencyContainer
from osu.Framework.Allocation import ISourceGeneratedDependencyActivator
from osu.Framework.Allocation import ISourceGeneratedLongRunningLoadCache
from osu.Framework.Graphics import Anchor
from osu.Framework.Graphics import Axes
from osu.Framework.Graphics import BlendingParameters
from osu.Framework.Graphics.Colour import ColourInfo
from osu.Framework.Graphics.Containers import CompositeDrawable
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
from osu.Framework.Graphics.Transforms import ITransformable
from osu.Framework.Graphics.Transforms import Transform
from osu.Framework.IO.Stores import IResourceStore
from osu.Framework.Input.Bindings import KeyBinding
from osu.Framework.Input.Bindings import KeyBindingContainer
from osu.Framework.Input.Events import UIEvent
from osu.Framework.Input import IFocusManager
from osu.Framework.Input import IRequireHighFrequencyMousePosition
from osu.Framework.Input import ISourceGeneratedHandleInputCache
from osu.Framework.Input import JoystickAxisEventManager
from osu.Framework.Input import JoystickAxisSource
from osu.Framework.Input import JoystickButton
from osu.Framework.Input import JoystickButtonEventManager
from osu.Framework.Input import KeyEventManager
from osu.Framework.Input import MidiKey
from osu.Framework.Input import MidiKeyEventManager
from osu.Framework.Input import MouseButtonEventManager
from osu.Framework.Input.StateChanges.Events import InputStateChangeEvent
from osu.Framework.Input.StateChanges import IInputStateChangeHandler
from osu.Framework.Input.States import InputState
from osu.Framework.Input import TabletAuxiliaryButton
from osu.Framework.Input import TabletAuxiliaryButtonEventManager
from osu.Framework.Input import TabletPenButton
from osu.Framework.Input import TabletPenButtonEventManager
from osu.Framework.Input import TouchEventManager
from osu.Framework.Input import TouchSource
from osu.Framework.Layout import InvalidationSource
from osu.Framework.Lists import SlimReadOnlyListWrapper
from osu.Framework.Localisation import LocalisableString
from osu.Framework.Timing import FrameTimeInfo
from osu.Framework.Timing import IFrameBasedClock
from osu.Game.Beatmaps import BeatmapDifficulty
from osu.Game.Beatmaps import IBeatmap
from osu.Game.Beatmaps import IBeatmapConverter
from osu.Game.Beatmaps import IBeatmapInfo
from osu.Game.Beatmaps import IBeatmapProcessor
from osu.Game.Beatmaps import IWorkingBeatmap
from osu.Game.Beatmaps.Legacy import LegacyMods
from osu.Game.Configuration import SettingsStore
from osu.Game.Input.Handlers import ReplayInputHandler
from osu.Game.Overlays.Settings import RulesetSettingsSubsection
from osu.Game.Rulesets.Configuration import IRulesetConfigManager
from osu.Game.Rulesets.Difficulty import DifficultyCalculator
from osu.Game.Rulesets.Difficulty import PerformanceCalculator
from osu.Game.Rulesets.Difficulty import RulesetBeatmapAttribute
from osu.Game.Rulesets.Edit import HitObjectComposer
from osu.Game.Rulesets.Edit import IBeatmapVerifier
from osu.Game.Rulesets.Filter import IRulesetFilterCriteria
from osu.Game.Rulesets import ILegacyRuleset
from osu.Game.Rulesets.Mods import IMod
from osu.Game.Rulesets.Mods import Mod
from osu.Game.Rulesets.Mods import ModAutoplay
from osu.Game.Rulesets.Mods import ModTouchDevice
from osu.Game.Rulesets.Mods import ModType
from osu.Game.Rulesets.Replays.Types import IConvertibleReplayFrame
from osu.Game.Rulesets import Ruleset
from osu.Game.Rulesets import RulesetInfo
from osu.Game.Rulesets.Scoring import HealthProcessor
from osu.Game.Rulesets.Scoring import HitResult
from osu.Game.Rulesets.Scoring.Legacy import ILegacyScoreSimulator
from osu.Game.Rulesets.Scoring import ScoreProcessor
from osu.Game.Rulesets.UI import DrawableRuleset
from osu.Game.Rulesets.UI import ICanAttachHUDPieces
from osu.Game.Rulesets.UI import IHasRecordingHandler
from osu.Game.Rulesets.UI import IHasReplayHandler
from osu.Game.Rulesets.UI import ReplayRecorder
from osu.Game.Rulesets.UI import RulesetInputManager
from osu.Game.Scoring import ScoreInfo
from osu.Game.Screens.Play.HUD.ClicksPerSecond import ClicksPerSecondController
from osu.Game.Screens.Play.HUD import InputCountController
from osu.Game.Screens.Ranking.Statistics import StatisticItem
from osu.Game.Skinning import ISkin
from osu.Game.Skinning import ISkinComponentLookup
from osu.Game.Skinning import SkinComponentLookup
from osuTK.Input import Key
from osuTK.Input import MouseButton
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
class OsuAction(Enum):
    """"""
    LeftButton: OsuAction = ...
    """"""
    RightButton: OsuAction = ...
    """"""
    Smoke: OsuAction = ...
    """"""
class OsuInputManager(RulesetInputManager[OsuAction], ICollection[Drawable], IEnumerable[Drawable], IReadOnlyCollection[Drawable], IReadOnlyList[Drawable], IEnumerable, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, IContainer, IContainerCollection[Drawable], IContainerEnumerable[Drawable], ITransformable, IDrawable, IInputStateChangeHandler, IFocusManager, IRequireHighFrequencyMousePosition, ISourceGeneratedHandleInputCache, ICanAttachHUDPieces, IHasRecordingHandler, IHasReplayHandler):
    """"""
    CurrentState: Final[InputState] = ...
    """"""
    KeyBindingContainer: Final[KeyBindingContainer[OsuAction]] = ...
    """
    
    :return: 
    """
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    def __init__(self, ruleset: RulesetInfo):
        """
        
        :param ruleset: 
        """
    @property
    def AcceptsFocus(self) -> bool:
        """"""
    @property
    def AliveChildren(self) -> IReadOnlyList[Drawable]:
        """"""
    @property
    def AllowGameplayInputs(self) -> bool:
        """
        
        :return: 
        """
    @AllowGameplayInputs.setter
    def AllowGameplayInputs(self, value: bool) -> None: ...
    @property
    def AllowUserCursorMovement(self) -> bool:
        """
        
        :return: 
        """
    @AllowUserCursorMovement.setter
    def AllowUserCursorMovement(self, value: bool) -> None: ...
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
    def DisposeOnDeathRemoval(self) -> bool:
        """"""
    @property
    def DragBlocksClick(self) -> bool:
        """"""
    @property
    def DraggedDrawable(self) -> Drawable:
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
    def FocusedDrawable(self) -> Drawable:
        """"""
    @property
    def ForceLocalVertexBatch(self) -> bool:
        """"""
    @ForceLocalVertexBatch.setter
    def ForceLocalVertexBatch(self, value: bool) -> None: ...
    @property
    def HandleHoverEvents(self) -> bool:
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
    def HoveredDrawables(self) -> SlimReadOnlyListWrapper[Drawable]:
        """"""
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
    def NonPositionalInputQueue(self) -> SlimReadOnlyListWrapper[Drawable]:
        """"""
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
    def PositionalInputQueue(self) -> SlimReadOnlyListWrapper[Drawable]:
        """"""
    @property
    def PressedActions(self) -> SlimReadOnlyListWrapper[OsuAction]:
        """
        
        :return: 
        """
    @property
    def PropagateNonPositionalInputSubTree(self) -> bool:
        """"""
    @property
    def PropagatePositionalInputSubTree(self) -> bool:
        """"""
    @property
    def Recorder(self) -> ReplayRecorder:
        """
        
        :return: 
        """
    @Recorder.setter
    def Recorder(self, value: ReplayRecorder) -> None: ...
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
    def ReplayInputHandler(self) -> ReplayInputHandler:
        """
        
        :return: 
        """
    @ReplayInputHandler.setter
    def ReplayInputHandler(self, value: ReplayInputHandler) -> None: ...
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
    def UseParentInput(self) -> bool:
        """"""
    @UseParentInput.setter
    def UseParentInput(self, value: bool) -> None: ...
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
    @overload
    def Attach(self, controller: ClicksPerSecondController) -> None:
        """
        
        :param controller: 
        """
    @overload
    def Attach(self, inputCountController: InputCountController) -> None:
        """
        
        :param inputCountController: 
        """
    def BeginAbsoluteSequence(self, newTransformStartTime: float, recursive: bool = ...) -> IDisposable:
        """"""
    def BeginDelayedSequence(self, delay: float, recursive: bool = ...) -> IDisposable:
        """"""
    def ChangeChildDepth(self, child: Drawable, newDepth: float) -> None:
        """"""
    def ChangeFocus(self, potentialFocusTarget: Drawable) -> bool:
        """"""
    def CheckScreenSpaceActionPressJudgeable(self, screenSpacePosition: Vector2) -> bool:
        """
        
        :param screenSpacePosition: 
        :return: 
        """
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
    @overload
    def GetButtonEventManagerFor(self, button: JoystickButton) -> JoystickButtonEventManager:
        """"""
    @overload
    def GetButtonEventManagerFor(self, key: MidiKey) -> MidiKeyEventManager:
        """"""
    @overload
    def GetButtonEventManagerFor(self, button: TabletAuxiliaryButton) -> TabletAuxiliaryButtonEventManager:
        """"""
    @overload
    def GetButtonEventManagerFor(self, button: TabletPenButton) -> TabletPenButtonEventManager:
        """"""
    @overload
    def GetButtonEventManagerFor(self, source: TouchSource) -> TouchEventManager:
        """"""
    @overload
    def GetButtonEventManagerFor(self, key: Key) -> KeyEventManager:
        """"""
    @overload
    def GetButtonEventManagerFor(self, button: MouseButton) -> MouseButtonEventManager:
        """"""
    def GetEnumerator(self) -> Container.Enumerator[Drawable]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetJoystickAxisEventManagerFor(self, source: JoystickAxisSource) -> JoystickAxisEventManager:
        """"""
    def GetType(self) -> Type:
        """"""
    def HandleInputStateChange(self, inputStateChange: InputStateChangeEvent) -> None:
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
    def TriggerFocusContention(self, triggerSource: Drawable) -> None:
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
    OnLoadComplete: EventType[Action[Drawable]] = ...
    """"""
    OnUpdate: EventType[Action[Drawable]] = ...
    """"""
    TouchLongPressBegan: EventType[Action[Vector2, float]] = ...
    """"""
    TouchLongPressCancelled: EventType[Action] = ...
    """"""
class OsuRuleset(Ruleset, ILegacyRuleset):
    """"""
    SHORT_NAME: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def AllMods(self) -> IEnumerable[IMod]:
        """
        
        :return: 
        """
    @property
    def AvailableVariants(self) -> IEnumerable[int]:
        """
        
        :return: 
        """
    @property
    def Description(self) -> str:
        """
        
        :return: 
        """
    @property
    def EditorShowScrollSpeed(self) -> bool:
        """
        
        :return: 
        """
    @property
    def LegacyID(self) -> int:
        """
        
        :return: 
        """
    @property
    def PlayingVerb(self) -> str:
        """
        
        :return: 
        """
    @property
    def RulesetAPIVersionSupported(self) -> str:
        """
        
        :return: 
        """
    @property
    def RulesetInfo(self) -> RulesetInfo:
        """
        
        :return: 
        """
    @property
    def ShortName(self) -> str:
        """
        
        :return: 
        """
    def ConvertFromLegacyMods(self, mods: LegacyMods) -> IEnumerable[Mod]:
        """
        
        :param mods: 
        :return: 
        """
    def ConvertToLegacyMods(self, mods: Array[Mod]) -> LegacyMods:
        """
        
        :param mods: 
        :return: 
        """
    def CreateAllMods(self) -> IEnumerable[Mod]:
        """
        
        :return: 
        """
    def CreateBeatmapConverter(self, beatmap: IBeatmap) -> IBeatmapConverter:
        """
        
        :param beatmap: 
        :return: 
        """
    def CreateBeatmapProcessor(self, beatmap: IBeatmap) -> IBeatmapProcessor:
        """
        
        :param beatmap: 
        :return: 
        """
    def CreateBeatmapVerifier(self) -> IBeatmapVerifier:
        """
        
        :return: 
        """
    def CreateConfig(self, settings: SettingsStore) -> IRulesetConfigManager:
        """
        
        :param settings: 
        :return: 
        """
    def CreateConvertibleReplayFrame(self) -> IConvertibleReplayFrame:
        """
        
        :return: 
        """
    def CreateDifficultyCalculator(self, beatmap: IWorkingBeatmap) -> DifficultyCalculator:
        """
        
        :param beatmap: 
        :return: 
        """
    def CreateDrawableRulesetWith(self, beatmap: IBeatmap, mods: IReadOnlyList[Mod] = ...) -> DrawableRuleset:
        """
        
        :param beatmap: 
        :param mods: 
        :return: 
        """
    def CreateEditorSetupSections(self) -> IEnumerable[Drawable]:
        """
        
        :return: 
        """
    def CreateHealthProcessor(self, drainStartTime: float) -> HealthProcessor:
        """
        
        :param drainStartTime: 
        :return: 
        """
    def CreateHitObjectComposer(self) -> HitObjectComposer:
        """
        
        :return: 
        """
    def CreateIcon(self) -> Drawable:
        """
        
        :return: 
        """
    def CreateLegacyScoreSimulator(self) -> ILegacyScoreSimulator:
        """
        
        :return: 
        """
    def CreateMod(self) -> T:
        """
        
        :return: 
        """
    def CreateModFromAcronym(self, acronym: str) -> Mod:
        """
        
        :param acronym: 
        :return: 
        """
    def CreatePerformanceCalculator(self) -> PerformanceCalculator:
        """
        
        :return: 
        """
    def CreateResourceStore(self) -> IResourceStore[Array[int]]:
        """
        
        :return: 
        """
    def CreateRulesetFilterCriteria(self) -> IRulesetFilterCriteria:
        """
        
        :return: 
        """
    def CreateScoreProcessor(self) -> ScoreProcessor:
        """
        
        :return: 
        """
    def CreateSettings(self) -> RulesetSettingsSubsection:
        """
        
        :return: 
        """
    def CreateSkinTransformer(self, skin: ISkin, beatmap: IBeatmap) -> ISkin:
        """
        
        :param skin: 
        :param beatmap: 
        :return: 
        """
    def CreateStatisticsForScore(self, score: ScoreInfo, playableBeatmap: IBeatmap) -> Array[StatisticItem]:
        """
        
        :param score: 
        :param playableBeatmap: 
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAdjustedDisplayDifficulty(self, difficulty: IBeatmapInfo, mods: IReadOnlyCollection[Mod]) -> BeatmapDifficulty:
        """
        
        :param beatmapInfo: 
        :param mods: 
        :return: 
        """
    def GetAutoplayMod(self) -> ModAutoplay:
        """
        
        :return: 
        """
    def GetBeatmapAttributesForDisplay(self, beatmapInfo: IBeatmapInfo, mods: IReadOnlyCollection[Mod]) -> IEnumerable[RulesetBeatmapAttribute]:
        """
        
        :param beatmapInfo: 
        :param mods: 
        :return: 
        """
    def GetDefaultKeyBindings(self, variant: int = ...) -> IEnumerable[KeyBinding]:
        """
        
        :param variant: 
        :return: 
        """
    def GetDisplayNameForHitResult(self, result: HitResult) -> LocalisableString:
        """
        
        :param result: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetHitResults(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    def GetKeyCount(self, beatmapInfo: IBeatmapInfo, mods: IReadOnlyList[Mod] = ...) -> int:
        """
        
        :param beatmapInfo: 
        :param mods: 
        :return: 
        """
    def GetModsFor(self, type: ModType) -> IEnumerable[Mod]:
        """
        
        :param type: 
        :return: 
        """
    def GetTouchDeviceMod(self) -> ModTouchDevice:
        """
        
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def GetVariantName(self, variant: int) -> LocalisableString:
        """
        
        :param variant: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class OsuSkinComponentLookup(SkinComponentLookup[OsuSkinComponents], ISkinComponentLookup):
    """"""
    Component: Final[OsuSkinComponents] = ...
    """
    
    :return: 
    """
    def __init__(self, component: OsuSkinComponents):
        """
        
        :param component: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class OsuSkinComponents(Enum):
    """"""
    HitCircle: OsuSkinComponents = ...
    """"""
    FollowPoint: OsuSkinComponents = ...
    """"""
    Cursor: OsuSkinComponents = ...
    """"""
    CursorTrail: OsuSkinComponents = ...
    """"""
    CursorParticles: OsuSkinComponents = ...
    """"""
    CursorRipple: OsuSkinComponents = ...
    """"""
    SliderScorePoint: OsuSkinComponents = ...
    """"""
    ReverseArrow: OsuSkinComponents = ...
    """"""
    HitCircleText: OsuSkinComponents = ...
    """"""
    SliderHeadHitCircle: OsuSkinComponents = ...
    """"""
    SliderTailHitCircle: OsuSkinComponents = ...
    """"""
    SliderFollowCircle: OsuSkinComponents = ...
    """"""
    SliderBall: OsuSkinComponents = ...
    """"""
    SliderBody: OsuSkinComponents = ...
    """"""
    SpinnerBody: OsuSkinComponents = ...
    """"""
    CursorSmoke: OsuSkinComponents = ...
    """"""
    ApproachCircle: OsuSkinComponents = ...
    """"""