from System import Action
from System import Array
from System.Collections.Generic import IList
from System.Threading import CancellationToken
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Framework.Bindables import Bindable
from osu.Framework.Bindables import BindableList
from osu.Framework.Bindables import BindableNumber
from osu.Framework.Lists import SlimReadOnlyListWrapper
from osu.Game.Audio import HitSampleInfo
from osu.Game.Beatmaps.ControlPoints import ControlPointInfo
from osu.Game.Beatmaps import DifficultyRange
from osu.Game.Beatmaps import IBeatmapDifficultyInfo
from osu.Game.Rulesets.Judgements import Judgement
from osu.Game.Rulesets.Judgements import JudgementResult
from osu.Game.Rulesets.Objects import HitObject
from osu.Game.Rulesets.Objects import SliderPath
from osu.Game.Rulesets.Objects.Types import IHasCombo
from osu.Game.Rulesets.Objects.Types import IHasComboInformation
from osu.Game.Rulesets.Objects.Types import IHasDistance
from osu.Game.Rulesets.Objects.Types import IHasDuration
from osu.Game.Rulesets.Objects.Types import IHasGenerateTicks
from osu.Game.Rulesets.Objects.Types import IHasPath
from osu.Game.Rulesets.Objects.Types import IHasPathWithRepeats
from osu.Game.Rulesets.Objects.Types import IHasPosition
from osu.Game.Rulesets.Objects.Types import IHasRepeats
from osu.Game.Rulesets.Objects.Types import IHasSliderVelocity
from osu.Game.Rulesets.Objects.Types import IHasTimePreempt
from osu.Game.Rulesets.Objects.Types import IHasXPosition
from osu.Game.Rulesets.Objects.Types import IHasYPosition
from osu.Game.Rulesets.Osu.Judgements import OsuJudgement
from osu.Game.Rulesets.Osu.Objects.SliderEndCircle import SliderEndJudgement
from osu.Game.Rulesets.Osu.Objects.SpinnerTick import OsuSpinnerTickJudgement
from osu.Game.Rulesets.Scoring import HitResult
from osu.Game.Rulesets.Scoring import HitWindows
from osu.Game.Skinning import ISkin
from osuTK.Graphics import Color4
from osuTK import Vector2
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import TypeVar
T = TypeVar("T")
class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...
class HitCircle(OsuHitObject, IHasCombo, IHasComboInformation, IHasPosition, IHasTimePreempt, IHasXPosition, IHasYPosition):
    """"""
    SamplesBindable: Final[BindableList[HitSampleInfo]] = ...
    """
    
    :return: 
    """
    StartTimeBindable: Final[Bindable[float]] = ...
    """
    
    :return: 
    """
    TimeFadeIn: Final[float] = ...
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
    def ComboIndex(self) -> int:
        """
        
        :return: 
        """
    @ComboIndex.setter
    def ComboIndex(self, value: int) -> None: ...
    @property
    def ComboIndexBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ComboIndexWithOffsets(self) -> int:
        """
        
        :return: 
        """
    @ComboIndexWithOffsets.setter
    def ComboIndexWithOffsets(self, value: int) -> None: ...
    @property
    def ComboIndexWithOffsetsBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ComboOffset(self) -> int:
        """
        
        :return: 
        """
    @ComboOffset.setter
    def ComboOffset(self, value: int) -> None: ...
    @property
    def ComboOffsetBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def EndPosition(self) -> Vector2:
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
    def IndexInCurrentCombo(self) -> int:
        """
        
        :return: 
        """
    @IndexInCurrentCombo.setter
    def IndexInCurrentCombo(self, value: int) -> None: ...
    @property
    def IndexInCurrentComboBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
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
    def LastInCombo(self) -> bool:
        """
        
        :return: 
        """
    @LastInCombo.setter
    def LastInCombo(self, value: bool) -> None: ...
    @property
    def LastInComboBindable(self) -> Bindable[bool]:
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
    def NewCombo(self) -> bool:
        """
        
        :return: 
        """
    @NewCombo.setter
    def NewCombo(self, value: bool) -> None: ...
    @property
    def Position(self) -> Vector2:
        """
        
        :return: 
        """
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
    @property
    def PositionBindable(self) -> Bindable[Vector2]:
        """
        
        :return: 
        """
    @property
    def Radius(self) -> float:
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
    def Scale(self) -> float:
        """
        
        :return: 
        """
    @Scale.setter
    def Scale(self, value: float) -> None: ...
    @property
    def ScaleBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
    @property
    def StackHeight(self) -> int:
        """
        
        :return: 
        """
    @StackHeight.setter
    def StackHeight(self, value: int) -> None: ...
    @property
    def StackHeightBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def StackOffset(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StackedEndPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StackedPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StartTime(self) -> float:
        """
        
        :return: 
        """
    @StartTime.setter
    def StartTime(self, value: float) -> None: ...
    @property
    def TimePreempt(self) -> float:
        """
        
        :return: 
        """
    @TimePreempt.setter
    def TimePreempt(self, value: float) -> None: ...
    @property
    def X(self) -> float:
        """
        
        :return: 
        """
    @X.setter
    def X(self, value: float) -> None: ...
    @property
    def Y(self) -> float:
        """
        
        :return: 
        """
    @Y.setter
    def Y(self, value: float) -> None: ...
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
    def GetComboColour(self, skin: ISkin) -> Color4:
        """
        
        :param skin: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def UpdateComboInformation(self, lastObj: IHasComboInformation) -> None:
        """
        
        :param lastObj: 
        """
    DefaultsApplied: EventType[Action[HitObject]] = ...
    """"""
class ISliderProgress:
    """"""
    def UpdateProgress(self, completionProgress: float) -> None:
        """
        
        :param completionProgress: 
        """
class OsuHitObject(ABC, HitObject, IHasCombo, IHasComboInformation, IHasPosition, IHasTimePreempt, IHasXPosition, IHasYPosition):
    """"""
    OBJECT_DIMENSIONS: Final[ClassVar[Vector2]] = ...
    """
    
    :return: 
    """
    OBJECT_RADIUS: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    PREEMPT_MAX: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    PREEMPT_MID: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    PREEMPT_MIN: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    PREEMPT_RANGE: Final[ClassVar[DifficultyRange]] = ...
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
    TimeFadeIn: Final[float] = ...
    """
    
    :return: 
    """
    @property
    def AuxiliarySamples(self) -> IList[HitSampleInfo]:
        """
        
        :return: 
        """
    @property
    def ComboIndex(self) -> int:
        """
        
        :return: 
        """
    @ComboIndex.setter
    def ComboIndex(self, value: int) -> None: ...
    @property
    def ComboIndexBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ComboIndexWithOffsets(self) -> int:
        """
        
        :return: 
        """
    @ComboIndexWithOffsets.setter
    def ComboIndexWithOffsets(self, value: int) -> None: ...
    @property
    def ComboIndexWithOffsetsBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ComboOffset(self) -> int:
        """
        
        :return: 
        """
    @ComboOffset.setter
    def ComboOffset(self, value: int) -> None: ...
    @property
    def ComboOffsetBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def EndPosition(self) -> Vector2:
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
    def IndexInCurrentCombo(self) -> int:
        """
        
        :return: 
        """
    @IndexInCurrentCombo.setter
    def IndexInCurrentCombo(self, value: int) -> None: ...
    @property
    def IndexInCurrentComboBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
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
    def LastInCombo(self) -> bool:
        """
        
        :return: 
        """
    @LastInCombo.setter
    def LastInCombo(self, value: bool) -> None: ...
    @property
    def LastInComboBindable(self) -> Bindable[bool]:
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
    def NewCombo(self) -> bool:
        """
        
        :return: 
        """
    @NewCombo.setter
    def NewCombo(self, value: bool) -> None: ...
    @property
    def Position(self) -> Vector2:
        """
        
        :return: 
        """
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
    @property
    def PositionBindable(self) -> Bindable[Vector2]:
        """
        
        :return: 
        """
    @property
    def Radius(self) -> float:
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
    def Scale(self) -> float:
        """
        
        :return: 
        """
    @Scale.setter
    def Scale(self, value: float) -> None: ...
    @property
    def ScaleBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
    @property
    def StackHeight(self) -> int:
        """
        
        :return: 
        """
    @StackHeight.setter
    def StackHeight(self, value: int) -> None: ...
    @property
    def StackHeightBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def StackOffset(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StackedEndPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StackedPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StartTime(self) -> float:
        """
        
        :return: 
        """
    @StartTime.setter
    def StartTime(self, value: float) -> None: ...
    @property
    def TimePreempt(self) -> float:
        """
        
        :return: 
        """
    @TimePreempt.setter
    def TimePreempt(self, value: float) -> None: ...
    @property
    def X(self) -> float:
        """
        
        :return: 
        """
    @X.setter
    def X(self, value: float) -> None: ...
    @property
    def Y(self) -> float:
        """
        
        :return: 
        """
    @Y.setter
    def Y(self, value: float) -> None: ...
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
    def GetComboColour(self, skin: ISkin) -> Color4:
        """
        
        :param skin: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def UpdateComboInformation(self, lastObj: IHasComboInformation) -> None:
        """
        
        :param lastObj: 
        """
    DefaultsApplied: EventType[Action[HitObject]] = ...
    """"""
class Slider(OsuHitObject, IHasCombo, IHasComboInformation, IHasDistance, IHasDuration, IHasGenerateTicks, IHasPath, IHasPathWithRepeats, IHasPosition, IHasRepeats, IHasSliderVelocity, IHasTimePreempt, IHasXPosition, IHasYPosition):
    """"""
    SamplesBindable: Final[BindableList[HitSampleInfo]] = ...
    """
    
    :return: 
    """
    StartTimeBindable: Final[Bindable[float]] = ...
    """
    
    :return: 
    """
    TickDistanceMultiplier: Final[float] = ...
    """
    
    :return: 
    """
    TimeFadeIn: Final[float] = ...
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
    def ClassicSliderBehaviour(self) -> bool:
        """
        
        :return: 
        """
    @ClassicSliderBehaviour.setter
    def ClassicSliderBehaviour(self, value: bool) -> None: ...
    @property
    def ComboIndex(self) -> int:
        """
        
        :return: 
        """
    @ComboIndex.setter
    def ComboIndex(self, value: int) -> None: ...
    @property
    def ComboIndexBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ComboIndexWithOffsets(self) -> int:
        """
        
        :return: 
        """
    @ComboIndexWithOffsets.setter
    def ComboIndexWithOffsets(self, value: int) -> None: ...
    @property
    def ComboIndexWithOffsetsBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ComboOffset(self) -> int:
        """
        
        :return: 
        """
    @ComboOffset.setter
    def ComboOffset(self, value: int) -> None: ...
    @property
    def ComboOffsetBindable(self) -> Bindable[int]:
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
    def EndPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def EndTime(self) -> float:
        """
        
        :return: 
        """
    @property
    def GenerateTicks(self) -> bool:
        """
        
        :return: 
        """
    @GenerateTicks.setter
    def GenerateTicks(self, value: bool) -> None: ...
    @property
    def HeadCircle(self) -> SliderHeadCircle:
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
    def IndexInCurrentCombo(self) -> int:
        """
        
        :return: 
        """
    @IndexInCurrentCombo.setter
    def IndexInCurrentCombo(self, value: int) -> None: ...
    @property
    def IndexInCurrentComboBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
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
    def LastInCombo(self) -> bool:
        """
        
        :return: 
        """
    @LastInCombo.setter
    def LastInCombo(self, value: bool) -> None: ...
    @property
    def LastInComboBindable(self) -> Bindable[bool]:
        """
        
        :return: 
        """
    @property
    def LastRepeat(self) -> SliderRepeat:
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
    def NewCombo(self) -> bool:
        """
        
        :return: 
        """
    @NewCombo.setter
    def NewCombo(self, value: bool) -> None: ...
    @property
    def NodeSamples(self) -> IList[IList[HitSampleInfo]]:
        """
        
        :return: 
        """
    @NodeSamples.setter
    def NodeSamples(self, value: IList[IList[HitSampleInfo]]) -> None: ...
    @property
    def Path(self) -> SliderPath:
        """
        
        :return: 
        """
    @Path.setter
    def Path(self, value: SliderPath) -> None: ...
    @property
    def Position(self) -> Vector2:
        """
        
        :return: 
        """
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
    @property
    def PositionBindable(self) -> Bindable[Vector2]:
        """
        
        :return: 
        """
    @property
    def Radius(self) -> float:
        """
        
        :return: 
        """
    @property
    def RepeatCount(self) -> int:
        """
        
        :return: 
        """
    @RepeatCount.setter
    def RepeatCount(self, value: int) -> None: ...
    @property
    def Samples(self) -> IList[HitSampleInfo]:
        """
        
        :return: 
        """
    @Samples.setter
    def Samples(self, value: IList[HitSampleInfo]) -> None: ...
    @property
    def Scale(self) -> float:
        """
        
        :return: 
        """
    @Scale.setter
    def Scale(self, value: float) -> None: ...
    @property
    def ScaleBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
    @property
    def SliderVelocityMultiplier(self) -> float:
        """
        
        :return: 
        """
    @SliderVelocityMultiplier.setter
    def SliderVelocityMultiplier(self, value: float) -> None: ...
    @property
    def SliderVelocityMultiplierBindable(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def SpanDuration(self) -> float:
        """
        
        :return: 
        """
    @property
    def StackHeight(self) -> int:
        """
        
        :return: 
        """
    @StackHeight.setter
    def StackHeight(self, value: int) -> None: ...
    @property
    def StackHeightBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def StackOffset(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StackedEndPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StackedPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StartTime(self) -> float:
        """
        
        :return: 
        """
    @StartTime.setter
    def StartTime(self, value: float) -> None: ...
    @property
    def TailCircle(self) -> SliderTailCircle:
        """
        
        :return: 
        """
    @property
    def TailSamples(self) -> IList[HitSampleInfo]:
        """
        
        :return: 
        """
    @property
    def TickDistance(self) -> float:
        """
        
        :return: 
        """
    @property
    def TimePreempt(self) -> float:
        """
        
        :return: 
        """
    @TimePreempt.setter
    def TimePreempt(self, value: float) -> None: ...
    @property
    def Velocity(self) -> float:
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
    @property
    def Y(self) -> float:
        """
        
        :return: 
        """
    @Y.setter
    def Y(self, value: float) -> None: ...
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
    def GetComboColour(self, skin: ISkin) -> Color4:
        """
        
        :param skin: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def StackedPositionAt(self, t: float) -> Vector2:
        """
        
        :param t: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    def UpdateComboInformation(self, lastObj: IHasComboInformation) -> None:
        """
        
        :param lastObj: 
        """
    DefaultsApplied: EventType[Action[HitObject]] = ...
    """"""
class SliderEndCircle(ABC, HitCircle, IHasCombo, IHasComboInformation, IHasPosition, IHasTimePreempt, IHasXPosition, IHasYPosition):
    """"""
    SamplesBindable: Final[BindableList[HitSampleInfo]] = ...
    """
    
    :return: 
    """
    StartTimeBindable: Final[Bindable[float]] = ...
    """
    
    :return: 
    """
    TimeFadeIn: Final[float] = ...
    """
    
    :return: 
    """
    @property
    def AuxiliarySamples(self) -> IList[HitSampleInfo]:
        """
        
        :return: 
        """
    @property
    def ComboIndex(self) -> int:
        """
        
        :return: 
        """
    @ComboIndex.setter
    def ComboIndex(self, value: int) -> None: ...
    @property
    def ComboIndexBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ComboIndexWithOffsets(self) -> int:
        """
        
        :return: 
        """
    @ComboIndexWithOffsets.setter
    def ComboIndexWithOffsets(self, value: int) -> None: ...
    @property
    def ComboIndexWithOffsetsBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ComboOffset(self) -> int:
        """
        
        :return: 
        """
    @ComboOffset.setter
    def ComboOffset(self, value: int) -> None: ...
    @property
    def ComboOffsetBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def EndPosition(self) -> Vector2:
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
    def IndexInCurrentCombo(self) -> int:
        """
        
        :return: 
        """
    @IndexInCurrentCombo.setter
    def IndexInCurrentCombo(self, value: int) -> None: ...
    @property
    def IndexInCurrentComboBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
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
    def LastInCombo(self) -> bool:
        """
        
        :return: 
        """
    @LastInCombo.setter
    def LastInCombo(self, value: bool) -> None: ...
    @property
    def LastInComboBindable(self) -> Bindable[bool]:
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
    def NewCombo(self) -> bool:
        """
        
        :return: 
        """
    @NewCombo.setter
    def NewCombo(self, value: bool) -> None: ...
    @property
    def Position(self) -> Vector2:
        """
        
        :return: 
        """
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
    @property
    def PositionBindable(self) -> Bindable[Vector2]:
        """
        
        :return: 
        """
    @property
    def Radius(self) -> float:
        """
        
        :return: 
        """
    @property
    def RepeatIndex(self) -> int:
        """
        
        :return: 
        """
    @RepeatIndex.setter
    def RepeatIndex(self, value: int) -> None: ...
    @property
    def Samples(self) -> IList[HitSampleInfo]:
        """
        
        :return: 
        """
    @Samples.setter
    def Samples(self, value: IList[HitSampleInfo]) -> None: ...
    @property
    def Scale(self) -> float:
        """
        
        :return: 
        """
    @Scale.setter
    def Scale(self, value: float) -> None: ...
    @property
    def ScaleBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
    @property
    def SpanDuration(self) -> float:
        """
        
        :return: 
        """
    @property
    def StackHeight(self) -> int:
        """
        
        :return: 
        """
    @StackHeight.setter
    def StackHeight(self, value: int) -> None: ...
    @property
    def StackHeightBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def StackOffset(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StackedEndPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StackedPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StartTime(self) -> float:
        """
        
        :return: 
        """
    @StartTime.setter
    def StartTime(self, value: float) -> None: ...
    @property
    def TimePreempt(self) -> float:
        """
        
        :return: 
        """
    @TimePreempt.setter
    def TimePreempt(self, value: float) -> None: ...
    @property
    def X(self) -> float:
        """
        
        :return: 
        """
    @X.setter
    def X(self, value: float) -> None: ...
    @property
    def Y(self) -> float:
        """
        
        :return: 
        """
    @Y.setter
    def Y(self, value: float) -> None: ...
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
    def GetComboColour(self, skin: ISkin) -> Color4:
        """
        
        :param skin: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def UpdateComboInformation(self, lastObj: IHasComboInformation) -> None:
        """
        
        :param lastObj: 
        """
    DefaultsApplied: EventType[Action[HitObject]] = ...
    """"""
    class SliderEndJudgement(OsuJudgement):
        """"""
        def __init__(self):
            """"""
        @property
        def MaxHealthIncrease(self) -> float:
            """
            
            :return: 
            """
        @property
        def MaxResult(self) -> HitResult:
            """
            
            :return: 
            """
        @property
        def MinResult(self) -> HitResult:
            """
            
            :return: 
            """
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def HealthIncreaseFor(self, result: JudgementResult) -> float:
            """
            
            :param result: 
            :return: 
            """
        def ToString(self) -> str:
            """"""
class SliderHeadCircle(HitCircle, IHasCombo, IHasComboInformation, IHasPosition, IHasTimePreempt, IHasXPosition, IHasYPosition):
    """"""
    ClassicSliderBehaviour: Final[bool] = ...
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
    TimeFadeIn: Final[float] = ...
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
    def ComboIndex(self) -> int:
        """
        
        :return: 
        """
    @ComboIndex.setter
    def ComboIndex(self, value: int) -> None: ...
    @property
    def ComboIndexBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ComboIndexWithOffsets(self) -> int:
        """
        
        :return: 
        """
    @ComboIndexWithOffsets.setter
    def ComboIndexWithOffsets(self, value: int) -> None: ...
    @property
    def ComboIndexWithOffsetsBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ComboOffset(self) -> int:
        """
        
        :return: 
        """
    @ComboOffset.setter
    def ComboOffset(self, value: int) -> None: ...
    @property
    def ComboOffsetBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def EndPosition(self) -> Vector2:
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
    def IndexInCurrentCombo(self) -> int:
        """
        
        :return: 
        """
    @IndexInCurrentCombo.setter
    def IndexInCurrentCombo(self, value: int) -> None: ...
    @property
    def IndexInCurrentComboBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
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
    def LastInCombo(self) -> bool:
        """
        
        :return: 
        """
    @LastInCombo.setter
    def LastInCombo(self, value: bool) -> None: ...
    @property
    def LastInComboBindable(self) -> Bindable[bool]:
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
    def NewCombo(self) -> bool:
        """
        
        :return: 
        """
    @NewCombo.setter
    def NewCombo(self, value: bool) -> None: ...
    @property
    def Position(self) -> Vector2:
        """
        
        :return: 
        """
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
    @property
    def PositionBindable(self) -> Bindable[Vector2]:
        """
        
        :return: 
        """
    @property
    def Radius(self) -> float:
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
    def Scale(self) -> float:
        """
        
        :return: 
        """
    @Scale.setter
    def Scale(self, value: float) -> None: ...
    @property
    def ScaleBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
    @property
    def StackHeight(self) -> int:
        """
        
        :return: 
        """
    @StackHeight.setter
    def StackHeight(self, value: int) -> None: ...
    @property
    def StackHeightBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def StackOffset(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StackedEndPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StackedPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StartTime(self) -> float:
        """
        
        :return: 
        """
    @StartTime.setter
    def StartTime(self, value: float) -> None: ...
    @property
    def TimePreempt(self) -> float:
        """
        
        :return: 
        """
    @TimePreempt.setter
    def TimePreempt(self, value: float) -> None: ...
    @property
    def X(self) -> float:
        """
        
        :return: 
        """
    @X.setter
    def X(self, value: float) -> None: ...
    @property
    def Y(self) -> float:
        """
        
        :return: 
        """
    @Y.setter
    def Y(self, value: float) -> None: ...
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
    def GetComboColour(self, skin: ISkin) -> Color4:
        """
        
        :param skin: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def UpdateComboInformation(self, lastObj: IHasComboInformation) -> None:
        """
        
        :param lastObj: 
        """
    DefaultsApplied: EventType[Action[HitObject]] = ...
    """"""
class SliderRepeat(SliderEndCircle, IHasCombo, IHasComboInformation, IHasPosition, IHasTimePreempt, IHasXPosition, IHasYPosition):
    """"""
    SamplesBindable: Final[BindableList[HitSampleInfo]] = ...
    """
    
    :return: 
    """
    StartTimeBindable: Final[Bindable[float]] = ...
    """
    
    :return: 
    """
    TimeFadeIn: Final[float] = ...
    """
    
    :return: 
    """
    def __init__(self, slider: Slider):
        """
        
        :param slider: 
        """
    @property
    def AuxiliarySamples(self) -> IList[HitSampleInfo]:
        """
        
        :return: 
        """
    @property
    def ComboIndex(self) -> int:
        """
        
        :return: 
        """
    @ComboIndex.setter
    def ComboIndex(self, value: int) -> None: ...
    @property
    def ComboIndexBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ComboIndexWithOffsets(self) -> int:
        """
        
        :return: 
        """
    @ComboIndexWithOffsets.setter
    def ComboIndexWithOffsets(self, value: int) -> None: ...
    @property
    def ComboIndexWithOffsetsBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ComboOffset(self) -> int:
        """
        
        :return: 
        """
    @ComboOffset.setter
    def ComboOffset(self, value: int) -> None: ...
    @property
    def ComboOffsetBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def EndPosition(self) -> Vector2:
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
    def IndexInCurrentCombo(self) -> int:
        """
        
        :return: 
        """
    @IndexInCurrentCombo.setter
    def IndexInCurrentCombo(self, value: int) -> None: ...
    @property
    def IndexInCurrentComboBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
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
    def LastInCombo(self) -> bool:
        """
        
        :return: 
        """
    @LastInCombo.setter
    def LastInCombo(self, value: bool) -> None: ...
    @property
    def LastInComboBindable(self) -> Bindable[bool]:
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
    def NewCombo(self) -> bool:
        """
        
        :return: 
        """
    @NewCombo.setter
    def NewCombo(self, value: bool) -> None: ...
    @property
    def PathProgress(self) -> float:
        """
        
        :return: 
        """
    @PathProgress.setter
    def PathProgress(self, value: float) -> None: ...
    @property
    def Position(self) -> Vector2:
        """
        
        :return: 
        """
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
    @property
    def PositionBindable(self) -> Bindable[Vector2]:
        """
        
        :return: 
        """
    @property
    def Radius(self) -> float:
        """
        
        :return: 
        """
    @property
    def RepeatIndex(self) -> int:
        """
        
        :return: 
        """
    @RepeatIndex.setter
    def RepeatIndex(self, value: int) -> None: ...
    @property
    def Samples(self) -> IList[HitSampleInfo]:
        """
        
        :return: 
        """
    @Samples.setter
    def Samples(self, value: IList[HitSampleInfo]) -> None: ...
    @property
    def Scale(self) -> float:
        """
        
        :return: 
        """
    @Scale.setter
    def Scale(self, value: float) -> None: ...
    @property
    def ScaleBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
    @property
    def SpanDuration(self) -> float:
        """
        
        :return: 
        """
    @property
    def StackHeight(self) -> int:
        """
        
        :return: 
        """
    @StackHeight.setter
    def StackHeight(self, value: int) -> None: ...
    @property
    def StackHeightBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def StackOffset(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StackedEndPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StackedPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StartTime(self) -> float:
        """
        
        :return: 
        """
    @StartTime.setter
    def StartTime(self, value: float) -> None: ...
    @property
    def TimePreempt(self) -> float:
        """
        
        :return: 
        """
    @TimePreempt.setter
    def TimePreempt(self, value: float) -> None: ...
    @property
    def X(self) -> float:
        """
        
        :return: 
        """
    @X.setter
    def X(self, value: float) -> None: ...
    @property
    def Y(self) -> float:
        """
        
        :return: 
        """
    @Y.setter
    def Y(self, value: float) -> None: ...
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
    def GetComboColour(self, skin: ISkin) -> Color4:
        """
        
        :param skin: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def UpdateComboInformation(self, lastObj: IHasComboInformation) -> None:
        """
        
        :param lastObj: 
        """
    DefaultsApplied: EventType[Action[HitObject]] = ...
    """"""
class SliderTailCircle(SliderEndCircle, IHasCombo, IHasComboInformation, IHasPosition, IHasTimePreempt, IHasXPosition, IHasYPosition):
    """"""
    ClassicSliderBehaviour: Final[bool] = ...
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
    TimeFadeIn: Final[float] = ...
    """
    
    :return: 
    """
    def __init__(self, slider: Slider):
        """
        
        :param slider: 
        """
    @property
    def AuxiliarySamples(self) -> IList[HitSampleInfo]:
        """
        
        :return: 
        """
    @property
    def ComboIndex(self) -> int:
        """
        
        :return: 
        """
    @ComboIndex.setter
    def ComboIndex(self, value: int) -> None: ...
    @property
    def ComboIndexBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ComboIndexWithOffsets(self) -> int:
        """
        
        :return: 
        """
    @ComboIndexWithOffsets.setter
    def ComboIndexWithOffsets(self, value: int) -> None: ...
    @property
    def ComboIndexWithOffsetsBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ComboOffset(self) -> int:
        """
        
        :return: 
        """
    @ComboOffset.setter
    def ComboOffset(self, value: int) -> None: ...
    @property
    def ComboOffsetBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def EndPosition(self) -> Vector2:
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
    def IndexInCurrentCombo(self) -> int:
        """
        
        :return: 
        """
    @IndexInCurrentCombo.setter
    def IndexInCurrentCombo(self, value: int) -> None: ...
    @property
    def IndexInCurrentComboBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
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
    def LastInCombo(self) -> bool:
        """
        
        :return: 
        """
    @LastInCombo.setter
    def LastInCombo(self, value: bool) -> None: ...
    @property
    def LastInComboBindable(self) -> Bindable[bool]:
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
    def NewCombo(self) -> bool:
        """
        
        :return: 
        """
    @NewCombo.setter
    def NewCombo(self, value: bool) -> None: ...
    @property
    def Position(self) -> Vector2:
        """
        
        :return: 
        """
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
    @property
    def PositionBindable(self) -> Bindable[Vector2]:
        """
        
        :return: 
        """
    @property
    def Radius(self) -> float:
        """
        
        :return: 
        """
    @property
    def RepeatIndex(self) -> int:
        """
        
        :return: 
        """
    @RepeatIndex.setter
    def RepeatIndex(self, value: int) -> None: ...
    @property
    def Samples(self) -> IList[HitSampleInfo]:
        """
        
        :return: 
        """
    @Samples.setter
    def Samples(self, value: IList[HitSampleInfo]) -> None: ...
    @property
    def Scale(self) -> float:
        """
        
        :return: 
        """
    @Scale.setter
    def Scale(self, value: float) -> None: ...
    @property
    def ScaleBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
    @property
    def SpanDuration(self) -> float:
        """
        
        :return: 
        """
    @property
    def StackHeight(self) -> int:
        """
        
        :return: 
        """
    @StackHeight.setter
    def StackHeight(self, value: int) -> None: ...
    @property
    def StackHeightBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def StackOffset(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StackedEndPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StackedPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StartTime(self) -> float:
        """
        
        :return: 
        """
    @StartTime.setter
    def StartTime(self, value: float) -> None: ...
    @property
    def TimePreempt(self) -> float:
        """
        
        :return: 
        """
    @TimePreempt.setter
    def TimePreempt(self, value: float) -> None: ...
    @property
    def X(self) -> float:
        """
        
        :return: 
        """
    @X.setter
    def X(self, value: float) -> None: ...
    @property
    def Y(self) -> float:
        """
        
        :return: 
        """
    @Y.setter
    def Y(self, value: float) -> None: ...
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
    def GetComboColour(self, skin: ISkin) -> Color4:
        """
        
        :param skin: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def UpdateComboInformation(self, lastObj: IHasComboInformation) -> None:
        """
        
        :param lastObj: 
        """
    DefaultsApplied: EventType[Action[HitObject]] = ...
    """"""
    class LegacyTailJudgement(OsuJudgement):
        """"""
        def __init__(self):
            """"""
        @property
        def MaxHealthIncrease(self) -> float:
            """
            
            :return: 
            """
        @property
        def MaxResult(self) -> HitResult:
            """
            
            :return: 
            """
        @property
        def MinResult(self) -> HitResult:
            """
            
            :return: 
            """
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def HealthIncreaseFor(self, result: JudgementResult) -> float:
            """
            
            :param result: 
            :return: 
            """
        def ToString(self) -> str:
            """"""
    class TailJudgement(SliderEndCircle.SliderEndJudgement):
        """"""
        def __init__(self):
            """"""
        @property
        def MaxHealthIncrease(self) -> float:
            """
            
            :return: 
            """
        @property
        def MaxResult(self) -> HitResult:
            """
            
            :return: 
            """
        @property
        def MinResult(self) -> HitResult:
            """
            
            :return: 
            """
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def HealthIncreaseFor(self, result: JudgementResult) -> float:
            """
            
            :param result: 
            :return: 
            """
        def ToString(self) -> str:
            """"""
class SliderTick(OsuHitObject, IHasCombo, IHasComboInformation, IHasPosition, IHasTimePreempt, IHasXPosition, IHasYPosition):
    """"""
    SamplesBindable: Final[BindableList[HitSampleInfo]] = ...
    """
    
    :return: 
    """
    StartTimeBindable: Final[Bindable[float]] = ...
    """
    
    :return: 
    """
    TimeFadeIn: Final[float] = ...
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
    def ComboIndex(self) -> int:
        """
        
        :return: 
        """
    @ComboIndex.setter
    def ComboIndex(self, value: int) -> None: ...
    @property
    def ComboIndexBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ComboIndexWithOffsets(self) -> int:
        """
        
        :return: 
        """
    @ComboIndexWithOffsets.setter
    def ComboIndexWithOffsets(self, value: int) -> None: ...
    @property
    def ComboIndexWithOffsetsBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ComboOffset(self) -> int:
        """
        
        :return: 
        """
    @ComboOffset.setter
    def ComboOffset(self, value: int) -> None: ...
    @property
    def ComboOffsetBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def EndPosition(self) -> Vector2:
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
    def IndexInCurrentCombo(self) -> int:
        """
        
        :return: 
        """
    @IndexInCurrentCombo.setter
    def IndexInCurrentCombo(self, value: int) -> None: ...
    @property
    def IndexInCurrentComboBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
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
    def LastInCombo(self) -> bool:
        """
        
        :return: 
        """
    @LastInCombo.setter
    def LastInCombo(self, value: bool) -> None: ...
    @property
    def LastInComboBindable(self) -> Bindable[bool]:
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
    def NewCombo(self) -> bool:
        """
        
        :return: 
        """
    @NewCombo.setter
    def NewCombo(self, value: bool) -> None: ...
    @property
    def PathProgress(self) -> float:
        """
        
        :return: 
        """
    @PathProgress.setter
    def PathProgress(self, value: float) -> None: ...
    @property
    def Position(self) -> Vector2:
        """
        
        :return: 
        """
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
    @property
    def PositionBindable(self) -> Bindable[Vector2]:
        """
        
        :return: 
        """
    @property
    def Radius(self) -> float:
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
    def Scale(self) -> float:
        """
        
        :return: 
        """
    @Scale.setter
    def Scale(self, value: float) -> None: ...
    @property
    def ScaleBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
    @property
    def SpanIndex(self) -> int:
        """
        
        :return: 
        """
    @SpanIndex.setter
    def SpanIndex(self, value: int) -> None: ...
    @property
    def SpanStartTime(self) -> float:
        """
        
        :return: 
        """
    @SpanStartTime.setter
    def SpanStartTime(self, value: float) -> None: ...
    @property
    def StackHeight(self) -> int:
        """
        
        :return: 
        """
    @StackHeight.setter
    def StackHeight(self, value: int) -> None: ...
    @property
    def StackHeightBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def StackOffset(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StackedEndPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StackedPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StartTime(self) -> float:
        """
        
        :return: 
        """
    @StartTime.setter
    def StartTime(self, value: float) -> None: ...
    @property
    def TimePreempt(self) -> float:
        """
        
        :return: 
        """
    @TimePreempt.setter
    def TimePreempt(self, value: float) -> None: ...
    @property
    def X(self) -> float:
        """
        
        :return: 
        """
    @X.setter
    def X(self, value: float) -> None: ...
    @property
    def Y(self) -> float:
        """
        
        :return: 
        """
    @Y.setter
    def Y(self, value: float) -> None: ...
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
    def GetComboColour(self, skin: ISkin) -> Color4:
        """
        
        :param skin: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def UpdateComboInformation(self, lastObj: IHasComboInformation) -> None:
        """
        
        :param lastObj: 
        """
    DefaultsApplied: EventType[Action[HitObject]] = ...
    """"""
class Spinner(OsuHitObject, IHasCombo, IHasComboInformation, IHasDuration, IHasPosition, IHasTimePreempt, IHasXPosition, IHasYPosition):
    """"""
    CLEAR_RPM_RANGE: Final[ClassVar[DifficultyRange]] = ...
    """
    
    :return: 
    """
    COMPLETE_RPM_RANGE: Final[ClassVar[DifficultyRange]] = ...
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
    TimeFadeIn: Final[float] = ...
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
    def ComboIndex(self) -> int:
        """
        
        :return: 
        """
    @ComboIndex.setter
    def ComboIndex(self, value: int) -> None: ...
    @property
    def ComboIndexBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ComboIndexWithOffsets(self) -> int:
        """
        
        :return: 
        """
    @ComboIndexWithOffsets.setter
    def ComboIndexWithOffsets(self, value: int) -> None: ...
    @property
    def ComboIndexWithOffsetsBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ComboOffset(self) -> int:
        """
        
        :return: 
        """
    @ComboOffset.setter
    def ComboOffset(self, value: int) -> None: ...
    @property
    def ComboOffsetBindable(self) -> Bindable[int]:
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
    def EndPosition(self) -> Vector2:
        """
        
        :return: 
        """
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
    def IndexInCurrentCombo(self) -> int:
        """
        
        :return: 
        """
    @IndexInCurrentCombo.setter
    def IndexInCurrentCombo(self, value: int) -> None: ...
    @property
    def IndexInCurrentComboBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
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
    def LastInCombo(self) -> bool:
        """
        
        :return: 
        """
    @LastInCombo.setter
    def LastInCombo(self, value: bool) -> None: ...
    @property
    def LastInComboBindable(self) -> Bindable[bool]:
        """
        
        :return: 
        """
    @property
    def MaximumBonusSpins(self) -> int:
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
    def NewCombo(self) -> bool:
        """
        
        :return: 
        """
    @NewCombo.setter
    def NewCombo(self, value: bool) -> None: ...
    @property
    def Position(self) -> Vector2:
        """
        
        :return: 
        """
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
    @property
    def PositionBindable(self) -> Bindable[Vector2]:
        """
        
        :return: 
        """
    @property
    def Radius(self) -> float:
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
    def Scale(self) -> float:
        """
        
        :return: 
        """
    @Scale.setter
    def Scale(self, value: float) -> None: ...
    @property
    def ScaleBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
    @property
    def SpinsRequired(self) -> int:
        """
        
        :return: 
        """
    @property
    def SpinsRequiredForBonus(self) -> int:
        """
        
        :return: 
        """
    @property
    def StackHeight(self) -> int:
        """
        
        :return: 
        """
    @StackHeight.setter
    def StackHeight(self, value: int) -> None: ...
    @property
    def StackHeightBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def StackOffset(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StackedEndPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StackedPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StartTime(self) -> float:
        """
        
        :return: 
        """
    @StartTime.setter
    def StartTime(self, value: float) -> None: ...
    @property
    def TimePreempt(self) -> float:
        """
        
        :return: 
        """
    @TimePreempt.setter
    def TimePreempt(self, value: float) -> None: ...
    @property
    def X(self) -> float:
        """
        
        :return: 
        """
    @X.setter
    def X(self, value: float) -> None: ...
    @property
    def Y(self) -> float:
        """
        
        :return: 
        """
    @Y.setter
    def Y(self, value: float) -> None: ...
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
    def CreateSpinningSamples(self) -> Array[HitSampleInfo]:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetComboColour(self, skin: ISkin) -> Color4:
        """
        
        :param skin: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def UpdateComboInformation(self, lastObj: IHasComboInformation) -> None:
        """
        
        :param lastObj: 
        """
    DefaultsApplied: EventType[Action[HitObject]] = ...
    """"""
class SpinnerBonusTick(SpinnerTick, IHasCombo, IHasComboInformation, IHasPosition, IHasTimePreempt, IHasXPosition, IHasYPosition):
    """"""
    SamplesBindable: Final[BindableList[HitSampleInfo]] = ...
    """
    
    :return: 
    """
    StartTimeBindable: Final[Bindable[float]] = ...
    """
    
    :return: 
    """
    TimeFadeIn: Final[float] = ...
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
    def ComboIndex(self) -> int:
        """
        
        :return: 
        """
    @ComboIndex.setter
    def ComboIndex(self, value: int) -> None: ...
    @property
    def ComboIndexBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ComboIndexWithOffsets(self) -> int:
        """
        
        :return: 
        """
    @ComboIndexWithOffsets.setter
    def ComboIndexWithOffsets(self, value: int) -> None: ...
    @property
    def ComboIndexWithOffsetsBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ComboOffset(self) -> int:
        """
        
        :return: 
        """
    @ComboOffset.setter
    def ComboOffset(self, value: int) -> None: ...
    @property
    def ComboOffsetBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def EndPosition(self) -> Vector2:
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
    def IndexInCurrentCombo(self) -> int:
        """
        
        :return: 
        """
    @IndexInCurrentCombo.setter
    def IndexInCurrentCombo(self, value: int) -> None: ...
    @property
    def IndexInCurrentComboBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
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
    def LastInCombo(self) -> bool:
        """
        
        :return: 
        """
    @LastInCombo.setter
    def LastInCombo(self, value: bool) -> None: ...
    @property
    def LastInComboBindable(self) -> Bindable[bool]:
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
    def NewCombo(self) -> bool:
        """
        
        :return: 
        """
    @NewCombo.setter
    def NewCombo(self, value: bool) -> None: ...
    @property
    def Position(self) -> Vector2:
        """
        
        :return: 
        """
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
    @property
    def PositionBindable(self) -> Bindable[Vector2]:
        """
        
        :return: 
        """
    @property
    def Radius(self) -> float:
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
    def Scale(self) -> float:
        """
        
        :return: 
        """
    @Scale.setter
    def Scale(self, value: float) -> None: ...
    @property
    def ScaleBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
    @property
    def SpinnerDuration(self) -> float:
        """
        
        :return: 
        """
    @SpinnerDuration.setter
    def SpinnerDuration(self, value: float) -> None: ...
    @property
    def StackHeight(self) -> int:
        """
        
        :return: 
        """
    @StackHeight.setter
    def StackHeight(self, value: int) -> None: ...
    @property
    def StackHeightBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def StackOffset(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StackedEndPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StackedPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StartTime(self) -> float:
        """
        
        :return: 
        """
    @StartTime.setter
    def StartTime(self, value: float) -> None: ...
    @property
    def TimePreempt(self) -> float:
        """
        
        :return: 
        """
    @TimePreempt.setter
    def TimePreempt(self, value: float) -> None: ...
    @property
    def X(self) -> float:
        """
        
        :return: 
        """
    @X.setter
    def X(self, value: float) -> None: ...
    @property
    def Y(self) -> float:
        """
        
        :return: 
        """
    @Y.setter
    def Y(self, value: float) -> None: ...
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
    def GetComboColour(self, skin: ISkin) -> Color4:
        """
        
        :param skin: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def UpdateComboInformation(self, lastObj: IHasComboInformation) -> None:
        """
        
        :param lastObj: 
        """
    DefaultsApplied: EventType[Action[HitObject]] = ...
    """"""
    class OsuSpinnerBonusTickJudgement(SpinnerTick.OsuSpinnerTickJudgement):
        """"""
        def __init__(self):
            """"""
        @property
        def MaxHealthIncrease(self) -> float:
            """
            
            :return: 
            """
        @property
        def MaxResult(self) -> HitResult:
            """
            
            :return: 
            """
        @property
        def MinResult(self) -> HitResult:
            """
            
            :return: 
            """
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def HealthIncreaseFor(self, result: JudgementResult) -> float:
            """
            
            :param result: 
            :return: 
            """
        def ToString(self) -> str:
            """"""
class SpinnerTick(OsuHitObject, IHasCombo, IHasComboInformation, IHasPosition, IHasTimePreempt, IHasXPosition, IHasYPosition):
    """"""
    SamplesBindable: Final[BindableList[HitSampleInfo]] = ...
    """
    
    :return: 
    """
    StartTimeBindable: Final[Bindable[float]] = ...
    """
    
    :return: 
    """
    TimeFadeIn: Final[float] = ...
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
    def ComboIndex(self) -> int:
        """
        
        :return: 
        """
    @ComboIndex.setter
    def ComboIndex(self, value: int) -> None: ...
    @property
    def ComboIndexBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ComboIndexWithOffsets(self) -> int:
        """
        
        :return: 
        """
    @ComboIndexWithOffsets.setter
    def ComboIndexWithOffsets(self, value: int) -> None: ...
    @property
    def ComboIndexWithOffsetsBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ComboOffset(self) -> int:
        """
        
        :return: 
        """
    @ComboOffset.setter
    def ComboOffset(self, value: int) -> None: ...
    @property
    def ComboOffsetBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def EndPosition(self) -> Vector2:
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
    def IndexInCurrentCombo(self) -> int:
        """
        
        :return: 
        """
    @IndexInCurrentCombo.setter
    def IndexInCurrentCombo(self, value: int) -> None: ...
    @property
    def IndexInCurrentComboBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
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
    def LastInCombo(self) -> bool:
        """
        
        :return: 
        """
    @LastInCombo.setter
    def LastInCombo(self, value: bool) -> None: ...
    @property
    def LastInComboBindable(self) -> Bindable[bool]:
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
    def NewCombo(self) -> bool:
        """
        
        :return: 
        """
    @NewCombo.setter
    def NewCombo(self, value: bool) -> None: ...
    @property
    def Position(self) -> Vector2:
        """
        
        :return: 
        """
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
    @property
    def PositionBindable(self) -> Bindable[Vector2]:
        """
        
        :return: 
        """
    @property
    def Radius(self) -> float:
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
    def Scale(self) -> float:
        """
        
        :return: 
        """
    @Scale.setter
    def Scale(self, value: float) -> None: ...
    @property
    def ScaleBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
    @property
    def SpinnerDuration(self) -> float:
        """
        
        :return: 
        """
    @SpinnerDuration.setter
    def SpinnerDuration(self, value: float) -> None: ...
    @property
    def StackHeight(self) -> int:
        """
        
        :return: 
        """
    @StackHeight.setter
    def StackHeight(self, value: int) -> None: ...
    @property
    def StackHeightBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def StackOffset(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StackedEndPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StackedPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def StartTime(self) -> float:
        """
        
        :return: 
        """
    @StartTime.setter
    def StartTime(self, value: float) -> None: ...
    @property
    def TimePreempt(self) -> float:
        """
        
        :return: 
        """
    @TimePreempt.setter
    def TimePreempt(self, value: float) -> None: ...
    @property
    def X(self) -> float:
        """
        
        :return: 
        """
    @X.setter
    def X(self, value: float) -> None: ...
    @property
    def Y(self) -> float:
        """
        
        :return: 
        """
    @Y.setter
    def Y(self, value: float) -> None: ...
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
    def GetComboColour(self, skin: ISkin) -> Color4:
        """
        
        :param skin: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def UpdateComboInformation(self, lastObj: IHasComboInformation) -> None:
        """
        
        :param lastObj: 
        """
    DefaultsApplied: EventType[Action[HitObject]] = ...
    """"""
    class OsuSpinnerTickJudgement(OsuJudgement):
        """"""
        def __init__(self):
            """"""
        @property
        def MaxHealthIncrease(self) -> float:
            """
            
            :return: 
            """
        @property
        def MaxResult(self) -> HitResult:
            """
            
            :return: 
            """
        @property
        def MinResult(self) -> HitResult:
            """
            
            :return: 
            """
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def HealthIncreaseFor(self, result: JudgementResult) -> float:
            """
            
            :param result: 
            :return: 
            """
        def ToString(self) -> str:
            """"""