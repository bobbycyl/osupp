from System import Guid
from System import Object
from System import Type
from __future__ import annotations
class MatchmakingAcceptDuelRequest(Object):
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
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class MatchmakingIssueDuelRequest(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def PoolId(self) -> int:
        """
        
        :return: 
        """
    @PoolId.setter
    def PoolId(self, value: int) -> None: ...
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
class MatchmakingJoinLobbyRequest(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def PoolId(self) -> int:
        """
        
        :return: 
        """
    @PoolId.setter
    def PoolId(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""