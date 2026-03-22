from System import Action
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IList
from System import IEquatable
from System import Object
from System.Threading import CancellationToken
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Framework.Bindables import Bindable
from osu.Framework.Bindables import BindableList
from osu.Framework.Bindables import BindableNumber
from osu.Framework.Lists import SlimReadOnlyListWrapper
from osu.Game.Audio import HitSampleInfo
from osu.Game.Audio import ISampleInfo
from osu.Game.Beatmaps import BeatmapDifficulty
from osu.Game.Beatmaps.ControlPoints import ControlPointInfo
from osu.Game.Beatmaps.ControlPoints import TimingControlPoint
from osu.Game.Beatmaps import IBeatmapDifficultyInfo
from osu.Game.Beatmaps.Legacy import LegacyHitObjectType
from osu.Game.Rulesets.Judgements import Judgement
from osu.Game.Rulesets.Objects import HitObject
from osu.Game.Rulesets.Objects import HitObjectParser
from osu.Game.Rulesets.Objects.Legacy.ConvertHitObjectParser import LegacyHitSampleInfo
from osu.Game.Rulesets.Objects import SliderPath
from osu.Game.Rulesets.Objects.Types import IHasCombo
from osu.Game.Rulesets.Objects.Types import IHasDistance
from osu.Game.Rulesets.Objects.Types import IHasDuration
from osu.Game.Rulesets.Objects.Types import IHasGenerateTicks
from osu.Game.Rulesets.Objects.Types import IHasPath
from osu.Game.Rulesets.Objects.Types import IHasPathWithRepeats
from osu.Game.Rulesets.Objects.Types import IHasPosition
from osu.Game.Rulesets.Objects.Types import IHasRepeats
from osu.Game.Rulesets.Objects.Types import IHasSliderVelocity
from osu.Game.Rulesets.Objects.Types import IHasXPosition
from osu.Game.Rulesets.Objects.Types import IHasYPosition
from osu.Game.Rulesets.Scoring import HitWindows
from osu.Game.Utils import Optional
from osuTK import Vector2
from typing import Final
from typing import Generic
from typing import TypeVar
from typing import overload
T = TypeVar("T")
class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...
class ConvertHitCircle(ConvertHitObject, IHasLegacyHitObjectType, IHasCombo, IHasPosition, IHasXPosition, IHasYPosition):
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
    def ComboOffset(self) -> int:
        """
        
        :return: 
        """
    @ComboOffset.setter
    def ComboOffset(self, value: int) -> None: ...
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
    def LegacyType(self) -> LegacyHitObjectType:
        """
        
        :return: 
        """
    @LegacyType.setter
    def LegacyType(self, value: LegacyHitObjectType) -> None: ...
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
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    DefaultsApplied: EventType[Action[HitObject]] = ...
    """"""
class ConvertHitObject(ABC, HitObject, IHasLegacyHitObjectType, IHasCombo, IHasPosition, IHasXPosition, IHasYPosition):
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
    def ComboOffset(self) -> int:
        """
        
        :return: 
        """
    @ComboOffset.setter
    def ComboOffset(self, value: int) -> None: ...
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
    def LegacyType(self) -> LegacyHitObjectType:
        """
        
        :return: 
        """
    @LegacyType.setter
    def LegacyType(self, value: LegacyHitObjectType) -> None: ...
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
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    DefaultsApplied: EventType[Action[HitObject]] = ...
    """"""
