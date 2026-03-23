from System import Action
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IList
from System.Collections.Generic import IReadOnlyList
from System import Enum
from System import Func
from System import IComparable
from System import IEquatable
from System import Object
from System.Threading import CancellationToken
from System import Type
from System import ValueType
from __future__ import annotations
from abc import ABC
from osu.Framework.Bindables import Bindable
from osu.Framework.Bindables import BindableList
from osu.Framework.Bindables import BindableNumber
from osu.Framework.Lists import SlimReadOnlyListWrapper
from osu.Game.Audio import HitSampleInfo
from osu.Game.Audio import ISampleInfo
from osu.Game.Beatmaps.ControlPoints import ControlPointInfo
from osu.Game.Beatmaps import DifficultyRange
from osu.Game.Beatmaps import IBeatmapDifficultyInfo
from osu.Game.Rulesets.Catch.Objects.Banana import BananaHitSampleInfo
from osu.Game.Rulesets.Judgements import Judgement
from osu.Game.Rulesets.Objects import HitObject
from osu.Game.Rulesets.Objects import SliderPath
from osu.Game.Rulesets.Objects.Types import IHasCombo
from osu.Game.Rulesets.Objects.Types import IHasComboInformation
from osu.Game.Rulesets.Objects.Types import IHasDistance
from osu.Game.Rulesets.Objects.Types import IHasDuration
from osu.Game.Rulesets.Objects.Types import IHasPath
from osu.Game.Rulesets.Objects.Types import IHasPathWithRepeats
from osu.Game.Rulesets.Objects.Types import IHasPosition
from osu.Game.Rulesets.Objects.Types import IHasRepeats
from osu.Game.Rulesets.Objects.Types import IHasSliderVelocity
from osu.Game.Rulesets.Objects.Types import IHasTimePreempt
from osu.Game.Rulesets.Objects.Types import IHasXPosition
from osu.Game.Rulesets.Objects.Types import IHasYPosition
from osu.Game.Rulesets.Scoring import HitWindows
from osu.Game.Skinning import ISkin
from osu.Game.Utils import Optional
from osuTK.Graphics import Color4
from osuTK import Vector2
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import TypeVar
from typing import overload
T = TypeVar("T")
class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...
class Banana(PalpableCatchHitObject, IHasCombo, IHasComboInformation, IHasPosition, IHasTimePreempt, IHasXPosition, IHasYPosition):
    """"""
    BananaIndex: Final[int] = ...
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
    def DistanceToHyperDash(self) -> float:
        """
        
        :return: 
        """
    @DistanceToHyperDash.setter
    def DistanceToHyperDash(self, value: float) -> None: ...
    @property
    def EffectiveX(self) -> float:
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
    def HyperDash(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HyperDashBindable(self) -> Bindable[bool]:
        """
        
        :return: 
        """
    @property
    def HyperDashTarget(self) -> CatchHitObject:
        """
        
        :return: 
        """
    @HyperDashTarget.setter
    def HyperDashTarget(self, value: CatchHitObject) -> None: ...
    @property
    def IndexInBeatmap(self) -> int:
        """
        
        :return: 
        """
    @IndexInBeatmap.setter
    def IndexInBeatmap(self, value: int) -> None: ...
    @property
    def IndexInBeatmapBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
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
    def LegacyConvertedY(self) -> float:
        """
        
        :return: 
        """
    @LegacyConvertedY.setter
    def LegacyConvertedY(self, value: float) -> None: ...
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
    def OriginalX(self) -> float:
        """
        
        :return: 
        """
    @OriginalX.setter
    def OriginalX(self, value: float) -> None: ...
    @property
    def OriginalXBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
    @property
    def Position(self) -> Vector2:
        """
        
        :return: 
        """
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
    @property
    def RandomSeed(self) -> int:
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
    def XOffset(self) -> float:
        """
        
        :return: 
        """
    @XOffset.setter
    def XOffset(self, value: float) -> None: ...
    @property
    def XOffsetBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
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
    class BananaHitSampleInfo(HitSampleInfo, IEquatable[HitSampleInfo], IEquatable[Banana.BananaHitSampleInfo], ISampleInfo):
        """"""
        Bank: Final[str] = ...
        """
        
        :return: 
        """
        Name: Final[str] = ...
        """
        
        :return: 
        """
        Suffix: Final[str] = ...
        """
        
        :return: 
        """
        def __init__(self, volume: int = ...):
            """"""
        @property
        def EditorAutoBank(self) -> bool:
            """
            
            :return: 
            """
        @property
        def LookupNames(self) -> IEnumerable[str]:
            """
            
            :return: 
            """
        @property
        def Volume(self) -> int:
            """
            
            :return: 
            """
        @overload
        def Equals(self, obj: object) -> bool:
            """"""
        @overload
        def Equals(self, other: HitSampleInfo) -> bool:
            """"""
        @overload
        def Equals(self, other: Banana.BananaHitSampleInfo) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def With(self, newName: Optional[str] = ..., newBank: Optional[str] = ..., newSuffix: Optional[str] = ..., newVolume: Optional[int] = ..., newEditorAutoBank: Optional[bool] = ...) -> HitSampleInfo:
            """
            
            :param newName: 
            :param newBank: 
            :param newSuffix: 
            :param newVolume: 
            :param newEditorAutoBank: 
            :return: 
            """
class BananaShower(CatchHitObject, IHasCombo, IHasComboInformation, IHasDuration, IHasPosition, IHasTimePreempt, IHasXPosition, IHasYPosition):
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
    def Duration(self) -> float:
        """
        
        :return: 
        """
    @Duration.setter
    def Duration(self, value: float) -> None: ...
    @property
    def EffectiveX(self) -> float:
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
    def IndexInBeatmap(self) -> int:
        """
        
        :return: 
        """
    @IndexInBeatmap.setter
    def IndexInBeatmap(self, value: int) -> None: ...
    @property
    def IndexInBeatmapBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
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
    @property
    def LastInComboBindable(self) -> Bindable[bool]:
        """
        
        :return: 
        """
    @property
    def LegacyConvertedY(self) -> float:
        """
        
        :return: 
        """
    @LegacyConvertedY.setter
    def LegacyConvertedY(self, value: float) -> None: ...
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
    def OriginalX(self) -> float:
        """
        
        :return: 
        """
    @OriginalX.setter
    def OriginalX(self, value: float) -> None: ...
    @property
    def OriginalXBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
    @property
    def Position(self) -> Vector2:
        """
        
        :return: 
        """
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
    @property
    def RandomSeed(self) -> int:
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
    def XOffset(self) -> float:
        """
        
        :return: 
        """
    @XOffset.setter
    def XOffset(self, value: float) -> None: ...
    @property
    def XOffsetBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
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
class CatchHitObject(ABC, HitObject, IHasCombo, IHasComboInformation, IHasPosition, IHasTimePreempt, IHasXPosition, IHasYPosition):
    """"""
    DEFAULT_LEGACY_CONVERT_Y: Final[ClassVar[float]] = ...
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
    def EffectiveX(self) -> float:
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
    def IndexInBeatmap(self) -> int:
        """
        
        :return: 
        """
    @IndexInBeatmap.setter
    def IndexInBeatmap(self, value: int) -> None: ...
    @property
    def IndexInBeatmapBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
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
    def LegacyConvertedY(self) -> float:
        """
        
        :return: 
        """
    @LegacyConvertedY.setter
    def LegacyConvertedY(self, value: float) -> None: ...
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
    def OriginalX(self) -> float:
        """
        
        :return: 
        """
    @OriginalX.setter
    def OriginalX(self, value: float) -> None: ...
    @property
    def OriginalXBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
    @property
    def Position(self) -> Vector2:
        """
        
        :return: 
        """
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
    @property
    def RandomSeed(self) -> int:
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
    def XOffset(self) -> float:
        """
        
        :return: 
        """
    @XOffset.setter
    def XOffset(self, value: float) -> None: ...
    @property
    def XOffsetBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
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
class Droplet(PalpableCatchHitObject, IHasCombo, IHasComboInformation, IHasPosition, IHasTimePreempt, IHasXPosition, IHasYPosition):
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
    def DistanceToHyperDash(self) -> float:
        """
        
        :return: 
        """
    @DistanceToHyperDash.setter
    def DistanceToHyperDash(self, value: float) -> None: ...
    @property
    def EffectiveX(self) -> float:
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
    def HyperDash(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HyperDashBindable(self) -> Bindable[bool]:
        """
        
        :return: 
        """
    @property
    def HyperDashTarget(self) -> CatchHitObject:
        """
        
        :return: 
        """
    @HyperDashTarget.setter
    def HyperDashTarget(self, value: CatchHitObject) -> None: ...
    @property
    def IndexInBeatmap(self) -> int:
        """
        
        :return: 
        """
    @IndexInBeatmap.setter
    def IndexInBeatmap(self, value: int) -> None: ...
    @property
    def IndexInBeatmapBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
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
    def LegacyConvertedY(self) -> float:
        """
        
        :return: 
        """
    @LegacyConvertedY.setter
    def LegacyConvertedY(self, value: float) -> None: ...
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
    def OriginalX(self) -> float:
        """
        
        :return: 
        """
    @OriginalX.setter
    def OriginalX(self, value: float) -> None: ...
    @property
    def OriginalXBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
    @property
    def Position(self) -> Vector2:
        """
        
        :return: 
        """
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
    @property
    def RandomSeed(self) -> int:
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
    def XOffset(self) -> float:
        """
        
        :return: 
        """
    @XOffset.setter
    def XOffset(self, value: float) -> None: ...
    @property
    def XOffsetBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
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
class Fruit(PalpableCatchHitObject, IHasCombo, IHasComboInformation, IHasPosition, IHasTimePreempt, IHasXPosition, IHasYPosition):
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
    def DistanceToHyperDash(self) -> float:
        """
        
        :return: 
        """
    @DistanceToHyperDash.setter
    def DistanceToHyperDash(self, value: float) -> None: ...
    @property
    def EffectiveX(self) -> float:
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
    def HyperDash(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HyperDashBindable(self) -> Bindable[bool]:
        """
        
        :return: 
        """
    @property
    def HyperDashTarget(self) -> CatchHitObject:
        """
        
        :return: 
        """
    @HyperDashTarget.setter
    def HyperDashTarget(self, value: CatchHitObject) -> None: ...
    @property
    def IndexInBeatmap(self) -> int:
        """
        
        :return: 
        """
    @IndexInBeatmap.setter
    def IndexInBeatmap(self, value: int) -> None: ...
    @property
    def IndexInBeatmapBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
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
    def LegacyConvertedY(self) -> float:
        """
        
        :return: 
        """
    @LegacyConvertedY.setter
    def LegacyConvertedY(self, value: float) -> None: ...
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
    def OriginalX(self) -> float:
        """
        
        :return: 
        """
    @OriginalX.setter
    def OriginalX(self, value: float) -> None: ...
    @property
    def OriginalXBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
    @property
    def Position(self) -> Vector2:
        """
        
        :return: 
        """
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
    @property
    def RandomSeed(self) -> int:
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
    def XOffset(self) -> float:
        """
        
        :return: 
        """
    @XOffset.setter
    def XOffset(self, value: float) -> None: ...
    @property
    def XOffsetBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
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
    @classmethod
    def GetVisualRepresentation(cls, indexInBeatmap: int) -> FruitVisualRepresentation:
        """
        
        :param indexInBeatmap: 
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
class FruitVisualRepresentation(Enum):
    """"""
    Pear: FruitVisualRepresentation = ...
    """"""
    Grape: FruitVisualRepresentation = ...
    """"""
    Pineapple: FruitVisualRepresentation = ...
    """"""
    Raspberry: FruitVisualRepresentation = ...
    """"""
class JuiceStream(CatchHitObject, IHasCombo, IHasComboInformation, IHasDistance, IHasDuration, IHasPath, IHasPathWithRepeats, IHasPosition, IHasRepeats, IHasSliderVelocity, IHasTimePreempt, IHasXPosition, IHasYPosition):
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
    def EffectiveX(self) -> float:
        """
        
        :return: 
        """
    @property
    def EndTime(self) -> float:
        """
        
        :return: 
        """
    @property
    def EndX(self) -> float:
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
    def IndexInBeatmap(self) -> int:
        """
        
        :return: 
        """
    @IndexInBeatmap.setter
    def IndexInBeatmap(self, value: int) -> None: ...
    @property
    def IndexInBeatmapBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
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
    def LegacyConvertedY(self) -> float:
        """
        
        :return: 
        """
    @LegacyConvertedY.setter
    def LegacyConvertedY(self, value: float) -> None: ...
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
    def OriginalX(self) -> float:
        """
        
        :return: 
        """
    @OriginalX.setter
    def OriginalX(self, value: float) -> None: ...
    @property
    def OriginalXBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
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
    def RandomSeed(self) -> int:
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
    def StartTime(self) -> float:
        """
        
        :return: 
        """
    @StartTime.setter
    def StartTime(self, value: float) -> None: ...
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
    def XOffset(self) -> float:
        """
        
        :return: 
        """
    @XOffset.setter
    def XOffset(self, value: float) -> None: ...
    @property
    def XOffsetBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
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
class JuiceStreamPath(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Duration(self) -> float:
        """
        
        :return: 
        """
    @property
    def InvalidationID(self) -> int:
        """
        
        :return: 
        """
    @property
    def Vertices(self) -> IReadOnlyList[JuiceStreamPathVertex]:
        """
        
        :return: 
        """
    def Add(self, time: float, x: float) -> None:
        """
        
        :param time: 
        :param x: 
        """
    def Clear(self) -> None:
        """"""
    def ComputeRequiredVelocity(self) -> float:
        """
        
        :return: 
        """
    def ConvertFromSliderPath(self, sliderPath: SliderPath, velocity: float) -> None:
        """
        
        :param sliderPath: 
        :param velocity: 
        """
    def ConvertToSliderPath(self, sliderPath: SliderPath, sliderStartY: float, velocity: float) -> None:
        """
        
        :param sliderPath: 
        :param sliderStartY: 
        :param velocity: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def InsertVertex(self, time: float) -> int:
        """
        
        :param time: 
        :return: 
        """
    def PositionAtTime(self, time: float) -> float:
        """
        
        :param time: 
        :return: 
        """
    def RemoveVertices(self, predicate: Func[JuiceStreamPathVertex, int, bool]) -> int:
        """
        
        :param predicate: 
        :return: 
        """
    def ResampleVertices(self, sampleTimes: IEnumerable[float]) -> None:
        """
        
        :param sampleTimes: 
        """
    def SetVertexPosition(self, index: int, newX: float) -> None:
        """
        
        :param index: 
        :param newX: 
        """
    def ToString(self) -> str:
        """"""
class JuiceStreamPathVertex(ValueType, IComparable[JuiceStreamPathVertex]):
    """"""
    Time: Final[float] = ...
    """
    
    :return: 
    """
    X: Final[float] = ...
    """
    
    :return: 
    """
    def __init__(self, time: float, x: float):
        """
        
        :param time: 
        :param x: 
        """
    def CompareTo(self, other: JuiceStreamPathVertex) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class PalpableCatchHitObject(ABC, CatchHitObject, IHasCombo, IHasComboInformation, IHasPosition, IHasTimePreempt, IHasXPosition, IHasYPosition):
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
    def DistanceToHyperDash(self) -> float:
        """
        
        :return: 
        """
    @DistanceToHyperDash.setter
    def DistanceToHyperDash(self, value: float) -> None: ...
    @property
    def EffectiveX(self) -> float:
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
    def HyperDash(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HyperDashBindable(self) -> Bindable[bool]:
        """
        
        :return: 
        """
    @property
    def HyperDashTarget(self) -> CatchHitObject:
        """
        
        :return: 
        """
    @HyperDashTarget.setter
    def HyperDashTarget(self, value: CatchHitObject) -> None: ...
    @property
    def IndexInBeatmap(self) -> int:
        """
        
        :return: 
        """
    @IndexInBeatmap.setter
    def IndexInBeatmap(self, value: int) -> None: ...
    @property
    def IndexInBeatmapBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
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
    def LegacyConvertedY(self) -> float:
        """
        
        :return: 
        """
    @LegacyConvertedY.setter
    def LegacyConvertedY(self, value: float) -> None: ...
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
    def OriginalX(self) -> float:
        """
        
        :return: 
        """
    @OriginalX.setter
    def OriginalX(self, value: float) -> None: ...
    @property
    def OriginalXBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
    @property
    def Position(self) -> Vector2:
        """
        
        :return: 
        """
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
    @property
    def RandomSeed(self) -> int:
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
    def XOffset(self) -> float:
        """
        
        :return: 
        """
    @XOffset.setter
    def XOffset(self, value: float) -> None: ...
    @property
    def XOffsetBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
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
class TinyDroplet(Droplet, IHasCombo, IHasComboInformation, IHasPosition, IHasTimePreempt, IHasXPosition, IHasYPosition):
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
    def DistanceToHyperDash(self) -> float:
        """
        
        :return: 
        """
    @DistanceToHyperDash.setter
    def DistanceToHyperDash(self, value: float) -> None: ...
    @property
    def EffectiveX(self) -> float:
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
    def HyperDash(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HyperDashBindable(self) -> Bindable[bool]:
        """
        
        :return: 
        """
    @property
    def HyperDashTarget(self) -> CatchHitObject:
        """
        
        :return: 
        """
    @HyperDashTarget.setter
    def HyperDashTarget(self, value: CatchHitObject) -> None: ...
    @property
    def IndexInBeatmap(self) -> int:
        """
        
        :return: 
        """
    @IndexInBeatmap.setter
    def IndexInBeatmap(self, value: int) -> None: ...
    @property
    def IndexInBeatmapBindable(self) -> Bindable[int]:
        """
        
        :return: 
        """
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
    def LegacyConvertedY(self) -> float:
        """
        
        :return: 
        """
    @LegacyConvertedY.setter
    def LegacyConvertedY(self, value: float) -> None: ...
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
    def OriginalX(self) -> float:
        """
        
        :return: 
        """
    @OriginalX.setter
    def OriginalX(self, value: float) -> None: ...
    @property
    def OriginalXBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
    @property
    def Position(self) -> Vector2:
        """
        
        :return: 
        """
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
    @property
    def RandomSeed(self) -> int:
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
    def XOffset(self) -> float:
        """
        
        :return: 
        """
    @XOffset.setter
    def XOffset(self, value: float) -> None: ...
    @property
    def XOffsetBindable(self) -> Bindable[float]:
        """
        
        :return: 
        """
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