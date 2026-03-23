from System.Collections.Generic import IList
from System import Enum
from System import IEquatable
from System import Object
from System import Type
from System import ValueType
from __future__ import annotations
from abc import ABC
from osu.Framework.Bindables import Bindable
from osu.Framework.Bindables import BindableNumber
from osu.Framework.Bindables import IHasDescription
from osu.Game.Audio import HitSampleInfo
from osu.Game.Rulesets.Objects import SliderPath
from osu.Game.Skinning import ISkin
from osuTK.Graphics import Color4
from osuTK import Vector2
from typing import ClassVar
from typing import Final
from typing import Optional
from typing import TypeVar
from typing import overload
T = TypeVar("T")
class HasPathWithRepeatsExtensions(ABC, Object):
    """"""
    @classmethod
    def CurvePositionAt(cls, obj: IHasPathWithRepeats, progress: float) -> Vector2:
        """
        
        :param obj: 
        :param progress: 
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ProgressAt(cls, obj: IHasPathWithRepeats, progress: float) -> float:
        """
        
        :param obj: 
        :param progress: 
        :return: 
        """
    @classmethod
    def SpanAt(cls, obj: IHasPathWithRepeats, progress: float) -> int:
        """
        
        :param obj: 
        :param progress: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class HasRepeatsExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetNodeSamples(cls, obj: T, nodeIndex: int) -> IList[HitSampleInfo]:
        """
        
        :param obj: 
        :param nodeIndex: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    @classmethod
    def PopulateNodeSamples(cls, obj: T) -> None:
        """
        
        :param obj: 
        """
    @classmethod
    def SpanCount(cls, obj: IHasRepeats) -> int:
        """
        
        :param obj: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class IHasColumn:
    """"""
    @property
    def Column(self) -> int:
        """
        
        :return: 
        """
class IHasCombo:
    """"""
    @property
    def ComboOffset(self) -> int:
        """
        
        :return: 
        """
    @property
    def NewCombo(self) -> bool:
        """
        
        :return: 
        """
class IHasComboInformation(IHasCombo):
    """"""
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
    def NewCombo(self) -> bool:
        """
        
        :return: 
        """
    @NewCombo.setter
    def NewCombo(self, value: bool) -> None: ...
    def GetComboColour(self, skin: ISkin) -> Color4:
        """
        
        :param skin: 
        :return: 
        """
    def UpdateComboInformation(self, lastObj: IHasComboInformation) -> None:
        """
        
        :param lastObj: 
        """
class IHasDisplayColour:
    """"""
    @property
    def DisplayColour(self) -> Bindable[Color4]:
        """
        
        :return: 
        """
class IHasDistance(IHasDuration):
    """"""
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
class IHasDuration:
    """"""
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
class IHasGenerateTicks:
    """"""
    @property
    def GenerateTicks(self) -> bool:
        """
        
        :return: 
        """
    @GenerateTicks.setter
    def GenerateTicks(self, value: bool) -> None: ...
class IHasHold:
    """"""
    @property
    def EndTime(self) -> float:
        """
        
        :return: 
        """
class IHasPath(IHasDistance, IHasDuration):
    """"""
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
    def Path(self) -> SliderPath:
        """
        
        :return: 
        """
class IHasPathWithRepeats(IHasDistance, IHasDuration, IHasPath, IHasRepeats):
    """"""
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
    def NodeSamples(self) -> IList[IList[HitSampleInfo]]:
        """
        
        :return: 
        """
    @property
    def Path(self) -> SliderPath:
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
class IHasPosition(IHasXPosition, IHasYPosition):
    """"""
    @property
    def Position(self) -> Vector2:
        """
        
        :return: 
        """
    @Position.setter
    def Position(self, value: Vector2) -> None: ...
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
class IHasRepeats(IHasDuration):
    """"""
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
    def NodeSamples(self) -> IList[IList[HitSampleInfo]]:
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
class IHasSliderVelocity:
    """"""
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
class IHasTimePreempt:
    """"""
    @property
    def TimePreempt(self) -> float:
        """
        
        :return: 
        """
class IHasXPosition:
    """"""
    @property
    def X(self) -> float:
        """
        
        :return: 
        """
    @X.setter
    def X(self, value: float) -> None: ...
class IHasYPosition:
    """"""
    @property
    def Y(self) -> float:
        """
        
        :return: 
        """
    @Y.setter
    def Y(self, value: float) -> None: ...
class PathType(ValueType, IEquatable[PathType], IHasDescription):
    """"""
    BEZIER: Final[ClassVar[PathType]] = ...
    """
    
    :return: 
    """
    CATMULL: Final[ClassVar[PathType]] = ...
    """
    
    :return: 
    """
    LINEAR: Final[ClassVar[PathType]] = ...
    """
    
    :return: 
    """
    PERFECT_CURVE: Final[ClassVar[PathType]] = ...
    """
    
    :return: 
    """
    def __init__(self, splineType: SplineType):
        """
        
        :param splineType: 
        """
    @property
    def Degree(self) -> Optional[int]:
        """
        
        :return: 
        """
    @Degree.setter
    def Degree(self, value: Optional[int]) -> None: ...
    @property
    def Description(self) -> str:
        """"""
    @property
    def Type(self) -> SplineType:
        """
        
        :return: 
        """
    @Type.setter
    def Type(self, value: SplineType) -> None: ...
    @classmethod
    def BSpline(cls, degree: int) -> PathType:
        """
        
        :param degree: 
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: PathType) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __eq__(self, other: PathType) -> bool:
        """
        
        :param other: 
        :return: 
        """
    def __ne__(self, other: PathType) -> bool:
        """
        
        :param other: 
        :return: 
        """
    @classmethod
    def op_Equality(cls, a: PathType, b: PathType) -> bool:
        """
        
        :param a: 
        :param b: 
        :return: 
        """
    @classmethod
    def op_Inequality(cls, a: PathType, b: PathType) -> bool:
        """
        
        :param a: 
        :param b: 
        :return: 
        """
class SplineType(Enum):
    """"""
    Catmull: SplineType = ...
    """"""
    BSpline: SplineType = ...
    """"""
    Linear: SplineType = ...
    """"""
    PerfectCurve: SplineType = ...
    """"""