class ConvertHitObjectParser(HitObjectParser):
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
    class LegacyHitSampleInfo(HitSampleInfo, IEquatable[HitSampleInfo], IEquatable[ConvertHitObjectParser.LegacyHitSampleInfo], ISampleInfo):
        """"""
        Bank: Final[str] = ...
        """
        
        :return: 
        """
        BankSpecified: Final[bool] = ...
        """"""
        CustomSampleBank: Final[int] = ...
        """"""
        IsLayered: Final[bool] = ...
        """"""
        Name: Final[str] = ...
        """
        
        :return: 
        """
        Suffix: Final[str] = ...
        """
        
        :return: 
        """
        def __init__(self, name: str, bank: str = ..., volume: int = ..., editorAutoBank: bool = ..., customSampleBank: int = ..., isLayered: bool = ...):
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
        def Equals(self, other: ConvertHitObjectParser.LegacyHitSampleInfo) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        @overload
        def With(self, newName: Optional[str] = ..., newBank: Optional[str] = ..., newSuffix: Optional[str] = ..., newVolume: Optional[int] = ..., newEditorAutoBank: Optional[bool] = ...) -> HitSampleInfo:
            """
            
            :param newName: 
            :param newBank: 
            :param newSuffix: 
            :param newVolume: 
            :param newEditorAutoBank: 
            :return: 
            """
        @overload
        def With(self, newName: Optional[str] = ..., newBank: Optional[str] = ..., newVolume: Optional[int] = ..., newEditorAutoBank: Optional[bool] = ..., newCustomSampleBank: Optional[int] = ..., newIsLayered: Optional[bool] = ...) -> ConvertHitObjectParser.LegacyHitSampleInfo:
            """"""
class ConvertHold(ConvertHitObject, IHasLegacyHitObjectType, IHasCombo, IHasDuration, IHasPosition, IHasXPosition, IHasYPosition):
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
    def EndTime(self) -> float:
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
    def LegacyType(self) -> LegacyHitObjectType:
        """
        
        :return: 
        """
    @LegacyType.setter
    def LegacyType(self, value: LegacyHitObjectType) -> None: ...
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
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    DefaultsApplied: EventType[Action[HitObject]] = ...
    """"""
class ConvertSlider(ConvertHitObject, IHasLegacyHitObjectType, IHasCombo, IHasDistance, IHasDuration, IHasGenerateTicks, IHasPath, IHasPathWithRepeats, IHasPosition, IHasRepeats, IHasSliderVelocity, IHasXPosition, IHasYPosition):
    """"""
    SamplesBindable: Final[BindableList[HitSampleInfo]] = ...
    """
    
    :return: 
    """
    StartTimeBindable: Final[Bindable[float]] = ...
    """
    
    :return: 
    """
    Velocity: Final[float] = ...
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
    def LegacyType(self) -> LegacyHitObjectType:
        """
        
        :return: 
        """
    @LegacyType.setter
    def LegacyType(self, value: LegacyHitObjectType) -> None: ...
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
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    DefaultsApplied: EventType[Action[HitObject]] = ...
    """"""
class ConvertSpinner(ConvertHitObject, IHasLegacyHitObjectType, IHasCombo, IHasDuration, IHasPosition, IHasXPosition, IHasYPosition):
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
    def EndTime(self) -> float:
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
    def LegacyType(self) -> LegacyHitObjectType:
        """
        
        :return: 
        """
    @LegacyType.setter
    def LegacyType(self, value: LegacyHitObjectType) -> None: ...
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
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    DefaultsApplied: EventType[Action[HitObject]] = ...
    """"""
class IHasLegacyHitObjectType:
    """"""
    @property
    def LegacyType(self) -> LegacyHitObjectType:
        """
        
        :return: 
        """
class LegacyRulesetExtensions(ABC, Object):
    """"""
    @classmethod
    def CalculateDifficultyPeppyStars(cls, difficulty: BeatmapDifficulty, objectCount: int, drainLength: int) -> int:
        """
        
        :param difficulty: 
        :param objectCount: 
        :param drainLength: 
        :return: 
        """
    @classmethod
    def CalculateScaleFromCircleSize(cls, circleSize: float, applyFudge: bool = ...) -> float:
        """
        
        :param circleSize: 
        :param applyFudge: 
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetPrecisionAdjustedBeatLength(cls, hasSliderVelocity: IHasSliderVelocity, timingControlPoint: TimingControlPoint, rulesetShortName: str) -> float:
        """
        
        :param hasSliderVelocity: 
        :param timingControlPoint: 
        :param rulesetShortName: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""