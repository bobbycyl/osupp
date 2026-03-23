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
from System import Attribute
from System.Collections.Generic import ICollection
from System.Collections.Generic import IDictionary
from System.Collections.Generic import IEnumerable
from System.ComponentModel import INotifyPropertyChanged
from System.ComponentModel import PropertyChangedEventHandler
from System import Enum
from System import Func
from System import Guid
from System import IComparable
from System import IDisposable
from System import Object
from System.Reflection import IReflectableType
from System.Reflection import PropertyInfo
from System.Reflection import TypeInfo
from System import Type
from System import ValueTuple
from System import ValueType
from __future__ import annotations
from abc import ABC
from osu.Framework.Allocation import IDependencyActivatorRegistry
from osu.Framework.Allocation import IDependencyInjectionCandidate
from osu.Framework.Allocation import ISourceGeneratedDependencyActivator
from osu.Framework.Allocation import ISourceGeneratedLongRunningLoadCache
from osu.Framework.Bindables import Bindable
from osu.Framework.Bindables import IBindable
from osu.Framework.Bindables import IBindableList
from osu.Framework.Configuration import ConfigManager
from osu.Framework.Configuration import IConfigManager
from osu.Framework.Configuration import IniConfigManager
from osu.Framework.Configuration.Tracking import ITrackableConfigManager
from osu.Framework.Configuration.Tracking import TrackedSettings
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
from osu.Framework.Localisation import LocalisableString
from osu.Framework.Platform import Storage
from osu.Framework.Timing import FrameTimeInfo
from osu.Framework.Timing import IFrameBasedClock
from osu.Game.Configuration.SessionAverageHitErrorTracker import DataPoint
from osu.Game.Database import RealmAccess
from osu.Game.Input.Bindings import GlobalAction
from osu.Game.Rulesets.Mods import Mod
from osuTK import Vector2
from typing import Final
from typing import Generic
from typing import Optional
from typing import TypeVar
from typing import overload
T = TypeVar("T")
TLookup = TypeVar("TLookup")
TValue = TypeVar("TValue")
class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...
class BackgroundSource(Enum):
    """"""
    Skin: BackgroundSource = ...
    """"""
    Beatmap: BackgroundSource = ...
    """"""
    BeatmapWithStoryboard: BackgroundSource = ...
    """"""
class DevelopmentOsuConfigManager(OsuConfigManager, IDisposable, ITrackableConfigManager, IConfigManager, IGameplaySettings):
    """"""
    def __init__(self, storage: Storage):
        """
        
        :param storage: 
        """
    @property
    def ComboColourNormalisationAmount(self) -> IBindable[float]:
        """
        
        :return: 
        """
    @property
    def LookupKeyBindings(self) -> Func[GlobalAction, LocalisableString]:
        """
        
        :return: 
        """
    @LookupKeyBindings.setter
    def LookupKeyBindings(self, value: Func[GlobalAction, LocalisableString]) -> None: ...
    @property
    def LookupSkinName(self) -> Func[Guid, str]:
        """
        
        :return: 
        """
    @LookupSkinName.setter
    def LookupSkinName(self, value: Func[Guid, str]) -> None: ...
    @property
    def PositionalHitsoundsLevel(self) -> IBindable[float]:
        """
        
        :return: 
        """
    def BindWith(self, lookup: OsuSetting, bindable: Bindable[TValue]) -> None:
        """"""
    def CreateTrackedSettings(self) -> TrackedSettings:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Get(self, lookup: OsuSetting) -> TValue:
        """"""
    def GetBindable(self, lookup: OsuSetting) -> Bindable[TValue]:
        """"""
    def GetCurrentConfigurationForLogging(self) -> IDictionary[OsuSetting, str]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Load(self) -> None:
        """"""
    def LoadInto(self, settings: TrackedSettings) -> None:
        """"""
    def Migrate(self) -> None:
        """"""
    def Save(self) -> bool:
        """"""
    def SetValue(self, lookup: OsuSetting, value: TValue) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class DiscordRichPresenceMode(Enum):
    """"""
    Off: DiscordRichPresenceMode = ...
    """"""
    Limited: DiscordRichPresenceMode = ...
    """"""
    Full: DiscordRichPresenceMode = ...
    """"""
