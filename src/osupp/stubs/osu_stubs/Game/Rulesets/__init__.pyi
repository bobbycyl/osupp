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
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IReadOnlyCollection
from System.Collections.Generic import IReadOnlyList
from System.Collections import IDictionary
from System.ComponentModel import INotifyPropertyChanged
from System.ComponentModel import PropertyChangedEventHandler
from System import Exception
from System import IComparable
from System import IDisposable
from System import IEquatable
from System import Int32
from System import Object
from System.Reflection import IReflectableType
from System.Reflection import MethodBase
from System.Reflection import TypeInfo
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System import Type
from System import ValueTuple
from __future__ import annotations
from abc import ABC
from osu.Framework.Allocation import IDependencyActivatorRegistry
from osu.Framework.Allocation import IDependencyInjectionCandidate
from osu.Framework.Allocation import IReadOnlyDependencyContainer
from osu.Framework.Allocation import ISourceGeneratedDependencyActivator
from osu.Framework.Allocation import ISourceGeneratedLongRunningLoadCache
from osu.Framework.Bindables import Bindable
from osu.Framework.Graphics import Anchor
from osu.Framework.Graphics import Axes
from osu.Framework.Graphics import BlendingParameters
from osu.Framework.Graphics.Colour import ColourInfo
from osu.Framework.Graphics import Component
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
from osu.Framework.Graphics.UserInterface import IHasCurrentValue
from osu.Framework.Graphics.UserInterface import TabControl
from osu.Framework.IO.Stores import IResourceStore
from osu.Framework.Input.Bindings import IKeyBindingHandler
from osu.Framework.Input.Bindings import KeyBinding
from osu.Framework.Input.Events import KeyBindingPressEvent
from osu.Framework.Input.Events import KeyBindingReleaseEvent
from osu.Framework.Input.Events import UIEvent
from osu.Framework.Input import ISourceGeneratedHandleInputCache
from osu.Framework.Input import PlatformAction
from osu.Framework.Layout import InvalidationSource
from osu.Framework.Localisation import LocalisableString
from osu.Framework.Platform import Storage
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
from osu.Game.Database import IHasOnlineID
from osu.Game.Database import RealmAccess
from osu.Game.Overlays.Settings import RulesetSettingsSubsection
from osu.Game.Rulesets.Configuration import IRulesetConfigManager
from osu.Game.Rulesets.Difficulty import DifficultyCalculator
from osu.Game.Rulesets.Difficulty import PerformanceCalculator
from osu.Game.Rulesets.Difficulty import RulesetBeatmapAttribute
from osu.Game.Rulesets.Edit import HitObjectComposer
from osu.Game.Rulesets.Edit import IBeatmapVerifier
from osu.Game.Rulesets.Filter import IRulesetFilterCriteria
from osu.Game.Rulesets.Mods import IMod
from osu.Game.Rulesets.Mods import Mod
from osu.Game.Rulesets.Mods import ModAutoplay
from osu.Game.Rulesets.Mods import ModTouchDevice
from osu.Game.Rulesets.Mods import ModType
from osu.Game.Rulesets.Replays.Types import IConvertibleReplayFrame
from osu.Game.Rulesets.Scoring import HealthProcessor
from osu.Game.Rulesets.Scoring import HitResult
from osu.Game.Rulesets.Scoring.Legacy import ILegacyScoreSimulator
from osu.Game.Rulesets.Scoring import ScoreProcessor
from osu.Game.Rulesets.UI import DrawableRuleset
from osu.Game.Scoring import ScoreInfo
from osu.Game.Screens.Ranking.Statistics import StatisticItem
from osu.Game.Skinning import ISkin
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
class AssemblyRulesetStore(RulesetStore, IDisposable, IRulesetStore):
    """"""
    @overload
    def __init__(self, path: str):
        """
        
        :param path: 
        """
    @overload
    def __init__(self, storage: Storage = ...):
        """
        
        :param storage: 
        """
    @property
    def AvailableRulesets(self) -> IEnumerable[RulesetInfo]:
        """
        
        :return: 
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetRuleset(self, id: int) -> RulesetInfo:
        """
        
        :param id: 
        :return: 
        """
    @overload
    def GetRuleset(self, shortName: str) -> RulesetInfo:
        """
        
        :param shortName: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class ILegacyRuleset:
    """"""
    MAX_LEGACY_RULESET_ID: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @property
    def LegacyID(self) -> int:
        """
        
        :return: 
        """
    def CreateLegacyScoreSimulator(self) -> ILegacyScoreSimulator:
        """
        
        :return: 
        """
    def GetKeyCount(self, beatmapInfo: IBeatmapInfo, mods: IReadOnlyList[Mod] = ...) -> int:
        """
        
        :param beatmapInfo: 
        :param mods: 
        :return: 
        """
