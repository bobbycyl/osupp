from Realms import DynamicObjectApi
from Realms import EmbeddedObject
from Realms import IEmbeddedObject
from Realms import IRealmAccessor
from Realms import IRealmObject
from Realms import IRealmObjectBase
from Realms import ISettableManagedAccessor
from Realms import QueryArgument
from Realms import Realm
from Realms import RealmObject
from Realms.Schema import ObjectSchema
from Realms.Weaving import IRealmObjectHelper
from System import Action
from System import Array
from System import Char
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IList
from System.Collections.Generic import IReadOnlyList
from System.Collections.Generic import List
from System.ComponentModel import INotifyPropertyChanged
from System.ComponentModel import PropertyChangedEventHandler
from System import DateTime
from System import DateTimeOffset
from System import Enum
from System import Func
from System import Guid
from System import IDisposable
from System import IEquatable
from System.IO import Stream
from System import Int32
from System.Linq.Expressions import Expression
from System.Linq import IQueryable
from System import Object
from System.Reflection import IReflectableType
from System.Reflection import TypeInfo
from System.Threading import CancellationToken
from System.Threading.Tasks import Task
from System import Type
from System import ValueTuple
from System import ValueType
from __future__ import annotations
from abc import ABC
from osu.Framework.Allocation import IDependencyActivatorRegistry
from osu.Framework.Allocation import IDependencyInjectionCandidate
from osu.Framework.Allocation import ISourceGeneratedDependencyActivator
from osu.Framework.Allocation import ISourceGeneratedLongRunningLoadCache
from osu.Framework.Audio import AudioManager
from osu.Framework.Audio import IHasAmplitudes
from osu.Framework.Audio.Track import ChannelAmplitudes
from osu.Framework.Audio.Track import ITrackStore
from osu.Framework.Audio.Track import Track
from osu.Framework.Audio.Track import Waveform
from osu.Framework.Bindables import IBindable
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
from osu.Framework.Graphics import ITexturedShaderDrawable
from osu.Framework.Graphics import Invalidation
from osu.Framework.Graphics import LoadState
from osu.Framework.Graphics import MarginPadding
from osu.Framework.Graphics.Primitives import Quad
from osu.Framework.Graphics.Primitives import RectangleF
from osu.Framework.Graphics.Rendering import IRenderer
from osu.Framework.Graphics.Shaders import IShader
from osu.Framework.Graphics.Sprites import Sprite
from osu.Framework.Graphics.Textures import Texture
from osu.Framework.Graphics.Textures import TextureStore
from osu.Framework.Graphics.Textures import TextureUpload
from osu.Framework.Graphics.Transforms import ITransformable
from osu.Framework.Graphics.Transforms import Transform
from osu.Framework.IO.Stores import IResourceStore
from osu.Framework.Input.Events import UIEvent
from osu.Framework.Input import ISourceGeneratedHandleInputCache
from osu.Framework.Layout import InvalidationSource
from osu.Framework.Lists import SortedList
from osu.Framework.Localisation import LocalisableString
from osu.Framework.Localisation import RomanisableString
from osu.Framework.Platform import GameHost
from osu.Framework.Platform import Storage
from osu.Framework.Timing import FrameTimeInfo
from osu.Framework.Timing import IAdjustableClock
from osu.Framework.Timing import IClock
from osu.Framework.Timing import IFrameBasedClock
from osu.Framework.Timing import ISourceChangeableClock
from osu.Game.Beatmaps.BeatmapDifficultyCache import DifficultyCacheLookup
from osu.Game.Beatmaps.ControlPoints import ControlPointInfo
from osu.Game.Beatmaps.Timing import BreakPeriod
from osu.Game.Database import ExternalEditOperation
from osu.Game.Database import ICanAcceptFiles
from osu.Game.Database import IHasGuidPrimaryKey
from osu.Game.Database import IHasNamedFiles
from osu.Game.Database import IHasOnlineID
from osu.Game.Database import IHasRealmFiles
from osu.Game.Database import IModelDownloader
from osu.Game.Database import IModelFileManager
from osu.Game.Database import IModelImporter
from osu.Game.Database import IModelManager
from osu.Game.Database import INamedFileUsage
from osu.Game.Database import IPostNotifications
from osu.Game.Database import ISoftDelete
from osu.Game.Database import ImportParameters
from osu.Game.Database import ImportTask
from osu.Game.Database import Live
from osu.Game.Database import MemoryCachingComponent
from osu.Game.Database import ModelDownloader
from osu.Game.Database import ModelManager
from osu.Game.Database import RealmAccess
from osu.Game.Database import RealmArchiveModelImporter
from osu.Game.IO.Archives import ArchiveReader
from osu.Game.IO import IStorageResourceProvider
from osu.Game.Models import RealmNamedFileUsage
from osu.Game.Models import RealmUser
from osu.Game.Online.API import ArchiveDownloadRequest
from osu.Game.Online.API import IAPIProvider
from osu.Game.Online.API.Requests.Responses import APIBeatmap
from osu.Game.Online.API.Requests.Responses import APIUser
from osu.Game.Online import LocalUserStatisticsProvider
from osu.Game.Online.Metadata import MetadataClient
from osu.Game.Overlays.Notifications import Notification
from osu.Game.Overlays.Notifications import ProgressNotification
from osu.Game.Rulesets.Difficulty import DifficultyAttributes
from osu.Game.Rulesets.Difficulty import PerformanceAttributes
from osu.Game.Rulesets.Difficulty import TimedDifficultyAttributes
from osu.Game.Rulesets import IRulesetInfo
from osu.Game.Rulesets.Mods import Mod
from osu.Game.Rulesets.Objects import HitObject
from osu.Game.Rulesets import Ruleset
from osu.Game.Rulesets import RulesetInfo
from osu.Game.Scoring import ScoreInfo
from osu.Game.Screens.Select.FilterCriteria import OptionalTextFilter
from osu.Game.Screens.Select import OptionalTextFilter
from osu.Game.Skinning import ISkin
from osu.Game.Storyboards import Storyboard
from osu.Game.Users import IUser
from osu.Game.Utils import IDeepCloneable
from osuTK import Vector2
from typing import Callable
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Optional
from typing import Tuple
from typing import TypeVar
from typing import overload
T = TypeVar("T")
class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...
class APIBeatmapMetadataSource(Object, IDisposable, IOnlineBeatmapMetadataSource):
    """"""
    def __init__(self, api: IAPIProvider):
        """
        
        :param api: 
        """
    @property
    def Available(self) -> bool:
        """
        
        :return: 
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
    def TryLookup(self, beatmapInfo: BeatmapInfo, onlineMetadata: OnlineBeatmapMetadata) -> Tuple[bool, OnlineBeatmapMetadata]:
        """
        
        :param beatmapInfo: 
        :param onlineMetadata: 
        :return: 
        """
class APIBeatmapTag(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def TagId(self) -> int:
        """
        
        :return: 
        """
    @TagId.setter
    def TagId(self, value: int) -> None: ...
    @property
    def VoteCount(self) -> int:
        """
        
        :return: 
        """
    @VoteCount.setter
    def VoteCount(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APIFailTimes(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Fails(self) -> Array[int]:
        """
        
        :return: 
        """
    @Fails.setter
    def Fails(self, value: Array[int]) -> None: ...
    @property
    def Retries(self) -> Array[int]:
        """
        
        :return: 
        """
    @Retries.setter
    def Retries(self, value: Array[int]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class BeatSyncProviderExtensions(ABC, Object):
    """"""
    @classmethod
    def CheckIsKiaiTime(cls, provider: IBeatSyncProvider) -> bool:
        """
        
        :param provider: 
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
class Beatmap(Generic[T], Object, IBeatmap, IBeatmap[T]):
    """"""
    def __init__(self):
        """"""
    @property
    def AudioLeadIn(self) -> float:
        """
        
        :return: 
        """
    @AudioLeadIn.setter
    def AudioLeadIn(self, value: float) -> None: ...
    @property
    def BeatmapInfo(self) -> BeatmapInfo:
        """
        
        :return: 
        """
    @BeatmapInfo.setter
    def BeatmapInfo(self, value: BeatmapInfo) -> None: ...
    @property
    def BeatmapVersion(self) -> int:
        """
        
        :return: 
        """
    @BeatmapVersion.setter
    def BeatmapVersion(self, value: int) -> None: ...
    @property
    def Bookmarks(self) -> Array[int]:
        """
        
        :return: 
        """
    @Bookmarks.setter
    def Bookmarks(self, value: Array[int]) -> None: ...
    @property
    def Breaks(self) -> SortedList[BreakPeriod]:
        """
        
        :return: 
        """
    @Breaks.setter
    def Breaks(self, value: SortedList[BreakPeriod]) -> None: ...
    @property
    def ControlPointInfo(self) -> ControlPointInfo:
        """
        
        :return: 
        """
    @ControlPointInfo.setter
    def ControlPointInfo(self, value: ControlPointInfo) -> None: ...
    @property
    def Countdown(self) -> CountdownType:
        """
        
        :return: 
        """
    @Countdown.setter
    def Countdown(self, value: CountdownType) -> None: ...
    @property
    def CountdownOffset(self) -> int:
        """
        
        :return: 
        """
    @CountdownOffset.setter
    def CountdownOffset(self, value: int) -> None: ...
    @property
    def Difficulty(self) -> BeatmapDifficulty:
        """
        
        :return: 
        """
    @Difficulty.setter
    def Difficulty(self, value: BeatmapDifficulty) -> None: ...
    @property
    def DistanceSpacing(self) -> float:
        """
        
        :return: 
        """
    @DistanceSpacing.setter
    def DistanceSpacing(self, value: float) -> None: ...
    @property
    def EpilepsyWarning(self) -> bool:
        """
        
        :return: 
        """
    @EpilepsyWarning.setter
    def EpilepsyWarning(self, value: bool) -> None: ...
    @property
    def GridSize(self) -> int:
        """
        
        :return: 
        """
    @GridSize.setter
    def GridSize(self, value: int) -> None: ...
    @property
    def HitObjects(self) -> List[T]:
        """
        
        :return: 
        """
    @HitObjects.setter
    def HitObjects(self, value: List[T]) -> None: ...
    @property
    def LetterboxInBreaks(self) -> bool:
        """
        
        :return: 
        """
    @LetterboxInBreaks.setter
    def LetterboxInBreaks(self, value: bool) -> None: ...
    @property
    def Metadata(self) -> BeatmapMetadata:
        """
        
        :return: 
        """
    @property
    def SamplesMatchPlaybackRate(self) -> bool:
        """
        
        :return: 
        """
    @SamplesMatchPlaybackRate.setter
    def SamplesMatchPlaybackRate(self, value: bool) -> None: ...
    @property
    def SpecialStyle(self) -> bool:
        """
        
        :return: 
        """
    @SpecialStyle.setter
    def SpecialStyle(self, value: bool) -> None: ...
    @property
    def StackLeniency(self) -> float:
        """
        
        :return: 
        """
    @StackLeniency.setter
    def StackLeniency(self, value: float) -> None: ...
    @property
    def TimelineZoom(self) -> float:
        """
        
        :return: 
        """
    @TimelineZoom.setter
    def TimelineZoom(self, value: float) -> None: ...
    @property
    def TotalBreakTime(self) -> float:
        """
        
        :return: 
        """
    @property
    def UnhandledEventLines(self) -> List[str]:
        """
        
        :return: 
        """
    @UnhandledEventLines.setter
    def UnhandledEventLines(self, value: List[str]) -> None: ...
    @property
    def WidescreenStoryboard(self) -> bool:
        """
        
        :return: 
        """
    @WidescreenStoryboard.setter
    def WidescreenStoryboard(self, value: bool) -> None: ...
    def Clone(self) -> Beatmap[T]:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMostCommonBeatLength(self) -> float:
        """
        
        :return: 
        """
    def GetStatistics(self) -> IEnumerable[BeatmapStatistic]:
        """
        
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class Beatmap(Beatmap[HitObject], IBeatmap, IBeatmap[HitObject]):
    """"""
    def __init__(self):
        """"""
    @property
    def AudioLeadIn(self) -> float:
        """
        
        :return: 
        """
    @AudioLeadIn.setter
    def AudioLeadIn(self, value: float) -> None: ...
    @property
    def BeatmapInfo(self) -> BeatmapInfo:
        """
        
        :return: 
        """
    @BeatmapInfo.setter
    def BeatmapInfo(self, value: BeatmapInfo) -> None: ...
    @property
    def BeatmapVersion(self) -> int:
        """
        
        :return: 
        """
    @BeatmapVersion.setter
    def BeatmapVersion(self, value: int) -> None: ...
    @property
    def Bookmarks(self) -> Array[int]:
        """
        
        :return: 
        """
    @Bookmarks.setter
    def Bookmarks(self, value: Array[int]) -> None: ...
    @property
    def Breaks(self) -> SortedList[BreakPeriod]:
        """
        
        :return: 
        """
    @Breaks.setter
    def Breaks(self, value: SortedList[BreakPeriod]) -> None: ...
    @property
    def ControlPointInfo(self) -> ControlPointInfo:
        """
        
        :return: 
        """
    @ControlPointInfo.setter
    def ControlPointInfo(self, value: ControlPointInfo) -> None: ...
    @property
    def Countdown(self) -> CountdownType:
        """
        
        :return: 
        """
    @Countdown.setter
    def Countdown(self, value: CountdownType) -> None: ...
    @property
    def CountdownOffset(self) -> int:
        """
        
        :return: 
        """
    @CountdownOffset.setter
    def CountdownOffset(self, value: int) -> None: ...
    @property
    def Difficulty(self) -> BeatmapDifficulty:
        """
        
        :return: 
        """
    @Difficulty.setter
    def Difficulty(self, value: BeatmapDifficulty) -> None: ...
    @property
    def DistanceSpacing(self) -> float:
        """
        
        :return: 
        """
    @DistanceSpacing.setter
    def DistanceSpacing(self, value: float) -> None: ...
    @property
    def EpilepsyWarning(self) -> bool:
        """
        
        :return: 
        """
    @EpilepsyWarning.setter
    def EpilepsyWarning(self, value: bool) -> None: ...
    @property
    def GridSize(self) -> int:
        """
        
        :return: 
        """
    @GridSize.setter
    def GridSize(self, value: int) -> None: ...
    @property
    def HitObjects(self) -> List[HitObject]:
        """
        
        :return: 
        """
    @HitObjects.setter
    def HitObjects(self, value: List[HitObject]) -> None: ...
    @property
    def LetterboxInBreaks(self) -> bool:
        """
        
        :return: 
        """
    @LetterboxInBreaks.setter
    def LetterboxInBreaks(self, value: bool) -> None: ...
    @property
    def Metadata(self) -> BeatmapMetadata:
        """
        
        :return: 
        """
    @property
    def SamplesMatchPlaybackRate(self) -> bool:
        """
        
        :return: 
        """
    @SamplesMatchPlaybackRate.setter
    def SamplesMatchPlaybackRate(self, value: bool) -> None: ...
    @property
    def SpecialStyle(self) -> bool:
        """
        
        :return: 
        """
    @SpecialStyle.setter
    def SpecialStyle(self, value: bool) -> None: ...
    @property
    def StackLeniency(self) -> float:
        """
        
        :return: 
        """
    @StackLeniency.setter
    def StackLeniency(self, value: float) -> None: ...
    @property
    def TimelineZoom(self) -> float:
        """
        
        :return: 
        """
    @TimelineZoom.setter
    def TimelineZoom(self, value: float) -> None: ...
    @property
    def TotalBreakTime(self) -> float:
        """
        
        :return: 
        """
    @property
    def UnhandledEventLines(self) -> List[str]:
        """
        
        :return: 
        """
    @UnhandledEventLines.setter
    def UnhandledEventLines(self, value: List[str]) -> None: ...
    @property
    def WidescreenStoryboard(self) -> bool:
        """
        
        :return: 
        """
    @WidescreenStoryboard.setter
    def WidescreenStoryboard(self, value: bool) -> None: ...
    def Clone(self) -> Beatmap[HitObject]:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMostCommonBeatLength(self) -> float:
        """
        
        :return: 
        """
    def GetStatistics(self) -> IEnumerable[BeatmapStatistic]:
        """
        
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class BeatmapConverter(ABC, Generic[T], Object, IBeatmapConverter):
    """"""
    @property
    def Beatmap(self) -> IBeatmap:
        """
        
        :return: 
        """
    def CanConvert(self) -> bool:
        """
        
        :return: 
        """
    def Convert(self, cancellationToken: CancellationToken = ...) -> IBeatmap:
        """
        
        :param cancellationToken: 
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
    ObjectConverted: EventType[Action[HitObject, IEnumerable[HitObject]]] = ...
    """"""
class BeatmapDifficulty(EmbeddedObject, IEmbeddedObject, IRealmObjectBase, ISettableManagedAccessor, INotifyPropertyChanged, IReflectableType, IBeatmapDifficultyInfo):
    """"""
    DEFAULT_DIFFICULTY: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, source: IBeatmapDifficultyInfo):
        """
        
        :param source: 
        """
    @property
    def Accessor(self) -> IRealmAccessor:
        """"""
    @property
    def ApproachRate(self) -> float:
        """
        
        :return: 
        """
    @ApproachRate.setter
    def ApproachRate(self, value: float) -> None: ...
    @property
    def BacklinksCount(self) -> int:
        """"""
    @property
    def CircleSize(self) -> float:
        """
        
        :return: 
        """
    @CircleSize.setter
    def CircleSize(self, value: float) -> None: ...
    @property
    def DrainRate(self) -> float:
        """
        
        :return: 
        """
    @DrainRate.setter
    def DrainRate(self, value: float) -> None: ...
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
    def ObjectSchema(self) -> ObjectSchema:
        """"""
    @property
    def OverallDifficulty(self) -> float:
        """
        
        :return: 
        """
    @OverallDifficulty.setter
    def OverallDifficulty(self, value: float) -> None: ...
    @property
    def Parent(self) -> IRealmObjectBase:
        """"""
    @property
    def Realm(self) -> Realm:
        """"""
    @property
    def SliderMultiplier(self) -> float:
        """
        
        :return: 
        """
    @SliderMultiplier.setter
    def SliderMultiplier(self, value: float) -> None: ...
    @property
    def SliderTickRate(self) -> float:
        """
        
        :return: 
        """
    @SliderTickRate.setter
    def SliderTickRate(self, value: float) -> None: ...
    def Clone(self) -> BeatmapDifficulty:
        """
        
        :return: 
        """
    def CopyFrom(self, other: IBeatmapDifficultyInfo) -> None:
        """
        
        :param other: 
        """
    def CopyTo(self, difficulty: BeatmapDifficulty) -> None:
        """
        
        :param difficulty: 
        """
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
class BeatmapDifficultyCache(MemoryCachingComponent[BeatmapDifficultyCache.DifficultyCacheLookup, StarDifficulty], IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
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
    def GetBindableDifficulty(self, beatmapInfo: IBeatmapInfo, cancellationToken: CancellationToken = ..., computationDelay: int = ...) -> IBindable[StarDifficulty]:
        """
        
        :param beatmapInfo: 
        :param cancellationToken: 
        :param computationDelay: 
        :return: 
        """
    def GetDifficultyAsync(self, beatmapInfo: IBeatmapInfo, rulesetInfo: IRulesetInfo = ..., mods: IEnumerable[Mod] = ..., cancellationToken: CancellationToken = ..., computationDelay: int = ...) -> Task[Optional[StarDifficulty]]:
        """
        
        :param beatmapInfo: 
        :param rulesetInfo: 
        :param mods: 
        :param cancellationToken: 
        :param computationDelay: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetTimedDifficultyAttributesAsync(self, beatmap: IWorkingBeatmap, ruleset: Ruleset, mods: Array[Mod], cancellationToken: CancellationToken = ...) -> Task[List[TimedDifficultyAttributes]]:
        """
        
        :param beatmap: 
        :param ruleset: 
        :param mods: 
        :param cancellationToken: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def Hide(self) -> None:
        """"""
    @overload
    def Invalidate(self, invalidation: Invalidation = ..., source: InvalidationSource = ...) -> bool:
        """"""
    @overload
    def Invalidate(self, oldBeatmap: IBeatmapInfo, newBeatmap: IBeatmapInfo) -> None:
        """
        
        :param oldBeatmap: 
        :param newBeatmap: 
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
    class DifficultyCacheLookup(ValueType, IEquatable[BeatmapDifficultyCache.DifficultyCacheLookup]):
        """"""
        BeatmapInfo: Final[BeatmapInfo] = ...
        """"""
        OrderedMods: Final[Array[Mod]] = ...
        """"""
        Ruleset: Final[RulesetInfo] = ...
        """"""
        def __init__(self, beatmapInfo: BeatmapInfo, ruleset: RulesetInfo, mods: IEnumerable[Mod]):
            """"""
        @overload
        def Equals(self, obj: object) -> bool:
            """"""
        @overload
        def Equals(self, other: BeatmapDifficultyCache.DifficultyCacheLookup) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
