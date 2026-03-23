from System.Collections.Generic import Stack
from System import Enum
from System import Type
from System import ValueTuple
from __future__ import annotations
from osu.Game.Rulesets.Judgements import Judgement
from osu.Game.Rulesets.Judgements import JudgementResult
from osu.Game.Rulesets.Objects import HitObject
from osu.Game.Rulesets.Osu.Objects.Drawables import SpinnerSpinHistory
from osu.Game.Rulesets.Osu.Objects import HitCircle
from osu.Game.Rulesets.Osu.Objects import Spinner
from osu.Game.Rulesets.Scoring import HitResult
from osuTK import Vector2
from typing import Final
from typing import Optional
class ComboResult(Enum):
    """"""
    _None: ComboResult = ...
    """"""
    Good: ComboResult = ...
    """"""
    Perfect: ComboResult = ...
    """"""
class OsuHitCircleJudgementResult(OsuJudgementResult):
    """"""
    ComboType: Final[ComboResult] = ...
    """
    
    :return: 
    """
    CursorPositionAtHit: Final[Optional[Vector2]] = ...
    """
    
    :return: 
    """
    HitObject: Final[HitObject] = ...
    """
    
    :return: 
    """
    Judgement: Final[Judgement] = ...
    """
    
    :return: 
    """
    Type: Final[HitResult] = ...
    """
    
    :return: 
    """
    def __init__(self, hitObject: HitObject, judgement: Judgement):
        """
        
        :param hitObject: 
        :param judgement: 
        """
    @property
    def ComboAfterJudgement(self) -> int:
        """
        
        :return: 
        """
    @property
    def ComboAtJudgement(self) -> int:
        """
        
        :return: 
        """
    @property
    def FailedAtJudgement(self) -> bool:
        """
        
        :return: 
        """
    @property
    def GameplayRate(self) -> Optional[float]:
        """
        
        :return: 
        """
    @property
    def HasResult(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HealthAtJudgement(self) -> float:
        """
        
        :return: 
        """
    @property
    def HealthIncrease(self) -> float:
        """
        
        :return: 
        """
    @property
    def HighestComboAfterJudgement(self) -> int:
        """
        
        :return: 
        """
    @property
    def HighestComboAtJudgement(self) -> int:
        """
        
        :return: 
        """
    @property
    def HitCircle(self) -> HitCircle:
        """
        
        :return: 
        """
    @property
    def IsHit(self) -> bool:
        """
        
        :return: 
        """
    @property
    def TimeAbsolute(self) -> float:
        """
        
        :return: 
        """
    @property
    def TimeOffset(self) -> float:
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
class OsuIgnoreJudgement(OsuJudgement):
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
class OsuJudgement(Judgement):
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
class OsuJudgementResult(JudgementResult):
    """"""
    ComboType: Final[ComboResult] = ...
    """
    
    :return: 
    """
    HitObject: Final[HitObject] = ...
    """
    
    :return: 
    """
    Judgement: Final[Judgement] = ...
    """
    
    :return: 
    """
    Type: Final[HitResult] = ...
    """
    
    :return: 
    """
    def __init__(self, hitObject: HitObject, judgement: Judgement):
        """
        
        :param hitObject: 
        :param judgement: 
        """
    @property
    def ComboAfterJudgement(self) -> int:
        """
        
        :return: 
        """
    @property
    def ComboAtJudgement(self) -> int:
        """
        
        :return: 
        """
    @property
    def FailedAtJudgement(self) -> bool:
        """
        
        :return: 
        """
    @property
    def GameplayRate(self) -> Optional[float]:
        """
        
        :return: 
        """
    @property
    def HasResult(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HealthAtJudgement(self) -> float:
        """
        
        :return: 
        """
    @property
    def HealthIncrease(self) -> float:
        """
        
        :return: 
        """
    @property
    def HighestComboAfterJudgement(self) -> int:
        """
        
        :return: 
        """
    @property
    def HighestComboAtJudgement(self) -> int:
        """
        
        :return: 
        """
    @property
    def IsHit(self) -> bool:
        """
        
        :return: 
        """
    @property
    def TimeAbsolute(self) -> float:
        """
        
        :return: 
        """
    @property
    def TimeOffset(self) -> float:
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
class OsuSliderJudgementResult(OsuJudgementResult):
    """"""
    ComboType: Final[ComboResult] = ...
    """
    
    :return: 
    """
    HitObject: Final[HitObject] = ...
    """
    
    :return: 
    """
    Judgement: Final[Judgement] = ...
    """
    
    :return: 
    """
    TrackingHistory: Final[Stack[ValueTuple, bool]] = ...
    """
    
    :return: 
    """
    Type: Final[HitResult] = ...
    """
    
    :return: 
    """
    def __init__(self, hitObject: HitObject, judgement: Judgement):
        """
        
        :param hitObject: 
        :param judgement: 
        """
    @property
    def ComboAfterJudgement(self) -> int:
        """
        
        :return: 
        """
    @property
    def ComboAtJudgement(self) -> int:
        """
        
        :return: 
        """
    @property
    def FailedAtJudgement(self) -> bool:
        """
        
        :return: 
        """
    @property
    def GameplayRate(self) -> Optional[float]:
        """
        
        :return: 
        """
    @property
    def HasResult(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HealthAtJudgement(self) -> float:
        """
        
        :return: 
        """
    @property
    def HealthIncrease(self) -> float:
        """
        
        :return: 
        """
    @property
    def HighestComboAfterJudgement(self) -> int:
        """
        
        :return: 
        """
    @property
    def HighestComboAtJudgement(self) -> int:
        """
        
        :return: 
        """
    @property
    def IsHit(self) -> bool:
        """
        
        :return: 
        """
    @property
    def TimeAbsolute(self) -> float:
        """
        
        :return: 
        """
    @property
    def TimeOffset(self) -> float:
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
class OsuSpinnerJudgementResult(OsuJudgementResult):
    """"""
    ComboType: Final[ComboResult] = ...
    """
    
    :return: 
    """
    History: Final[SpinnerSpinHistory] = ...
    """
    
    :return: 
    """
    HitObject: Final[HitObject] = ...
    """
    
    :return: 
    """
    Judgement: Final[Judgement] = ...
    """
    
    :return: 
    """
    TimeCompleted: Final[Optional[float]] = ...
    """
    
    :return: 
    """
    TimeStarted: Final[Optional[float]] = ...
    """
    
    :return: 
    """
    Type: Final[HitResult] = ...
    """
    
    :return: 
    """
    def __init__(self, hitObject: HitObject, judgement: Judgement):
        """
        
        :param hitObject: 
        :param judgement: 
        """
    @property
    def ComboAfterJudgement(self) -> int:
        """
        
        :return: 
        """
    @property
    def ComboAtJudgement(self) -> int:
        """
        
        :return: 
        """
    @property
    def FailedAtJudgement(self) -> bool:
        """
        
        :return: 
        """
    @property
    def GameplayRate(self) -> Optional[float]:
        """
        
        :return: 
        """
    @property
    def HasResult(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HealthAtJudgement(self) -> float:
        """
        
        :return: 
        """
    @property
    def HealthIncrease(self) -> float:
        """
        
        :return: 
        """
    @property
    def HighestComboAfterJudgement(self) -> int:
        """
        
        :return: 
        """
    @property
    def HighestComboAtJudgement(self) -> int:
        """
        
        :return: 
        """
    @property
    def IsHit(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Spinner(self) -> Spinner:
        """
        
        :return: 
        """
    @property
    def TimeAbsolute(self) -> float:
        """
        
        :return: 
        """
    @property
    def TimeOffset(self) -> float:
        """
        
        :return: 
        """
    @property
    def TotalRotation(self) -> float:
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
class SliderTickJudgement(OsuJudgement):
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