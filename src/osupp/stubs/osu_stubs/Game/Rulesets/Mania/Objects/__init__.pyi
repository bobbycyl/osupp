from System import Action
from System.Collections.Generic import IList
from System.Collections.Generic import List
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
from osu.Game.Rulesets.Objects.Types import IHasColumn
from osu.Game.Rulesets.Objects.Types import IHasDuration
from osu.Game.Rulesets.Objects.Types import IHasXPosition
from osu.Game.Rulesets.Scoring import HitWindows
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import TypeVar
T = TypeVar("T")
class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...
class BarLine(ManiaHitObject, IHasColumn, IHasXPosition, IBarLine):
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
    def Column(self) -> int:
        """
        
        :return: 
        """
    @Column.setter
    def Column(self, value: int) -> None: ...
    @property
    def ColumnBindable(self) -> Bindable[int]:
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
    @property
    def X(self) -> float:
        """
        
        :return: 
        """
    @X.setter
    def X(self, value: float) -> None: ...
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
class HeadNote(Note, IHasColumn, IHasXPosition):
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
    def Column(self) -> int:
        """
        
        :return: 
        """
    @Column.setter
    def Column(self, value: int) -> None: ...
    @property
    def ColumnBindable(self) -> Bindable[int]:
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
    @property
    def X(self) -> float:
        """
        
        :return: 
        """
    @X.setter
    def X(self, value: float) -> None: ...
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
class HoldNote(ManiaHitObject, IHasColumn, IHasDuration, IHasXPosition):
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
    def Body(self) -> HoldNoteBody:
        """
        
        :return: 
        """
    @property
    def Column(self) -> int:
        """
        
        :return: 
        """
    @Column.setter
    def Column(self, value: int) -> None: ...
    @property
    def ColumnBindable(self) -> Bindable[int]:
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
    def Head(self) -> HeadNote:
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
    def NodeSamples(self) -> IList[IList[HitSampleInfo]]:
        """
        
        :return: 
        """
    @NodeSamples.setter
    def NodeSamples(self, value: IList[IList[HitSampleInfo]]) -> None: ...
    @property
    def PlaySlidingSamples(self) -> bool:
        """
        
        :return: 
        """
    @PlaySlidingSamples.setter
    def PlaySlidingSamples(self, value: bool) -> None: ...
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
    def Tail(self) -> TailNote:
        """
        
        :return: 
        """
    @property
    def X(self) -> float:
        """
        
        :return: 
        """
    @X.setter
    def X(self, value: float) -> None: ...
    def ApplyDefaults(self, controlPointInfo: ControlPointInfo, difficulty: IBeatmapDifficultyInfo, cancellationToken: CancellationToken = ...) -> None:
        """
        
        :param controlPointInfo: 
        :param difficulty: 
        :param cancellationToken: 
        """
    @classmethod
    def CreateDefaultNodeSamples(cls, obj: HitObject) -> List[IList[HitSampleInfo]]:
        """
        
        :param obj: 
        :return: 
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
    def GetNodeSamples(self, nodeIndex: int) -> IList[HitSampleInfo]:
        """
        
        :param nodeIndex: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    DefaultsApplied: EventType[Action[HitObject]] = ...
    """"""
class HoldNoteBody(ManiaHitObject, IHasColumn, IHasXPosition):
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
    def Column(self) -> int:
        """
        
        :return: 
        """
    @Column.setter
    def Column(self, value: int) -> None: ...
    @property
    def ColumnBindable(self) -> Bindable[int]:
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
    @property
    def X(self) -> float:
        """
        
        :return: 
        """
    @X.setter
    def X(self, value: float) -> None: ...
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
class ManiaHitObject(ABC, HitObject, IHasColumn, IHasXPosition):
    """"""
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
    def Column(self) -> int:
        """
        
        :return: 
        """
    @Column.setter
    def Column(self, value: int) -> None: ...
    @property
    def ColumnBindable(self) -> Bindable[int]:
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
    @property
    def X(self) -> float:
        """
        
        :return: 
        """
    @X.setter
    def X(self, value: float) -> None: ...
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
class Note(ManiaHitObject, IHasColumn, IHasXPosition):
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
    def Column(self) -> int:
        """
        
        :return: 
        """
    @Column.setter
    def Column(self, value: int) -> None: ...
    @property
    def ColumnBindable(self) -> Bindable[int]:
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
    @property
    def X(self) -> float:
        """
        
        :return: 
        """
    @X.setter
    def X(self, value: float) -> None: ...
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
class TailNote(Note, IHasColumn, IHasXPosition):
    """"""
    RELEASE_WINDOW_LENIENCE: Final[ClassVar[float]] = ...
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
    def Column(self) -> int:
        """
        
        :return: 
        """
    @Column.setter
    def Column(self, value: int) -> None: ...
    @property
    def ColumnBindable(self) -> Bindable[int]:
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
    @property
    def X(self) -> float:
        """
        
        :return: 
        """
    @X.setter
    def X(self, value: float) -> None: ...
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