class HUDVisibilityMode(Enum):
    """"""
    Never: HUDVisibilityMode = ...
    """"""
    HideDuringGameplay: HUDVisibilityMode = ...
    """"""
    Always: HUDVisibilityMode = ...
    """"""
class IGameplaySettings:
    """"""
    @property
    def ComboColourNormalisationAmount(self) -> IBindable[float]:
        """
        
        :return: 
        """
    @property
    def PositionalHitsoundsLevel(self) -> IBindable[float]:
        """
        
        :return: 
        """
class InMemoryConfigManager(Generic[TLookup], ConfigManager[TLookup], IDisposable, ITrackableConfigManager, IConfigManager):
    """"""
    def __init__(self):
        """"""
    def BindWith(self, lookup: TLookup, bindable: Bindable[TValue]) -> None:
        """"""
    def CreateTrackedSettings(self) -> TrackedSettings:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Get(self, lookup: TLookup) -> TValue:
        """"""
    def GetBindable(self, lookup: TLookup) -> Bindable[TValue]:
        """"""
    def GetCurrentConfigurationForLogging(self) -> IDictionary[TLookup, str]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Load(self) -> None:
        """"""
    def LoadInto(self, settings: TrackedSettings) -> None:
        """"""
    def Save(self) -> bool:
        """"""
    def SetValue(self, lookup: TLookup, value: TValue) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class IntroSequence(Enum):
    """"""
    Circles: IntroSequence = ...
    """"""
    Welcome: IntroSequence = ...
    """"""
    Triangles: IntroSequence = ...
    """"""
    Random: IntroSequence = ...
    """"""