class IRulesetConfigCache:
    """"""
    def GetConfigFor(self, ruleset: Ruleset) -> IRulesetConfigManager:
        """
        
        :param ruleset: 
        :return: 
        """
class IRulesetInfo(IComparable[IRulesetInfo], IEquatable[IRulesetInfo], IHasOnlineID[Int32]):
    """"""
    @property
    def InstantiationInfo(self) -> str:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def OnlineID(self) -> int:
        """
        
        :return: 
        """
    @property
    def ShortName(self) -> str:
        """
        
        :return: 
        """
    def CompareTo(self, other: IRulesetInfo) -> int:
        """"""
    def CreateInstance(self) -> Ruleset:
        """
        
        :return: 
        """
    def Equals(self, other: IRulesetInfo) -> bool:
        """"""
class IRulesetStore:
    """"""
    @property
    def AvailableRulesets(self) -> IEnumerable[IRulesetInfo]:
        """
        
        :return: 
        """
    @overload
    def GetRuleset(self, id: int) -> IRulesetInfo:
        """
        
        :param id: 
        :return: 
        """
    @overload
    def GetRuleset(self, shortName: str) -> IRulesetInfo:
        """
        
        :param shortName: 
        :return: 
        """
class RealmRulesetStore(RulesetStore, IDisposable, IRulesetStore):
    """"""
    def __init__(self, realmAccess: RealmAccess, storage: Storage = ...):
        """
        
        :param realmAccess: 
        :param storage: 
        """
    @property
    def AvailableRulesets(self) -> IEnumerable[RulesetInfo]:
        """
        
        :return: 
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetRuleset(self, id: int) -> RulesetInfo:
        """
        
        :param id: 
        :return: 
        """
    @overload
    def GetRuleset(self, shortName: str) -> RulesetInfo:
        """
        
        :param shortName: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class Ruleset(ABC, Object):
    """"""
    CURRENT_RULESET_API_VERSION: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
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
    def GetAdjustedDisplayDifficulty(self, beatmapInfo: IBeatmapInfo, mods: IReadOnlyCollection[Mod]) -> BeatmapDifficulty:
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
class RulesetConfigCache(Component, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache, IRulesetConfigCache):
    """"""
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    def __init__(self, realm: RealmAccess, rulesets: RulesetStore):
        """
        
        :param realm: 
        :param rulesets: 
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
    def GetConfigFor(self, ruleset: Ruleset) -> IRulesetConfigManager:
        """
        
        :param ruleset: 
        :return: 
        """
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
class RulesetInfo(RealmObject, IRealmObject, IRealmObjectBase, ISettableManagedAccessor, INotifyPropertyChanged, IReflectableType, IComparable[IRulesetInfo], IComparable[RulesetInfo], IEquatable[IRulesetInfo], IEquatable[RulesetInfo], IHasOnlineID[Int32], IRulesetInfo):
    """"""
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, shortName: str, name: str, instantiationInfo: str, onlineID: int):
        """
        
        :param shortName: 
        :param name: 
        :param instantiationInfo: 
        :param onlineID: 
        """
    @property
    def Accessor(self) -> IRealmAccessor:
        """"""
    @property
    def Available(self) -> bool:
        """
        
        :return: 
        """
    @Available.setter
    def Available(self, value: bool) -> None: ...
    @property
    def BacklinksCount(self) -> int:
        """"""
    @property
    def DynamicApi(self) -> DynamicObjectApi:
        """"""
    @property
    def InstantiationInfo(self) -> str:
        """
        
        :return: 
        """
    @InstantiationInfo.setter
    def InstantiationInfo(self, value: str) -> None: ...
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
    def LastAppliedDifficultyVersion(self) -> int:
        """
        
        :return: 
        """
    @LastAppliedDifficultyVersion.setter
    def LastAppliedDifficultyVersion(self, value: int) -> None: ...
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
    def OnlineID(self) -> int:
        """
        
        :return: 
        """
    @OnlineID.setter
    def OnlineID(self, value: int) -> None: ...
    @property
    def Realm(self) -> Realm:
        """"""
    @property
    def ShortName(self) -> str:
        """
        
        :return: 
        """
    @ShortName.setter
    def ShortName(self, value: str) -> None: ...
    def Clone(self) -> RulesetInfo:
        """
        
        :return: 
        """
    @overload
    def CompareTo(self, other: IRulesetInfo) -> int:
        """"""
    @overload
    def CompareTo(self, other: RulesetInfo) -> int:
        """"""
    def CreateInstance(self) -> Ruleset:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IRulesetInfo) -> bool:
        """"""
    @overload
    def Equals(self, other: RulesetInfo) -> bool:
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
class RulesetLoadException(Exception, ISerializable):
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
class RulesetSelector(ABC, TabControl[RulesetInfo], IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IHasCurrentValue[RulesetInfo], IDrawable, IKeyBindingHandler, IKeyBindingHandler[PlatformAction], ISourceGeneratedHandleInputCache):
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
    def AutoSizeAxes(self) -> Axes:
        """"""
    @property
    def AutoSizeDuration(self) -> float:
        """"""
    @property
    def AutoSizeEasing(self) -> Easing:
        """"""
    @property
    def AutoSort(self) -> bool:
        """"""
    @AutoSort.setter
    def AutoSort(self, value: bool) -> None: ...
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
    def Current(self) -> Bindable[RulesetInfo]:
        """"""
    @Current.setter
    def Current(self, value: Bindable[RulesetInfo]) -> None: ...
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
    def IsSwitchable(self) -> bool:
        """"""
    @IsSwitchable.setter
    def IsSwitchable(self, value: bool) -> None: ...
    @property
    def Items(self) -> IReadOnlyList[RulesetInfo]:
        """"""
    @Items.setter
    def Items(self, value: IReadOnlyList[RulesetInfo]) -> None: ...
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
    def SelectFirstTabByDefault(self) -> bool:
        """"""
    @SelectFirstTabByDefault.setter
    def SelectFirstTabByDefault(self, value: bool) -> None: ...
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
    def SwitchTabOnRemove(self) -> bool:
        """"""
    @SwitchTabOnRemove.setter
    def SwitchTabOnRemove(self, value: bool) -> None: ...
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
    def VisibleItems(self) -> IEnumerable[RulesetInfo]:
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
    def AddItem(self, item: RulesetInfo) -> None:
        """"""
    def AddTransform(self, transform: Transform, customTransformID: Optional[int] = ...) -> None:
        """"""
    def ApplyTransformsAt(self, time: float, propagateChildren: bool = ...) -> None:
        """"""
    def BeginAbsoluteSequence(self, newTransformStartTime: float, recursive: bool = ...) -> IDisposable:
        """"""
    def BeginDelayedSequence(self, delay: float, recursive: bool = ...) -> IDisposable:
        """"""
    def Clear(self) -> None:
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
    def OnPressed(self, e: KeyBindingPressEvent[PlatformAction]) -> bool:
        """"""
    def OnReleased(self, e: KeyBindingReleaseEvent[PlatformAction]) -> None:
        """"""
    def PinItem(self, item: RulesetInfo) -> None:
        """"""
    def ReceivePositionalInputAt(self, screenSpacePos: Vector2) -> bool:
        """"""
    def RegisterForDependencyActivation(self, registry: IDependencyActivatorRegistry) -> None:
        """"""
    def RemoveItem(self, item: RulesetInfo) -> None:
        """"""
    def RemoveTransform(self, toRemove: Transform) -> None:
        """"""
    def SelectItem(self, item: RulesetInfo) -> None:
        """"""
    def Show(self) -> None:
        """"""
    def SwitchTab(self, direction: int, wrap: bool = ...) -> None:
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
    def UnpinItem(self, item: RulesetInfo) -> None:
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
class RulesetStore(ABC, Object, IDisposable, IRulesetStore):
    """"""
    @property
    def AvailableRulesets(self) -> IEnumerable[RulesetInfo]:
        """
        
        :return: 
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetRuleset(self, id: int) -> RulesetInfo:
        """
        
        :param id: 
        :return: 
        """
    @overload
    def GetRuleset(self, shortName: str) -> RulesetInfo:
        """
        
        :param shortName: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""