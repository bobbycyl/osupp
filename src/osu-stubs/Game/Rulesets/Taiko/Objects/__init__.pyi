from System import Action
from System.Collections.Generic import IList
from System import Enum
from System.Threading import CancellationToken
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Framework.Bindables import Bindable
from osu.Framework.Bindables import BindableList
from osu.Framework.Lists import SlimReadOnlyListWrapper
from osu.Game.Audio import HitSampleInfo
from osu.Game.Beatmaps.ControlPoints import ControlPointInfo
from osu.Game.Beatmaps import IBeatmapDifficultyInfo
from osu.Game.Rulesets.Judgements import Judgement
from osu.Game.Rulesets.Objects import HitObject
from osu.Game.Rulesets.Objects import IBarLine
from osu.Game.Rulesets.Objects import SliderPath
from osu.Game.Rulesets.Objects.Types import IHasDisplayColour
from osu.Game.Rulesets.Objects.Types import IHasDistance
from osu.Game.Rulesets.Objects.Types import IHasDuration
from osu.Game.Rulesets.Objects.Types import IHasPath
from osu.Game.Rulesets.Scoring import HitWindows
from osuTK.Graphics import Color4
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import TypeVar
T = TypeVar("T")
class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...
class BarLine(TaikoHitObject, IBarLine):
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
    def Major(self) -> bool:
        """
        
        :return: 
        """
    @Major.setter
    def Major(self, value: bool) -> None: ...
    @property
    def MajorBindable(self) -> Bindable[bool]:
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
class DrumRoll(TaikoStrongableHitObject, IHasDistance, IHasDuration, IHasPath):
    """"""
    IsStrongBindable: Final[Bindable[bool]] = ...
    """
    
    :return: 
    """
    SamplesBindable: Final[BindableList[HitSampleInfo]] = ...
    """
    
    :return: 
    """
    StartTimeBindable: Final[Bindable[float]] = ...
    """
    
    :return: 
    """
    TickRate: Final[int] = ...
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
    def Distance(self) -> float:
        """
        
        :return: 
        """
    @property
    def Duration(self) -> float:
        """
        
        :return: 
        """
    @Duration.setter
    def Duration(self, value: float) -> None: ...
    @property
    def EndTime(self) -> float:
        """
        
        :return: 
        """
    @EndTime.setter
    def EndTime(self, value: float) -> None: ...
    @property
    def HitWindows(self) -> HitWindows:
        """
        
        :return: 
        """
    @HitWindows.setter
    def HitWindows(self, value: HitWindows) -> None: ...
    @property
    def IsStrong(self) -> bool:
        """
        
        :return: 
        """
    @IsStrong.setter
    def IsStrong(self, value: bool) -> None: ...
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
    def Path(self) -> SliderPath:
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
    @property
    def Velocity(self) -> float:
        """
        
        :return: 
        """
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
    class StrongNestedHit(StrongNestedHitObject):
        """"""
        Parent: Final[TaikoHitObject] = ...
        """
        
        :return: 
        """
        SamplesBindable: Final[BindableList[HitSampleInfo]] = ...
        """
        
        :return: 
        """
        StartTimeBindable: Final[Bindable[float]] = ...
        """
        
        :return: 
        """
        def __init__(self, parent: TaikoHitObject):
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
class DrumRollTick(TaikoStrongableHitObject):
    """"""
    FirstTick: Final[bool] = ...
    """
    
    :return: 
    """
    IsStrongBindable: Final[Bindable[bool]] = ...
    """
    
    :return: 
    """
    Parent: Final[DrumRoll] = ...
    """
    
    :return: 
    """
    SamplesBindable: Final[BindableList[HitSampleInfo]] = ...
    """
    
    :return: 
    """
    StartTimeBindable: Final[Bindable[float]] = ...
    """
    
    :return: 
    """
    TickSpacing: Final[float] = ...
    """
    
    :return: 
    """
    def __init__(self, parent: DrumRoll):
        """
        
        :param parent: 
        """
    @property
    def AuxiliarySamples(self) -> IList[HitSampleInfo]:
        """
        
        :return: 
        """
    @property
    def HitWindow(self) -> float:
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
    def IsStrong(self) -> bool:
        """
        
        :return: 
        """
    @IsStrong.setter
    def IsStrong(self, value: bool) -> None: ...
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
    class StrongNestedHit(StrongNestedHitObject):
        """"""
        Parent: Final[TaikoHitObject] = ...
        """
        
        :return: 
        """
        SamplesBindable: Final[BindableList[HitSampleInfo]] = ...
        """
        
        :return: 
        """
        StartTimeBindable: Final[Bindable[float]] = ...
        """
        
        :return: 
        """
        def __init__(self, parent: TaikoHitObject):
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
class Hit(TaikoStrongableHitObject, IHasDisplayColour):
    """"""
    COLOUR_CENTRE: Final[ClassVar[Color4]] = ...
    """
    
    :return: 
    """
    COLOUR_RIM: Final[ClassVar[Color4]] = ...
    """
    
    :return: 
    """
    IsStrongBindable: Final[Bindable[bool]] = ...
    """
    
    :return: 
    """
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
    def DisplayColour(self) -> Bindable[Color4]:
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
    def IsStrong(self) -> bool:
        """
        
        :return: 
        """
    @IsStrong.setter
    def IsStrong(self, value: bool) -> None: ...
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
    @property
    def Type(self) -> HitType:
        """
        
        :return: 
        """
    @Type.setter
    def Type(self, value: HitType) -> None: ...
    @property
    def TypeBindable(self) -> Bindable[HitType]:
        """
        
        :return: 
        """
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
    class StrongNestedHit(StrongNestedHitObject):
        """"""
        Parent: Final[TaikoHitObject] = ...
        """
        
        :return: 
        """
        SamplesBindable: Final[BindableList[HitSampleInfo]] = ...
        """
        
        :return: 
        """
        StartTimeBindable: Final[Bindable[float]] = ...
        """
        
        :return: 
        """
        def __init__(self, parent: TaikoHitObject):
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
class HitType(Enum):
    """"""
    Centre: HitType = ...
    """"""
    Rim: HitType = ...
    """"""
