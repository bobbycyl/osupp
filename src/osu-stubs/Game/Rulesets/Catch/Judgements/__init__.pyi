from System import Type
from __future__ import annotations
from osu.Game.Rulesets.Catch.UI import CatcherAnimationState
from osu.Game.Rulesets.Judgements import Judgement
from osu.Game.Rulesets.Judgements import JudgementResult
from osu.Game.Rulesets.Objects import HitObject
from osu.Game.Rulesets.Scoring import HitResult
from typing import Final
from typing import Optional
class CatchBananaJudgement(CatchJudgement):
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
    def ShouldExplodeFor(self, result: JudgementResult) -> bool:
        """
        
        :param result: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class CatchDropletJudgement(CatchJudgement):
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
    def ShouldExplodeFor(self, result: JudgementResult) -> bool:
        """
        
        :param result: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class CatchJudgement(Judgement):
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
    def ShouldExplodeFor(self, result: JudgementResult) -> bool:
        """
        
        :param result: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class CatchJudgementResult(JudgementResult):
    """"""
    CatcherAnimationState: Final[CatcherAnimationState] = ...
    """
    
    :return: 
    """
    CatcherHyperDash: Final[bool] = ...
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
class CatchTinyDropletJudgement(CatchJudgement):
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
    def ShouldExplodeFor(self, result: JudgementResult) -> bool:
        """
        
        :param result: 
        :return: 
        """
    def ToString(self) -> str:
        """"""