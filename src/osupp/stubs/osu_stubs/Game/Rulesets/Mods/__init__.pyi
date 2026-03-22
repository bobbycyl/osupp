from Newtonsoft.Json import JsonReader
from Newtonsoft.Json import JsonSerializer
from Newtonsoft.Json import JsonWriter
from Realms import DynamicObjectApi
from Realms import IRealmAccessor
from Realms import IRealmObject
from Realms import IRealmObjectBase
from Realms import ISettableManagedAccessor
from Realms import Realm
from Realms import RealmObject
from Realms.Schema import ObjectSchema
from Realms.Weaving import IRealmObjectHelper
from System import Action
from System import Array
from System.Collections.Generic import ICollection
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IReadOnlyCollection
from System.Collections.Generic import IReadOnlyList
from System.Collections import IEnumerable
from System.ComponentModel import INotifyPropertyChanged
from System.ComponentModel import PropertyChangedEventHandler
from System import Enum
from System import Func
from System import Guid
from System import IDisposable
from System import IEquatable
from System import IFormatProvider
from System import IFormattable
from System import Int32
from System import Object
from System import Predicate
from System.Reflection import IReflectableType
from System.Reflection import TypeInfo
from System import Single
from System import Type
from System import ValueTuple
from __future__ import annotations
from abc import ABC
from osu.Framework.Allocation import IDependencyActivatorRegistry
from osu.Framework.Allocation import IDependencyInjectionCandidate
from osu.Framework.Allocation import IReadOnlyDependencyContainer
from osu.Framework.Allocation import ISourceGeneratedDependencyActivator
from osu.Framework.Allocation import ISourceGeneratedLongRunningLoadCache
from osu.Framework.Audio import AdjustableProperty
from osu.Framework.Audio import IAdjustableAudioComponent
from osu.Framework.Audio import IAggregateAudioAdjustment
from osu.Framework.Bindables import Bindable
from osu.Framework.Bindables import BindableBool
from osu.Framework.Bindables import BindableFloat
from osu.Framework.Bindables import BindableInt
from osu.Framework.Bindables import BindableNumber
from osu.Framework.Bindables import IBindable
from osu.Framework.Bindables import IBindableNumber
from osu.Framework.Bindables import ICanBeDisabled
from osu.Framework.Bindables import IHasDefaultValue
from osu.Framework.Bindables import IHasDescription
from osu.Framework.Bindables import IParseable
from osu.Framework.Bindables import IUnbindable
from osu.Framework.Bindables import LeasedBindable
from osu.Framework.Bindables import ValueChangedEvent
from osu.Framework.Graphics import Anchor
from osu.Framework.Graphics import Axes
from osu.Framework.Graphics import BlendingParameters
from osu.Framework.Graphics.Colour import ColourInfo
from osu.Framework.Graphics.Containers import CompositeDrawable
from osu.Framework.Graphics.Containers.Container import Enumerator
from osu.Framework.Graphics.Containers import IConditionalFilterable
from osu.Framework.Graphics.Containers import IContainer
from osu.Framework.Graphics.Containers import IContainerCollection
from osu.Framework.Graphics.Containers import IContainerEnumerable
from osu.Framework.Graphics.Containers import IFilterable
from osu.Framework.Graphics.Containers import IHasFilterTerms
from osu.Framework.Graphics.Cursor import IHasTooltip
from osu.Framework.Graphics.Cursor import ITooltipContentProvider
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
from osu.Framework.Graphics import RotationDirection
from osu.Framework.Graphics.Sprites import IconUsage
from osu.Framework.Graphics.Transforms import ITransformable
from osu.Framework.Graphics.Transforms import Transform
from osu.Framework.Graphics.UserInterface import IHasCurrentValue
from osu.Framework.IO.Serialization import ISerializableBindable
from osu.Framework.Input.Events import UIEvent
from osu.Framework.Input import ISourceGeneratedHandleInputCache
from osu.Framework.Layout import InvalidationSource
from osu.Framework.Localisation import LocalisableString
from osu.Framework.Timing import FrameTimeInfo
from osu.Framework.Timing import IFrameBasedClock
from osu.Game.Beatmaps import BeatmapDifficulty
from osu.Game.Beatmaps import IBeatmap
from osu.Game.Beatmaps import IBeatmapConverter
from osu.Game.Beatmaps import IBeatmapDifficultyInfo
from osu.Game.Beatmaps import IBeatmapProcessor
from osu.Game.Configuration import OsuConfigManager
from osu.Game.Database import IHasGuidPrimaryKey
from osu.Game.Database import IHasOnlineID
from osu.Game.Database import ISoftDelete
from osu.Game.Graphics.Containers import BeatSyncedContainer
from osu.Game.Graphics.UserInterface import RoundedSliderBar
from osu.Game.Overlays.Settings import ISettingsItem
from osu.Game.Overlays.Settings import SettingsItem
from osu.Game.Replays import Replay
from osu.Game.Rulesets.Mods.ModAccuracyChallenge import AccuracyMode
from osu.Game.Rulesets.Objects.Drawables import DrawableHitObject
from osu.Game.Rulesets.Objects import HitObject
from osu.Game.Rulesets import RulesetInfo
from osu.Game.Rulesets.Scoring import HealthProcessor
from osu.Game.Rulesets.Scoring import ScoreProcessor
from osu.Game.Rulesets.UI import DrawableRuleset
from osu.Game.Rulesets.UI import Playfield
from osu.Game.Scoring import Score
from osu.Game.Scoring import ScoreRank
from osu.Game.Screens.Play import HUDOverlay
from osu.Game.Screens.Play import Player
from osu.Game.Users import CountryCode
from osu.Game.Users import IUser
from osu.Game.Utils import IDeepCloneable
from osuTK.Graphics import Color4
from osuTK import Vector2
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Iterator
from typing import Optional
from typing import TypeVar
from typing import overload
T = TypeVar("T")
TObject = TypeVar("TObject")
class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...
class DifficultyAdjustSettingsControl(SettingsItem[Single], ICollection[Drawable], IEnumerable[Drawable], IReadOnlyCollection[Drawable], IReadOnlyList[Drawable], IEnumerable, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, IConditionalFilterable, IContainer, IContainerCollection[Drawable], IContainerEnumerable[Drawable], IFilterable, IHasFilterTerms, IHasTooltip, ITooltipContentProvider, ITransformable, IHasCurrentValue[Single], IDrawable, ISourceGeneratedHandleInputCache, ISettingsItem):
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
    def CanBeShown(self) -> BindableBool:
        """"""
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
    def ClassicDefault(self) -> Optional[float]:
        """
        
        :return: 
        """
    @ClassicDefault.setter
    def ClassicDefault(self, value: Optional[float]) -> None: ...
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
    def Current(self) -> Bindable[Optional[float]]:
        """"""
    @Current.setter
    def Current(self, value: Bindable[Optional[float]]) -> None: ...
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
    def FilterTerms(self) -> IEnumerable[LocalisableString]:
        """"""
    @property
    def FilteringActive(self) -> bool:
        """"""
    @FilteringActive.setter
    def FilteringActive(self, value: bool) -> None: ...
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
    def HasClassicDefault(self) -> bool:
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
    def Keywords(self) -> IEnumerable[str]:
        """
        
        :return: 
        """
    @Keywords.setter
    def Keywords(self, value: IEnumerable[str]) -> None: ...
    @property
    def LabelText(self) -> LocalisableString:
        """
        
        :return: 
        """
    @LabelText.setter
    def LabelText(self, value: LocalisableString) -> None: ...
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
    def MatchingFilter(self) -> bool:
        """"""
    @MatchingFilter.setter
    def MatchingFilter(self, value: bool) -> None: ...
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
    def SettingSourceObject(self) -> object:
        """
        
        :return: 
        """
    @property
    def Shear(self) -> Vector2:
        """"""
    @Shear.setter
    def Shear(self, value: Vector2) -> None: ...
    @property
    def ShowsDefaultIndicator(self) -> bool:
        """
        
        :return: 
        """
    @ShowsDefaultIndicator.setter
    def ShowsDefaultIndicator(self, value: bool) -> None: ...
    @property
    def Size(self) -> Vector2:
        """"""
    @Size.setter
    def Size(self, value: Vector2) -> None: ...
    @property
    def Time(self) -> FrameTimeInfo:
        """"""
    @property
    def TooltipText(self) -> LocalisableString:
        """"""
    @TooltipText.setter
    def TooltipText(self, value: LocalisableString) -> None: ...
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
    def Add(self, drawable: Drawable) -> None:
        """"""
    def AddRange(self, range: IEnumerable[Drawable]) -> None:
        """"""
    def AddTransform(self, transform: Transform, customTransformID: Optional[int] = ...) -> None:
        """"""
    def ApplyClassicDefault(self) -> None:
        """"""
    def ApplyDefault(self) -> None:
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
    def ClearNoticeText(self) -> None:
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
    def SetNoticeText(self, text: LocalisableString, isWarning: bool = ...) -> None:
        """
        
        :param text: 
        :param isWarning: 
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
    SettingChanged: EventType[Action] = ...
    """"""
class DifficultyBindable(Bindable[Single], IFormattable, IBindable, IBindable[Single], ICanBeDisabled, IHasDefaultValue, IHasDescription, IParseable, IUnbindable, ISerializableBindable):
    """"""
    ExtendedLimits: Final[BindableBool] = ...
    """
    
    :return: 
    """
    ReadCurrentFromDifficulty: Final[Func[IBeatmapDifficultyInfo, float]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, defaultValue: Optional[float] = ...):
        """
        
        :param defaultValue: 
        """
    @property
    def BindTarget(self) -> IBindable[Optional[float]]:
        """"""
    @BindTarget.setter
    def BindTarget(self, value: IBindable[Optional[float]]) -> None: ...
    @property
    def Default(self) -> Optional[float]:
        """"""
    @Default.setter
    def Default(self, value: Optional[float]) -> None: ...
    @property
    def Description(self) -> str:
        """"""
    @Description.setter
    def Description(self, value: str) -> None: ...
    @property
    def Disabled(self) -> bool:
        """"""
    @Disabled.setter
    def Disabled(self, value: bool) -> None: ...
    @property
    def ExtendedMaxValue(self) -> Optional[float]:
        """
        
        :return: 
        """
    @ExtendedMaxValue.setter
    def ExtendedMaxValue(self, value: Optional[float]) -> None: ...
    @property
    def ExtendedMinValue(self) -> Optional[float]:
        """
        
        :return: 
        """
    @ExtendedMinValue.setter
    def ExtendedMinValue(self, value: Optional[float]) -> None: ...
    @property
    def IsDefault(self) -> bool:
        """"""
    @property
    def MaxValue(self) -> float:
        """
        
        :return: 
        """
    @MaxValue.setter
    def MaxValue(self, value: float) -> None: ...
    @property
    def MinValue(self) -> float:
        """
        
        :return: 
        """
    @MinValue.setter
    def MinValue(self, value: float) -> None: ...
    @property
    def Precision(self) -> float:
        """
        
        :return: 
        """
    @Precision.setter
    def Precision(self, value: float) -> None: ...
    @property
    def Value(self) -> Optional[float]:
        """"""
    @Value.setter
    def Value(self, value: Optional[float]) -> None: ...
    def BeginLease(self, revertValueOnReturn: bool) -> LeasedBindable[Optional[float]]:
        """"""
    def BindDisabledChanged(self, onChange: Action[bool], runOnceImmediately: bool = ...) -> None:
        """"""
    @overload
    def BindTo(self, them: Bindable[Optional[float]]) -> None:
        """"""
    @overload
    def BindTo(self, them: IBindable) -> None:
        """"""
    @overload
    def BindTo(self, them: IBindable[Optional[float]]) -> None:
        """"""
    def BindValueChanged(self, onChange: Action[ValueChangedEvent[Optional[float]]], runOnceImmediately: bool = ...) -> None:
        """"""
    def CopyTo(self, them: Bindable[Optional[float]]) -> None:
        """"""
    def DeserializeFrom(self, reader: JsonReader, serializer: JsonSerializer) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBoundCopy(self) -> Bindable[Optional[float]]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUnboundCopy(self) -> Bindable[Optional[float]]:
        """"""
    def Parse(self, input: object, provider: IFormatProvider) -> None:
        """"""
    def SerializeTo(self, writer: JsonWriter, serializer: JsonSerializer) -> None:
        """"""
    def SetDefault(self) -> None:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str:
        """"""
    def TriggerChange(self) -> None:
        """"""
    def UnbindAll(self) -> None:
        """"""
    def UnbindBindings(self) -> None:
        """"""
    def UnbindEvents(self) -> None:
        """"""
    def UnbindFrom(self, them: IUnbindable) -> None:
        """"""
    DefaultChanged: EventType[Action[ValueChangedEvent[Optional[float]]]] = ...
    """"""
    DisabledChanged: EventType[Action[bool]] = ...
    """"""
    ValueChanged: EventType[Action[ValueChangedEvent[Optional[float]]]] = ...
    """"""
class HiddenComboSlider(RoundedSliderBar[Int32], ICollection[Drawable], IEnumerable[Drawable], IReadOnlyCollection[Drawable], IReadOnlyList[Drawable], IEnumerable, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, IContainer, IContainerCollection[Drawable], IContainerEnumerable[Drawable], IHasTooltip, ITooltipContentProvider, ITransformable, IHasCurrentValue[Int32], IDrawable, ISourceGeneratedHandleInputCache):
    """"""
    KeyboardStep: Final[float] = ...
    """"""
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    RangePadding: Final[float] = ...
    """"""
    TransferValueOnCommit: Final[bool] = ...
    """"""
    def __init__(self):
        """"""
    @property
    def AccentColour(self) -> Color4:
        """
        
        :return: 
        """
    @AccentColour.setter
    def AccentColour(self, value: Color4) -> None: ...
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
    def BackgroundColour(self) -> Color4:
        """
        
        :return: 
        """
    @BackgroundColour.setter
    def BackgroundColour(self, value: Color4) -> None: ...
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
    def Current(self) -> Bindable[int]:
        """"""
    @Current.setter
    def Current(self, value: Bindable[int]) -> None: ...
    @property
    def Dependencies(self) -> IReadOnlyDependencyContainer:
        """"""
    @property
    def Depth(self) -> float:
        """"""
    @Depth.setter
    def Depth(self, value: float) -> None: ...
    @property
    def DisplayAsPercentage(self) -> bool:
        """
        
        :return: 
        """
    @DisplayAsPercentage.setter
    def DisplayAsPercentage(self, value: bool) -> None: ...
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
    def PlaySamplesOnAdjust(self) -> bool:
        """
        
        :return: 
        """
    @PlaySamplesOnAdjust.setter
    def PlaySamplesOnAdjust(self, value: bool) -> None: ...
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
    def ResetToDefault(self) -> Action:
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
    def TooltipText(self) -> LocalisableString:
        """"""
    @property
    def TransformStartTime(self) -> float:
        """"""
    @property
    def Transforms(self) -> IEnumerable[Transform]:
        """"""
    @property
    def UsableWidth(self) -> float:
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
    def GetDisplayableValue(self, value: int) -> LocalisableString:
        """
        
        :param value: 
        :return: 
        """
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
    OnLoadComplete: EventType[Action[Drawable]] = ...
    """"""
    OnUpdate: EventType[Action[Drawable]] = ...
    """"""
class IApplicableAfterBeatmapConversion(IApplicableMod):
    """"""
    def ApplyToBeatmap(self, beatmap: IBeatmap) -> None:
        """
        
        :param beatmap: 
        """
class IApplicableFailOverride(IApplicableMod):
    """"""
    @property
    def RestartOnFail(self) -> bool:
        """
        
        :return: 
        """
    def PerformFail(self) -> bool:
        """
        
        :return: 
        """
class IApplicableHealthProcessor:
    """"""
    def CreateHealthProcessor(self, drainStartTime: float) -> HealthProcessor:
        """
        
        :param drainStartTime: 
        :return: 
        """
class IApplicableMod:
    """"""
class IApplicableToAudio(IApplicableMod, IApplicableToSample, IApplicableToTrack):
    """"""
    def ApplyToSample(self, sample: IAdjustableAudioComponent) -> None:
        """
        
        :param sample: 
        """
    def ApplyToTrack(self, track: IAdjustableAudioComponent) -> None:
        """
        
        :param track: 
        """
class IApplicableToBeatmap(IApplicableMod):
    """"""
    def ApplyToBeatmap(self, beatmap: IBeatmap) -> None:
        """
        
        :param beatmap: 
        """
class IApplicableToBeatmapConverter(IApplicableMod):
    """"""
    def ApplyToBeatmapConverter(self, beatmapConverter: IBeatmapConverter) -> None:
        """
        
        :param beatmapConverter: 
        """
class IApplicableToBeatmapProcessor(IApplicableMod):
    """"""
    def ApplyToBeatmapProcessor(self, beatmapProcessor: IBeatmapProcessor) -> None:
        """
        
        :param beatmapProcessor: 
        """
class IApplicableToDifficulty(IApplicableMod):
    """"""
    def ApplyToDifficulty(self, difficulty: BeatmapDifficulty) -> None:
        """
        
        :param difficulty: 
        """
class IApplicableToDrawableHitObject(IApplicableMod):
    """"""
    def ApplyToDrawableHitObject(self, drawable: DrawableHitObject) -> None:
        """
        
        :param drawable: 
        """
class IApplicableToDrawableRuleset(Generic[TObject], IApplicableMod):
    """"""
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[TObject]) -> None:
        """
        
        :param drawableRuleset: 
        """
class IApplicableToHUD(IApplicableMod):
    """"""
    def ApplyToHUD(self, overlay: HUDOverlay) -> None:
        """
        
        :param overlay: 
        """
class IApplicableToHealthProcessor(IApplicableMod):
    """"""
    def ApplyToHealthProcessor(self, healthProcessor: HealthProcessor) -> None:
        """
        
        :param healthProcessor: 
        """
class IApplicableToHitObject(IApplicableMod):
    """"""
    def ApplyToHitObject(self, hitObject: HitObject) -> None:
        """
        
        :param hitObject: 
        """
class IApplicableToPlayer(IApplicableMod):
    """"""
    def ApplyToPlayer(self, player: Player) -> None:
        """
        
        :param player: 
        """
class IApplicableToRate(IApplicableMod, IApplicableToAudio, IApplicableToSample, IApplicableToTrack):
    """"""
    def ApplyToRate(self, time: float, rate: float = ...) -> float:
        """
        
        :param time: 
        :param rate: 
        :return: 
        """
    def ApplyToSample(self, sample: IAdjustableAudioComponent) -> None:
        """
        
        :param sample: 
        """
    def ApplyToTrack(self, track: IAdjustableAudioComponent) -> None:
        """
        
        :param track: 
        """
class IApplicableToSample(IApplicableMod):
    """"""
    def ApplyToSample(self, sample: IAdjustableAudioComponent) -> None:
        """
        
        :param sample: 
        """
class IApplicableToScoreProcessor(IApplicableMod):
    """"""
    def AdjustRank(self, rank: ScoreRank, accuracy: float) -> ScoreRank:
        """
        
        :param rank: 
        :param accuracy: 
        :return: 
        """
    def ApplyToScoreProcessor(self, scoreProcessor: ScoreProcessor) -> None:
        """
        
        :param scoreProcessor: 
        """
class IApplicableToTrack(IApplicableMod):
    """"""
    def ApplyToTrack(self, track: IAdjustableAudioComponent) -> None:
        """
        
        :param track: 
        """
class ICreateReplayData:
    """"""
    def CreateReplayData(self, beatmap: IBeatmap, mods: IReadOnlyList[Mod]) -> ModReplayData:
        """
        
        :param beatmap: 
        :param mods: 
        :return: 
        """
class IHasNoTimedInputs:
    """"""
class IHasSeed:
    """"""
    @property
    def Seed(self) -> Bindable[Optional[int]]:
        """
        
        :return: 
        """
class IMod(IEquatable[IMod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def Equals(self, other: IMod) -> bool:
        """"""
class IReadFromConfig:
    """"""
    def ReadFromConfig(self, config: OsuConfigManager) -> None:
        """
        
        :param config: 
        """
class IUpdatableByPlayfield(IApplicableMod):
    """"""
    def Update(self, playfield: Playfield) -> None:
        """
        
        :param playfield: 
        """
class MetronomeBeat(BeatSyncedContainer, ICollection[Drawable], IEnumerable[Drawable], IReadOnlyCollection[Drawable], IReadOnlyList[Drawable], IEnumerable, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, IAdjustableAudioComponent, IAggregateAudioAdjustment, IContainer, IContainerCollection[Drawable], IContainerEnumerable[Drawable], ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
    """"""
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    def __init__(self, firstHitTime: float):
        """
        
        :param firstHitTime: 
        """
    @property
    def AcceptsFocus(self) -> bool:
        """"""
    @property
    def AggregateBalance(self) -> IBindable[float]:
        """"""
    @property
    def AggregateFrequency(self) -> IBindable[float]:
        """"""
    @property
    def AggregateTempo(self) -> IBindable[float]:
        """"""
    @property
    def AggregateVolume(self) -> IBindable[float]:
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
    def Balance(self) -> BindableNumber[float]:
        """"""
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
    def Divisor(self) -> int:
        """
        
        :return: 
        """
    @Divisor.setter
    def Divisor(self, value: int) -> None: ...
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
    def Frequency(self) -> BindableNumber[float]:
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
    def MinimumBeatLength(self) -> float:
        """
        
        :return: 
        """
    @MinimumBeatLength.setter
    def MinimumBeatLength(self, value: float) -> None: ...
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
    def Tempo(self) -> BindableNumber[float]:
        """"""
    @property
    def Time(self) -> FrameTimeInfo:
        """"""
    @property
    def TimeSinceLastBeat(self) -> float:
        """
        
        :return: 
        """
    @property
    def TimeUntilNextBeat(self) -> float:
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
    def Volume(self) -> BindableNumber[float]:
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
    def Add(self, drawable: Drawable) -> None:
        """"""
    def AddAdjustment(self, type: AdjustableProperty, adjustBindable: IBindable[float]) -> None:
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
    def BindAdjustments(self, component: IAggregateAudioAdjustment) -> None:
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
    def RemoveAdjustment(self, type: AdjustableProperty, adjustBindable: IBindable[float]) -> None:
        """"""
    def RemoveAll(self, pred: Predicate[Drawable], disposeImmediately: bool) -> int:
        """"""
    def RemoveAllAdjustments(self, type: AdjustableProperty) -> None:
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
    def UnbindAdjustments(self, component: IAggregateAudioAdjustment) -> None:
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
class Mod(ABC, Object, IEquatable[IMod], IEquatable[Mod], IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModAccuracyChallenge(ModFailCondition, IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToHealthProcessor, IApplicableToScoreProcessor, IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def AccuracyJudgeMode(self) -> Bindable[ModAccuracyChallenge.AccuracyMode]:
        """
        
        :return: 
        """
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def MinimumAccuracy(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Restart(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def RestartOnFail(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def AdjustRank(self, rank: ScoreRank, accuracy: float) -> ScoreRank:
        """
        
        :param rank: 
        :param accuracy: 
        :return: 
        """
    def ApplyToHealthProcessor(self, healthProcessor: HealthProcessor) -> None:
        """
        
        :param healthProcessor: 
        """
    def ApplyToScoreProcessor(self, scoreProcessor: ScoreProcessor) -> None:
        """
        
        :param scoreProcessor: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PerformFail(self) -> bool:
        """
        
        :return: 
        """
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    class AccuracyMode(Enum):
        """"""
        MaximumAchievable: AccuracyMode = ...
        """"""
        Standard: AccuracyMode = ...
        """"""