class IgnoreHit(Hit, IHasDisplayColour):
    """"""
    IsStrongBindable: Final[Bindable[bool]] = ...
    """
    
    :return: 
    """
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
    def DisplayColour(self) -> Bindable[Color4]:
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
    def IsStrong(self) -> bool:
        """
        
        :return: 
        """
    @IsStrong.setter
    def IsStrong(self, value: bool) -> None: ...
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
    @property
    def Type(self) -> HitType:
        """
        
        :return: 
        """
    @Type.setter
    def Type(self, value: HitType) -> None: ...
    @property
    def TypeBindable(self) -> Bindable[HitType]:
        """
        
        :return: 
        """
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
class StrongNestedHitObject(ABC, TaikoHitObject):
    """"""
    Parent: Final[TaikoHitObject] = ...
    """
    
    :return: 
    """
    SamplesBindable: Final[BindableList[HitSampleInfo]] = ...
    """
    
    :return: 
    """
    StartTimeBindable: Final[Bindable[float]] = ...
    """
    
    :return: 
    """
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
class Swell(TaikoHitObject, IHasDuration):
    """"""
    RequiredHits: Final[int] = ...
    """
    
    :return: 
    """
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
    def Duration(self) -> float:
        """
        
        :return: 
        """
    @Duration.setter
    def Duration(self, value: float) -> None: ...
    @property
    def EndTime(self) -> float:
        """
        
        :return: 
        """
    @EndTime.setter
    def EndTime(self, value: float) -> None: ...
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
class SwellTick(TaikoHitObject):
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
class TaikoHitObject(ABC, HitObject):
    """"""
    DEFAULT_SIZE: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    SamplesBindable: Final[BindableList[HitSampleInfo]] = ...
    """
    
    :return: 
    """
    StartTimeBindable: Final[Bindable[float]] = ...
    """
    
    :return: 
    """
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
class TaikoStrongableHitObject(ABC, TaikoHitObject):
    """"""
    DEFAULT_STRONG_SIZE: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    IsStrongBindable: Final[Bindable[bool]] = ...
    """
    
    :return: 
    """
    STRONG_SCALE: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    SamplesBindable: Final[BindableList[HitSampleInfo]] = ...
    """
    
    :return: 
    """
    StartTimeBindable: Final[Bindable[float]] = ...
    """
    
    :return: 
    """
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
    def IsStrong(self) -> bool:
        """
        
        :return: 
        """
    @IsStrong.setter
    def IsStrong(self, value: bool) -> None: ...
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