class ModSettingChangeTracker(Object, IDisposable):
    """"""
    SettingChanged: Final[Action[Mod]] = ...
    """
    
    :return: 
    """
    def __init__(self, mods: IEnumerable[Mod]):
        """
        
        :param mods: 
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class OsuConfigManager(IniConfigManager[OsuSetting], IDisposable, ITrackableConfigManager, IConfigManager, IGameplaySettings):
    """"""
    def __init__(self, storage: Storage):
        """
        
        :param storage: 
        """
    @property
    def ComboColourNormalisationAmount(self) -> IBindable[float]:
        """
        
        :return: 
        """
    @property
    def LookupKeyBindings(self) -> Func[GlobalAction, LocalisableString]:
        """
        
        :return: 
        """
    @LookupKeyBindings.setter
    def LookupKeyBindings(self, value: Func[GlobalAction, LocalisableString]) -> None: ...
    @property
    def LookupSkinName(self) -> Func[Guid, str]:
        """
        
        :return: 
        """
    @LookupSkinName.setter
    def LookupSkinName(self, value: Func[Guid, str]) -> None: ...
    @property
    def PositionalHitsoundsLevel(self) -> IBindable[float]:
        """
        
        :return: 
        """
    def BindWith(self, lookup: OsuSetting, bindable: Bindable[TValue]) -> None:
        """"""
    def CreateTrackedSettings(self) -> TrackedSettings:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Get(self, lookup: OsuSetting) -> TValue:
        """"""
    def GetBindable(self, lookup: OsuSetting) -> Bindable[TValue]:
        """"""
    def GetCurrentConfigurationForLogging(self) -> IDictionary[OsuSetting, str]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Load(self) -> None:
        """"""
    def LoadInto(self, settings: TrackedSettings) -> None:
        """"""
    def Migrate(self) -> None:
        """"""
    def Save(self) -> bool:
        """"""
    def SetValue(self, lookup: OsuSetting, value: TValue) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class OsuSetting(Enum):
    """"""
    Ruleset: OsuSetting = ...
    """"""
    Token: OsuSetting = ...
    """"""
    MenuCursorSize: OsuSetting = ...
    """"""
    GameplayCursorSize: OsuSetting = ...
    """"""
    AutoCursorSize: OsuSetting = ...
    """"""
    GameplayCursorDuringTouch: OsuSetting = ...
    """"""
    DimLevel: OsuSetting = ...
    """"""
    BlurLevel: OsuSetting = ...
    """"""
    EditorDim: OsuSetting = ...
    """"""
    LightenDuringBreaks: OsuSetting = ...
    """"""
    ShowStoryboard: OsuSetting = ...
    """"""
    KeyOverlay: OsuSetting = ...
    """"""
    GameplayLeaderboard: OsuSetting = ...
    """"""
    PositionalHitsoundsLevel: OsuSetting = ...
    """"""
    AlwaysPlayFirstComboBreak: OsuSetting = ...
    """"""
    FloatingComments: OsuSetting = ...
    """"""
    HUDVisibilityMode: OsuSetting = ...
    """"""
    ShowHealthDisplayWhenCantFail: OsuSetting = ...
    """"""
    FadePlayfieldWhenHealthLow: OsuSetting = ...
    """"""
    MouseDisableButtons: OsuSetting = ...
    """"""
    MouseDisableWheel: OsuSetting = ...
    """"""
    ConfineMouseMode: OsuSetting = ...
    """"""
    AudioOffset: OsuSetting = ...
    """"""
    VolumeInactive: OsuSetting = ...
    """"""
    MenuMusic: OsuSetting = ...
    """"""
    MenuVoice: OsuSetting = ...
    """"""
    MenuTips: OsuSetting = ...
    """"""
    CursorRotation: OsuSetting = ...
    """"""
    MenuParallax: OsuSetting = ...
    """"""
    Prefer24HourTime: OsuSetting = ...
    """"""
    BeatmapDetailTab: OsuSetting = ...
    """"""
    BeatmapLeaderboardSortMode: OsuSetting = ...
    """"""
    BeatmapDetailModsFilter: OsuSetting = ...
    """"""
    Username: OsuSetting = ...
    """"""
    ReleaseStream: OsuSetting = ...
    """"""
    SavePassword: OsuSetting = ...
    """"""
    SaveUsername: OsuSetting = ...
    """"""
    DisplayStarsMinimum: OsuSetting = ...
    """"""
    DisplayStarsMaximum: OsuSetting = ...
    """"""
    SongSelectGroupMode: OsuSetting = ...
    """"""
    SongSelectSortingMode: OsuSetting = ...
    """"""
    RandomSelectAlgorithm: OsuSetting = ...
    """"""
    ModSelectHotkeyStyle: OsuSetting = ...
    """"""
    ShowFpsDisplay: OsuSetting = ...
    """"""
    ChatDisplayHeight: OsuSetting = ...
    """"""
    BeatmapListingCardSize: OsuSetting = ...
    """"""
    ToolbarClockDisplayMode: OsuSetting = ...
    """"""
    SongSelectBackgroundBlur: OsuSetting = ...
    """"""
    Version: OsuSetting = ...
    """"""
    ShowFirstRunSetup: OsuSetting = ...
    """"""
    ShowConvertedBeatmaps: OsuSetting = ...
    """"""
    Skin: OsuSetting = ...
    """"""
    ScreenshotFormat: OsuSetting = ...
    """"""
    ScreenshotCaptureMenuCursor: OsuSetting = ...
    """"""
    BeatmapSkins: OsuSetting = ...
    """"""
    BeatmapColours: OsuSetting = ...
    """"""
    BeatmapHitsounds: OsuSetting = ...
    """"""
    IncreaseFirstObjectVisibility: OsuSetting = ...
    """"""
    ScoreDisplayMode: OsuSetting = ...
    """"""
    ExternalLinkWarning: OsuSetting = ...
    """"""
    PreferNoVideo: OsuSetting = ...
    """"""
    Scaling: OsuSetting = ...
    """"""
    ScalingPositionX: OsuSetting = ...
    """"""
    ScalingPositionY: OsuSetting = ...
    """"""
    ScalingSizeX: OsuSetting = ...
    """"""
    ScalingSizeY: OsuSetting = ...
    """"""
    ScalingBackgroundDim: OsuSetting = ...
    """"""
    UIScale: OsuSetting = ...
    """"""
    IntroSequence: OsuSetting = ...
    """"""
    NotifyOnUsernameMentioned: OsuSetting = ...
    """"""
    NotifyOnPrivateMessage: OsuSetting = ...
    """"""
    NotifyOnFriendPresenceChange: OsuSetting = ...
    """"""
    UIHoldActivationDelay: OsuSetting = ...
    """"""
    HitLighting: OsuSetting = ...
    """"""
    StarFountains: OsuSetting = ...
    """"""
    MenuBackgroundSource: OsuSetting = ...
    """"""
    GameplayDisableWinKey: OsuSetting = ...
    """"""
    SeasonalBackgroundMode: OsuSetting = ...
    """"""
    EditorWaveformOpacity: OsuSetting = ...
    """"""
    EditorShowHitMarkers: OsuSetting = ...
    """"""
    EditorAutoSeekOnPlacement: OsuSetting = ...
    """"""
    DiscordRichPresence: OsuSetting = ...
    """"""
    ShowOnlineExplicitContent: OsuSetting = ...
    """"""
    LastProcessedMetadataId: OsuSetting = ...
    """"""
    SafeAreaConsiderations: OsuSetting = ...
    """"""
    ComboColourNormalisationAmount: OsuSetting = ...
    """"""
    ProfileCoverExpanded: OsuSetting = ...
    """"""
    EditorLimitedDistanceSnap: OsuSetting = ...
    """"""
    ReplaySettingsOverlay: OsuSetting = ...
    """"""
    ReplayPlaybackControlsExpanded: OsuSetting = ...
    """"""
    AutomaticallyDownloadMissingBeatmaps: OsuSetting = ...
    """"""
    EditorShowSpeedChanges: OsuSetting = ...
    """"""
    TouchDisableGameplayTaps: OsuSetting = ...
    """"""
    ModSelectTextSearchStartsActive: OsuSetting = ...
    """"""
    UserOnlineStatus: OsuSetting = ...
    """"""
    MultiplayerRoomFilter: OsuSetting = ...
    """"""
    HideCountryFlags: OsuSetting = ...
    """"""
    EditorTimelineShowTimingChanges: OsuSetting = ...
    """"""
    EditorTimelineShowTicks: OsuSetting = ...
    """"""
    AlwaysShowHoldForMenuButton: OsuSetting = ...
    """"""
    EditorContractSidebars: OsuSetting = ...
    """"""
    EditorScaleOrigin: OsuSetting = ...
    """"""
    EditorRotationOrigin: OsuSetting = ...
    """"""
    EditorTimelineShowBreaks: OsuSetting = ...
    """"""
    EditorAdjustExistingObjectsOnTimingChanges: OsuSetting = ...
    """"""
    AlwaysRequireHoldingForPause: OsuSetting = ...
    """"""
    MultiplayerShowInProgressFilter: OsuSetting = ...
    """"""
    BeatmapListingFeaturedArtistFilter: OsuSetting = ...
    """"""
    ShowMobileDisclaimer: OsuSetting = ...
    """"""
    EditorShowStoryboard: OsuSetting = ...
    """"""
    EditorSubmissionNotifyOnDiscussionReplies: OsuSetting = ...
    """"""
    EditorSubmissionLoadInBrowserAfterSubmission: OsuSetting = ...
    """"""
    WasSupporter: OsuSetting = ...
    """"""
    LastOnlineTagsPopulation: OsuSetting = ...
    """"""
    AutomaticallyAdjustBeatmapOffset: OsuSetting = ...
    """"""
class RandomSelectAlgorithm(Enum):
    """"""
    RandomPermutation: RandomSelectAlgorithm = ...
    """"""
    Random: RandomSelectAlgorithm = ...
    """"""
class RealmRulesetSetting(RealmObject, IRealmObject, IRealmObjectBase, ISettableManagedAccessor, INotifyPropertyChanged, IReflectableType):
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
    def DynamicApi(self) -> DynamicObjectApi:
        """"""
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
    def Key(self) -> str:
        """
        
        :return: 
        """
    @Key.setter
    def Key(self, value: str) -> None: ...
    @property
    def ObjectSchema(self) -> ObjectSchema:
        """"""
    @property
    def Realm(self) -> Realm:
        """"""
    @property
    def RulesetName(self) -> str:
        """
        
        :return: 
        """
    @RulesetName.setter
    def RulesetName(self, value: str) -> None: ...
    @property
    def Value(self) -> str:
        """
        
        :return: 
        """
    @Value.setter
    def Value(self, value: str) -> None: ...
    @property
    def Variant(self) -> int:
        """
        
        :return: 
        """
    @Variant.setter
    def Variant(self, value: int) -> None: ...
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
class ReleaseStream(Enum):
    """"""
    Lazer: ReleaseStream = ...
    """"""
    Tachyon: ReleaseStream = ...
    """"""
class ScalingMode(Enum):
    """"""
    Off: ScalingMode = ...
    """"""
    Everything: ScalingMode = ...
    """"""
    ExcludeOverlays: ScalingMode = ...
    """"""
    Gameplay: ScalingMode = ...
    """"""
class ScreenshotFormat(Enum):
    """"""
    Jpg: ScreenshotFormat = ...
    """"""
    Png: ScreenshotFormat = ...
    """"""
class ScrollVisualisationMethod(Enum):
    """"""
    Sequential: ScrollVisualisationMethod = ...
    """"""
    Overlapping: ScrollVisualisationMethod = ...
    """"""
    Constant: ScrollVisualisationMethod = ...
    """"""
class SeasonalBackgroundMode(Enum):
    """"""
    Always: SeasonalBackgroundMode = ...
    """"""
    Sometimes: SeasonalBackgroundMode = ...
    """"""
    Never: SeasonalBackgroundMode = ...
    """"""
class SessionAverageHitErrorTracker(Component, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
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
    def AverageHitErrorHistory(self) -> IBindableList[SessionAverageHitErrorTracker.DataPoint]:
        """
        
        :return: 
        """
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
    def ClearHistory(self) -> None:
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
    class DataPoint(ValueType):
        """"""
        def __init__(self, averageHitError: float, globalOffset: float):
            """"""
        @property
        def AverageHitError(self) -> float:
            """"""
        @property
        def GlobalAudioOffset(self) -> float:
            """"""
        @property
        def SuggestedGlobalAudioOffset(self) -> float:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
class SessionStatics(InMemoryConfigManager[Static], IDisposable, ITrackableConfigManager, IConfigManager):
    """"""
    def __init__(self):
        """"""
    def BindWith(self, lookup: Static, bindable: Bindable[TValue]) -> None:
        """"""
    def CreateTrackedSettings(self) -> TrackedSettings:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Get(self, lookup: Static) -> TValue:
        """"""
    def GetBindable(self, lookup: Static) -> Bindable[TValue]:
        """"""
    def GetCurrentConfigurationForLogging(self) -> IDictionary[Static, str]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Load(self) -> None:
        """"""
    def LoadInto(self, settings: TrackedSettings) -> None:
        """"""
    def ResetAfterInactivity(self) -> None:
        """"""
    def Save(self) -> bool:
        """"""
    def SetValue(self, lookup: Static, value: TValue) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class SettingSourceAttribute(Attribute, IComparable[SettingSourceAttribute]):
    """"""
    @overload
    def __init__(self, label: str, description: str = ...):
        """
        
        :param label: 
        :param description: 
        """
    @overload
    def __init__(self, label: str, description: str, orderPosition: int):
        """
        
        :param label: 
        :param description: 
        :param orderPosition: 
        """
    @overload
    def __init__(self, declaringType: Type, label: str, description: str = ...):
        """
        
        :param declaringType: 
        :param label: 
        :param description: 
        """
    @overload
    def __init__(self, declaringType: Type, label: str, description: str, orderPosition: int):
        """
        
        :param declaringType: 
        :param label: 
        :param description: 
        :param orderPosition: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def Label(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def OrderPosition(self) -> Optional[int]:
        """
        
        :return: 
        """
    @property
    def SettingControlType(self) -> Type:
        """
        
        :return: 
        """
    @SettingControlType.setter
    def SettingControlType(self, value: Type) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    def CompareTo(self, other: SettingSourceAttribute) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
class SettingSourceExtensions(ABC, Object):
    """"""
    @classmethod
    def CreateSettingsControls(cls, obj: object) -> IEnumerable[Drawable]:
        """
        
        :param obj: 
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetOrderedSettingsSourceProperties(cls, obj: object) -> ICollection[ValueTuple, PropertyInfo]:
        """
        
        :param obj: 
        :return: 
        """
    @classmethod
    def GetSettingsSourceProperties(cls, obj: object) -> IEnumerable[ValueTuple, PropertyInfo]:
        """
        
        :param obj: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetUnderlyingSettingValue(cls, setting: object) -> object:
        """
        
        :param setting: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class SettingsStore(Object):
    """"""
    Realm: Final[RealmAccess] = ...
    """
    
    :return: 
    """
    def __init__(self, realm: RealmAccess):
        """
        
        :param realm: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class Static(Enum):
    """"""
    LoginOverlayDisplayed: Static = ...
    """"""
    MutedAudioNotificationShownOnce: Static = ...
    """"""
    LowBatteryNotificationShownOnce: Static = ...
    """"""
    FeaturedArtistDisclaimerShownOnce: Static = ...
    """"""
    SeasonalBackgrounds: Static = ...
    """"""
    LastHoverSoundPlaybackTime: Static = ...
    """"""
    LastModSelectPanelSamplePlaybackTime: Static = ...
    """"""
    LastRankChangeSamplePlaybackTime: Static = ...
    """"""
    TouchInputActive: Static = ...
    """"""
    LastLocalUserScore: Static = ...
    """"""
    LastAppliedOffsetScore: Static = ...
    """"""
    DailyChallengeIntroPlayed: Static = ...
    """"""
    UserOnlineActivity: Static = ...
    """"""
    AllBeatmapTags: Static = ...
    """"""
class StorageConfig(Enum):
    """"""
    FullPath: StorageConfig = ...
    """"""
class StorageConfigManager(IniConfigManager[StorageConfig], IDisposable, ITrackableConfigManager, IConfigManager):
    """"""
    def __init__(self, storage: Storage):
        """
        
        :param storage: 
        """
    def BindWith(self, lookup: StorageConfig, bindable: Bindable[TValue]) -> None:
        """"""
    def CreateTrackedSettings(self) -> TrackedSettings:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Get(self, lookup: StorageConfig) -> TValue:
        """"""
    def GetBindable(self, lookup: StorageConfig) -> Bindable[TValue]:
        """"""
    def GetCurrentConfigurationForLogging(self) -> IDictionary[StorageConfig, str]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Load(self) -> None:
        """"""
    def LoadInto(self, settings: TrackedSettings) -> None:
        """"""
    def Save(self) -> bool:
        """"""
    def SetValue(self, lookup: StorageConfig, value: TValue) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ToolbarClockDisplayMode(Enum):
    """"""
    Analog: ToolbarClockDisplayMode = ...
    """"""
    Digital: ToolbarClockDisplayMode = ...
    """"""
    DigitalWithRuntime: ToolbarClockDisplayMode = ...
    """"""
    Full: ToolbarClockDisplayMode = ...
    """"""