class BeatmapExtensions(ABC, Object):
    """"""
    @classmethod
    def CalculateDrainLength(cls, beatmap: IBeatmap) -> float:
        """
        
        :param beatmap: 
        :return: 
        """
    @classmethod
    @overload
    def CalculatePlayableBounds(cls, objects: IEnumerable[HitObject]) -> ValueTuple[float, float]:
        """
        
        :param objects: 
        :return: 
        """
    @classmethod
    @overload
    def CalculatePlayableBounds(cls, beatmap: IBeatmap) -> ValueTuple[float, float]:
        """
        
        :param beatmap: 
        :return: 
        """
    @classmethod
    @overload
    def CalculatePlayableLength(cls, objects: IEnumerable[HitObject]) -> float:
        """
        
        :param objects: 
        :return: 
        """
    @classmethod
    @overload
    def CalculatePlayableLength(cls, beatmap: IBeatmap) -> float:
        """
        
        :param beatmap: 
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetLastObjectTime(cls, beatmap: IBeatmap) -> float:
        """
        
        :param beatmap: 
        :return: 
        """
    @classmethod
    def GetMaxCombo(cls, beatmap: IBeatmap) -> int:
        """
        
        :param beatmap: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class BeatmapImporter(RealmArchiveModelImporter[BeatmapSetInfo], ICanAcceptFiles, IModelImporter[BeatmapSetInfo], IPostNotifications):
    """"""
    def __init__(self, storage: Storage, realm: RealmAccess):
        """
        
        :param storage: 
        :param realm: 
        """
    @property
    def HandledExtensions(self) -> IEnumerable[str]:
        """
        
        :return: 
        """
    @property
    def HumanisedModelName(self) -> str:
        """
        
        :return: 
        """
    @property
    def PauseImports(self) -> bool:
        """
        
        :return: 
        """
    @PauseImports.setter
    def PauseImports(self, value: bool) -> None: ...
    @property
    def PostNotification(self) -> Action[Notification]:
        """
        
        :return: 
        """
    @PostNotification.setter
    def PostNotification(self, value: Action[Notification]) -> None: ...
    @property
    def PresentImport(self) -> Action[IEnumerable[Live[BeatmapSetInfo]]]:
        """
        
        :return: 
        """
    @PresentImport.setter
    def PresentImport(self, value: Action[IEnumerable[Live[BeatmapSetInfo]]]) -> None: ...
    @property
    def ProcessBeatmap(self) -> ProcessBeatmapDelegate:
        """
        
        :return: 
        """
    @ProcessBeatmap.setter
    def ProcessBeatmap(self, value: ProcessBeatmapDelegate) -> None: ...
    def BeginExternalEditing(self, model: BeatmapSetInfo) -> Task[ExternalEditOperation[BeatmapSetInfo]]:
        """
        
        :param model: 
        :return: 
        """
    def ComputeHash(self, item: BeatmapSetInfo) -> str:
        """
        
        :param item: 
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
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
    @overload
    def Import(self, task: ImportTask, parameters: ImportParameters = ..., cancellationToken: CancellationToken = ...) -> Task[Live[BeatmapSetInfo]]:
        """
        
        :param task: 
        :param parameters: 
        :param cancellationToken: 
        :return: 
        """
    @overload
    def Import(self, notification: ProgressNotification, tasks: Array[ImportTask], parameters: ImportParameters = ...) -> Task[IEnumerable[Live[BeatmapSetInfo]]]:
        """
        
        :param notification: 
        :param tasks: 
        :param parameters: 
        :return: 
        """
    def ImportAsUpdate(self, notification: ProgressNotification, importTask: ImportTask, original: BeatmapSetInfo) -> Task[Live[BeatmapSetInfo]]:
        """
        
        :param notification: 
        :param task: 
        :param original: 
        :return: 
        """
    def ImportModel(self, item: BeatmapSetInfo, archive: ArchiveReader = ..., parameters: ImportParameters = ..., cancellationToken: CancellationToken = ...) -> Live[BeatmapSetInfo]:
        """
        
        :param item: 
        :param archive: 
        :param parameters: 
        :param cancellationToken: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class BeatmapInfo(RealmObject, IRealmObject, IRealmObjectBase, ISettableManagedAccessor, INotifyPropertyChanged, IReflectableType, IEquatable[BeatmapInfo], IEquatable[IBeatmapInfo], IBeatmapInfo, IHasGuidPrimaryKey, IHasOnlineID[Int32]):
    """"""
    def __init__(self, ruleset: RulesetInfo = ..., difficulty: BeatmapDifficulty = ..., metadata: BeatmapMetadata = ...):
        """
        
        :param ruleset: 
        :param difficulty: 
        :param metadata: 
        """
    @property
    def Accessor(self) -> IRealmAccessor:
        """"""
    @property
    def BPM(self) -> float:
        """
        
        :return: 
        """
    @BPM.setter
    def BPM(self, value: float) -> None: ...
    @property
    def BacklinksCount(self) -> int:
        """"""
    @property
    def BeatDivisor(self) -> int:
        """
        
        :return: 
        """
    @BeatDivisor.setter
    def BeatDivisor(self, value: int) -> None: ...
    @property
    def BeatmapSet(self) -> BeatmapSetInfo:
        """
        
        :return: 
        """
    @BeatmapSet.setter
    def BeatmapSet(self, value: BeatmapSetInfo) -> None: ...
    @property
    def Difficulty(self) -> BeatmapDifficulty:
        """
        
        :return: 
        """
    @Difficulty.setter
    def Difficulty(self, value: BeatmapDifficulty) -> None: ...
    @property
    def DifficultyName(self) -> str:
        """
        
        :return: 
        """
    @DifficultyName.setter
    def DifficultyName(self, value: str) -> None: ...
    @property
    def DynamicApi(self) -> DynamicObjectApi:
        """"""
    @property
    def EditorTimestamp(self) -> Optional[float]:
        """
        
        :return: 
        """
    @EditorTimestamp.setter
    def EditorTimestamp(self, value: Optional[float]) -> None: ...
    @property
    def EndTimeObjectCount(self) -> int:
        """
        
        :return: 
        """
    @EndTimeObjectCount.setter
    def EndTimeObjectCount(self, value: int) -> None: ...
    @property
    def File(self) -> RealmNamedFileUsage:
        """
        
        :return: 
        """
    @property
    def Hash(self) -> str:
        """
        
        :return: 
        """
    @Hash.setter
    def Hash(self, value: str) -> None: ...
    @property
    def Hidden(self) -> bool:
        """
        
        :return: 
        """
    @Hidden.setter
    def Hidden(self, value: bool) -> None: ...
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
    def LastLocalUpdate(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @LastLocalUpdate.setter
    def LastLocalUpdate(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def LastOnlineUpdate(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @LastOnlineUpdate.setter
    def LastOnlineUpdate(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def LastPlayed(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @LastPlayed.setter
    def LastPlayed(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def Length(self) -> float:
        """
        
        :return: 
        """
    @Length.setter
    def Length(self, value: float) -> None: ...
    @property
    def MD5Hash(self) -> str:
        """
        
        :return: 
        """
    @MD5Hash.setter
    def MD5Hash(self, value: str) -> None: ...
    @property
    def MatchesOnlineVersion(self) -> bool:
        """
        
        :return: 
        """
    @property
    def MaxCombo(self) -> Optional[int]:
        """
        
        :return: 
        """
    @MaxCombo.setter
    def MaxCombo(self, value: Optional[int]) -> None: ...
    @property
    def Metadata(self) -> BeatmapMetadata:
        """
        
        :return: 
        """
    @Metadata.setter
    def Metadata(self, value: BeatmapMetadata) -> None: ...
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
    def OnlineInfo(self) -> APIBeatmap:
        """
        
        :return: 
        """
    @OnlineInfo.setter
    def OnlineInfo(self, value: APIBeatmap) -> None: ...
    @property
    def OnlineMD5Hash(self) -> str:
        """
        
        :return: 
        """
    @OnlineMD5Hash.setter
    def OnlineMD5Hash(self, value: str) -> None: ...
    @property
    def Path(self) -> str:
        """
        
        :return: 
        """
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
    @property
    def Scores(self) -> IQueryable[ScoreInfo]:
        """
        
        :return: 
        """
    @property
    def StarRating(self) -> float:
        """
        
        :return: 
        """
    @StarRating.setter
    def StarRating(self, value: float) -> None: ...
    @property
    def Status(self) -> BeatmapOnlineStatus:
        """
        
        :return: 
        """
    @Status.setter
    def Status(self, value: BeatmapOnlineStatus) -> None: ...
    @property
    def StatusInt(self) -> int:
        """
        
        :return: 
        """
    @StatusInt.setter
    def StatusInt(self, value: int) -> None: ...
    @property
    def TotalObjectCount(self) -> int:
        """
        
        :return: 
        """
    @TotalObjectCount.setter
    def TotalObjectCount(self, value: int) -> None: ...
    @property
    def UserSettings(self) -> BeatmapUserSettings:
        """
        
        :return: 
        """
    @UserSettings.setter
    def UserSettings(self, value: BeatmapUserSettings) -> None: ...
    def AudioEquals(self, other: BeatmapInfo) -> bool:
        """
        
        :param other: 
        :return: 
        """
    def BackgroundEquals(self, other: BeatmapInfo) -> bool:
        """
        
        :param other: 
        :return: 
        """
    def Clone(self) -> BeatmapInfo:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: BeatmapInfo) -> bool:
        """"""
    @overload
    def Equals(self, other: IBeatmapInfo) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self) -> TypeInfo:
        """"""
    def ResetOnlineInfo(self, resetOnlineId: bool = ...) -> None:
        """
        
        :param resetOnlineId: 
        """
    def SetManagedAccessor(self, accessor: IRealmAccessor, helper: IRealmObjectHelper = ..., update: bool = ..., skipDefaults: bool = ...) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransferCollectionReferences(self, realm: Realm, previousMD5Hash: str) -> None:
        """
        
        :param realm: 
        :param previousMD5Hash: 
        """
    def UpdateLocalScores(self, realm: Realm) -> None:
        """
        
        :param realm: 
        """
    PropertyChanged: EventType[PropertyChangedEventHandler] = ...
    """"""
class BeatmapInfoExtensions(ABC, Object):
    """"""
    @classmethod
    def AllowGameplayWithRuleset(cls, beatmap: IBeatmapInfo, ruleset: RulesetInfo, allowConversion: bool) -> bool:
        """
        
        :param beatmap: 
        :param ruleset: 
        :param allowConversion: 
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetDisplayTitle(cls, beatmapInfo: IBeatmapInfo) -> str:
        """
        
        :param beatmapInfo: 
        :return: 
        """
    @classmethod
    def GetDisplayTitleRomanisable(cls, beatmapInfo: IBeatmapInfo, includeDifficultyName: bool = ..., includeCreator: bool = ...) -> RomanisableString:
        """
        
        :param beatmapInfo: 
        :param includeDifficultyName: 
        :param includeCreator: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetOnlineURL(cls, beatmapInfo: IBeatmapInfo, api: IAPIProvider, ruleset: IRulesetInfo = ...) -> str:
        """
        
        :param beatmapInfo: 
        :param api: 
        :param ruleset: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Match(cls, beatmapInfo: IBeatmapInfo, filters: Array[OptionalTextFilter]) -> bool:
        """
        
        :param beatmapInfo: 
        :param filters: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    @classmethod
    def UpdateStatisticsFromBeatmap(cls, beatmapInfo: BeatmapInfo, beatmap: IBeatmap) -> None:
        """
        
        :param beatmapInfo: 
        :param beatmap: 
        """
class BeatmapManager(ModelManager[BeatmapSetInfo], IWorkingBeatmapCache, ICanAcceptFiles, IModelFileManager[BeatmapSetInfo, RealmNamedFileUsage], IModelImporter[BeatmapSetInfo], IModelManager[BeatmapSetInfo], IPostNotifications):
    """"""
    def __init__(self, storage: Storage, realm: RealmAccess, api: IAPIProvider, audioManager: AudioManager, gameResources: IResourceStore[Array[int]], host: GameHost = ..., defaultBeatmap: WorkingBeatmap = ..., difficultyCache: BeatmapDifficultyCache = ..., performOnlineLookups: bool = ...):
        """
        
        :param storage: 
        :param realm: 
        :param api: 
        :param audioManager: 
        :param gameResources: 
        :param host: 
        :param defaultBeatmap: 
        :param difficultyCache: 
        :param performOnlineLookups: 
        """
    @property
    def BeatmapTrackStore(self) -> ITrackStore:
        """
        
        :return: 
        """
    @property
    def DefaultBeatmap(self) -> IWorkingBeatmap:
        """
        
        :return: 
        """
    @property
    def HandledExtensions(self) -> IEnumerable[str]:
        """
        
        :return: 
        """
    @property
    def HumanisedModelName(self) -> str:
        """
        
        :return: 
        """
    @property
    def PauseImports(self) -> bool:
        """
        
        :return: 
        """
    @PauseImports.setter
    def PauseImports(self, value: bool) -> None: ...
    @property
    def PostNotification(self) -> Action[Notification]:
        """
        
        :return: 
        """
    @PostNotification.setter
    def PostNotification(self, value: Action[Notification]) -> None: ...
    @property
    def PresentImport(self) -> Action[IEnumerable[Live[BeatmapSetInfo]]]:
        """
        
        :return: 
        """
    @PresentImport.setter
    def PresentImport(self, value: Action[IEnumerable[Live[BeatmapSetInfo]]]) -> None: ...
    @property
    def ProcessBeatmap(self) -> ProcessBeatmapDelegate:
        """
        
        :return: 
        """
    @ProcessBeatmap.setter
    def ProcessBeatmap(self, value: ProcessBeatmapDelegate) -> None: ...
    @overload
    def AddFile(self, item: BeatmapSetInfo, contents: Stream, filename: str) -> None:
        """
        
        :param model: 
        :param contents: 
        :param filename: 
        """
    @overload
    def AddFile(self, item: BeatmapSetInfo, contents: Stream, filename: str, realm: Realm) -> None:
        """
        
        :param item: 
        :param contents: 
        :param filename: 
        :param realm: 
        """
    def BeginExternalEditing(self, model: BeatmapSetInfo) -> Task[ExternalEditOperation[BeatmapSetInfo]]:
        """
        
        :param model: 
        :return: 
        """
    def CanHide(self, beatmapInfo: BeatmapInfo) -> bool:
        """
        
        :param beatmapInfo: 
        :return: 
        """
    def CopyExistingDifficulty(self, targetBeatmapSet: BeatmapSetInfo, referenceWorkingBeatmap: WorkingBeatmap) -> WorkingBeatmap:
        """
        
        :param targetBeatmapSet: 
        :param referenceWorkingBeatmap: 
        :return: 
        """
    def CreateNew(self, ruleset: RulesetInfo, user: APIUser) -> WorkingBeatmap:
        """
        
        :param ruleset: 
        :param user: 
        :return: 
        """
    def CreateNewDifficulty(self, targetBeatmapSet: BeatmapSetInfo, referenceWorkingBeatmap: WorkingBeatmap, rulesetInfo: RulesetInfo) -> WorkingBeatmap:
        """
        
        :param targetBeatmapSet: 
        :param referenceWorkingBeatmap: 
        :param rulesetInfo: 
        :return: 
        """
    @overload
    def Delete(self, item: BeatmapSetInfo) -> bool:
        """
        
        :param item: 
        :return: 
        """
    @overload
    def Delete(self, items: List[BeatmapSetInfo], silent: bool = ...) -> None:
        """
        
        :param item: 
        :return: 
        """
    @overload
    def Delete(self, filter: Expression[Func, bool] = ..., silent: bool = ...) -> None:
        """"""
    def DeleteAllVideos(self) -> None:
        """"""
    def DeleteDifficultyImmediately(self, beatmapInfo: BeatmapInfo) -> None:
        """
        
        :param beatmapInfo: 
        """
    @overload
    def DeleteFile(self, item: BeatmapSetInfo, file: RealmNamedFileUsage) -> None:
        """
        
        :param model: 
        :param file: 
        """
    @overload
    def DeleteFile(self, item: BeatmapSetInfo, file: RealmNamedFileUsage, realm: Realm) -> None:
        """
        
        :param item: 
        :param file: 
        :param realm: 
        """
    def DeleteVideos(self, items: List[BeatmapSetInfo], silent: bool = ...) -> None:
        """
        
        :param items: 
        :param silent: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def Export(self, beatmapSet: BeatmapSetInfo) -> Task:
        """
        
        :param beatmapSet: 
        :return: 
        """
    @overload
    def ExportLegacy(self, beatmap: BeatmapInfo) -> Task:
        """
        
        :param beatmap: 
        :return: 
        """
    @overload
    def ExportLegacy(self, beatmapSet: BeatmapSetInfo) -> Task:
        """
        
        :param beatmapSet: 
        :return: 
        """
    def GetAllUsableBeatmapSets(self) -> List[BeatmapSetInfo]:
        """
        
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def GetWorkingBeatmap(self, beatmapInfo: BeatmapInfo) -> WorkingBeatmap:
        """
        
        :param beatmapInfo: 
        :return: 
        """
    @overload
    def GetWorkingBeatmap(self, beatmapInfo: BeatmapInfo, refetch: bool = ...) -> WorkingBeatmap:
        """
        
        :param beatmapInfo: 
        :param refetch: 
        :return: 
        """
    def Hide(self, beatmapInfo: BeatmapInfo) -> bool:
        """
        
        :param beatmapInfo: 
        :return: 
        """
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
    @overload
    def Import(self, item: BeatmapSetInfo, archive: ArchiveReader = ..., cancellationToken: CancellationToken = ...) -> Live[BeatmapSetInfo]:
        """
        
        :param item: 
        :param archive: 
        :param cancellationToken: 
        :return: 
        """
    @overload
    def Import(self, task: ImportTask, parameters: ImportParameters = ..., cancellationToken: CancellationToken = ...) -> Task[Live[BeatmapSetInfo]]:
        """
        
        :param task: 
        :param parameters: 
        :param cancellationToken: 
        :return: 
        """
    @overload
    def Import(self, notification: ProgressNotification, tasks: Array[ImportTask], parameters: ImportParameters = ...) -> Task[IEnumerable[Live[BeatmapSetInfo]]]:
        """
        
        :param notification: 
        :param tasks: 
        :param parameters: 
        :return: 
        """
    def ImportAsUpdate(self, notification: ProgressNotification, importTask: ImportTask, original: BeatmapSetInfo) -> Task[Live[BeatmapSetInfo]]:
        """
        
        :param notification: 
        :param task: 
        :param original: 
        :return: 
        """
    @overload
    def Invalidate(self, beatmapInfo: BeatmapInfo) -> None:
        """
        
        :param beatmapInfo: 
        """
    @overload
    def Invalidate(self, beatmapSetInfo: BeatmapSetInfo) -> None:
        """
        
        :param beatmapSetInfo: 
        """
    @overload
    def IsAvailableLocally(self, model: BeatmapSetInfo) -> bool:
        """
        
        :param model: 
        :return: 
        """
    @overload
    def IsAvailableLocally(self, model: IBeatmapInfo) -> bool:
        """
        
        :param model: 
        :return: 
        """
    def MarkNotPlayed(self, beatmapSetInfo: BeatmapInfo) -> None:
        """
        
        :param beatmapSetInfo: 
        """
    def MarkPlayed(self, beatmapSetInfo: BeatmapInfo) -> None:
        """
        
        :param beatmapSetInfo: 
        """
    @overload
    def QueryBeatmap(self, query: Expression[Func, bool]) -> BeatmapInfo:
        """"""
    @overload
    def QueryBeatmap(self, query: str, arguments: Array[QueryArgument]) -> BeatmapInfo:
        """
        
        :param query: 
        :param arguments: 
        :return: 
        """
    def QueryBeatmapSet(self, query: Expression[Func, bool]) -> Live[BeatmapSetInfo]:
        """"""
    def QueryOnlineBeatmapId(self, id: int) -> BeatmapInfo:
        """
        
        :param id: 
        :return: 
        """
    @overload
    def ReplaceFile(self, item: BeatmapSetInfo, file: RealmNamedFileUsage, contents: Stream) -> None:
        """
        
        :param model: 
        :param file: 
        :param contents: 
        """
    @overload
    def ReplaceFile(self, file: RealmNamedFileUsage, contents: Stream, realm: Realm) -> None:
        """
        
        :param file: 
        :param contents: 
        :param realm: 
        """
    def ResetAllOffsets(self) -> None:
        """"""
    def Restore(self, beatmapInfo: BeatmapInfo) -> None:
        """
        
        :param beatmapInfo: 
        """
    def RestoreAll(self) -> None:
        """"""
    def Save(self, beatmapInfo: BeatmapInfo, beatmapContent: IBeatmap, beatmapSkin: ISkin = ...) -> None:
        """
        
        :param beatmapInfo: 
        :param beatmapContent: 
        :param beatmapSkin: 
        """
    def ToString(self) -> str:
        """"""
    @overload
    def Undelete(self, item: BeatmapSetInfo) -> None:
        """
        
        :param item: 
        """
    @overload
    def Undelete(self, items: List[BeatmapSetInfo], silent: bool = ...) -> None:
        """
        
        :param item: 
        """
    def UndeleteAll(self) -> None:
        """"""
    OnInvalidated: EventType[Action[WorkingBeatmap]] = ...
    """"""
class BeatmapMetadata(RealmObject, IRealmObject, IRealmObjectBase, ISettableManagedAccessor, INotifyPropertyChanged, IReflectableType, IEquatable[IBeatmapMetadataInfo], IBeatmapMetadataInfo, IDeepCloneable[BeatmapMetadata]):
    """"""
    def __init__(self, user: RealmUser = ...):
        """
        
        :param user: 
        """
    @property
    def Accessor(self) -> IRealmAccessor:
        """"""
    @property
    def Artist(self) -> str:
        """
        
        :return: 
        """
    @Artist.setter
    def Artist(self, value: str) -> None: ...
    @property
    def ArtistUnicode(self) -> str:
        """
        
        :return: 
        """
    @ArtistUnicode.setter
    def ArtistUnicode(self, value: str) -> None: ...
    @property
    def AudioFile(self) -> str:
        """
        
        :return: 
        """
    @AudioFile.setter
    def AudioFile(self, value: str) -> None: ...
    @property
    def Author(self) -> RealmUser:
        """
        
        :return: 
        """
    @Author.setter
    def Author(self, value: RealmUser) -> None: ...
    @property
    def BackgroundFile(self) -> str:
        """
        
        :return: 
        """
    @BackgroundFile.setter
    def BackgroundFile(self, value: str) -> None: ...
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
    def ObjectSchema(self) -> ObjectSchema:
        """"""
    @property
    def PreviewTime(self) -> int:
        """
        
        :return: 
        """
    @PreviewTime.setter
    def PreviewTime(self, value: int) -> None: ...
    @property
    def Realm(self) -> Realm:
        """"""
    @property
    def Source(self) -> str:
        """
        
        :return: 
        """
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def Tags(self) -> str:
        """
        
        :return: 
        """
    @Tags.setter
    def Tags(self, value: str) -> None: ...
    @property
    def Title(self) -> str:
        """
        
        :return: 
        """
    @Title.setter
    def Title(self, value: str) -> None: ...
    @property
    def TitleUnicode(self) -> str:
        """
        
        :return: 
        """
    @TitleUnicode.setter
    def TitleUnicode(self, value: str) -> None: ...
    @property
    def UserTags(self) -> IList[str]:
        """
        
        :return: 
        """
    def DeepClone(self) -> BeatmapMetadata:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IBeatmapMetadataInfo) -> bool:
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
class BeatmapMetadataInfoExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetDisplayTitle(cls, metadataInfo: IBeatmapMetadataInfo) -> str:
        """
        
        :param metadataInfo: 
        :return: 
        """
    @classmethod
    def GetDisplayTitleRomanisable(cls, metadataInfo: IBeatmapMetadataInfo, includeCreator: bool = ...) -> RomanisableString:
        """
        
        :param metadataInfo: 
        :param includeCreator: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetSearchableTerms(cls, metadataInfo: IBeatmapMetadataInfo) -> Array[str]:
        """
        
        :param metadataInfo: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Match(cls, metadataInfo: IBeatmapMetadataInfo, filter: FilterCriteria.OptionalTextFilter) -> bool:
        """
        
        :param metadataInfo: 
        :param filter: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class BeatmapModelDownloader(ModelDownloader[BeatmapSetInfo, IBeatmapSetInfo], IModelDownloader[IBeatmapSetInfo], IPostNotifications):
    """"""
    def __init__(self, beatmapImporter: IModelImporter[BeatmapSetInfo], api: IAPIProvider):
        """
        
        :param beatmapImporter: 
        :param api: 
        """
    @property
    def PostNotification(self) -> Action[Notification]:
        """
        
        :return: 
        """
    @PostNotification.setter
    def PostNotification(self, value: Action[Notification]) -> None: ...
    def Download(self, model: IBeatmapSetInfo, minimiseDownloadSize: bool = ...) -> bool:
        """
        
        :param item: 
        :param minimiseDownloadSize: 
        :return: 
        """
    def DownloadAsUpdate(self, originalModel: BeatmapSetInfo, minimiseDownloadSize: bool) -> None:
        """
        
        :param originalModel: 
        :param minimiseDownloadSize: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetExistingDownload(self, model: IBeatmapSetInfo) -> ArchiveDownloadRequest[IBeatmapSetInfo]:
        """
        
        :param item: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    DownloadBegan: EventType[Action[ArchiveDownloadRequest[IBeatmapSetInfo]]] = ...
    """"""
    DownloadFailed: EventType[Action[ArchiveDownloadRequest[IBeatmapSetInfo]]] = ...
    """"""
class BeatmapOnlineChangeIngest(Component, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
    """"""
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    def __init__(self, beatmapUpdater: IBeatmapUpdater, realm: RealmAccess, metadataClient: MetadataClient):
        """
        
        :param beatmapUpdater: 
        :param realm: 
        :param metadataClient: 
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
class BeatmapOnlineStatus(Enum):
    """"""
    Pending: BeatmapOnlineStatus = ...
    """"""
    Ranked: BeatmapOnlineStatus = ...
    """"""
    Approved: BeatmapOnlineStatus = ...
    """"""
    Qualified: BeatmapOnlineStatus = ...
    """"""
    Loved: BeatmapOnlineStatus = ...
    """"""
    LocallyModified: BeatmapOnlineStatus = ...
    """"""
    _None: BeatmapOnlineStatus = ...
    """"""
    Graveyard: BeatmapOnlineStatus = ...
    """"""
    WIP: BeatmapOnlineStatus = ...
    """"""
class BeatmapPanelBackgroundTextureLoaderStore(Object, IDisposable, IResourceStore[TextureUpload]):
    """"""
    def __init__(self, textureStore: IResourceStore[TextureUpload]):
        """
        
        :param textureStore: 
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Get(self, name: str) -> TextureUpload:
        """"""
    def GetAsync(self, name: str, cancellationToken: CancellationToken = ...) -> Task[TextureUpload]:
        """"""
    def GetAvailableResources(self) -> IEnumerable[str]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetStream(self, name: str) -> Stream:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class BeatmapProcessor(Object, IBeatmapProcessor):
    """"""
    def __init__(self, beatmap: IBeatmap):
        """
        
        :param beatmap: 
        """
    @property
    def Beatmap(self) -> IBeatmap:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PostProcess(self) -> None:
        """"""
    def PreProcess(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class BeatmapSetHypeStatus(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Current(self) -> int:
        """
        
        :return: 
        """
    @Current.setter
    def Current(self, value: int) -> None: ...
    @property
    def Required(self) -> int:
        """
        
        :return: 
        """
    @Required.setter
    def Required(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class BeatmapSetInfo(RealmObject, IRealmObject, IRealmObjectBase, ISettableManagedAccessor, INotifyPropertyChanged, IReflectableType, IEquatable[BeatmapSetInfo], IEquatable[IBeatmapSetInfo], IBeatmapSetInfo, IHasGuidPrimaryKey, IHasNamedFiles, IHasOnlineID[Int32], IHasRealmFiles, ISoftDelete):
    """"""
    def __init__(self, beatmaps: IEnumerable[BeatmapInfo] = ...):
        """
        
        :param beatmaps: 
        """
    @property
    def Accessor(self) -> IRealmAccessor:
        """"""
    @property
    def AllBeatmapsUpToDate(self) -> bool:
        """
        
        :return: 
        """
    @property
    def BacklinksCount(self) -> int:
        """"""
    @property
    def Beatmaps(self) -> IList[BeatmapInfo]:
        """
        
        :return: 
        """
    @property
    def DateAdded(self) -> DateTimeOffset:
        """
        
        :return: 
        """
    @DateAdded.setter
    def DateAdded(self, value: DateTimeOffset) -> None: ...
    @property
    def DateRanked(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @DateRanked.setter
    def DateRanked(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def DateSubmitted(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @DateSubmitted.setter
    def DateSubmitted(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def DeletePending(self) -> bool:
        """
        
        :return: 
        """
    @DeletePending.setter
    def DeletePending(self, value: bool) -> None: ...
    @property
    def DynamicApi(self) -> DynamicObjectApi:
        """"""
    @property
    def Files(self) -> IList[RealmNamedFileUsage]:
        """
        
        :return: 
        """
    @property
    def Hash(self) -> str:
        """
        
        :return: 
        """
    @Hash.setter
    def Hash(self, value: str) -> None: ...
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
    def MaxBPM(self) -> float:
        """
        
        :return: 
        """
    @property
    def MaxLength(self) -> float:
        """
        
        :return: 
        """
    @property
    def MaxStarDifficulty(self) -> float:
        """
        
        :return: 
        """
    @property
    def Metadata(self) -> IBeatmapMetadataInfo:
        """
        
        :return: 
        """
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
    def Protected(self) -> bool:
        """
        
        :return: 
        """
    @Protected.setter
    def Protected(self, value: bool) -> None: ...
    @property
    def Realm(self) -> Realm:
        """"""
    @property
    def Status(self) -> BeatmapOnlineStatus:
        """
        
        :return: 
        """
    @Status.setter
    def Status(self, value: BeatmapOnlineStatus) -> None: ...
    @property
    def StatusInt(self) -> int:
        """
        
        :return: 
        """
    @StatusInt.setter
    def StatusInt(self, value: int) -> None: ...
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: BeatmapSetInfo) -> bool:
        """"""
    @overload
    def Equals(self, other: IBeatmapSetInfo) -> bool:
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
class BeatmapSetInfoExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetFile(cls, model: IHasRealmFiles, filename: str) -> RealmNamedFileUsage:
        """
        
        :param model: 
        :param filename: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetOnlineURL(cls, beatmapSetInfo: IBeatmapSetInfo, api: IAPIProvider, ruleset: IRulesetInfo = ...) -> str:
        """
        
        :param beatmapSetInfo: 
        :param api: 
        :param ruleset: 
        :return: 
        """
    @classmethod
    def GetPathForFile(cls, model: IHasRealmFiles, filename: str) -> str:
        """
        
        :param model: 
        :param filename: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class BeatmapSetNominationRequiredMeta(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def MainRuleset(self) -> int:
        """
        
        :return: 
        """
    @MainRuleset.setter
    def MainRuleset(self, value: int) -> None: ...
    @property
    def NonMainRuleset(self) -> int:
        """
        
        :return: 
        """
    @NonMainRuleset.setter
    def NonMainRuleset(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class BeatmapSetNominationStatus(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Current(self) -> int:
        """
        
        :return: 
        """
    @Current.setter
    def Current(self, value: int) -> None: ...
    @property
    def RequiredMeta(self) -> BeatmapSetNominationRequiredMeta:
        """
        
        :return: 
        """
    @RequiredMeta.setter
    def RequiredMeta(self, value: BeatmapSetNominationRequiredMeta) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class BeatmapSetOnlineAvailability(ValueType):
    """"""
    @property
    def DownloadDisabled(self) -> bool:
        """
        
        :return: 
        """
    @DownloadDisabled.setter
    def DownloadDisabled(self, value: bool) -> None: ...
    @property
    def ExternalLink(self) -> str:
        """
        
        :return: 
        """
    @ExternalLink.setter
    def ExternalLink(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class BeatmapSetOnlineCovers(ValueType):
    """"""
    @property
    def Card(self) -> str:
        """
        
        :return: 
        """
    @Card.setter
    def Card(self, value: str) -> None: ...
    @property
    def CardLowRes(self) -> str:
        """
        
        :return: 
        """
    @CardLowRes.setter
    def CardLowRes(self, value: str) -> None: ...
    @property
    def Cover(self) -> str:
        """
        
        :return: 
        """
    @Cover.setter
    def Cover(self, value: str) -> None: ...
    @property
    def CoverLowRes(self) -> str:
        """
        
        :return: 
        """
    @CoverLowRes.setter
    def CoverLowRes(self, value: str) -> None: ...
    @property
    def List(self) -> str:
        """
        
        :return: 
        """
    @List.setter
    def List(self, value: str) -> None: ...
    @property
    def ListLowRes(self) -> str:
        """
        
        :return: 
        """
    @ListLowRes.setter
    def ListLowRes(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class BeatmapSetOnlineGenre(ValueType):
    """"""
    @property
    def Id(self) -> int:
        """
        
        :return: 
        """
    @Id.setter
    def Id(self, value: int) -> None: ...
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class BeatmapSetOnlineLanguage(ValueType):
    """"""
    @property
    def Id(self) -> int:
        """
        
        :return: 
        """
    @Id.setter
    def Id(self, value: int) -> None: ...
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class BeatmapSetOnlineNomination(ValueType):
    """"""
    @property
    def BeatmapsetId(self) -> int:
        """
        
        :return: 
        """
    @BeatmapsetId.setter
    def BeatmapsetId(self, value: int) -> None: ...
    @property
    def Reset(self) -> bool:
        """
        
        :return: 
        """
    @Reset.setter
    def Reset(self, value: bool) -> None: ...
    @property
    def Rulesets(self) -> Array[str]:
        """
        
        :return: 
        """
    @Rulesets.setter
    def Rulesets(self, value: Array[str]) -> None: ...
    @property
    def UserId(self) -> int:
        """
        
        :return: 
        """
    @UserId.setter
    def UserId(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class BeatmapSetOnlineStatusExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GrantsPerformancePoints(cls, status: BeatmapOnlineStatus) -> bool:
        """
        
        :param status: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class BeatmapStatistic(Object):
    """"""
    BarDisplayLength: Final[Optional[float]] = ...
    """
    
    :return: 
    """
    Content: Final[str] = ...
    """
    
    :return: 
    """
    CreateIcon: Final[Func[Drawable]] = ...
    """
    
    :return: 
    """
    Name: Final[LocalisableString] = ...
    """
    
    :return: 
    """
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
class BeatmapStatisticIcon(Sprite, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ITexturedShaderDrawable, ISourceGeneratedHandleInputCache):
    """"""
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    def __init__(self, iconType: BeatmapStatisticsIconType):
        """
        
        :param iconType: 
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
    def ConservativeScreenSpaceDrawQuad(self) -> Quad:
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
    def DrawTextureRectangle(self) -> RectangleF:
        """"""
    @property
    def DrawWidth(self) -> float:
        """"""
    @property
    def EdgeSmoothness(self) -> Vector2:
        """"""
    @EdgeSmoothness.setter
    def EdgeSmoothness(self, value: Vector2) -> None: ...
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
    def InflationAmount(self) -> Vector2:
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
    def Texture(self) -> Texture:
        """"""
    @Texture.setter
    def Texture(self, value: Texture) -> None: ...
    @property
    def TextureRectangle(self) -> RectangleF:
        """"""
    @TextureRectangle.setter
    def TextureRectangle(self, value: RectangleF) -> None: ...
    @property
    def TextureRelativeSizeAxes(self) -> Axes:
        """"""
    @TextureRelativeSizeAxes.setter
    def TextureRelativeSizeAxes(self, value: Axes) -> None: ...
    @property
    def TextureShader(self) -> IShader:
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
class BeatmapStatisticsIconType(Enum):
    """"""
    Accuracy: BeatmapStatisticsIconType = ...
    """"""
    ApproachRate: BeatmapStatisticsIconType = ...
    """"""
    Bpm: BeatmapStatisticsIconType = ...
    """"""
    Circles: BeatmapStatisticsIconType = ...
    """"""
    HpDrain: BeatmapStatisticsIconType = ...
    """"""
    Length: BeatmapStatisticsIconType = ...
    """"""
    OverallDifficulty: BeatmapStatisticsIconType = ...
    """"""
    Size: BeatmapStatisticsIconType = ...
    """"""
    Sliders: BeatmapStatisticsIconType = ...
    """"""
    Spinners: BeatmapStatisticsIconType = ...
    """"""
class BeatmapUpdater(Object, IDisposable, IBeatmapUpdater):
    """"""
    def __init__(self, workingBeatmapCache: IWorkingBeatmapCache, difficultyCache: BeatmapDifficultyCache, api: IAPIProvider, storage: Storage):
        """
        
        :param workingBeatmapCache: 
        :param difficultyCache: 
        :param api: 
        :param storage: 
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Process(self, beatmapSet: BeatmapSetInfo, lookupScope: MetadataLookupScope = ...) -> None:
        """
        
        :param beatmapSet: 
        :param lookupScope: 
        """
    def ProcessObjectCounts(self, beatmapInfo: BeatmapInfo, lookupScope: MetadataLookupScope = ...) -> None:
        """
        
        :param beatmapInfo: 
        :param lookupScope: 
        """
    def Queue(self, beatmapSet: Live[BeatmapSetInfo], lookupScope: MetadataLookupScope = ...) -> None:
        """
        
        :param beatmapSet: 
        :param lookupScope: 
        """
    def ToString(self) -> str:
        """"""
class BeatmapUpdaterMetadataLookup(Object, IDisposable):
    """"""
    def __init__(self, api: IAPIProvider, storage: Storage):
        """
        
        :param api: 
        :param storage: 
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
    def Update(self, beatmapSet: BeatmapSetInfo, preferOnlineFetch: bool) -> None:
        """
        
        :param beatmapSet: 
        :param preferOnlineFetch: 
        """
class BeatmapUserSettings(EmbeddedObject, IEmbeddedObject, IRealmObjectBase, ISettableManagedAccessor, INotifyPropertyChanged, IReflectableType):
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
    def ObjectSchema(self) -> ObjectSchema:
        """"""
    @property
    def Offset(self) -> float:
        """
        
        :return: 
        """
    @Offset.setter
    def Offset(self, value: float) -> None: ...
    @property
    def Parent(self) -> IRealmObjectBase:
        """"""
    @property
    def Realm(self) -> Realm:
        """"""
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
class CountdownType(Enum):
    """"""
    _None: CountdownType = ...
    """"""
    Normal: CountdownType = ...
    """"""
    HalfSpeed: CountdownType = ...
    """"""
    DoubleSpeed: CountdownType = ...
    """"""
class DifficultyRange(ValueType, IEquatable[DifficultyRange]):
    """"""
    def __init__(self, Min: float, Mid: float, Max: float):
        """
        
        :param Min: 
        :param Mid: 
        :param Max: 
        """
    @property
    def Max(self) -> float:
        """
        
        :return: 
        """
    @Max.setter
    def Max(self, value: float) -> None: ...
    @property
    def Mid(self) -> float:
        """
        
        :return: 
        """
    @Mid.setter
    def Mid(self, value: float) -> None: ...
    @property
    def Min(self) -> float:
        """
        
        :return: 
        """
    @Min.setter
    def Min(self, value: float) -> None: ...
    def Deconstruct(self, Min: float, Mid: float, Max: float) -> Tuple[None, float, float, float]:
        """
        
        :param Min: 
        :param Mid: 
        :param Max: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: DifficultyRange) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __eq__(self, other: DifficultyRange) -> bool:
        """
        
        :param other: 
        :return: 
        """
    def __ne__(self, other: DifficultyRange) -> bool:
        """
        
        :param other: 
        :return: 
        """
    @classmethod
    def op_Equality(cls, left: DifficultyRange, right: DifficultyRange) -> bool:
        """
        
        :param left: 
        :param right: 
        :return: 
        """
    @classmethod
    def op_Inequality(cls, left: DifficultyRange, right: DifficultyRange) -> bool:
        """
        
        :param left: 
        :param right: 
        :return: 
        """
class DifficultyRating(Enum):
    """"""
    Easy: DifficultyRating = ...
    """"""
    Normal: DifficultyRating = ...
    """"""
    Hard: DifficultyRating = ...
    """"""
    Insane: DifficultyRating = ...
    """"""
    Expert: DifficultyRating = ...
    """"""
    ExpertPlus: DifficultyRating = ...
    """"""
class DifficultyRecommender(Component, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
    """"""
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    def __init__(self, statisticsProvider: LocalUserStatisticsProvider):
        """
        
        :param statisticsProvider: 
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
    def GetHashCode(self) -> int:
        """"""
    def GetRecommendedBeatmap(self, beatmaps: IEnumerable[BeatmapInfo]) -> BeatmapInfo:
        """
        
        :param beatmaps: 
        :return: 
        """
    def GetRecommendedStarRatingFor(self, ruleset: RulesetInfo) -> Optional[float]:
        """
        
        :param ruleset: 
        :return: 
        """
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
    StarRatingUpdated: EventType[Action] = ...
    """"""
class DummyWorkingBeatmap(WorkingBeatmap, IWorkingBeatmap):
    """"""
    BeatmapInfo: Final[BeatmapInfo] = ...
    """
    
    :return: 
    """
    BeatmapSetInfo: Final[BeatmapSetInfo] = ...
    """
    
    :return: 
    """
    def __init__(self, audio: AudioManager, textures: TextureStore):
        """
        
        :param audio: 
        :param textures: 
        """
    @property
    def Beatmap(self) -> IBeatmap:
        """
        
        :return: 
        """
    @property
    def BeatmapInfo(self) -> IBeatmapInfo:
        """
        
        :return: 
        """
    @property
    def BeatmapLoaded(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Metadata(self) -> BeatmapMetadata:
        """
        
        :return: 
        """
    @property
    def Skin(self) -> ISkin:
        """
        
        :return: 
        """
    @property
    def Storyboard(self) -> Storyboard:
        """
        
        :return: 
        """
    @property
    def Track(self) -> Track:
        """
        
        :return: 
        """
    @property
    def TrackLoaded(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Waveform(self) -> Waveform:
        """
        
        :return: 
        """
    def BeginAsyncLoad(self) -> None:
        """"""
    def CancelAsyncLoad(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBackground(self) -> Texture:
        """
        
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetPanelBackground(self) -> Texture:
        """
        
        :return: 
        """
    @overload
    def GetPlayableBeatmap(self, ruleset: IRulesetInfo, mods: IReadOnlyList[Mod] = ...) -> IBeatmap:
        """
        
        :param ruleset: 
        :param mods: 
        :return: 
        """
    @overload
    def GetPlayableBeatmap(self, ruleset: IRulesetInfo, mods: IReadOnlyList[Mod], token: CancellationToken) -> IBeatmap:
        """
        
        :param ruleset: 
        :param mods: 
        :param cancellationToken: 
        :return: 
        """
    def GetStream(self, storagePath: str) -> Stream:
        """
        
        :param storagePath: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def LoadTrack(self) -> Track:
        """
        
        :return: 
        """
    def PrepareTrackForPreview(self, looping: bool, offsetFromPreviewPoint: float = ...) -> None:
        """
        
        :param looping: 
        :param offsetFromPreviewPoint: 
        """
    def ToString(self) -> str:
        """"""
    def TryTransferTrack(self, target: WorkingBeatmap) -> bool:
        """
        
        :param target: 
        :return: 
        """
class FlatWorkingBeatmap(WorkingBeatmap, IWorkingBeatmap):
    """"""
    BeatmapInfo: Final[BeatmapInfo] = ...
    """
    
    :return: 
    """
    BeatmapSetInfo: Final[BeatmapSetInfo] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, beatmap: IBeatmap):
        """
        
        :param beatmap: 
        """
    @overload
    def __init__(self, file: str, beatmapId: Optional[int] = ...):
        """
        
        :param file: 
        :param beatmapId: 
        """
    @property
    def Beatmap(self) -> IBeatmap:
        """
        
        :return: 
        """
    @property
    def BeatmapInfo(self) -> IBeatmapInfo:
        """
        
        :return: 
        """
    @property
    def BeatmapLoaded(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Metadata(self) -> BeatmapMetadata:
        """
        
        :return: 
        """
    @property
    def Skin(self) -> ISkin:
        """
        
        :return: 
        """
    @property
    def Storyboard(self) -> Storyboard:
        """
        
        :return: 
        """
    @property
    def Track(self) -> Track:
        """
        
        :return: 
        """
    @property
    def TrackLoaded(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Waveform(self) -> Waveform:
        """
        
        :return: 
        """
    def BeginAsyncLoad(self) -> None:
        """"""
    def CancelAsyncLoad(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBackground(self) -> Texture:
        """
        
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetPanelBackground(self) -> Texture:
        """
        
        :return: 
        """
    @overload
    def GetPlayableBeatmap(self, ruleset: IRulesetInfo, mods: IReadOnlyList[Mod] = ...) -> IBeatmap:
        """
        
        :param ruleset: 
        :param mods: 
        :return: 
        """
    @overload
    def GetPlayableBeatmap(self, ruleset: IRulesetInfo, mods: IReadOnlyList[Mod], token: CancellationToken) -> IBeatmap:
        """
        
        :param ruleset: 
        :param mods: 
        :param cancellationToken: 
        :return: 
        """
    def GetStream(self, storagePath: str) -> Stream:
        """
        
        :param storagePath: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def LoadTrack(self) -> Track:
        """
        
        :return: 
        """
    def PrepareTrackForPreview(self, looping: bool, offsetFromPreviewPoint: float = ...) -> None:
        """
        
        :param looping: 
        :param offsetFromPreviewPoint: 
        """
    def ToString(self) -> str:
        """"""
    def TryTransferTrack(self, target: WorkingBeatmap) -> bool:
        """
        
        :param target: 
        :return: 
        """
class FramedBeatmapClock(Component, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache, IAdjustableClock, IClock, IFrameBasedClock, ISourceChangeableClock):
    """"""
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    def __init__(self, applyOffsets: bool, requireDecoupling: bool, source: IClock = ...):
        """
        
        :param applyOffsets: 
        :param requireDecoupling: 
        :param source: 
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
    def CurrentTime(self) -> float:
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
    def ElapsedFrameTime(self) -> float:
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
    def FramesPerSecond(self) -> float:
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
    def IsRewinding(self) -> bool:
        """
        
        :return: 
        """
    @property
    def IsRunning(self) -> bool:
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
    def Rate(self) -> float:
        """"""
    @Rate.setter
    def Rate(self, value: float) -> None: ...
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
    def Source(self) -> IClock:
        """"""
    @property
    def Time(self) -> FrameTimeInfo:
        """"""
    @property
    def TimeInfo(self) -> FrameTimeInfo:
        """"""
    @property
    def TotalAppliedOffset(self) -> float:
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
    def AddTransform(self, transform: Transform, customTransformID: Optional[int] = ...) -> None:
        """"""
    def ApplyTransformsAt(self, time: float, propagateChildren: bool = ...) -> None:
        """"""
    def BeginAbsoluteSequence(self, newTransformStartTime: float, recursive: bool = ...) -> IDisposable:
        """"""
    def BeginDelayedSequence(self, delay: float, recursive: bool = ...) -> IDisposable:
        """"""
    def ChangeSource(self, source: IClock) -> None:
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
    def GetSnapshot(self) -> str:
        """
        
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def Hide(self) -> None:
        """"""
    def Invalidate(self, invalidation: Invalidation = ..., source: InvalidationSource = ...) -> bool:
        """"""
    def ProcessFrame(self) -> None:
        """"""
    def ReceivePositionalInputAt(self, screenSpacePos: Vector2) -> bool:
        """"""
    def RegisterForDependencyActivation(self, registry: IDependencyActivatorRegistry) -> None:
        """"""
    def RemoveTransform(self, toRemove: Transform) -> None:
        """"""
    def Reset(self) -> None:
        """"""
    def ResetSpeedAdjustments(self) -> None:
        """"""
    def Seek(self, position: float) -> bool:
        """"""
    def Show(self) -> None:
        """"""
    def Start(self) -> None:
        """"""
    def Stop(self) -> None:
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
class IBeatSyncProvider(IHasAmplitudes):
    """"""
    @property
    def Clock(self) -> IClock:
        """
        
        :return: 
        """
    @property
    def ControlPoints(self) -> ControlPointInfo:
        """
        
        :return: 
        """
    @property
    def CurrentAmplitudes(self) -> ChannelAmplitudes:
        """"""
class IBeatmap:
    """"""
    @property
    def AudioLeadIn(self) -> float:
        """
        
        :return: 
        """
    @property
    def BeatmapInfo(self) -> BeatmapInfo:
        """
        
        :return: 
        """
    @BeatmapInfo.setter
    def BeatmapInfo(self, value: BeatmapInfo) -> None: ...
    @property
    def BeatmapVersion(self) -> int:
        """
        
        :return: 
        """
    @property
    def Bookmarks(self) -> Array[int]:
        """
        
        :return: 
        """
    @property
    def Breaks(self) -> SortedList[BreakPeriod]:
        """
        
        :return: 
        """
    @Breaks.setter
    def Breaks(self, value: SortedList[BreakPeriod]) -> None: ...
    @property
    def ControlPointInfo(self) -> ControlPointInfo:
        """
        
        :return: 
        """
    @ControlPointInfo.setter
    def ControlPointInfo(self, value: ControlPointInfo) -> None: ...
    @property
    def Countdown(self) -> CountdownType:
        """
        
        :return: 
        """
    @property
    def CountdownOffset(self) -> int:
        """
        
        :return: 
        """
    @property
    def Difficulty(self) -> BeatmapDifficulty:
        """
        
        :return: 
        """
    @Difficulty.setter
    def Difficulty(self, value: BeatmapDifficulty) -> None: ...
    @property
    def DistanceSpacing(self) -> float:
        """
        
        :return: 
        """
    @property
    def EpilepsyWarning(self) -> bool:
        """
        
        :return: 
        """
    @property
    def GridSize(self) -> int:
        """
        
        :return: 
        """
    @property
    def HitObjects(self) -> IReadOnlyList[HitObject]:
        """
        
        :return: 
        """
    @property
    def LetterboxInBreaks(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Metadata(self) -> BeatmapMetadata:
        """
        
        :return: 
        """
    @property
    def SamplesMatchPlaybackRate(self) -> bool:
        """
        
        :return: 
        """
    @property
    def SpecialStyle(self) -> bool:
        """
        
        :return: 
        """
    @property
    def StackLeniency(self) -> float:
        """
        
        :return: 
        """
    @property
    def TimelineZoom(self) -> float:
        """
        
        :return: 
        """
    @property
    def TotalBreakTime(self) -> float:
        """
        
        :return: 
        """
    @property
    def UnhandledEventLines(self) -> List[str]:
        """
        
        :return: 
        """
    @property
    def WidescreenStoryboard(self) -> bool:
        """
        
        :return: 
        """
    def Clone(self) -> IBeatmap:
        """
        
        :return: 
        """
    def GetMostCommonBeatLength(self) -> float:
        """
        
        :return: 
        """
    def GetStatistics(self) -> IEnumerable[BeatmapStatistic]:
        """
        
        :return: 
        """
class IBeatmap(Generic[T], IBeatmap):
    """"""
    @property
    def AudioLeadIn(self) -> float:
        """
        
        :return: 
        """
    @property
    def BeatmapInfo(self) -> BeatmapInfo:
        """
        
        :return: 
        """
    @BeatmapInfo.setter
    def BeatmapInfo(self, value: BeatmapInfo) -> None: ...
    @property
    def BeatmapVersion(self) -> int:
        """
        
        :return: 
        """
    @property
    def Bookmarks(self) -> Array[int]:
        """
        
        :return: 
        """
    @property
    def Breaks(self) -> SortedList[BreakPeriod]:
        """
        
        :return: 
        """
    @Breaks.setter
    def Breaks(self, value: SortedList[BreakPeriod]) -> None: ...
    @property
    def ControlPointInfo(self) -> ControlPointInfo:
        """
        
        :return: 
        """
    @ControlPointInfo.setter
    def ControlPointInfo(self, value: ControlPointInfo) -> None: ...
    @property
    def Countdown(self) -> CountdownType:
        """
        
        :return: 
        """
    @property
    def CountdownOffset(self) -> int:
        """
        
        :return: 
        """
    @property
    def Difficulty(self) -> BeatmapDifficulty:
        """
        
        :return: 
        """
    @Difficulty.setter
    def Difficulty(self, value: BeatmapDifficulty) -> None: ...
    @property
    def DistanceSpacing(self) -> float:
        """
        
        :return: 
        """
    @property
    def EpilepsyWarning(self) -> bool:
        """
        
        :return: 
        """
    @property
    def GridSize(self) -> int:
        """
        
        :return: 
        """
    @property
    def HitObjects(self) -> IReadOnlyList[T]:
        """
        
        :return: 
        """
    @property
    def LetterboxInBreaks(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Metadata(self) -> BeatmapMetadata:
        """
        
        :return: 
        """
    @property
    def SamplesMatchPlaybackRate(self) -> bool:
        """
        
        :return: 
        """
    @property
    def SpecialStyle(self) -> bool:
        """
        
        :return: 
        """
    @property
    def StackLeniency(self) -> float:
        """
        
        :return: 
        """
    @property
    def TimelineZoom(self) -> float:
        """
        
        :return: 
        """
    @property
    def TotalBreakTime(self) -> float:
        """
        
        :return: 
        """
    @property
    def UnhandledEventLines(self) -> List[str]:
        """
        
        :return: 
        """
    @property
    def WidescreenStoryboard(self) -> bool:
        """
        
        :return: 
        """
    def Clone(self) -> IBeatmap:
        """
        
        :return: 
        """
    def GetMostCommonBeatLength(self) -> float:
        """
        
        :return: 
        """
    def GetStatistics(self) -> IEnumerable[BeatmapStatistic]:
        """
        
        :return: 
        """
class IBeatmapConverter:
    """"""
    @property
    def Beatmap(self) -> IBeatmap:
        """
        
        :return: 
        """
    def CanConvert(self) -> bool:
        """
        
        :return: 
        """
    def Convert(self, cancellationToken: CancellationToken = ...) -> IBeatmap:
        """
        
        :param cancellationToken: 
        :return: 
        """
    ObjectConverted: EventType[Action[HitObject, IEnumerable[HitObject]]] = ...
    """"""
class IBeatmapDifficultyInfo:
    """"""
    DEFAULT_DIFFICULTY: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    @property
    def ApproachRate(self) -> float:
        """
        
        :return: 
        """
    @property
    def CircleSize(self) -> float:
        """
        
        :return: 
        """
    @property
    def DrainRate(self) -> float:
        """
        
        :return: 
        """
    @property
    def OverallDifficulty(self) -> float:
        """
        
        :return: 
        """
    @property
    def SliderMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SliderTickRate(self) -> float:
        """
        
        :return: 
        """
    @classmethod
    @overload
    def DifficultyRange(cls, difficulty: float) -> float:
        """
        
        :param difficulty: 
        :return: 
        """
    @classmethod
    @overload
    def DifficultyRange(cls, difficulty: float, range: DifficultyRange) -> float:
        """
        
        :param difficulty: 
        :param range: 
        :return: 
        """
    @classmethod
    @overload
    def DifficultyRange(cls, difficulty: float, min: float, mid: float, max: float) -> float:
        """
        
        :param difficulty: 
        :param min: 
        :param mid: 
        :param max: 
        :return: 
        """
    @classmethod
    def DifficultyRangeInt(cls, difficulty: float, range: DifficultyRange) -> int:
        """
        
        :param difficulty: 
        :param range: 
        :return: 
        """
    @classmethod
    @overload
    def InverseDifficultyRange(cls, difficultyValue: float, range: DifficultyRange) -> float:
        """
        
        :param difficultyValue: 
        :param range: 
        :return: 
        """
    @classmethod
    @overload
    def InverseDifficultyRange(cls, difficultyValue: float, diff0: float, diff5: float, diff10: float) -> float:
        """
        
        :param difficultyValue: 
        :param diff0: 
        :param diff5: 
        :param diff10: 
        :return: 
        """
class IBeatmapInfo(IEquatable[IBeatmapInfo], IHasOnlineID[Int32]):
    """"""
    @property
    def BPM(self) -> float:
        """
        
        :return: 
        """
    @property
    def BeatmapSet(self) -> IBeatmapSetInfo:
        """
        
        :return: 
        """
    @property
    def Difficulty(self) -> IBeatmapDifficultyInfo:
        """
        
        :return: 
        """
    @property
    def DifficultyName(self) -> str:
        """
        
        :return: 
        """
    @property
    def EndTimeObjectCount(self) -> int:
        """
        
        :return: 
        """
    @property
    def Hash(self) -> str:
        """
        
        :return: 
        """
    @property
    def Length(self) -> float:
        """
        
        :return: 
        """
    @property
    def MD5Hash(self) -> str:
        """
        
        :return: 
        """
    @property
    def Metadata(self) -> IBeatmapMetadataInfo:
        """
        
        :return: 
        """
    @property
    def OnlineID(self) -> int:
        """
        
        :return: 
        """
    @property
    def Ruleset(self) -> IRulesetInfo:
        """
        
        :return: 
        """
    @property
    def StarRating(self) -> float:
        """
        
        :return: 
        """
    @property
    def TotalObjectCount(self) -> int:
        """
        
        :return: 
        """
    def Equals(self, other: IBeatmapInfo) -> bool:
        """"""
class IBeatmapMetadataInfo(IEquatable[IBeatmapMetadataInfo]):
    """"""
    @property
    def Artist(self) -> str:
        """
        
        :return: 
        """
    @property
    def ArtistUnicode(self) -> str:
        """
        
        :return: 
        """
    @property
    def AudioFile(self) -> str:
        """
        
        :return: 
        """
    @property
    def Author(self) -> IUser:
        """
        
        :return: 
        """
    @property
    def BackgroundFile(self) -> str:
        """
        
        :return: 
        """
    @property
    def PreviewTime(self) -> int:
        """
        
        :return: 
        """
    @property
    def Source(self) -> str:
        """
        
        :return: 
        """
    @property
    def Tags(self) -> str:
        """
        
        :return: 
        """
    @property
    def Title(self) -> str:
        """
        
        :return: 
        """
    @property
    def TitleUnicode(self) -> str:
        """
        
        :return: 
        """
    def Equals(self, other: IBeatmapMetadataInfo) -> bool:
        """"""
class IBeatmapOnlineInfo:
    """"""
    @property
    def ApproachRate(self) -> float:
        """
        
        :return: 
        """
    @property
    def CircleCount(self) -> int:
        """
        
        :return: 
        """
    @property
    def CircleSize(self) -> float:
        """
        
        :return: 
        """
    @property
    def DrainRate(self) -> float:
        """
        
        :return: 
        """
    @property
    def FailTimes(self) -> APIFailTimes:
        """
        
        :return: 
        """
    @property
    def HitLength(self) -> float:
        """
        
        :return: 
        """
    @property
    def MaxCombo(self) -> Optional[int]:
        """
        
        :return: 
        """
    @property
    def OverallDifficulty(self) -> float:
        """
        
        :return: 
        """
    @property
    def PassCount(self) -> int:
        """
        
        :return: 
        """
    @property
    def PlayCount(self) -> int:
        """
        
        :return: 
        """
    @property
    def SliderCount(self) -> int:
        """
        
        :return: 
        """
    @property
    def SpinnerCount(self) -> int:
        """
        
        :return: 
        """
class IBeatmapProcessor:
    """"""
    @property
    def Beatmap(self) -> IBeatmap:
        """
        
        :return: 
        """
    def PostProcess(self) -> None:
        """"""
    def PreProcess(self) -> None:
        """"""
class IBeatmapResourceProvider(IStorageResourceProvider):
    """"""
    @property
    def AudioManager(self) -> AudioManager:
        """
        
        :return: 
        """
    @property
    def BeatmapPanelTextureStore(self) -> TextureStore:
        """
        
        :return: 
        """
    @property
    def Files(self) -> IResourceStore[Array[int]]:
        """
        
        :return: 
        """
    @property
    def LargeTextureStore(self) -> TextureStore:
        """
        
        :return: 
        """
    @property
    def RealmAccess(self) -> RealmAccess:
        """
        
        :return: 
        """
    @property
    def Renderer(self) -> IRenderer:
        """
        
        :return: 
        """
    @property
    def Resources(self) -> IResourceStore[Array[int]]:
        """
        
        :return: 
        """
    @property
    def Tracks(self) -> ITrackStore:
        """
        
        :return: 
        """
    def CreateTextureLoaderStore(self, underlyingStore: IResourceStore[Array[int]]) -> IResourceStore[TextureUpload]:
        """
        
        :param underlyingStore: 
        :return: 
        """
class IBeatmapSetInfo(IEquatable[IBeatmapSetInfo], IHasNamedFiles, IHasOnlineID[Int32]):
    """"""
    @property
    def Beatmaps(self) -> IEnumerable[IBeatmapInfo]:
        """
        
        :return: 
        """
    @property
    def DateAdded(self) -> DateTimeOffset:
        """
        
        :return: 
        """
    @property
    def Files(self) -> IEnumerable[INamedFileUsage]:
        """
        
        :return: 
        """
    @property
    def MaxBPM(self) -> float:
        """
        
        :return: 
        """
    @property
    def MaxLength(self) -> float:
        """
        
        :return: 
        """
    @property
    def MaxStarDifficulty(self) -> float:
        """
        
        :return: 
        """
    @property
    def Metadata(self) -> IBeatmapMetadataInfo:
        """
        
        :return: 
        """
    @property
    def OnlineID(self) -> int:
        """
        
        :return: 
        """
    def Equals(self, other: IBeatmapSetInfo) -> bool:
        """"""
class IBeatmapSetOnlineInfo:
    """"""
    @property
    def Availability(self) -> BeatmapSetOnlineAvailability:
        """
        
        :return: 
        """
    @property
    def BPM(self) -> float:
        """
        
        :return: 
        """
    @property
    def Covers(self) -> BeatmapSetOnlineCovers:
        """
        
        :return: 
        """
    @property
    def FavouriteCount(self) -> int:
        """
        
        :return: 
        """
    @property
    def Genre(self) -> BeatmapSetOnlineGenre:
        """
        
        :return: 
        """
    @property
    def HasExplicitContent(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasFavourited(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasStoryboard(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasVideo(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HypeStatus(self) -> BeatmapSetHypeStatus:
        """
        
        :return: 
        """
    @property
    def Language(self) -> BeatmapSetOnlineLanguage:
        """
        
        :return: 
        """
    @property
    def LastUpdated(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @property
    def NominationStatus(self) -> BeatmapSetNominationStatus:
        """
        
        :return: 
        """
    @property
    def PlayCount(self) -> int:
        """
        
        :return: 
        """
    @property
    def Preview(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @property
    def Ratings(self) -> Array[int]:
        """
        
        :return: 
        """
    @property
    def Status(self) -> BeatmapOnlineStatus:
        """
        
        :return: 
        """
    @property
    def Submitted(self) -> DateTimeOffset:
        """
        
        :return: 
        """
    @property
    def TrackId(self) -> Optional[int]:
        """
        
        :return: 
        """
class IBeatmapUpdater(IDisposable):
    """"""
    def Dispose(self) -> None:
        """"""
    def Process(self, beatmapSet: BeatmapSetInfo, lookupScope: MetadataLookupScope = ...) -> None:
        """
        
        :param beatmapSet: 
        :param lookupScope: 
        """
    def ProcessObjectCounts(self, beatmapInfo: BeatmapInfo, lookupScope: MetadataLookupScope = ...) -> None:
        """
        
        :param beatmapInfo: 
        :param lookupScope: 
        """
    def Queue(self, beatmapSet: Live[BeatmapSetInfo], lookupScope: MetadataLookupScope = ...) -> None:
        """
        
        :param beatmapSet: 
        :param lookupScope: 
        """
class IOnlineBeatmapMetadataSource(IDisposable):
    """"""
    @property
    def Available(self) -> bool:
        """
        
        :return: 
        """
    def Dispose(self) -> None:
        """"""
    def TryLookup(self, beatmapInfo: BeatmapInfo, onlineMetadata: OnlineBeatmapMetadata) -> Tuple[bool, OnlineBeatmapMetadata]:
        """
        
        :param beatmapInfo: 
        :param onlineMetadata: 
        :return: 
        """
class IWorkingBeatmap:
    """"""
    @property
    def Beatmap(self) -> IBeatmap:
        """
        
        :return: 
        """
    @property
    def BeatmapInfo(self) -> IBeatmapInfo:
        """
        
        :return: 
        """
    @property
    def BeatmapLoaded(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Skin(self) -> ISkin:
        """
        
        :return: 
        """
    @property
    def Storyboard(self) -> Storyboard:
        """
        
        :return: 
        """
    @property
    def Track(self) -> Track:
        """
        
        :return: 
        """
    @property
    def TrackLoaded(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Waveform(self) -> Waveform:
        """
        
        :return: 
        """
    def BeginAsyncLoad(self) -> None:
        """"""
    def CancelAsyncLoad(self) -> None:
        """"""
    def GetBackground(self) -> Texture:
        """
        
        :return: 
        """
    def GetPanelBackground(self) -> Texture:
        """
        
        :return: 
        """
    @overload
    def GetPlayableBeatmap(self, ruleset: IRulesetInfo, mods: IReadOnlyList[Mod] = ...) -> IBeatmap:
        """
        
        :param ruleset: 
        :param mods: 
        :return: 
        """
    @overload
    def GetPlayableBeatmap(self, ruleset: IRulesetInfo, mods: IReadOnlyList[Mod], cancellationToken: CancellationToken) -> IBeatmap:
        """
        
        :param ruleset: 
        :param mods: 
        :param cancellationToken: 
        :return: 
        """
    def GetStream(self, storagePath: str) -> Stream:
        """
        
        :param storagePath: 
        :return: 
        """
    def LoadTrack(self) -> Track:
        """
        
        :return: 
        """
    def PrepareTrackForPreview(self, looping: bool, offsetFromPreviewPoint: float = ...) -> None:
        """
        
        :param looping: 
        :param offsetFromPreviewPoint: 
        """
class IWorkingBeatmapCache:
    """"""
    def GetWorkingBeatmap(self, beatmapInfo: BeatmapInfo) -> WorkingBeatmap:
        """
        
        :param beatmapInfo: 
        :return: 
        """
    @overload
    def Invalidate(self, beatmapInfo: BeatmapInfo) -> None:
        """
        
        :param beatmapInfo: 
        """
    @overload
    def Invalidate(self, beatmapSetInfo: BeatmapSetInfo) -> None:
        """
        
        :param beatmapSetInfo: 
        """
class LocalCachedBeatmapMetadataSource(Object, IDisposable, IOnlineBeatmapMetadataSource):
    """"""
    def __init__(self, storage: Storage):
        """
        
        :param storage: 
        """
    @property
    def Available(self) -> bool:
        """
        
        :return: 
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FetchCache(self) -> Task:
        """
        
        :return: 
        """
    def GetCacheFetchDate(self) -> Optional[DateTime]:
        """
        
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsAtLeastVersion(self, version: int) -> bool:
        """
        
        :param version: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    def TryLookup(self, beatmapInfo: BeatmapInfo, onlineMetadata: OnlineBeatmapMetadata) -> Tuple[bool, OnlineBeatmapMetadata]:
        """
        
        :param beatmapInfo: 
        :param onlineMetadata: 
        :return: 
        """
class MetadataLookupScope(Enum):
    """"""
    _None: MetadataLookupScope = ...
    """"""
    LocalCacheFirst: MetadataLookupScope = ...
    """"""
    OnlineFirst: MetadataLookupScope = ...
    """"""
class MetadataUtils(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def IsRomanised(cls, c: Char) -> bool:
        """
        
        :param c: 
        :return: 
        """
    @classmethod
    @overload
    def IsRomanised(cls, str: str) -> bool:
        """
        
        :param str: 
        :return: 
        """
    @classmethod
    def StripNonRomanisedCharacters(cls, str: str) -> str:
        """
        
        :param str: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class OnlineBeatmapMetadata(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def AuthorID(self) -> int:
        """
        
        :return: 
        """
    @AuthorID.setter
    def AuthorID(self, value: int) -> None: ...
    @property
    def BeatmapID(self) -> int:
        """
        
        :return: 
        """
    @BeatmapID.setter
    def BeatmapID(self, value: int) -> None: ...
    @property
    def BeatmapSetID(self) -> int:
        """
        
        :return: 
        """
    @BeatmapSetID.setter
    def BeatmapSetID(self, value: int) -> None: ...
    @property
    def BeatmapSetStatus(self) -> Optional[BeatmapOnlineStatus]:
        """
        
        :return: 
        """
    @BeatmapSetStatus.setter
    def BeatmapSetStatus(self, value: Optional[BeatmapOnlineStatus]) -> None: ...
    @property
    def BeatmapStatus(self) -> BeatmapOnlineStatus:
        """
        
        :return: 
        """
    @BeatmapStatus.setter
    def BeatmapStatus(self, value: BeatmapOnlineStatus) -> None: ...
    @property
    def DateRanked(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @DateRanked.setter
    def DateRanked(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def DateSubmitted(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @DateSubmitted.setter
    def DateSubmitted(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def LastUpdated(self) -> DateTimeOffset:
        """
        
        :return: 
        """
    @LastUpdated.setter
    def LastUpdated(self, value: DateTimeOffset) -> None: ...
    @property
    def MD5Hash(self) -> str:
        """
        
        :return: 
        """
    @MD5Hash.setter
    def MD5Hash(self, value: str) -> None: ...
    @property
    def UserTags(self) -> List[str]:
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
ProcessBeatmapDelegate: Callable[[BeatmapSetInfo, MetadataLookupScope], None] = ...
"""

:param beatmapSet: 
:param lookupScope: 
"""
class StarDifficulty(ValueType):
    """"""
    DifficultyAttributes: Final[DifficultyAttributes] = ...
    """
    
    :return: 
    """
    MaxCombo: Final[int] = ...
    """
    
    :return: 
    """
    PerformanceAttributes: Final[PerformanceAttributes] = ...
    """
    
    :return: 
    """
    Stars: Final[float] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, starDifficulty: float, maxCombo: int):
        """
        
        :param starDifficulty: 
        :param maxCombo: 
        """
    @overload
    def __init__(self, difficulty: DifficultyAttributes, performance: PerformanceAttributes):
        """
        
        :param difficulty: 
        :param performance: 
        """
    @property
    def DifficultyRating(self) -> DifficultyRating:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetDifficultyRating(cls, starRating: float) -> DifficultyRating:
        """
        
        :param starRating: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class WorkingBeatmap(ABC, Object, IWorkingBeatmap):
    """"""
    BeatmapInfo: Final[BeatmapInfo] = ...
    """
    
    :return: 
    """
    BeatmapSetInfo: Final[BeatmapSetInfo] = ...
    """
    
    :return: 
    """
    @property
    def Beatmap(self) -> IBeatmap:
        """
        
        :return: 
        """
    @property
    def BeatmapInfo(self) -> IBeatmapInfo:
        """
        
        :return: 
        """
    @property
    def BeatmapLoaded(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Metadata(self) -> BeatmapMetadata:
        """
        
        :return: 
        """
    @property
    def Skin(self) -> ISkin:
        """
        
        :return: 
        """
    @property
    def Storyboard(self) -> Storyboard:
        """
        
        :return: 
        """
    @property
    def Track(self) -> Track:
        """
        
        :return: 
        """
    @property
    def TrackLoaded(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Waveform(self) -> Waveform:
        """
        
        :return: 
        """
    def BeginAsyncLoad(self) -> None:
        """"""
    def CancelAsyncLoad(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBackground(self) -> Texture:
        """
        
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetPanelBackground(self) -> Texture:
        """
        
        :return: 
        """
    @overload
    def GetPlayableBeatmap(self, ruleset: IRulesetInfo, mods: IReadOnlyList[Mod] = ...) -> IBeatmap:
        """
        
        :param ruleset: 
        :param mods: 
        :return: 
        """
    @overload
    def GetPlayableBeatmap(self, ruleset: IRulesetInfo, mods: IReadOnlyList[Mod], token: CancellationToken) -> IBeatmap:
        """
        
        :param ruleset: 
        :param mods: 
        :param cancellationToken: 
        :return: 
        """
    def GetStream(self, storagePath: str) -> Stream:
        """
        
        :param storagePath: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def LoadTrack(self) -> Track:
        """
        
        :return: 
        """
    def PrepareTrackForPreview(self, looping: bool, offsetFromPreviewPoint: float = ...) -> None:
        """
        
        :param looping: 
        :param offsetFromPreviewPoint: 
        """
    def ToString(self) -> str:
        """"""
    def TryTransferTrack(self, target: WorkingBeatmap) -> bool:
        """
        
        :param target: 
        :return: 
        """
class WorkingBeatmapCache(Object, IBeatmapResourceProvider, IWorkingBeatmapCache, IStorageResourceProvider):
    """"""
    DefaultBeatmap: Final[WorkingBeatmap] = ...
    """
    
    :return: 
    """
    def __init__(self, trackStore: ITrackStore, audioManager: AudioManager, resources: IResourceStore[Array[int]], files: IResourceStore[Array[int]], defaultBeatmap: WorkingBeatmap = ..., host: GameHost = ..., realm: RealmAccess = ...):
        """
        
        :param trackStore: 
        :param audioManager: 
        :param resources: 
        :param files: 
        :param defaultBeatmap: 
        :param host: 
        :param realm: 
        """
    @property
    def AudioManager(self) -> AudioManager:
        """
        
        :return: 
        """
    @property
    def BeatmapPanelTextureStore(self) -> TextureStore:
        """
        
        :return: 
        """
    @property
    def Files(self) -> IResourceStore[Array[int]]:
        """
        
        :return: 
        """
    @property
    def LargeTextureStore(self) -> TextureStore:
        """
        
        :return: 
        """
    @property
    def RealmAccess(self) -> RealmAccess:
        """
        
        :return: 
        """
    @property
    def Renderer(self) -> IRenderer:
        """
        
        :return: 
        """
    @property
    def Resources(self) -> IResourceStore[Array[int]]:
        """
        
        :return: 
        """
    @property
    def Tracks(self) -> ITrackStore:
        """
        
        :return: 
        """
    def CreateTextureLoaderStore(self, underlyingStore: IResourceStore[Array[int]]) -> IResourceStore[TextureUpload]:
        """
        
        :param underlyingStore: 
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetWorkingBeatmap(self, beatmapInfo: BeatmapInfo) -> WorkingBeatmap:
        """
        
        :param beatmapInfo: 
        :return: 
        """
    @overload
    def Invalidate(self, info: BeatmapInfo) -> None:
        """
        
        :param beatmapInfo: 
        """
    @overload
    def Invalidate(self, info: BeatmapSetInfo) -> None:
        """
        
        :param beatmapSetInfo: 
        """
    def ToString(self) -> str:
        """"""
    OnInvalidated: EventType[Action[WorkingBeatmap]] = ...
    """"""