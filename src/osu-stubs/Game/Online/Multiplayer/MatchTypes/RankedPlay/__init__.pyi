from System.Collections.Generic import Dictionary
from System.Collections.Generic import List
from System import Enum
from System import Guid
from System import IEquatable
from System import Object
from System import Type
from __future__ import annotations
from osu.Game.Online.Multiplayer import MatchRoomState
from typing import Final
from typing import Optional
from typing import overload
class RankedPlayCardItem(Object, IEquatable[RankedPlayCardItem]):
    """"""
    def __init__(self):
        """"""
    @property
    def ID(self) -> Guid:
        """
        
        :return: 
        """
    @ID.setter
    def ID(self, value: Guid) -> None: ...
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: RankedPlayCardItem) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class RankedPlayDamageInfo(Object, IEquatable[RankedPlayDamageInfo]):
    """"""
    def __init__(self):
        """"""
    @property
    def BonusDamage(self) -> int:
        """
        
        :return: 
        """
    @BonusDamage.setter
    def BonusDamage(self, value: int) -> None: ...
    @property
    def Damage(self) -> int:
        """
        
        :return: 
        """
    @Damage.setter
    def Damage(self, value: int) -> None: ...
    @property
    def DirectDamage(self) -> int:
        """
        
        :return: 
        """
    @DirectDamage.setter
    def DirectDamage(self, value: int) -> None: ...
    @property
    def Multiplier(self) -> float:
        """
        
        :return: 
        """
    @Multiplier.setter
    def Multiplier(self, value: float) -> None: ...
    @property
    def NewLife(self) -> int:
        """
        
        :return: 
        """
    @NewLife.setter
    def NewLife(self, value: int) -> None: ...
    @property
    def OldLife(self) -> int:
        """
        
        :return: 
        """
    @OldLife.setter
    def OldLife(self, value: int) -> None: ...
    @property
    def RawDamage(self) -> int:
        """
        
        :return: 
        """
    @RawDamage.setter
    def RawDamage(self, value: int) -> None: ...
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: RankedPlayDamageInfo) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class RankedPlayRoomState(MatchRoomState):
    """"""
    def __init__(self):
        """"""
    @property
    def ActiveUser(self) -> RankedPlayUserInfo:
        """
        
        :return: 
        """
    @property
    def ActiveUserId(self) -> Optional[int]:
        """
        
        :return: 
        """
    @ActiveUserId.setter
    def ActiveUserId(self, value: Optional[int]) -> None: ...
    @property
    def CurrentRound(self) -> int:
        """
        
        :return: 
        """
    @CurrentRound.setter
    def CurrentRound(self, value: int) -> None: ...
    @property
    def DamageMultiplier(self) -> float:
        """
        
        :return: 
        """
    @DamageMultiplier.setter
    def DamageMultiplier(self, value: float) -> None: ...
    @property
    def Stage(self) -> RankedPlayStage:
        """
        
        :return: 
        """
    @Stage.setter
    def Stage(self, value: RankedPlayStage) -> None: ...
    @property
    def StarRating(self) -> float:
        """
        
        :return: 
        """
    @StarRating.setter
    def StarRating(self, value: float) -> None: ...
    @property
    def Users(self) -> Dictionary[int, RankedPlayUserInfo]:
        """
        
        :return: 
        """
    @Users.setter
    def Users(self, value: Dictionary[int, RankedPlayUserInfo]) -> None: ...
    @property
    def WinningUser(self) -> RankedPlayUserInfo:
        """
        
        :return: 
        """
    @property
    def WinningUserId(self) -> Optional[int]:
        """
        
        :return: 
        """
    @WinningUserId.setter
    def WinningUserId(self, value: Optional[int]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class RankedPlayStage(Enum):
    """"""
    WaitForJoin: RankedPlayStage = ...
    """"""
    RoundWarmup: RankedPlayStage = ...
    """"""
    CardDiscard: RankedPlayStage = ...
    """"""
    FinishCardDiscard: RankedPlayStage = ...
    """"""
    CardPlay: RankedPlayStage = ...
    """"""
    FinishCardPlay: RankedPlayStage = ...
    """"""
    GameplayWarmup: RankedPlayStage = ...
    """"""
    Gameplay: RankedPlayStage = ...
    """"""
    Results: RankedPlayStage = ...
    """"""
    Ended: RankedPlayStage = ...
    """"""
class RankedPlayUserInfo(Object):
    """"""
    DamageInfo: Final[RankedPlayDamageInfo] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def DamageMultiplier(self) -> float:
        """
        
        :return: 
        """
    @DamageMultiplier.setter
    def DamageMultiplier(self, value: float) -> None: ...
    @property
    def Hand(self) -> List[RankedPlayCardItem]:
        """
        
        :return: 
        """
    @Hand.setter
    def Hand(self, value: List[RankedPlayCardItem]) -> None: ...
    @property
    def Life(self) -> int:
        """
        
        :return: 
        """
    @Life.setter
    def Life(self, value: int) -> None: ...
    @property
    def Rating(self) -> int:
        """
        
        :return: 
        """
    @Rating.setter
    def Rating(self, value: int) -> None: ...
    @property
    def RatingAfter(self) -> int:
        """
        
        :return: 
        """
    @RatingAfter.setter
    def RatingAfter(self, value: int) -> None: ...
    @property
    def RoundsWon(self) -> int:
        """
        
        :return: 
        """
    @RoundsWon.setter
    def RoundsWon(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""