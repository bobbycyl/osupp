from System import Array
from System import Enum
from System import Guid
from System import IEquatable
from System import Object
from System.Threading.Tasks import Task
from System import TimeSpan
from System import Type
from System import ValueTuple
from __future__ import annotations
from abc import ABC
from osu.Game.Online import IStatefulUserHubClient
from osu.Game.Online.Matchmaking.Requests import MatchmakingAcceptDuelRequest
from osu.Game.Online.Matchmaking.Requests import MatchmakingIssueDuelRequest
from osu.Game.Online.Matchmaking.Requests import MatchmakingJoinLobbyRequest
from osu.Game.Online.Matchmaking.Responses import MatchmakingAcceptDuelResponse
from osu.Game.Online.Matchmaking.Responses import MatchmakingIssueDuelResponse
from osu.Game.Online.Matchmaking.Responses import MatchmakingJoinLobbyResponse
from osu.Game.Online.Multiplayer import MatchRoomState
from osu.Game.Online.Multiplayer.MatchTypes.Matchmaking import MatchmakingStage
from osu.Game.Online.Multiplayer import MultiplayerCountdown
from typing import Optional
from typing import overload
class IMatchmakingClient(IStatefulUserHubClient):
    """"""
    def DisconnectRequested(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingDuelIssued(self, issue: MatchmakingDuelIssuedParams) -> Task:
        """
        
        :param issue: 
        :return: 
        """
    def MatchmakingItemDeselected(self, userId: int, playlistItemId: int) -> Task:
        """
        
        :param userId: 
        :param playlistItemId: 
        :return: 
        """
    def MatchmakingItemSelected(self, userId: int, playlistItemId: int) -> Task:
        """
        
        :param userId: 
        :param playlistItemId: 
        :return: 
        """
    def MatchmakingLobbyStatusChanged(self, status: MatchmakingLobbyStatus) -> Task:
        """
        
        :param status: 
        :return: 
        """
    def MatchmakingQueueJoined(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingQueueLeft(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingQueueStatusChanged(self, status: MatchmakingQueueStatus) -> Task:
        """
        
        :param status: 
        :return: 
        """
    def MatchmakingRoomInvited(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingRoomInvitedWithParams(self, invitation: MatchmakingRoomInvitationParams) -> Task:
        """
        
        :param invitation: 
        :return: 
        """
    def MatchmakingRoomReady(self, roomId: int, password: str) -> Task:
        """
        
        :param roomId: 
        :param password: 
        :return: 
        """
    def ServerShuttingDown(self) -> Task:
        """
        
        :return: 
        """
class IMatchmakingServer:
    """"""
    def GetMatchmakingPoolsOfType(self, type: MatchmakingPoolType) -> Task[Array[MatchmakingPool]]:
        """
        
        :param type: 
        :return: 
        """
    def MatchmakingAcceptDuel(self, request: MatchmakingAcceptDuelRequest) -> Task[MatchmakingAcceptDuelResponse]:
        """
        
        :param request: 
        :return: 
        """
    def MatchmakingAcceptInvitation(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingDeclineInvitation(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingIssueDuel(self, request: MatchmakingIssueDuelRequest) -> Task[MatchmakingIssueDuelResponse]:
        """
        
        :param request: 
        :return: 
        """
    def MatchmakingJoinLobbyWithParams(self, request: MatchmakingJoinLobbyRequest) -> Task[MatchmakingJoinLobbyResponse]:
        """
        
        :param request: 
        :return: 
        """
    def MatchmakingJoinQueue(self, poolId: int) -> Task:
        """
        
        :param poolId: 
        :return: 
        """
    def MatchmakingLeaveLobby(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingLeaveQueue(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingSkipToNextStage(self) -> Task:
        """
        
        :return: 
        """
    def MatchmakingToggleSelection(self, playlistItemId: int) -> Task:
        """
        
        :param playlistItemId: 
        :return: 
        """
class MatchmakingDuelIssuedParams(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Id(self) -> Guid:
        """
        
        :return: 
        """
    @Id.setter
    def Id(self, value: Guid) -> None: ...
    @property
    def Pool(self) -> MatchmakingPool:
        """
        
        :return: 
        """
    @Pool.setter
    def Pool(self, value: MatchmakingPool) -> None: ...
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
class MatchmakingLobbyStatus(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def RatingDistribution(self) -> Array[ValueTuple, int]:
        """
        
        :return: 
        """
    @RatingDistribution.setter
    def RatingDistribution(self, value: Array[ValueTuple, int]) -> None: ...
    @property
    def RecentMatches(self) -> Array[MatchRoomState]:
        """
        
        :return: 
        """
    @RecentMatches.setter
    def RecentMatches(self, value: Array[MatchRoomState]) -> None: ...
    @property
    def UserRating(self) -> Optional[int]:
        """
        
        :return: 
        """
    @UserRating.setter
    def UserRating(self, value: Optional[int]) -> None: ...
    @property
    def UsersInQueue(self) -> Array[int]:
        """
        
        :return: 
        """
    @UsersInQueue.setter
    def UsersInQueue(self, value: Array[int]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class MatchmakingPool(Object, IEquatable[MatchmakingPool]):
    """"""
    def __init__(self):
        """"""
    @property
    def DisplayName(self) -> str:
        """
        
        :return: 
        """
    @property
    def Id(self) -> int:
        """
        
        :return: 
        """
    @Id.setter
    def Id(self, value: int) -> None: ...
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def RulesetId(self) -> int:
        """
        
        :return: 
        """
    @RulesetId.setter
    def RulesetId(self, value: int) -> None: ...
    @property
    def Type(self) -> MatchmakingPoolType:
        """
        
        :return: 
        """
    @Type.setter
    def Type(self, value: MatchmakingPoolType) -> None: ...
    @property
    def Variant(self) -> int:
        """
        
        :return: 
        """
    @Variant.setter
    def Variant(self, value: int) -> None: ...
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: MatchmakingPool) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class MatchmakingPoolType(Enum):
    """"""
    QuickPlay: MatchmakingPoolType = ...
    """"""
    RankedPlay: MatchmakingPoolType = ...
    """"""
class MatchmakingQueueStatus(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    class JoiningMatch(MatchmakingQueueStatus):
        """"""
        def __init__(self):
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
    class MatchFound(MatchmakingQueueStatus):
        """"""
        def __init__(self):
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
    class Searching(MatchmakingQueueStatus):
        """"""
        def __init__(self):
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
class MatchmakingRoomInvitationParams(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Type(self) -> MatchmakingPoolType:
        """
        
        :return: 
        """
    @Type.setter
    def Type(self, value: MatchmakingPoolType) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class MatchmakingStageCountdown(MultiplayerCountdown):
    """"""
    def __init__(self):
        """"""
    @property
    def ID(self) -> int:
        """
        
        :return: 
        """
    @ID.setter
    def ID(self, value: int) -> None: ...
    @property
    def IsExclusive(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Stage(self) -> MatchmakingStage:
        """
        
        :return: 
        """
    @Stage.setter
    def Stage(self, value: MatchmakingStage) -> None: ...
    @property
    def TimeRemaining(self) -> TimeSpan:
        """
        
        :return: 
        """
    @TimeRemaining.setter
    def TimeRemaining(self, value: TimeSpan) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""