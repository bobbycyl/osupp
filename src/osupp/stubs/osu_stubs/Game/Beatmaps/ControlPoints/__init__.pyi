from System import Action
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IReadOnlyList
from System import Enum
from System import IComparable
from System import IEquatable
from System import Object
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Framework.Bindables import Bindable
from osu.Framework.Bindables import BindableBool
from osu.Framework.Bindables import BindableDouble
from osu.Framework.Bindables import BindableInt
from osu.Framework.Bindables import IBindableList
from osu.Game.Audio import HitSampleInfo
from osu.Game.Beatmaps.Timing import TimeSignature
from osu.Game.Graphics import OsuColour
from osu.Game.Utils import IDeepCloneable
from osuTK.Graphics import Color4
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
class ControlPoint(ABC, Object, IComparable[ControlPoint], IEquatable[ControlPoint], IControlPoint, IDeepCloneable[ControlPoint]):
    """"""
    @property
    def Time(self) -> float:
        """
        
        :return: 
        """
    @Time.setter
    def Time(self, value: float) -> None: ...
    def AttachGroup(self, pointGroup: ControlPointGroup) -> None:
        """
        
        :param pointGroup: 
        """
    def CompareTo(self, other: ControlPoint) -> int:
        """"""
    def CopyFrom(self, other: ControlPoint) -> None:
        """
        
        :param other: 
        """
    def DeepClone(self) -> ControlPoint:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: ControlPoint) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetRepresentingColour(self, colours: OsuColour) -> Color4:
        """
        
        :param colours: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def IsRedundant(self, existing: ControlPoint) -> bool:
        """
        
        :param existing: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    Changed: EventType[Action[ControlPoint]] = ...
    """"""
class ControlPointGroup(Object, IComparable[ControlPointGroup], IEquatable[ControlPointGroup]):
    """"""
    def __init__(self, time: float):
        """
        
        :param time: 
        """
    @property
    def ControlPoints(self) -> IBindableList[ControlPoint]:
        """
        
        :return: 
        """
    @property
    def Time(self) -> float:
        """
        
        :return: 
        """
    def Add(self, point: ControlPoint) -> None:
        """
        
        :param point: 
        """
    def CompareTo(self, other: ControlPointGroup) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: ControlPointGroup) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, point: ControlPoint) -> None:
        """
        
        :param point: 
        """
    def ToString(self) -> str:
        """"""
    def __delitem__(self, point: ControlPoint) -> None:
        """
        
        :param point: 
        """
    ItemAdded: EventType[Action[ControlPoint]] = ...
    """"""
    ItemChanged: EventType[Action[ControlPoint]] = ...
    """"""
    ItemRemoved: EventType[Action[ControlPoint]] = ...
    """"""
