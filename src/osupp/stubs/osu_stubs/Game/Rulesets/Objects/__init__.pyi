from System import Action
from System import Array
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IList
from System.Collections.Generic import List
from System import Enum
from System import IEquatable
from System import Object
from System import ReadOnlySpan
from System.Threading import CancellationToken
from System import Type
from System import ValueType
from __future__ import annotations
from abc import ABC
from osu.Framework.Bindables import Bindable
from osu.Framework.Bindables import BindableList
from osu.Framework.Bindables import IBindable
from osu.Framework.Graphics.Performance import LifetimeEntry
from osu.Framework.Lists import SlimReadOnlyListWrapper
from osu.Game.Audio import HitSampleInfo
from osu.Game.Beatmaps.ControlPoints import ControlPointInfo
from osu.Game.Beatmaps import IBeatmap
from osu.Game.Beatmaps import IBeatmapDifficultyInfo
from osu.Game.Rulesets.Edit import IDistanceSnapProvider
from osu.Game.Rulesets.Judgements import Judgement
from osu.Game.Rulesets.Objects.Types import PathType
from osu.Game.Rulesets.Scoring import HitWindows
from osuTK import Vector2
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Optional
from typing import Tuple
from typing import TypeVar
from typing import overload
T = TypeVar("T")
TBarLine = TypeVar("TBarLine")
THitObject = TypeVar("THitObject")
class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...
class BarLineGenerator(Generic[TBarLine], Object):
    """"""
    BarLines: Final[List[TBarLine]] = ...
    """
    
    :return: 
    """
    def __init__(self, beatmap: IBeatmap):
        """
        
        :param beatmap: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class BezierConverter(ABC, Object):
    """"""
    @classmethod
    def ConvertCatmullToBezierAnchors(cls, controlPoints: ReadOnlySpan[Vector2]) -> Array[Vector2]:
        """
        
        :param controlPoints: 
        :return: 
        """
    @classmethod
    def ConvertCircleToBezierAnchors(cls, controlPoints: ReadOnlySpan[Vector2]) -> Array[Vector2]:
        """
        
        :param controlPoints: 
        :return: 
        """
    @classmethod
    def ConvertLinearToBezierAnchors(cls, controlPoints: ReadOnlySpan[Vector2]) -> Array[Vector2]:
        """
        
        :param controlPoints: 
        :return: 
        """
    @classmethod
    def ConvertToLegacyBezier(cls, controlPoints: IList[PathControlPoint], position: Vector2) -> List[Vector2]:
        """
        
        :param controlPoints: 
        :param position: 
        :return: 
        """
    @classmethod
    def ConvertToModernBezier(cls, controlPoints: IList[PathControlPoint]) -> List[PathControlPoint]:
        """
        
        :param controlPoints: 
        :return: 
        """
    @classmethod
    def CountSegments(cls, controlPoints: IList[PathControlPoint]) -> int:
        """
        
        :param controlPoints: 
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
class HitObject(Object):
    """"""
    SamplesBindable: Final[BindableList[HitSampleInfo]] = ...
    """
    
    :return: 
    """
    StartTimeBindable: Final[Bindable[float]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def AuxiliarySamples(self) -> IList[HitSampleInfo]:
        """
        
        :return: 
        """
    @property
    def HitWindows(self) -> HitWindows:
        """
        
        :return: 
        """
    @HitWindows.setter
    def HitWindows(self, value: HitWindows) -> None: ...
    @property
    def Judgement(self) -> Judgement:
        """
        
        :return: 
        """
    @property
    def Kiai(self) -> bool:
        """
        
        :return: 
        """
    @property
    def MaximumJudgementOffset(self) -> float:
        """
        
        :return: 
        """
    @property
    def NestedHitObjects(self) -> SlimReadOnlyListWrapper[HitObject]:
        """
        
        :return: 
        """
    @property
    def Samples(self) -> IList[HitSampleInfo]:
        """
        
        :return: 
        """
    @Samples.setter
    def Samples(self, value: IList[HitSampleInfo]) -> None: ...
    @property
    def StartTime(self) -> float:
        """
        
        :return: 
        """
    @StartTime.setter
    def StartTime(self, value: float) -> None: ...
    def ApplyDefaults(self, controlPointInfo: ControlPointInfo, difficulty: IBeatmapDifficultyInfo, cancellationToken: CancellationToken = ...) -> None:
        """
        
        :param controlPointInfo: 
        :param difficulty: 
        :param cancellationToken: 
        """
    def CreateHitSampleInfo(self, sampleName: str = ...) -> HitSampleInfo:
        """
        
        :param sampleName: 
        :return: 
        """
    def CreateJudgement(self) -> Judgement:
        """
        
        :return: 
        """
    def CreateSlidingSamples(self) -> IList[HitSampleInfo]:
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
    DefaultsApplied: EventType[Action[HitObject]] = ...
    """"""
class HitObjectExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetEndTime(cls, hitObject: HitObject) -> float:
        """
        
        :param hitObject: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class HitObjectLifetimeEntry(LifetimeEntry):
    """"""
    HitObject: Final[HitObject] = ...
    """
    
    :return: 
    """
    def __init__(self, hitObject: HitObject):
        """
        
        :param hitObject: 
        """
    @property
    def AllJudged(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Judged(self) -> bool:
        """
        
        :return: 
        """
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
    def NestedEntries(self) -> List[HitObjectLifetimeEntry]:
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
    LifetimeChanged: EventType[Action[LifetimeEntry]] = ...
    """"""
class HitObjectParser(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Parse(self, text: str) -> HitObject:
        """
        
        :param text: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class HitObjectProperty(Generic[T], ValueType):
    """"""
    def __init__(self, value: T = ...):
        """
        
        :param value: 
        """
    @property
    def Bindable(self) -> Bindable[T]:
        """
        
        :return: 
        """
    @property
    def Value(self) -> T:
        """
        
        :return: 
        """
    @Value.setter
    def Value(self, value: T) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class IBarLine:
    """"""
    @property
    def Major(self) -> bool:
        """
        
        :return: 
        """
    @Major.setter
    def Major(self, value: bool) -> None: ...
    @property
    def StartTime(self) -> float:
        """
        
        :return: 
        """
    @StartTime.setter
    def StartTime(self, value: float) -> None: ...
class PathControlPoint(Object, IEquatable[PathControlPoint]):
    """"""
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, position: Vector2, type: Optional[PathType] = ...):
        """
        
        :param position: 
        :param type: 
        """
    @property
    def Position(self) -> Vector2:
        """
        
        :return: 
        """
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
    @property
    def Type(self) -> Optional[PathType]:
        """
        
        :return: 
        """
    @Type.setter
    def Type(self, value: Optional[PathType]) -> None: ...
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: PathControlPoint) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    Changed: EventType[Action] = ...
    """"""
