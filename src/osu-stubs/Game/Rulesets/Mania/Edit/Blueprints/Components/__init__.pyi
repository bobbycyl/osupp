from System import Action
from System.Collections.Generic import IEnumerable
from System import IDisposable
from System import Type
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
from osu.Framework.Input.Events import UIEvent
from osu.Framework.Input import ISourceGeneratedHandleInputCache
from osu.Framework.Layout import InvalidationSource
from osu.Framework.Timing import FrameTimeInfo
from osu.Framework.Timing import IFrameBasedClock
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
class EditBodyPiece(CompositeDrawable, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
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
class EditHoldNoteEndPiece(CompositeDrawable, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
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
    def DragEnded(self) -> Action:
        """
        
        :return: 
        """
    @DragEnded.setter
    def DragEnded(self, value: Action) -> None: ...
    @property
    def DragStarted(self) -> Action:
        """
        
        :return: 
        """
    @DragStarted.setter
    def DragStarted(self, value: Action) -> None: ...
    @property
    def Dragging(self) -> Action[Vector2]:
        """
        
        :return: 
        """
    @Dragging.setter
    def Dragging(self, value: Action[Vector2]) -> None: ...
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
class EditNotePiece(CompositeDrawable, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
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