from System import Action
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IReadOnlyList
from System import Enum
from System import Type
from __future__ import annotations
from osu.Framework.Bindables import IBindableList
from osu.Game.Beatmaps.ControlPoints import ControlPoint
from osu.Game.Beatmaps.ControlPoints import ControlPointGroup
from osu.Game.Beatmaps.ControlPoints import ControlPointInfo
from osu.Game.Beatmaps.ControlPoints import DifficultyControlPoint
from osu.Game.Beatmaps.ControlPoints import EffectControlPoint
from osu.Game.Beatmaps.ControlPoints import SampleControlPoint
from osu.Game.Beatmaps.ControlPoints import TimingControlPoint
from osu.Game.Utils import IDeepCloneable
from typing import Generic
from typing import Optional
from typing import TypeVar
from typing import overload
T = TypeVar("T")
class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...
class LegacyControlPointInfo(ControlPointInfo, IDeepCloneable[ControlPointInfo]):
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
    def DifficultyPoints(self) -> IReadOnlyList[DifficultyControlPoint]:
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
    def SamplePoints(self) -> IReadOnlyList[SampleControlPoint]:
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
    def Clear(self) -> None:
        """"""
    def DeepClone(self) -> ControlPointInfo:
        """
        
        :return: 
        """
    def DifficultyPointAt(self, time: float) -> DifficultyControlPoint:
        """
        
        :param time: 
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
    def SamplePointAt(self, time: float) -> SampleControlPoint:
        """
        
        :param time: 
        :return: 
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
class LegacyEffectFlags(Enum):
    """"""
    _None: LegacyEffectFlags = ...
    """"""
    Kiai: LegacyEffectFlags = ...
    """"""
    OmitFirstBarLine: LegacyEffectFlags = ...
    """"""
class LegacyEventType(Enum):
    """"""
    Background: LegacyEventType = ...
    """"""
    Video: LegacyEventType = ...
    """"""
    Break: LegacyEventType = ...
    """"""
    Colour: LegacyEventType = ...
    """"""
    Sprite: LegacyEventType = ...
    """"""
    Sample: LegacyEventType = ...
    """"""
    Animation: LegacyEventType = ...
    """"""
class LegacyHitObjectType(Enum):
    """"""
    Circle: LegacyHitObjectType = ...
    """"""
    Slider: LegacyHitObjectType = ...
    """"""
    NewCombo: LegacyHitObjectType = ...
    """"""
    Spinner: LegacyHitObjectType = ...
    """"""
    ComboOffset: LegacyHitObjectType = ...
    """"""
    Hold: LegacyHitObjectType = ...
    """"""
    ObjectTypes: LegacyHitObjectType = ...
    """"""
class LegacyHitSoundType(Enum):
    """"""
    _None: LegacyHitSoundType = ...
    """"""
    Normal: LegacyHitSoundType = ...
    """"""
    Whistle: LegacyHitSoundType = ...
    """"""
    Finish: LegacyHitSoundType = ...
    """"""
    Clap: LegacyHitSoundType = ...
    """"""
class LegacyMods(Enum):
    """"""
    _None: LegacyMods = ...
    """"""
    NoFail: LegacyMods = ...
    """"""
    Easy: LegacyMods = ...
    """"""
    TouchDevice: LegacyMods = ...
    """"""
    Hidden: LegacyMods = ...
    """"""
    HardRock: LegacyMods = ...
    """"""
    SuddenDeath: LegacyMods = ...
    """"""
    DoubleTime: LegacyMods = ...
    """"""
    Relax: LegacyMods = ...
    """"""
    HalfTime: LegacyMods = ...
    """"""
    Nightcore: LegacyMods = ...
    """"""
    Flashlight: LegacyMods = ...
    """"""
    Autoplay: LegacyMods = ...
    """"""
    SpunOut: LegacyMods = ...
    """"""
    Autopilot: LegacyMods = ...
    """"""
    Perfect: LegacyMods = ...
    """"""
    Key4: LegacyMods = ...
    """"""
    Key5: LegacyMods = ...
    """"""
    Key6: LegacyMods = ...
    """"""
    Key7: LegacyMods = ...
    """"""
    Key8: LegacyMods = ...
    """"""
    FadeIn: LegacyMods = ...
    """"""
    Random: LegacyMods = ...
    """"""
    Cinema: LegacyMods = ...
    """"""
    Target: LegacyMods = ...
    """"""
    Key9: LegacyMods = ...
    """"""
    KeyCoop: LegacyMods = ...
    """"""
    Key1: LegacyMods = ...
    """"""
    Key3: LegacyMods = ...
    """"""
    Key2: LegacyMods = ...
    """"""
    ScoreV2: LegacyMods = ...
    """"""
    Mirror: LegacyMods = ...
    """"""
class LegacyOrigins(Enum):
    """"""
    TopLeft: LegacyOrigins = ...
    """"""
    Centre: LegacyOrigins = ...
    """"""
    CentreLeft: LegacyOrigins = ...
    """"""
    TopRight: LegacyOrigins = ...
    """"""
    BottomCentre: LegacyOrigins = ...
    """"""
    TopCentre: LegacyOrigins = ...
    """"""
    Custom: LegacyOrigins = ...
    """"""
    CentreRight: LegacyOrigins = ...
    """"""
    BottomLeft: LegacyOrigins = ...
    """"""
    BottomRight: LegacyOrigins = ...
    """"""
class LegacySampleBank(Enum):
    """"""
    _None: LegacySampleBank = ...
    """"""
    Normal: LegacySampleBank = ...
    """"""
    Soft: LegacySampleBank = ...
    """"""
    Drum: LegacySampleBank = ...
    """"""
class LegacyStoryLayer(Enum):
    """"""
    Background: LegacyStoryLayer = ...
    """"""
    Fail: LegacyStoryLayer = ...
    """"""
    Pass: LegacyStoryLayer = ...
    """"""
    Foreground: LegacyStoryLayer = ...
    """"""
    Overlay: LegacyStoryLayer = ...
    """"""
    Video: LegacyStoryLayer = ...
    """"""