class SliderEventDescriptor(ValueType):
    """"""
    PathProgress: Final[float] = ...
    """
    
    :return: 
    """
    SpanIndex: Final[int] = ...
    """
    
    :return: 
    """
    SpanStartTime: Final[float] = ...
    """
    
    :return: 
    """
    Time: Final[float] = ...
    """
    
    :return: 
    """
    Type: Final[SliderEventType] = ...
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
class SliderEventGenerator(ABC, Object):
    """"""
    TAIL_LENIENCY: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def Generate(cls, startTime: float, spanDuration: float, velocity: float, tickDistance: float, totalDistance: float, spanCount: int, cancellationToken: CancellationToken = ...) -> IEnumerable[SliderEventDescriptor]:
        """
        
        :param startTime: 
        :param spanDuration: 
        :param velocity: 
        :param tickDistance: 
        :param totalDistance: 
        :param spanCount: 
        :param cancellationToken: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class SliderEventType(Enum):
    """"""
    Tick: SliderEventType = ...
    """"""
    LegacyLastTick: SliderEventType = ...
    """"""
    Head: SliderEventType = ...
    """"""
    Tail: SliderEventType = ...
    """"""
    Repeat: SliderEventType = ...
    """"""
class SliderPath(Object):
    """"""
    ControlPoints: Final[BindableList[PathControlPoint]] = ...
    """
    
    :return: 
    """
    ExpectedDistance: Final[Bindable[Optional[float]]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, controlPoints: Array[PathControlPoint], expectedDistance: Optional[float] = ...):
        """
        
        :param controlPoints: 
        :param expectedDistance: 
        """
    @overload
    def __init__(self, type: PathType, controlPoints: Array[Vector2], expectedDistance: Optional[float] = ...):
        """
        
        :param type: 
        :param controlPoints: 
        :param expectedDistance: 
        """
    @property
    def CalculatedDistance(self) -> float:
        """
        
        :return: 
        """
    @property
    def Distance(self) -> float:
        """
        
        :return: 
        """
    @property
    def HasValidLengthForPlacement(self) -> bool:
        """
        
        :return: 
        """
    @property
    def OptimiseCatmull(self) -> bool:
        """
        
        :return: 
        """
    @OptimiseCatmull.setter
    def OptimiseCatmull(self, value: bool) -> None: ...
    @property
    def Version(self) -> IBindable[int]:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetPathToProgress(self, path: List[Vector2], p0: float, p1: float) -> None:
        """
        
        :param path: 
        :param p0: 
        :param p1: 
        """
    def GetSegmentEnds(self) -> IEnumerable[float]:
        """
        
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def PointsInSegment(self, controlPoint: PathControlPoint) -> List[PathControlPoint]:
        """
        
        :param controlPoint: 
        :return: 
        """
    def PositionAt(self, progress: float) -> Vector2:
        """
        
        :param progress: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class SliderPathExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Reverse(cls, sliderPath: SliderPath, positionalOffset: Vector2) -> Tuple[None, Vector2]:
        """
        
        :param sliderPath: 
        :param positionalOffset: 
        """
    @classmethod
    def SnapTo(cls, hitObject: THitObject, snapProvider: IDistanceSnapProvider) -> None:
        """
        
        :param hitObject: 
        :param snapProvider: 
        """
    def ToString(self) -> str:
        """"""
class SyntheticHitObjectEntry(HitObjectLifetimeEntry):
    """"""
    HitObject: Final[HitObject] = ...
    """
    
    :return: 
    """
    def __init__(self, hitObject: HitObject):
        """
        
        :param hitObject: 
        """
    @property
    def AllJudged(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Judged(self) -> bool:
        """
        
        :return: 
        """
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
    def NestedEntries(self) -> List[HitObjectLifetimeEntry]:
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
    LifetimeChanged: EventType[Action[LifetimeEntry]] = ...
    """"""