class ControlPointInfo(Object, IDeepCloneable[ControlPointInfo]):
    """"""
    def __init__(self):
        """"""
    @property
    def AllControlPoints(self) -> IEnumerable[ControlPoint]:
        """
        
        :return: 
        """
    @property
    def BPMMaximum(self) -> float:
        """
        
        :return: 
        """
    @property
    def BPMMinimum(self) -> float:
        """
        
        :return: 
        """
    @property
    def EffectPoints(self) -> IReadOnlyList[EffectControlPoint]:
        """
        
        :return: 
        """
    @property
    def Groups(self) -> IBindableList[ControlPointGroup]:
        """
        
        :return: 
        """
    @property
    def TimingPoints(self) -> IReadOnlyList[TimingControlPoint]:
        """
        
        :return: 
        """
    def Add(self, time: float, controlPoint: ControlPoint) -> bool:
        """
        
        :param time: 
        :param controlPoint: 
        :return: 
        """
    @classmethod
    @overload
    def BinarySearch(cls, list: IReadOnlyList[T], time: float) -> T:
        """
        
        :param list: 
        :param time: 
        :return: 
        """
    @classmethod
    @overload
    def BinarySearch(cls, list: IReadOnlyList[T], time: float, equalitySelection: EqualitySelection) -> int:
        """
        
        :param list: 
        :param time: 
        :param equalitySelection: 
        :return: 
        """
    @classmethod
    def BinarySearchWithFallback(cls, list: IReadOnlyList[T], time: float, fallback: T) -> T:
        """
        
        :param list: 
        :param time: 
        :param fallback: 
        :return: 
        """
    def Clear(self) -> None:
        """"""
    def DeepClone(self) -> ControlPointInfo:
        """
        
        :return: 
        """
    def EffectPointAt(self, time: float) -> EffectControlPoint:
        """
        
        :param time: 
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetClosestBeatDivisor(self, time: float, referenceTime: Optional[float] = ...) -> int:
        """
        
        :param time: 
        :param referenceTime: 
        :return: 
        """
    @overload
    def GetClosestSnappedTime(self, time: float) -> float:
        """
        
        :param time: 
        :return: 
        """
    @overload
    def GetClosestSnappedTime(self, time: float, beatDivisor: int, referenceTime: Optional[float] = ...) -> float:
        """
        
        :param time: 
        :param beatDivisor: 
        :param referenceTime: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GroupAt(self, time: float, addIfNotExisting: bool = ...) -> ControlPointGroup:
        """
        
        :param time: 
        :param addIfNotExisting: 
        :return: 
        """
    def RemoveGroup(self, group: ControlPointGroup) -> None:
        """
        
        :param group: 
        """
    def TimingPointAfter(self, time: float) -> TimingControlPoint:
        """
        
        :param time: 
        :return: 
        """
    def TimingPointAt(self, time: float) -> TimingControlPoint:
        """
        
        :param time: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    ControlPointsChanged: EventType[Action] = ...
    """"""
class DifficultyControlPoint(ControlPoint, IComparable[ControlPoint], IEquatable[ControlPoint], IEquatable[DifficultyControlPoint], IControlPoint, IDeepCloneable[ControlPoint]):
    """"""
    DEFAULT: Final[ClassVar[DifficultyControlPoint]] = ...
    """
    
    :return: 
    """
    SliderVelocityBindable: Final[BindableDouble] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def GenerateTicks(self) -> bool:
        """
        
        :return: 
        """
    @GenerateTicks.setter
    def GenerateTicks(self, value: bool) -> None: ...
    @property
    def SliderVelocity(self) -> float:
        """
        
        :return: 
        """
    @SliderVelocity.setter
    def SliderVelocity(self, value: float) -> None: ...
    @property
    def Time(self) -> float:
        """
        
        :return: 
        """
    @Time.setter
    def Time(self, value: float) -> None: ...
    def AttachGroup(self, pointGroup: ControlPointGroup) -> None:
        """
        
        :param pointGroup: 
        """
    def CompareTo(self, other: ControlPoint) -> int:
        """"""
    def CopyFrom(self, other: ControlPoint) -> None:
        """
        
        :param other: 
        """
    def DeepClone(self) -> ControlPoint:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: ControlPoint) -> bool:
        """"""
    @overload
    def Equals(self, other: DifficultyControlPoint) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetRepresentingColour(self, colours: OsuColour) -> Color4:
        """
        
        :param colours: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def IsRedundant(self, existing: ControlPoint) -> bool:
        """
        
        :param existing: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    Changed: EventType[Action[ControlPoint]] = ...
    """"""
class EffectControlPoint(ControlPoint, IComparable[ControlPoint], IEquatable[ControlPoint], IEquatable[EffectControlPoint], IControlPoint, IDeepCloneable[ControlPoint]):
    """"""
    DEFAULT: Final[ClassVar[EffectControlPoint]] = ...
    """
    
    :return: 
    """
    KiaiModeBindable: Final[BindableBool] = ...
    """
    
    :return: 
    """
    ScrollSpeedBindable: Final[BindableDouble] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def KiaiMode(self) -> bool:
        """
        
        :return: 
        """
    @KiaiMode.setter
    def KiaiMode(self, value: bool) -> None: ...
    @property
    def ScrollSpeed(self) -> float:
        """
        
        :return: 
        """
    @ScrollSpeed.setter
    def ScrollSpeed(self, value: float) -> None: ...
    @property
    def Time(self) -> float:
        """
        
        :return: 
        """
    @Time.setter
    def Time(self, value: float) -> None: ...
    def AttachGroup(self, pointGroup: ControlPointGroup) -> None:
        """
        
        :param pointGroup: 
        """
    def CompareTo(self, other: ControlPoint) -> int:
        """"""
    def CopyFrom(self, other: ControlPoint) -> None:
        """
        
        :param other: 
        """
    def DeepClone(self) -> ControlPoint:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: ControlPoint) -> bool:
        """"""
    @overload
    def Equals(self, other: EffectControlPoint) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetRepresentingColour(self, colours: OsuColour) -> Color4:
        """
        
        :param colours: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def IsRedundant(self, existing: ControlPoint) -> bool:
        """
        
        :param existing: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    Changed: EventType[Action[ControlPoint]] = ...
    """"""
class EqualitySelection(Enum):
    """"""
    FirstFound: EqualitySelection = ...
    """"""
    Leftmost: EqualitySelection = ...
    """"""
    Rightmost: EqualitySelection = ...
    """"""
class IControlPoint:
    """"""
    @property
    def Time(self) -> float:
        """
        
        :return: 
        """
class SampleControlPoint(ControlPoint, IComparable[ControlPoint], IEquatable[ControlPoint], IEquatable[SampleControlPoint], IControlPoint, IDeepCloneable[ControlPoint]):
    """"""
    DEFAULT: Final[ClassVar[SampleControlPoint]] = ...
    """
    
    :return: 
    """
    DEFAULT_BANK: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    SampleBankBindable: Final[Bindable[str]] = ...
    """
    
    :return: 
    """
    SampleVolumeBindable: Final[BindableInt] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def SampleBank(self) -> str:
        """
        
        :return: 
        """
    @SampleBank.setter
    def SampleBank(self, value: str) -> None: ...
    @property
    def SampleVolume(self) -> int:
        """
        
        :return: 
        """
    @SampleVolume.setter
    def SampleVolume(self, value: int) -> None: ...
    @property
    def Time(self) -> float:
        """
        
        :return: 
        """
    @Time.setter
    def Time(self, value: float) -> None: ...
    def ApplyTo(self, hitSampleInfo: HitSampleInfo) -> HitSampleInfo:
        """
        
        :param hitSampleInfo: 
        :return: 
        """
    def AttachGroup(self, pointGroup: ControlPointGroup) -> None:
        """
        
        :param pointGroup: 
        """
    def CompareTo(self, other: ControlPoint) -> int:
        """"""
    def CopyFrom(self, other: ControlPoint) -> None:
        """
        
        :param other: 
        """
    def DeepClone(self) -> ControlPoint:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: ControlPoint) -> bool:
        """"""
    @overload
    def Equals(self, other: SampleControlPoint) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetRepresentingColour(self, colours: OsuColour) -> Color4:
        """
        
        :param colours: 
        :return: 
        """
    def GetSampleInfo(self, sampleName: str = ...) -> HitSampleInfo:
        """
        
        :param sampleName: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def IsRedundant(self, existing: ControlPoint) -> bool:
        """
        
        :param existing: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    Changed: EventType[Action[ControlPoint]] = ...
    """"""
class TimingControlPoint(ControlPoint, IComparable[ControlPoint], IEquatable[ControlPoint], IEquatable[TimingControlPoint], IControlPoint, IDeepCloneable[ControlPoint]):
    """"""
    BeatLengthBindable: Final[BindableDouble] = ...
    """
    
    :return: 
    """
    DEFAULT: Final[ClassVar[TimingControlPoint]] = ...
    """
    
    :return: 
    """
    DEFAULT_BEAT_LENGTH: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    OmitFirstBarLineBindable: Final[BindableBool] = ...
    """
    
    :return: 
    """
    TimeSignatureBindable: Final[Bindable[TimeSignature]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def BPM(self) -> float:
        """
        
        :return: 
        """
    @property
    def BeatLength(self) -> float:
        """
        
        :return: 
        """
    @BeatLength.setter
    def BeatLength(self, value: float) -> None: ...
    @property
    def OmitFirstBarLine(self) -> bool:
        """
        
        :return: 
        """
    @OmitFirstBarLine.setter
    def OmitFirstBarLine(self, value: bool) -> None: ...
    @property
    def Time(self) -> float:
        """
        
        :return: 
        """
    @Time.setter
    def Time(self, value: float) -> None: ...
    @property
    def TimeSignature(self) -> TimeSignature:
        """
        
        :return: 
        """
    @TimeSignature.setter
    def TimeSignature(self, value: TimeSignature) -> None: ...
    def AttachGroup(self, pointGroup: ControlPointGroup) -> None:
        """
        
        :param pointGroup: 
        """
    def CompareTo(self, other: ControlPoint) -> int:
        """"""
    def CopyFrom(self, other: ControlPoint) -> None:
        """
        
        :param other: 
        """
    def DeepClone(self) -> ControlPoint:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: ControlPoint) -> bool:
        """"""
    @overload
    def Equals(self, other: TimingControlPoint) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetRepresentingColour(self, colours: OsuColour) -> Color4:
        """
        
        :param colours: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def IsRedundant(self, existing: ControlPoint) -> bool:
        """
        
        :param existing: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    Changed: EventType[Action[ControlPoint]] = ...
    """"""