class ModAdaptiveSpeed(Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToAudio, IApplicableToBeatmap, IApplicableToDrawableHitObject, IApplicableToRate, IApplicableToSample, IApplicableToTrack, IMod, IUpdatableByPlayfield, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AdjustPitch(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def InitialRate(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def SpeedChange(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToBeatmap(self, beatmap: IBeatmap) -> None:
        """
        
        :param beatmap: 
        """
    def ApplyToDrawableHitObject(self, drawable: DrawableHitObject) -> None:
        """
        
        :param drawable: 
        """
    def ApplyToRate(self, time: float, rate: float = ...) -> float:
        """
        
        :param time: 
        :param rate: 
        :return: 
        """
    def ApplyToSample(self, sample: IAdjustableAudioComponent) -> None:
        """
        
        :param sample: 
        """
    def ApplyToTrack(self, track: IAdjustableAudioComponent) -> None:
        """
        
        :param track: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, playfield: Playfield) -> None:
        """
        
        :param playfield: 
        """
class ModAutoplay(ABC, Mod, IEquatable[IMod], IEquatable[Mod], ICreateReplayData, IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def CreateReplayData(self, beatmap: IBeatmap, mods: IReadOnlyList[Mod]) -> ModReplayData:
        """
        
        :param beatmap: 
        :param mods: 
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModBarrelRoll(ABC, Generic[TObject], Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableRuleset[TObject], IMod, IUpdatableByPlayfield, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def Direction(self) -> Bindable[RotationDirection]:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def SpinSpeed(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[TObject]) -> None:
        """
        
        :param drawableRuleset: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, playfield: Playfield) -> None:
        """
        
        :param playfield: 
        """
class ModCinema(ABC, Generic[T], ModCinema, IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToDrawableRuleset[T], IApplicableToHUD, IApplicableToPlayer, ICreateReplayData, IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RestartOnFail(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[T]) -> None:
        """
        
        :param drawableRuleset: 
        """
    def ApplyToHUD(self, overlay: HUDOverlay) -> None:
        """
        
        :param overlay: 
        """
    def ApplyToPlayer(self, player: Player) -> None:
        """
        
        :param player: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def CreateReplayData(self, beatmap: IBeatmap, mods: IReadOnlyList[Mod]) -> ModReplayData:
        """
        
        :param beatmap: 
        :param mods: 
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PerformFail(self) -> bool:
        """
        
        :return: 
        """
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModCinema(ModAutoplay, IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToHUD, IApplicableToPlayer, ICreateReplayData, IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RestartOnFail(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToHUD(self, overlay: HUDOverlay) -> None:
        """
        
        :param overlay: 
        """
    def ApplyToPlayer(self, player: Player) -> None:
        """
        
        :param player: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def CreateReplayData(self, beatmap: IBeatmap, mods: IReadOnlyList[Mod]) -> ModReplayData:
        """
        
        :param beatmap: 
        :param mods: 
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PerformFail(self) -> bool:
        """
        
        :return: 
        """
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModClassic(ABC, Mod, IEquatable[IMod], IEquatable[Mod], IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModCreatedUser(Object, IEquatable[IUser], IHasOnlineID[Int32], IUser):
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
    def Equals(self, other: IUser) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class ModDaycore(ABC, ModRateAdjust, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToAudio, IApplicableToRate, IApplicableToSample, IApplicableToTrack, IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def SpeedChange(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToRate(self, time: float, rate: float) -> float:
        """
        
        :param time: 
        :param rate: 
        :return: 
        """
    def ApplyToSample(self, sample: IAdjustableAudioComponent) -> None:
        """
        
        :param sample: 
        """
    def ApplyToTrack(self, track: IAdjustableAudioComponent) -> None:
        """
        
        :param track: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModDifficultyAdjust(ABC, Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDifficulty, IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def DrainRate(self) -> DifficultyBindable:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def ExtendedLimits(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def OverallDifficulty(self) -> DifficultyBindable:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToDifficulty(self, difficulty: BeatmapDifficulty) -> None:
        """
        
        :param difficulty: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModDoubleTime(ABC, ModRateAdjust, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToAudio, IApplicableToRate, IApplicableToSample, IApplicableToTrack, IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AdjustPitch(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def SpeedChange(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToRate(self, time: float, rate: float) -> float:
        """
        
        :param time: 
        :param rate: 
        :return: 
        """
    def ApplyToSample(self, sample: IAdjustableAudioComponent) -> None:
        """
        
        :param sample: 
        """
    def ApplyToTrack(self, track: IAdjustableAudioComponent) -> None:
        """
        
        :param track: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModEasy(ABC, Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDifficulty, IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToDifficulty(self, difficulty: BeatmapDifficulty) -> None:
        """
        
        :param difficulty: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModEasyWithExtraLives(ABC, ModEasy, IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToDifficulty, IApplicableToHealthProcessor, IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RestartOnFail(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Retries(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToDifficulty(self, difficulty: BeatmapDifficulty) -> None:
        """
        
        :param difficulty: 
        """
    def ApplyToHealthProcessor(self, healthProcessor: HealthProcessor) -> None:
        """
        
        :param healthProcessor: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PerformFail(self) -> bool:
        """
        
        :return: 
        """
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModExtensions(ABC, Object):
    """"""
    @classmethod
    def AsOrdered(cls, mods: IEnumerable[Mod]) -> IEnumerable[Mod]:
        """
        
        :param mods: 
        :return: 
        """
    @classmethod
    def CreateScoreFromReplayData(cls, mod: ICreateReplayData, beatmap: IBeatmap, mods: IReadOnlyList[Mod]) -> Score:
        """
        
        :param mod: 
        :param beatmap: 
        :param mods: 
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
class ModFailCondition(ABC, Mod, IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToHealthProcessor, IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Restart(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def RestartOnFail(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToHealthProcessor(self, healthProcessor: HealthProcessor) -> None:
        """
        
        :param healthProcessor: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PerformFail(self) -> bool:
        """
        
        :return: 
        """
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModFlashlight(ABC, Mod, IEquatable[IMod], IEquatable[Mod], IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ComboBasedSize(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def DefaultFlashlightSize(self) -> float:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def SizeMultiplier(self) -> BindableFloat:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModFlashlight(ABC, Generic[T], ModFlashlight, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableRuleset[T], IApplicableToScoreProcessor, IMod, IDeepCloneable[Mod]):
    """"""
    FLASHLIGHT_FADE_DURATION: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ComboBasedSize(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def DefaultFlashlightSize(self) -> float:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def SizeMultiplier(self) -> BindableFloat:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def AdjustRank(self, rank: ScoreRank, accuracy: float) -> ScoreRank:
        """
        
        :param rank: 
        :param accuracy: 
        :return: 
        """
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[T]) -> None:
        """
        
        :param drawableRuleset: 
        """
    def ApplyToScoreProcessor(self, scoreProcessor: ScoreProcessor) -> None:
        """
        
        :param scoreProcessor: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    class Flashlight(ABC, Generic[T], Drawable, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
        """"""
        Combo: Final[BindableInt] = ...
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
        def FlashlightDim(self) -> float:
            """"""
        @FlashlightDim.setter
        def FlashlightDim(self, value: float) -> None: ...
        @property
        def FlashlightSmoothness(self) -> float:
            """"""
        @FlashlightSmoothness.setter
        def FlashlightSmoothness(self, value: float) -> None: ...
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
        def GetSize(self) -> float:
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
class ModHalfTime(ABC, ModRateAdjust, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToAudio, IApplicableToRate, IApplicableToSample, IApplicableToTrack, IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AdjustPitch(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def SpeedChange(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToRate(self, time: float, rate: float) -> float:
        """
        
        :param time: 
        :param rate: 
        :return: 
        """
    def ApplyToSample(self, sample: IAdjustableAudioComponent) -> None:
        """
        
        :param sample: 
        """
    def ApplyToTrack(self, track: IAdjustableAudioComponent) -> None:
        """
        
        :param track: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModHardRock(ABC, Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDifficulty, IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToDifficulty(self, difficulty: BeatmapDifficulty) -> None:
        """
        
        :param difficulty: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModHidden(ABC, ModWithVisibilityAdjustment, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IApplicableToDrawableHitObject, IApplicableToScoreProcessor, IMod, IReadFromConfig, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def AdjustRank(self, rank: ScoreRank, accuracy: float) -> ScoreRank:
        """
        
        :param rank: 
        :param accuracy: 
        :return: 
        """
    def ApplyToBeatmap(self, beatmap: IBeatmap) -> None:
        """
        
        :param beatmap: 
        """
    def ApplyToDrawableHitObject(self, dho: DrawableHitObject) -> None:
        """
        
        :param drawable: 
        """
    def ApplyToScoreProcessor(self, scoreProcessor: ScoreProcessor) -> None:
        """
        
        :param scoreProcessor: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ReadFromConfig(self, config: OsuConfigManager) -> None:
        """
        
        :param config: 
        """
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModMirror(ABC, Mod, IEquatable[IMod], IEquatable[Mod], IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModMuted(ABC, Mod, IEquatable[IMod], IEquatable[Mod], IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModMuted(ABC, Generic[TObject], ModMuted, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableRuleset[TObject], IApplicableToScoreProcessor, IApplicableToTrack, IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AffectsHitSounds(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def EnableMetronome(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def InverseMuting(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def MuteComboCount(self) -> BindableInt:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def AdjustRank(self, rank: ScoreRank, accuracy: float) -> ScoreRank:
        """
        
        :param rank: 
        :param accuracy: 
        :return: 
        """
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[TObject]) -> None:
        """
        
        :param drawableRuleset: 
        """
    def ApplyToScoreProcessor(self, scoreProcessor: ScoreProcessor) -> None:
        """
        
        :param scoreProcessor: 
        """
    def ApplyToTrack(self, track: IAdjustableAudioComponent) -> None:
        """
        
        :param track: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModNightcore(ABC, ModRateAdjust, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToAudio, IApplicableToRate, IApplicableToSample, IApplicableToTrack, IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def SpeedChange(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToRate(self, time: float, rate: float) -> float:
        """
        
        :param time: 
        :param rate: 
        :return: 
        """
    def ApplyToSample(self, sample: IAdjustableAudioComponent) -> None:
        """
        
        :param sample: 
        """
    def ApplyToTrack(self, track: IAdjustableAudioComponent) -> None:
        """
        
        :param track: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModNightcore(ABC, Generic[TObject], ModNightcore, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToAudio, IApplicableToDrawableRuleset[TObject], IApplicableToRate, IApplicableToSample, IApplicableToTrack, IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def SpeedChange(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[TObject]) -> None:
        """
        
        :param drawableRuleset: 
        """
    def ApplyToRate(self, time: float, rate: float) -> float:
        """
        
        :param time: 
        :param rate: 
        :return: 
        """
    def ApplyToSample(self, sample: IAdjustableAudioComponent) -> None:
        """
        
        :param sample: 
        """
    def ApplyToTrack(self, track: IAdjustableAudioComponent) -> None:
        """
        
        :param track: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    class NightcoreBeatContainer(Generic[TObject], BeatSyncedContainer, ICollection[Drawable], IEnumerable[Drawable], IReadOnlyCollection[Drawable], IReadOnlyList[Drawable], IEnumerable, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, IContainer, IContainerCollection[Drawable], IContainerEnumerable[Drawable], ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
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
        def DisposeOnDeathRemoval(self) -> bool:
            """"""
        @property
        def Divisor(self) -> int:
            """
            
            :return: 
            """
        @Divisor.setter
        def Divisor(self, value: int) -> None: ...
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
        def MinimumBeatLength(self) -> float:
            """
            
            :return: 
            """
        @MinimumBeatLength.setter
        def MinimumBeatLength(self, value: float) -> None: ...
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
        def TimeSinceLastBeat(self) -> float:
            """
            
            :return: 
            """
        @property
        def TimeUntilNextBeat(self) -> float:
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
        OnLoadComplete: EventType[Action[Drawable]] = ...
        """"""
        OnUpdate: EventType[Action[Drawable]] = ...
        """"""
class ModNoFail(ABC, Mod, IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToHUD, IMod, IReadFromConfig, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RestartOnFail(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToHUD(self, overlay: HUDOverlay) -> None:
        """
        
        :param overlay: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PerformFail(self) -> bool:
        """
        
        :return: 
        """
    def ReadFromConfig(self, config: OsuConfigManager) -> None:
        """
        
        :param config: 
        """
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModNoMod(Mod, IEquatable[IMod], IEquatable[Mod], IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModNoScope(ABC, Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToPlayer, IApplicableToScoreProcessor, IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HiddenComboCount(self) -> BindableInt:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def AdjustRank(self, rank: ScoreRank, accuracy: float) -> ScoreRank:
        """
        
        :param rank: 
        :param accuracy: 
        :return: 
        """
    def ApplyToPlayer(self, player: Player) -> None:
        """
        
        :param player: 
        """
    def ApplyToScoreProcessor(self, scoreProcessor: ScoreProcessor) -> None:
        """
        
        :param scoreProcessor: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModPerfect(ABC, ModFailCondition, IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToHealthProcessor, IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Restart(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def RestartOnFail(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToHealthProcessor(self, healthProcessor: HealthProcessor) -> None:
        """
        
        :param healthProcessor: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PerformFail(self) -> bool:
        """
        
        :return: 
        """
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModPreset(RealmObject, IRealmObject, IRealmObjectBase, ISettableManagedAccessor, INotifyPropertyChanged, IReflectableType, IHasGuidPrimaryKey, ISoftDelete):
    """"""
    def __init__(self):
        """"""
    @property
    def Accessor(self) -> IRealmAccessor:
        """"""
    @property
    def BacklinksCount(self) -> int:
        """"""
    @property
    def DeletePending(self) -> bool:
        """
        
        :return: 
        """
    @DeletePending.setter
    def DeletePending(self, value: bool) -> None: ...
    @property
    def Description(self) -> str:
        """
        
        :return: 
        """
    @Description.setter
    def Description(self, value: str) -> None: ...
    @property
    def DynamicApi(self) -> DynamicObjectApi:
        """"""
    @property
    def ID(self) -> Guid:
        """
        
        :return: 
        """
    @ID.setter
    def ID(self, value: Guid) -> None: ...
    @property
    def IsFrozen(self) -> bool:
        """"""
    @property
    def IsManaged(self) -> bool:
        """"""
    @property
    def IsValid(self) -> bool:
        """"""
    @property
    def Mods(self) -> ICollection[Mod]:
        """
        
        :return: 
        """
    @Mods.setter
    def Mods(self, value: ICollection[Mod]) -> None: ...
    @property
    def ModsJson(self) -> str:
        """
        
        :return: 
        """
    @ModsJson.setter
    def ModsJson(self, value: str) -> None: ...
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def ObjectSchema(self) -> ObjectSchema:
        """"""
    @property
    def Realm(self) -> Realm:
        """"""
    @property
    def Ruleset(self) -> RulesetInfo:
        """
        
        :return: 
        """
    @Ruleset.setter
    def Ruleset(self, value: RulesetInfo) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self) -> TypeInfo:
        """"""
    def SetManagedAccessor(self, accessor: IRealmAccessor, helper: IRealmObjectHelper = ..., update: bool = ..., skipDefaults: bool = ...) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    PropertyChanged: EventType[PropertyChangedEventHandler] = ...
    """"""
class ModRandom(ABC, Mod, IEquatable[IMod], IEquatable[Mod], IHasSeed, IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def Seed(self) -> Bindable[Optional[int]]:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModRateAdjust(ABC, Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToAudio, IApplicableToRate, IApplicableToSample, IApplicableToTrack, IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def SpeedChange(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToRate(self, time: float, rate: float) -> float:
        """
        
        :param time: 
        :param rate: 
        :return: 
        """
    def ApplyToSample(self, sample: IAdjustableAudioComponent) -> None:
        """
        
        :param sample: 
        """
    def ApplyToTrack(self, track: IAdjustableAudioComponent) -> None:
        """
        
        :param track: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModRelax(ABC, Mod, IEquatable[IMod], IEquatable[Mod], IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModReplayData(Object):
    """"""
    Replay: Final[Replay] = ...
    """
    
    :return: 
    """
    User: Final[ModCreatedUser] = ...
    """
    
    :return: 
    """
    def __init__(self, replay: Replay, user: ModCreatedUser = ...):
        """
        
        :param replay: 
        :param user: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class ModScoreV2(Mod, IEquatable[IMod], IEquatable[Mod], IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModSuddenDeath(ABC, ModFailCondition, IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToHealthProcessor, IMod, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Restart(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def RestartOnFail(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToHealthProcessor(self, healthProcessor: HealthProcessor) -> None:
        """
        
        :param healthProcessor: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PerformFail(self) -> bool:
        """
        
        :return: 
        """
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModSynesthesia(Mod, IEquatable[IMod], IEquatable[Mod], IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModTimeRamp(ABC, Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToAudio, IApplicableToBeatmap, IApplicableToRate, IApplicableToSample, IApplicableToTrack, IMod, IUpdatableByPlayfield, IDeepCloneable[Mod]):
    """"""
    FINAL_RATE_PROGRESS: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AdjustPitch(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def FinalRate(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def InitialRate(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def SpeedChange(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToBeatmap(self, beatmap: IBeatmap) -> None:
        """
        
        :param beatmap: 
        """
    def ApplyToRate(self, time: float, rate: float = ...) -> float:
        """
        
        :param time: 
        :param rate: 
        :return: 
        """
    def ApplyToSample(self, sample: IAdjustableAudioComponent) -> None:
        """
        
        :param sample: 
        """
    def ApplyToTrack(self, track: IAdjustableAudioComponent) -> None:
        """
        
        :param track: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, playfield: Playfield) -> None:
        """
        
        :param playfield: 
        """
class ModTouchDevice(Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ModType(Enum):
    """"""
    DifficultyReduction: ModType = ...
    """"""
    DifficultyIncrease: ModType = ...
    """"""
    Conversion: ModType = ...
    """"""
    Automation: ModType = ...
    """"""
    Fun: ModType = ...
    """"""
    System: ModType = ...
    """"""
class ModWindDown(ModTimeRamp, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToAudio, IApplicableToBeatmap, IApplicableToRate, IApplicableToSample, IApplicableToTrack, IMod, IUpdatableByPlayfield, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AdjustPitch(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def FinalRate(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def InitialRate(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def SpeedChange(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToBeatmap(self, beatmap: IBeatmap) -> None:
        """
        
        :param beatmap: 
        """
    def ApplyToRate(self, time: float, rate: float = ...) -> float:
        """
        
        :param time: 
        :param rate: 
        :return: 
        """
    def ApplyToSample(self, sample: IAdjustableAudioComponent) -> None:
        """
        
        :param sample: 
        """
    def ApplyToTrack(self, track: IAdjustableAudioComponent) -> None:
        """
        
        :param track: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, playfield: Playfield) -> None:
        """
        
        :param playfield: 
        """
class ModWindUp(ModTimeRamp, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToAudio, IApplicableToBeatmap, IApplicableToRate, IApplicableToSample, IApplicableToTrack, IMod, IUpdatableByPlayfield, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AdjustPitch(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def FinalRate(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def InitialRate(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def SpeedChange(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToBeatmap(self, beatmap: IBeatmap) -> None:
        """
        
        :param beatmap: 
        """
    def ApplyToRate(self, time: float, rate: float = ...) -> float:
        """
        
        :param time: 
        :param rate: 
        :return: 
        """
    def ApplyToSample(self, sample: IAdjustableAudioComponent) -> None:
        """
        
        :param sample: 
        """
    def ApplyToTrack(self, track: IAdjustableAudioComponent) -> None:
        """
        
        :param track: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, playfield: Playfield) -> None:
        """
        
        :param playfield: 
        """
class ModWithVisibilityAdjustment(ABC, Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IApplicableToDrawableHitObject, IMod, IReadFromConfig, IDeepCloneable[Mod]):
    """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToBeatmap(self, beatmap: IBeatmap) -> None:
        """
        
        :param beatmap: 
        """
    def ApplyToDrawableHitObject(self, dho: DrawableHitObject) -> None:
        """
        
        :param drawable: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ReadFromConfig(self, config: OsuConfigManager) -> None:
        """
        
        :param config: 
        """
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class MultiMod(Mod, IEquatable[IMod], IEquatable[Mod], IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self, mods: Array[Mod]):
        """
        
        :param mods: 
        """
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Mods(self) -> Array[Mod]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class MuteComboSlider(RoundedSliderBar[Int32], ICollection[Drawable], IEnumerable[Drawable], IReadOnlyCollection[Drawable], IReadOnlyList[Drawable], IEnumerable, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, IContainer, IContainerCollection[Drawable], IContainerEnumerable[Drawable], IHasTooltip, ITooltipContentProvider, ITransformable, IHasCurrentValue[Int32], IDrawable, ISourceGeneratedHandleInputCache):
    """"""
    KeyboardStep: Final[float] = ...
    """"""
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    RangePadding: Final[float] = ...
    """"""
    TransferValueOnCommit: Final[bool] = ...
    """"""
    def __init__(self):
        """"""
    @property
    def AccentColour(self) -> Color4:
        """
        
        :return: 
        """
    @AccentColour.setter
    def AccentColour(self, value: Color4) -> None: ...
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
    def BackgroundColour(self) -> Color4:
        """
        
        :return: 
        """
    @BackgroundColour.setter
    def BackgroundColour(self, value: Color4) -> None: ...
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
    def Current(self) -> Bindable[int]:
        """"""
    @Current.setter
    def Current(self, value: Bindable[int]) -> None: ...
    @property
    def Dependencies(self) -> IReadOnlyDependencyContainer:
        """"""
    @property
    def Depth(self) -> float:
        """"""
    @Depth.setter
    def Depth(self, value: float) -> None: ...
    @property
    def DisplayAsPercentage(self) -> bool:
        """
        
        :return: 
        """
    @DisplayAsPercentage.setter
    def DisplayAsPercentage(self, value: bool) -> None: ...
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
    def PlaySamplesOnAdjust(self) -> bool:
        """
        
        :return: 
        """
    @PlaySamplesOnAdjust.setter
    def PlaySamplesOnAdjust(self, value: bool) -> None: ...
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
    def ResetToDefault(self) -> Action:
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
    def TooltipText(self) -> LocalisableString:
        """"""
    @property
    def TransformStartTime(self) -> float:
        """"""
    @property
    def Transforms(self) -> IEnumerable[Transform]:
        """"""
    @property
    def UsableWidth(self) -> float:
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
    def GetDisplayableValue(self, value: int) -> LocalisableString:
        """
        
        :param value: 
        :return: 
        """
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
    OnLoadComplete: EventType[Action[Drawable]] = ...
    """"""
    OnUpdate: EventType[Action[Drawable]] = ...
    """"""
class RateAdjustModHelper(Object, IApplicableMod, IApplicableToTrack):
    """"""
    SpeedChange: Final[IBindableNumber[float]] = ...
    """
    
    :return: 
    """
    def __init__(self, speedChange: IBindableNumber[float]):
        """
        
        :param speedChange: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    def ApplyToTrack(self, track: IAdjustableAudioComponent) -> None:
        """
        
        :param track: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def HandleAudioAdjustments(self, adjustPitch: BindableBool) -> None:
        """
        
        :param adjustPitch: 
        """
    def ToString(self) -> str:
        """"""
class UnknownMod(Mod, IEquatable[IMod], IEquatable[Mod], IMod, IDeepCloneable[Mod]):
    """"""
    OriginalAcronym: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self, acronym: str):
        """
        
        :param acronym: 
        """
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""