from System import Array
from System.Collections.Generic import Comparer
from System.Collections.Generic import IComparer
from System.Collections.Generic import IDictionary
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEnumerator
from System.Collections import IComparer
from System.Collections import IEnumerable
from System import DateTimeOffset
from System import Enum
from System import Object
from System import Type
from __future__ import annotations
from osu.Game.Online.API.Requests.Responses import SoloScoreInfo
from osu.Game.Online.Multiplayer import MatchRoomState
from osu.Game.Rulesets.Scoring import HitResult
from typing import Iterator
from typing import Optional
from typing import overload
class MatchmakingRoomState(MatchRoomState):
    """"""
    def __init__(self):
        """"""
    @property
    def CandidateItem(self) -> int:
        """
        
        :return: 
        """
    @CandidateItem.setter
    def CandidateItem(self, value: int) -> None: ...
    @property
    def CandidateItems(self) -> Array[int]:
        """
        
        :return: 
        """
    @CandidateItems.setter
    def CandidateItems(self, value: Array[int]) -> None: ...
    @property
    def CurrentRound(self) -> int:
        """
        
        :return: 
        """
    @CurrentRound.setter
    def CurrentRound(self, value: int) -> None: ...
    @property
    def GameplayItem(self) -> int:
        """
        
        :return: 
        """
    @GameplayItem.setter
    def GameplayItem(self, value: int) -> None: ...
    @property
    def Stage(self) -> MatchmakingStage:
        """
        
        :return: 
        """
    @Stage.setter
    def Stage(self, value: MatchmakingStage) -> None: ...
    @property
    def Users(self) -> MatchmakingUserList:
        """
        
        :return: 
        """
    @Users.setter
    def Users(self, value: MatchmakingUserList) -> None: ...
    def AdvanceRound(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def RecordScores(self, scores: Array[SoloScoreInfo], placementPoints: Array[int]) -> None:
        """
        
        :param scores: 
        :param placementPoints: 
        """
    def ToString(self) -> str:
        """"""
class MatchmakingRound(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Accuracy(self) -> float:
        """
        
        :return: 
        """
    @Accuracy.setter
    def Accuracy(self, value: float) -> None: ...
    @property
    def MaxCombo(self) -> int:
        """
        
        :return: 
        """
    @MaxCombo.setter
    def MaxCombo(self, value: int) -> None: ...
    @property
    def Placement(self) -> int:
        """
        
        :return: 
        """
    @Placement.setter
    def Placement(self, value: int) -> None: ...
    @property
    def Round(self) -> int:
        """
        
        :return: 
        """
    @Round.setter
    def Round(self, value: int) -> None: ...
    @property
    def Statistics(self) -> IDictionary[HitResult, int]:
        """
        
        :return: 
        """
    @Statistics.setter
    def Statistics(self, value: IDictionary[HitResult, int]) -> None: ...
    @property
    def TotalScore(self) -> int:
        """
        
        :return: 
        """
    @TotalScore.setter
    def TotalScore(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class MatchmakingRoundList(Object, IEnumerable[MatchmakingRound], IEnumerable):
    """"""
    def __init__(self):
        """"""
    @property
    def Count(self) -> int:
        """
        
        :return: 
        """
    @property
    def RoundsDictionary(self) -> IDictionary[int, MatchmakingRound]:
        """
        
        :return: 
        """
    @RoundsDictionary.setter
    def RoundsDictionary(self, value: IDictionary[int, MatchmakingRound]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[MatchmakingRound]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOrAdd(self, round: int) -> MatchmakingRound:
        """
        
        :param round: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator[MatchmakingRound]:
        """"""
    def __len__(self) -> int:
        """
        
        :return: 
        """
class MatchmakingStage(Enum):
    """"""
    WaitingForClientsJoin: MatchmakingStage = ...
    """"""
    RoundWarmupTime: MatchmakingStage = ...
    """"""
    UserBeatmapSelect: MatchmakingStage = ...
    """"""
    ServerBeatmapFinalised: MatchmakingStage = ...
    """"""
    WaitingForClientsBeatmapDownload: MatchmakingStage = ...
    """"""
    GameplayWarmupTime: MatchmakingStage = ...
    """"""
    Gameplay: MatchmakingStage = ...
    """"""
    ResultsDisplaying: MatchmakingStage = ...
    """"""
    Ended: MatchmakingStage = ...
    """"""
class MatchmakingUser(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def AbandonedAt(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @AbandonedAt.setter
    def AbandonedAt(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def Placement(self) -> Optional[int]:
        """
        
        :return: 
        """
    @Placement.setter
    def Placement(self, value: Optional[int]) -> None: ...
    @property
    def Points(self) -> int:
        """
        
        :return: 
        """
    @Points.setter
    def Points(self, value: int) -> None: ...
    @property
    def Rounds(self) -> MatchmakingRoundList:
        """
        
        :return: 
        """
    @Rounds.setter
    def Rounds(self, value: MatchmakingRoundList) -> None: ...
    @property
    def UserId(self) -> int:
        """
        
        :return: 
        """
    @UserId.setter
    def UserId(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class MatchmakingUserComparer(Comparer[MatchmakingUser], IComparer[MatchmakingUser], IComparer):
    """"""
    def __init__(self, rounds: int):
        """
        
        :param rounds: 
        """
    @overload
    def Compare(self, x: object, y: object) -> int:
        """"""
    @overload
    def Compare(self, x: MatchmakingUser, y: MatchmakingUser) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class MatchmakingUserList(Object, IEnumerable[MatchmakingUser], IEnumerable):
    """"""
    def __init__(self):
        """"""
    @property
    def Count(self) -> int:
        """
        
        :return: 
        """
    @property
    def UserDictionary(self) -> IDictionary[int, MatchmakingUser]:
        """
        
        :return: 
        """
    @UserDictionary.setter
    def UserDictionary(self, value: IDictionary[int, MatchmakingUser]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[MatchmakingUser]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetOrAdd(self, userId: int) -> MatchmakingUser:
        """
        
        :param userId: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator[MatchmakingUser]:
        """"""
    def __len__(self) -> int:
        """
        
        :return: 
        """