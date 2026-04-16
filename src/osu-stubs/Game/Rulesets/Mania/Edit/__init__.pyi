from System import Action
from System import Array
from System.Collections.Generic import Dictionary
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IReadOnlyList
from System.Collections.Generic import List
from System import Func
from System import IDisposable
from System import Object
from System import Type
from System import ValueTuple
from __future__ import annotations
from osu.Framework.Allocation import IDependencyActivatorRegistry
from osu.Framework.Allocation import IDependencyInjectionCandidate
from osu.Framework.Allocation import IReadOnlyDependencyContainer
from osu.Framework.Allocation import ISourceGeneratedDependencyActivator
from osu.Framework.Allocation import ISourceGeneratedLongRunningLoadCache
from osu.Framework.Audio import IAdjustableAudioComponent
from osu.Framework.Bindables import Bindable
from osu.Framework.Bindables import BindableBool
from osu.Framework.Bindables import BindableList
from osu.Framework.Graphics import Anchor
from osu.Framework.Graphics import Axes
from osu.Framework.Graphics import BlendingParameters
from osu.Framework.Graphics.Colour import ColourInfo
from osu.Framework.Graphics.Containers import CompositeDrawable
from osu.Framework.Graphics.Containers import Container
from osu.Framework.Graphics.Cursor import IHasContextMenu
from osu.Framework.Graphics import Direction
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
from osu.Framework.Graphics.UserInterface import MenuItem
from osu.Framework.Input.Bindings import IKeyBindingHandler
from osu.Framework.Input.Events import KeyBindingPressEvent
from osu.Framework.Input.Events import KeyBindingReleaseEvent
from osu.Framework.Input.Events import UIEvent
from osu.Framework.Input import ISourceGeneratedHandleInputCache
from osu.Framework.Input import PlatformAction
from osu.Framework.Layout import InvalidationSource
from osu.Framework.Localisation import LocalisableString
from osu.Framework.Timing import FrameTimeInfo
from osu.Framework.Timing import IFrameBasedClock
from osu.Game.Audio import ISampleInfo
from osu.Game.Beatmaps import Beatmap
from osu.Game.Beatmaps import IBeatmap
from osu.Game.Configuration import ScrollVisualisationMethod
from osu.Game.Graphics.Cursor import IProvideCursor
from osu.Game.Graphics.UserInterface import TernaryState
from osu.Game.Input.Bindings import GlobalAction
from osu.Game.Rulesets.Edit import BeatmapVerifierContext
from osu.Game.Rulesets.Edit.Checks.Components import Issue
from osu.Game.Rulesets.Edit import HitObjectPlacementBlueprint
from osu.Game.Rulesets.Edit import HitObjectSelectionBlueprint
from osu.Game.Rulesets.Edit import IBeatmapVerifier
from osu.Game.Rulesets.Edit import PlacementBlueprint
from osu.Game.Rulesets.Edit import ScrollingHitObjectComposer
from osu.Game.Rulesets.Edit import SelectionBlueprint
from osu.Game.Rulesets.Edit import SnapResult
from osu.Game.Rulesets.Edit.Tools import CompositionTool
from osu.Game.Rulesets.Judgements import JudgementResult
from osu.Game.Rulesets.Mania.Beatmaps import ManiaBeatmap
from osu.Game.Rulesets.Mania.Beatmaps import StageDefinition
from osu.Game.Rulesets.Mania import ManiaAction
from osu.Game.Rulesets.Mania.Objects import BarLine
from osu.Game.Rulesets.Mania.Objects import ManiaHitObject
from osu.Game.Rulesets.Mania.UI import Column
from osu.Game.Rulesets.Mania.UI.Components import ColumnHitObjectArea
from osu.Game.Rulesets.Mania.UI import DrawableManiaRuleset
from osu.Game.Rulesets.Mania.UI import ManiaPlayfield
from osu.Game.Rulesets.Mania.UI import Stage
from osu.Game.Rulesets.Mods import Mod
from osu.Game.Rulesets.Objects.Drawables import DrawableHitObject
from osu.Game.Rulesets.Objects import HitObject
from osu.Game.Rulesets import Ruleset
from osu.Game.Rulesets.Scoring import HitWindows
from osu.Game.Rulesets.UI import GameplayCursorContainer
from osu.Game.Rulesets.UI import HitObjectContainer
from osu.Game.Rulesets.UI import ICanAttachHUDPieces
from osu.Game.Rulesets.UI import IFrameStableClock
from osu.Game.Rulesets.UI import IPooledHitObjectProvider
from osu.Game.Rulesets.UI import Playfield
from osu.Game.Rulesets.UI import PlayfieldAdjustmentContainer
from osu.Game.Rulesets.UI.Scrolling import IDrawableScrollingRuleset
from osu.Game.Rulesets.UI.Scrolling import IScrollingInfo
from osu.Game.Rulesets.UI.Scrolling import ISupportConstantAlgorithmToggle
from osu.Game.Scoring import Score
from osu.Game.Screens.Edit.Components.TernaryButtons import SampleBankTernaryButton
from osu.Game.Screens.Edit.Compose.Components import BeatSnapGrid
from osu.Game.Screens.Edit.Compose.Components.BlueprintContainer import SelectionBlueprintContainer
from osu.Game.Screens.Edit.Compose.Components import ComposeBlueprintContainer
from osu.Game.Screens.Edit.Compose.Components import EditorSelectionHandler
from osu.Game.Screens.Edit.Compose.Components import MoveSelectionEvent
from osu.Game.Screens.Edit.Compose.Components import SelectionBox
from osu.Game.Screens.Edit.Compose.Components import SelectionHandler
from osu.Game.Screens.Edit.Compose.Components import SelectionRotationHandler
from osu.Game.Screens.Edit.Compose.Components import SelectionScaleHandler
from osu.Game.Screens.Edit.Compose import IPlacementHandler
from osu.Game.Screens.Play.HUD.ClicksPerSecond import ClicksPerSecondController
from osu.Game.Screens.Play.HUD import InputCountController
from osu.Game.Screens.Play import ResumeOverlay
from osu.Game.Skinning import IPooledSampleProvider
from osu.Game.Skinning import PoolableSkinnableSample
from osuTK.Graphics import Color4
from osuTK import Vector2
from typing import Final
from typing import Generic
from typing import Optional
from typing import TypeVar
from typing import overload
T = TypeVar("T")
class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...
class DrawableManiaEditorRuleset(DrawableManiaRuleset, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, IKeyBindingHandler, IKeyBindingHandler[GlobalAction], ISourceGeneratedHandleInputCache, IProvideCursor, IDrawableScrollingRuleset, ISupportConstantAlgorithmToggle, ICanAttachHUDPieces):
    """"""
    BarLines: Final[IEnumerable[BarLine]] = ...
    """
    
    :return: 
    """
    Beatmap: Final[Beatmap[ManiaHitObject]] = ...
    """
    
    :return: 
    """
    HasReplayLoaded: Final[BindableBool] = ...
    """
    
    :return: 
    """
    IsPaused: Final[BindableBool] = ...
    """
    
    :return: 
    """
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    Ruleset: Final[Ruleset] = ...
    """
    
    :return: 
    """
    def __init__(self, ruleset: Ruleset, beatmap: IBeatmap, mods: IReadOnlyList[Mod]):
        """
        
        :param ruleset: 
        :param beatmap: 
        :param mods: 
        """
    @property
    def AcceptsFocus(self) -> bool:
        """"""
    @property
    def AllowGameplayOverlays(self) -> bool:
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
    def Audio(self) -> IAdjustableAudioComponent:
        """
        
        :return: 
        """
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
    def Beatmap(self) -> ManiaBeatmap:
        """
        
        :return: 
        """
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
    def Cursor(self) -> GameplayCursorContainer:
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
    def FirstAvailableHitWindows(self) -> HitWindows:
        """
        
        :return: 
        """
    @property
    def ForceLocalVertexBatch(self) -> bool:
        """"""
    @property
    def FrameStableClock(self) -> IFrameStableClock:
        """
        
        :return: 
        """
    @property
    def FrameStableComponents(self) -> Container:
        """
        
        :return: 
        """
    @property
    def GameplayStartTime(self) -> float:
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
    def Masking(self) -> bool:
        """"""
    @property
    def MaskingSmoothness(self) -> float:
        """"""
    @property
    def Mods(self) -> IReadOnlyList[Mod]:
        """
        
        :return: 
        """
    @property
    def Objects(self) -> IEnumerable[HitObject]:
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
    def Overlays(self) -> Container:
        """
        
        :return: 
        """
    @property
    def Padding(self) -> MarginPadding:
        """"""
    @property
    def Parent(self) -> CompositeDrawable:
        """"""
    @property
    def Playfield(self) -> Playfield:
        """
        
        :return: 
        """
    @property
    def PlayfieldAdjustmentContainer(self) -> PlayfieldAdjustmentContainer:
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
    def ProvidingUserCursor(self) -> bool:
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
    def ReplayScore(self) -> Score:
        """
        
        :return: 
        """
    @property
    def RequestsFocus(self) -> bool:
        """"""
    @property
    def RequiresPortraitOrientation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ResumeOverlay(self) -> ResumeOverlay:
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
    def ScrollingInfo(self) -> IScrollingInfo:
        """
        
        :return: 
        """
    @property
    def Shear(self) -> Vector2:
        """"""
    @Shear.setter
    def Shear(self, value: Vector2) -> None: ...
    @property
    def ShowSpeedChanges(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def Size(self) -> Vector2:
        """"""
    @Size.setter
    def Size(self, value: Vector2) -> None: ...
    @property
    def TargetTimeRange(self) -> float:
        """
        
        :return: 
        """
    @property
    def Time(self) -> FrameTimeInfo:
        """"""
    @property
    def TimelineTimeRange(self) -> Optional[float]:
        """
        
        :return: 
        """
    @TimelineTimeRange.setter
    def TimelineTimeRange(self, value: Optional[float]) -> None: ...
    @property
    def TransformStartTime(self) -> float:
        """"""
    @property
    def Transforms(self) -> IEnumerable[Transform]:
        """"""
    @property
    def UseResumeOverlay(self) -> bool:
        """
        
        :return: 
        """
    @UseResumeOverlay.setter
    def UseResumeOverlay(self, value: bool) -> None: ...
    @property
    def Variant(self) -> int:
        """
        
        :return: 
        """
    @property
    def VisualisationMethod(self) -> ScrollVisualisationMethod:
        """
        
        :return: 
        """
    @VisualisationMethod.setter
    def VisualisationMethod(self, value: ScrollVisualisationMethod) -> None: ...
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
    def AddHitObject(self, hitObject: ManiaHitObject) -> None:
        """
        
        :param hitObject: 
        """
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
    def CancelResume(self) -> None:
        """"""
    def ClearTransforms(self, propagateChildren: bool = ..., targetMember: str = ...) -> None:
        """"""
    def ClearTransformsAfter(self, time: float, propagateChildren: bool = ..., targetMember: str = ...) -> None:
        """"""
    def ComputeMaskingBounds(self) -> RectangleF:
        """"""
    def Contains(self, screenSpacePos: Vector2) -> bool:
        """"""
    def CreateDrawableRepresentation(self, h: ManiaHitObject) -> DrawableHitObject[ManiaHitObject]:
        """
        
        :param h: 
        :return: 
        """
    def CreatePlayfieldAdjustmentContainer(self) -> PlayfieldAdjustmentContainer:
        """
        
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
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Hide(self) -> None:
        """"""
    def Invalidate(self, invalidation: Invalidation = ..., source: InvalidationSource = ...) -> bool:
        """"""
    def OnPressed(self, e: KeyBindingPressEvent[GlobalAction]) -> bool:
        """"""
    def OnReleased(self, e: KeyBindingReleaseEvent[GlobalAction]) -> None:
        """"""
    def ReceivePositionalInputAt(self, screenSpacePos: Vector2) -> bool:
        """"""
    def RegisterForDependencyActivation(self, registry: IDependencyActivatorRegistry) -> None:
        """"""
    def RemoveHitObject(self, hitObject: ManiaHitObject) -> bool:
        """
        
        :param hitObject: 
        :return: 
        """
    def RemoveTransform(self, toRemove: Transform) -> None:
        """"""
    def RequestResume(self, continueResume: Action) -> None:
        """
        
        :param continueResume: 
        """
    def SetRecordTarget(self, score: Score) -> None:
        """
        
        :param score: 
        """
    def SetReplayScore(self, replayScore: Score) -> None:
        """
        
        :param replayScore: 
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
    def UpdateSubTree(self) -> bool:
        """"""
    def UpdateSubTreeMasking(self) -> bool:
        """"""
    def WithEffect(self, effect: IEffect[T], initializationAction: Action[T] = ...) -> T:
        """"""
    def __contains__(self, screenSpacePos: Vector2) -> bool:
        """"""
    NewResult: EventType[Action[JudgementResult]] = ...
    """"""
    OnLoadComplete: EventType[Action[Drawable]] = ...
    """"""
    OnUpdate: EventType[Action[Drawable]] = ...
    """"""
    RevertResult: EventType[Action[JudgementResult]] = ...
    """"""
class EditorColumn(Column, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, IKeyBindingHandler, IKeyBindingHandler[ManiaAction], ISourceGeneratedHandleInputCache, IPooledHitObjectProvider, IPooledSampleProvider):
    """"""
    AccentColour: Final[Bindable[Color4]] = ...
    """
    
    :return: 
    """
    Action: Final[Bindable[ManiaAction]] = ...
    """
    
    :return: 
    """
    DisplayJudgements: Final[BindableBool] = ...
    """
    
    :return: 
    """
    HitObjectArea: Final[ColumnHitObjectArea] = ...
    """
    
    :return: 
    """
    Index: Final[int] = ...
    """
    
    :return: 
    """
    IsSpecial: Final[bool] = ...
    """
    
    :return: 
    """
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    def __init__(self, index: int, isSpecial: bool):
        """
        
        :param index: 
        :param isSpecial: 
        """
    @property
    def AcceptsFocus(self) -> bool:
        """"""
    @property
    def AllHitObjects(self) -> IEnumerable[DrawableHitObject]:
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
    def Cursor(self) -> GameplayCursorContainer:
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
    def GamefieldToScreenSpace(self) -> Func[Vector2, Vector2]:
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
    def HitObjectContainer(self) -> HitObjectContainer:
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
    def IsNested(self) -> bool:
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
    @property
    def MaskingSmoothness(self) -> float:
        """"""
    @property
    def NestedPlayfields(self) -> IEnumerable[Playfield]:
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
    def ScreenSpaceToGamefield(self) -> Func[Vector2, Vector2]:
        """
        
        :return: 
        """
    @property
    def ScrollingInfo(self) -> IScrollingInfo:
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
    def SkinnableComponentScreenSpaceDrawQuad(self) -> Quad:
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
    def UnderlayElements(self) -> Container:
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
    @overload
    def Add(self, h: DrawableHitObject) -> None:
        """
        
        :param h: 
        """
    @overload
    def Add(self, hitObject: HitObject) -> None:
        """
        
        :param hitObject: 
        """
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
    def GetPooledDrawableRepresentation(self, hitObject: HitObject, parent: DrawableHitObject) -> DrawableHitObject:
        """
        
        :param hitObject: 
        :param parent: 
        :return: 
        """
    def GetPooledSample(self, sampleInfo: ISampleInfo) -> PoolableSkinnableSample:
        """
        
        :param sampleInfo: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def Hide(self) -> None:
        """"""
    def Invalidate(self, invalidation: Invalidation = ..., source: InvalidationSource = ...) -> bool:
        """"""
    def OnPressed(self, e: KeyBindingPressEvent[ManiaAction]) -> bool:
        """"""
    def OnReleased(self, e: KeyBindingReleaseEvent[ManiaAction]) -> None:
        """"""
    def PostProcess(self) -> None:
        """"""
    def ReceivePositionalInputAt(self, screenSpacePos: Vector2) -> bool:
        """"""
    def RegisterForDependencyActivation(self, registry: IDependencyActivatorRegistry) -> None:
        """"""
    def RegisterPool(self, initialSize: int, maximumSize: Optional[int] = ...) -> None:
        """
        
        :param initialSize: 
        :param maximumSize: 
        """
    @overload
    def Remove(self, h: DrawableHitObject) -> bool:
        """
        
        :param h: 
        :return: 
        """
    @overload
    def Remove(self, hitObject: HitObject) -> bool:
        """
        
        :param hitObject: 
        :return: 
        """
    def RemoveTransform(self, toRemove: Transform) -> None:
        """"""
    def ScreenSpacePositionAtTime(self, time: float) -> Vector2:
        """
        
        :param time: 
        :return: 
        """
    def Show(self) -> None:
        """"""
    def TimeAtScreenSpacePosition(self, screenSpacePosition: Vector2) -> float:
        """
        
        :param screenSpacePosition: 
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
    @overload
    def __delitem__(self, h: DrawableHitObject) -> bool:
        """
        
        :param h: 
        :return: 
        """
    @overload
    def __delitem__(self, hitObject: HitObject) -> bool:
        """
        
        :param hitObject: 
        :return: 
        """
    NewResult: EventType[Action[DrawableHitObject, JudgementResult]] = ...
    """"""
    OnLoadComplete: EventType[Action[Drawable]] = ...
    """"""
    OnUpdate: EventType[Action[Drawable]] = ...
    """"""
    RevertResult: EventType[Action[JudgementResult]] = ...
    """"""
class EditorStage(Stage, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache, IPooledHitObjectProvider, IPooledSampleProvider):
    """"""
    Definition: Final[StageDefinition] = ...
    """
    
    :return: 
    """
    DisplayJudgements: Final[BindableBool] = ...
    """
    
    :return: 
    """
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    def __init__(self, firstColumnIndex: int, definition: StageDefinition, columnStartAction: ManiaAction):
        """
        
        :param firstColumnIndex: 
        :param definition: 
        :param columnStartAction: 
        """
    @property
    def AcceptsFocus(self) -> bool:
        """"""
    @property
    def AllHitObjects(self) -> IEnumerable[DrawableHitObject]:
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
    def Columns(self) -> Array[Column]:
        """
        
        :return: 
        """
    @property
    def CornerExponent(self) -> float:
        """"""
    @property
    def CornerRadius(self) -> float:
        """"""
    @property
    def Cursor(self) -> GameplayCursorContainer:
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
    def GamefieldToScreenSpace(self) -> Func[Vector2, Vector2]:
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
    def HitObjectContainer(self) -> HitObjectContainer:
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
    def IsNested(self) -> bool:
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
    @property
    def MaskingSmoothness(self) -> float:
        """"""
    @property
    def NestedPlayfields(self) -> IEnumerable[Playfield]:
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
    def ScreenSpaceToGamefield(self) -> Func[Vector2, Vector2]:
        """
        
        :return: 
        """
    @property
    def ScrollingInfo(self) -> IScrollingInfo:
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
    def SkinnableComponentScreenSpaceDrawQuad(self) -> Quad:
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
    @overload
    def Add(self, barLine: BarLine) -> None:
        """
        
        :param barLine: 
        """
    @overload
    def Add(self, h: DrawableHitObject) -> None:
        """
        
        :param h: 
        """
    @overload
    def Add(self, hitObject: HitObject) -> None:
        """
        
        :param hitObject: 
        """
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
    def GetPooledDrawableRepresentation(self, hitObject: HitObject, parent: DrawableHitObject) -> DrawableHitObject:
        """
        
        :param hitObject: 
        :param parent: 
        :return: 
        """
    def GetPooledSample(self, sampleInfo: ISampleInfo) -> PoolableSkinnableSample:
        """
        
        :param sampleInfo: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def Hide(self) -> None:
        """"""
    def Invalidate(self, invalidation: Invalidation = ..., source: InvalidationSource = ...) -> bool:
        """"""
    def PostProcess(self) -> None:
        """"""
    def ReceivePositionalInputAt(self, screenSpacePos: Vector2) -> bool:
        """"""
    def RegisterForDependencyActivation(self, registry: IDependencyActivatorRegistry) -> None:
        """"""
    def RegisterPool(self, initialSize: int, maximumSize: Optional[int] = ...) -> None:
        """
        
        :param initialSize: 
        :param maximumSize: 
        """
    @overload
    def Remove(self, h: DrawableHitObject) -> bool:
        """
        
        :param h: 
        :return: 
        """
    @overload
    def Remove(self, hitObject: HitObject) -> bool:
        """
        
        :param hitObject: 
        :return: 
        """
    def RemoveTransform(self, toRemove: Transform) -> None:
        """"""
    def ScreenSpacePositionAtTime(self, time: float) -> Vector2:
        """
        
        :param time: 
        :return: 
        """
    def Show(self) -> None:
        """"""
    def TimeAtScreenSpacePosition(self, screenSpacePosition: Vector2) -> float:
        """
        
        :param screenSpacePosition: 
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
    @overload
    def __delitem__(self, h: DrawableHitObject) -> bool:
        """
        
        :param h: 
        :return: 
        """
    @overload
    def __delitem__(self, hitObject: HitObject) -> bool:
        """
        
        :param hitObject: 
        :return: 
        """
    NewResult: EventType[Action[DrawableHitObject, JudgementResult]] = ...
    """"""
    OnLoadComplete: EventType[Action[Drawable]] = ...
    """"""
    OnUpdate: EventType[Action[Drawable]] = ...
    """"""
    RevertResult: EventType[Action[JudgementResult]] = ...
    """"""
class HoldNoteCompositionTool(CompositionTool):
    """"""
    Name: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def TooltipText(self) -> LocalisableString:
        """
        
        :return: 
        """
    @TooltipText.setter
    def TooltipText(self, value: LocalisableString) -> None: ...
    def CreateIcon(self) -> Drawable:
        """
        
        :return: 
        """
    def CreatePlacementBlueprint(self) -> PlacementBlueprint:
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
class ManiaBeatSnapGrid(BeatSnapGrid, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
    """"""
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    def __init__(self):
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
    def Masking(self) -> bool:
        """"""
    @property
    def MaskingSmoothness(self) -> float:
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
    def SelectionTimeRange(self) -> Optional[ValueTuple[float, float]]:
        """
        
        :return: 
        """
    @SelectionTimeRange.setter
    def SelectionTimeRange(self, value: Optional[ValueTuple[float, float]]) -> None: ...
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
class ManiaBeatmapVerifier(Object, IBeatmapVerifier):
    """"""
    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Run(self, context: BeatmapVerifierContext) -> IEnumerable[Issue]:
        """
        
        :param context: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class ManiaBlueprintContainer(ComposeBlueprintContainer, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, IKeyBindingHandler, IKeyBindingHandler[PlatformAction], IKeyBindingHandler[GlobalAction], ISourceGeneratedHandleInputCache):
    """"""
    Name: Final[str] = ...
    """"""
    NewCombo: Final[Bindable[TernaryState]] = ...
    """
    
    :return: 
    """
    ProcessCustomClock: Final[bool] = ...
    """"""
    def __init__(self, composer: ManiaHitObjectComposer):
        """
        
        :param composer: 
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
    def Composer(self) -> ManiaHitObjectComposer:
        """
        
        :return: 
        """
    @property
    def CornerExponent(self) -> float:
        """"""
    @property
    def CornerRadius(self) -> float:
        """"""
    @property
    def CurrentHitObjectPlacement(self) -> HitObjectPlacementBlueprint:
        """
        
        :return: 
        """
    @property
    def CurrentPlacement(self) -> PlacementBlueprint:
        """
        
        :return: 
        """
    @property
    def CurrentTool(self) -> CompositionTool:
        """
        
        :return: 
        """
    @CurrentTool.setter
    def CurrentTool(self, value: CompositionTool) -> None: ...
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
    def MainTernaryStates(self) -> Array[Drawable]:
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
    def SampleBankTernaryStates(self) -> Array[SampleBankTernaryButton]:
        """
        
        :return: 
        """
    @property
    def Scale(self) -> Vector2:
        """"""
    @Scale.setter
    def Scale(self, value: Vector2) -> None: ...
    @property
    def ScreenSpaceDrawQuad(self) -> Quad:
        """"""
    @property
    def SelectionBlueprints(self) -> BlueprintContainer.SelectionBlueprintContainer[HitObject]:
        """
        
        :return: 
        """
    @property
    def SelectionHandler(self) -> SelectionHandler[HitObject]:
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
    def CommitIfPlacementActive(self) -> None:
        """"""
    def ComputeMaskingBounds(self) -> RectangleF:
        """"""
    def Contains(self, screenSpacePos: Vector2) -> bool:
        """"""
    def CreateHitObjectBlueprintFor(self, hitObject: HitObject) -> HitObjectSelectionBlueprint:
        """
        
        :param hitObject: 
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
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Hide(self) -> None:
        """"""
    def Invalidate(self, invalidation: Invalidation = ..., source: InvalidationSource = ...) -> bool:
        """"""
    @overload
    def OnPressed(self, e: KeyBindingPressEvent[PlatformAction]) -> bool:
        """"""
    @overload
    def OnPressed(self, e: KeyBindingPressEvent[GlobalAction]) -> bool:
        """"""
    @overload
    def OnReleased(self, e: KeyBindingReleaseEvent[PlatformAction]) -> None:
        """"""
    @overload
    def OnReleased(self, e: KeyBindingReleaseEvent[GlobalAction]) -> None:
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
class ManiaEditorPlayfield(ManiaPlayfield, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache, IPooledHitObjectProvider, IPooledSampleProvider):
    """"""
    DisplayJudgements: Final[BindableBool] = ...
    """
    
    :return: 
    """
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    def __init__(self, stages: List[StageDefinition]):
        """
        
        :param stages: 
        """
    @property
    def AcceptsFocus(self) -> bool:
        """"""
    @property
    def AllHitObjects(self) -> IEnumerable[DrawableHitObject]:
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
    def Cursor(self) -> GameplayCursorContainer:
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
    def GamefieldToScreenSpace(self) -> Func[Vector2, Vector2]:
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
    def HitObjectContainer(self) -> HitObjectContainer:
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
    def IsNested(self) -> bool:
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
    @property
    def MaskingSmoothness(self) -> float:
        """"""
    @property
    def NestedPlayfields(self) -> IEnumerable[Playfield]:
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
    def ScreenSpaceToGamefield(self) -> Func[Vector2, Vector2]:
        """
        
        :return: 
        """
    @property
    def ScrollingInfo(self) -> IScrollingInfo:
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
    def SkinnableComponentScreenSpaceDrawQuad(self) -> Quad:
        """
        
        :return: 
        """
    @property
    def Stages(self) -> IReadOnlyList[Stage]:
        """
        
        :return: 
        """
    @property
    def Time(self) -> FrameTimeInfo:
        """"""
    @property
    def TotalColumns(self) -> int:
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
    @overload
    def Add(self, barLine: BarLine) -> None:
        """
        
        :param barLine: 
        """
    @overload
    def Add(self, h: DrawableHitObject) -> None:
        """
        
        :param h: 
        """
    @overload
    def Add(self, hitObject: HitObject) -> None:
        """
        
        :param hitObject: 
        """
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
    def GetColumn(self, index: int) -> Column:
        """
        
        :param index: 
        :return: 
        """
    def GetColumnByPosition(self, screenSpacePosition: Vector2) -> Column:
        """
        
        :param screenSpacePosition: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetPooledDrawableRepresentation(self, hitObject: HitObject, parent: DrawableHitObject) -> DrawableHitObject:
        """
        
        :param hitObject: 
        :param parent: 
        :return: 
        """
    def GetPooledSample(self, sampleInfo: ISampleInfo) -> PoolableSkinnableSample:
        """
        
        :param sampleInfo: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def Hide(self) -> None:
        """"""
    def Invalidate(self, invalidation: Invalidation = ..., source: InvalidationSource = ...) -> bool:
        """"""
    def PostProcess(self) -> None:
        """"""
    def ReceivePositionalInputAt(self, screenSpacePos: Vector2) -> bool:
        """"""
    def RegisterForDependencyActivation(self, registry: IDependencyActivatorRegistry) -> None:
        """"""
    def RegisterPool(self, initialSize: int, maximumSize: Optional[int] = ...) -> None:
        """
        
        :param initialSize: 
        :param maximumSize: 
        """
    @overload
    def Remove(self, h: DrawableHitObject) -> bool:
        """
        
        :param h: 
        :return: 
        """
    @overload
    def Remove(self, hitObject: HitObject) -> bool:
        """
        
        :param hitObject: 
        :return: 
        """
    def RemoveTransform(self, toRemove: Transform) -> None:
        """"""
    def ScreenSpacePositionAtTime(self, time: float) -> Vector2:
        """
        
        :param time: 
        :return: 
        """
    def Show(self) -> None:
        """"""
    def TimeAtScreenSpacePosition(self, screenSpacePosition: Vector2) -> float:
        """
        
        :param screenSpacePosition: 
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
    @overload
    def __delitem__(self, h: DrawableHitObject) -> bool:
        """
        
        :param h: 
        :return: 
        """
    @overload
    def __delitem__(self, hitObject: HitObject) -> bool:
        """
        
        :param hitObject: 
        :return: 
        """
    NewResult: EventType[Action[DrawableHitObject, JudgementResult]] = ...
    """"""
    OnLoadComplete: EventType[Action[Drawable]] = ...
    """"""
    OnUpdate: EventType[Action[Drawable]] = ...
    """"""
    RevertResult: EventType[Action[JudgementResult]] = ...
    """"""
class ManiaHitObjectComposer(ScrollingHitObjectComposer[ManiaHitObject], IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache, IPlacementHandler):
    """"""
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    Ruleset: Final[Ruleset] = ...
    """
    
    :return: 
    """
    def __init__(self, ruleset: Ruleset):
        """
        
        :param ruleset: 
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
    def BlueprintContainer(self) -> ComposeBlueprintContainer:
        """
        
        :return: 
        """
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
    def CursorInPlacementArea(self) -> bool:
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
    def HitObjects(self) -> IEnumerable[DrawableHitObject]:
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
    def Masking(self) -> bool:
        """"""
    @property
    def MaskingSmoothness(self) -> float:
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
    @property
    def Parent(self) -> CompositeDrawable:
        """"""
    @property
    def Playfield(self) -> Playfield:
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
    def ScrollingInfo(self) -> IScrollingInfo:
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
    def CommitPlacement(self, hitObject: HitObject) -> None:
        """
        
        :param hitObject: 
        """
    def ComputeMaskingBounds(self) -> RectangleF:
        """"""
    def Contains(self, screenSpacePos: Vector2) -> bool:
        """"""
    def ConvertSelectionToString(self) -> str:
        """
        
        :return: 
        """
    def CreateProxy(self) -> Drawable:
        """"""
    def Delete(self, hitObject: HitObject) -> None:
        """
        
        :param hitObject: 
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Expire(self, calculateLifetimeStart: bool = ...) -> None:
        """"""
    def FindSnappedPositionAndTime(self, screenSpacePosition: Vector2) -> SnapResult:
        """
        
        :param screenSpacePosition: 
        :return: 
        """
    def FinishTransforms(self, propagateChildren: bool = ..., targetMember: str = ...) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Hide(self) -> None:
        """"""
    def HidePlacement(self) -> None:
        """"""
    def Invalidate(self, invalidation: Invalidation = ..., source: InvalidationSource = ...) -> bool:
        """"""
    def ReceivePositionalInputAt(self, screenSpacePos: Vector2) -> bool:
        """"""
    def RegisterForDependencyActivation(self, registry: IDependencyActivatorRegistry) -> None:
        """"""
    def RemoveTransform(self, toRemove: Transform) -> None:
        """"""
    def SelectFromTimestamp(self, timestamp: float, objectDescription: str) -> None:
        """
        
        :param timestamp: 
        :param objectDescription: 
        """
    def SetLastTool(self) -> None:
        """"""
    def SetSelectTool(self) -> None:
        """"""
    def Show(self) -> None:
        """"""
    def ShowPlacement(self, hitObject: HitObject) -> None:
        """
        
        :param hitObject: 
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
    def WithEffect(self, effect: IEffect[T], initializationAction: Action[T] = ...) -> T:
        """"""
    def __contains__(self, screenSpacePos: Vector2) -> bool:
        """"""
    OnLoadComplete: EventType[Action[Drawable]] = ...
    """"""
    OnUpdate: EventType[Action[Drawable]] = ...
    """"""
class ManiaSelectionHandler(EditorSelectionHandler, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, IHasContextMenu, ITransformable, IDrawable, IKeyBindingHandler, IKeyBindingHandler[PlatformAction], IKeyBindingHandler[GlobalAction], ISourceGeneratedHandleInputCache):
    """"""
    AutoSelectionBankEnabled: Final[Bindable[bool]] = ...
    """
    
    :return: 
    """
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    SelectedItems: Final[BindableList[HitObject]] = ...
    """
    
    :return: 
    """
    SelectionAdditionBankStates: Final[Dictionary[str, Bindable[TernaryState]]] = ...
    """
    
    :return: 
    """
    SelectionBankStates: Final[Dictionary[str, Bindable[TernaryState]]] = ...
    """
    
    :return: 
    """
    SelectionNewComboState: Final[Bindable[TernaryState]] = ...
    """
    
    :return: 
    """
    SelectionSampleStates: Final[Dictionary[str, Bindable[TernaryState]]] = ...
    """
    
    :return: 
    """
    def __init__(self):
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
    def ContextMenuItems(self) -> Array[MenuItem]:
        """"""
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
    def Masking(self) -> bool:
        """"""
    @property
    def MaskingSmoothness(self) -> float:
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
    def RightClickAlwaysQuickDeletes(self) -> bool:
        """
        
        :return: 
        """
    @RightClickAlwaysQuickDeletes.setter
    def RightClickAlwaysQuickDeletes(self, value: bool) -> None: ...
    @property
    def Rotation(self) -> float:
        """"""
    @Rotation.setter
    def Rotation(self, value: float) -> None: ...
    @property
    def RotationHandler(self) -> SelectionRotationHandler:
        """
        
        :return: 
        """
    @property
    def Scale(self) -> Vector2:
        """"""
    @Scale.setter
    def Scale(self, value: Vector2) -> None: ...
    @property
    def ScaleHandler(self) -> SelectionScaleHandler:
        """
        
        :return: 
        """
    @property
    def ScreenSpaceDrawQuad(self) -> Quad:
        """"""
    @property
    def SelectedBlueprints(self) -> IReadOnlyList[SelectionBlueprint[HitObject]]:
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
    def AddHitSample(self, sampleName: str) -> None:
        """
        
        :param sampleName: 
        """
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
    def CreateRotationHandler(self) -> SelectionRotationHandler:
        """
        
        :return: 
        """
    def CreateScaleHandler(self) -> SelectionScaleHandler:
        """
        
        :return: 
        """
    def CreateSelectionBox(self) -> SelectionBox:
        """
        
        :return: 
        """
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
    def HandleFlip(self, direction: Direction, flipOverOrigin: bool) -> bool:
        """
        
        :param direction: 
        :param flipOverOrigin: 
        :return: 
        """
    def HandleMovement(self, moveEvent: MoveSelectionEvent[HitObject]) -> bool:
        """
        
        :param moveEvent: 
        :return: 
        """
    def HandleReverse(self) -> bool:
        """
        
        :return: 
        """
    def HandleRotation(self, angle: float) -> bool:
        """
        
        :param angle: 
        :return: 
        """
    def Hide(self) -> None:
        """"""
    def Invalidate(self, invalidation: Invalidation = ..., source: InvalidationSource = ...) -> bool:
        """"""
    @overload
    def OnPressed(self, e: KeyBindingPressEvent[PlatformAction]) -> bool:
        """"""
    @overload
    def OnPressed(self, e: KeyBindingPressEvent[GlobalAction]) -> bool:
        """"""
    @overload
    def OnReleased(self, e: KeyBindingReleaseEvent[PlatformAction]) -> None:
        """"""
    @overload
    def OnReleased(self, e: KeyBindingReleaseEvent[GlobalAction]) -> None:
        """"""
    def ReceivePositionalInputAt(self, screenSpacePos: Vector2) -> bool:
        """"""
    def RegisterForDependencyActivation(self, registry: IDependencyActivatorRegistry) -> None:
        """"""
    def RemoveHitSample(self, sampleName: str) -> None:
        """
        
        :param sampleName: 
        """
    def RemoveTransform(self, toRemove: Transform) -> None:
        """"""
    def SetNewCombo(self, state: bool) -> None:
        """
        
        :param state: 
        """
    def SetSampleAdditionBank(self, bankName: str) -> None:
        """
        
        :param bankName: 
        """
    def SetSampleBank(self, bankName: str) -> None:
        """
        
        :param bankName: 
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
class NoteCompositionTool(CompositionTool):
    """"""
    Name: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def TooltipText(self) -> LocalisableString:
        """
        
        :return: 
        """
    @TooltipText.setter
    def TooltipText(self, value: LocalisableString) -> None: ...
    def CreateIcon(self) -> Drawable:
        """
        
        :return: 
        """
    def CreatePlacementBlueprint(self) -> PlacementBlueprint:
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