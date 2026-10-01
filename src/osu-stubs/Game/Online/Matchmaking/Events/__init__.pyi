from System import Enum
from System import Type
from __future__ import annotations
from osu.Game.Online.Multiplayer import MatchServerEvent
from osu.Game.Online.Multiplayer import MatchUserRequest
class MatchmakingAvatarAction(Enum):
    """"""
    Jump: MatchmakingAvatarAction = ...
    """"""
class MatchmakingAvatarActionEvent(MatchServerEvent):
    """"""
    def __init__(self):
        """"""
    @property
    def Action(self) -> MatchmakingAvatarAction:
        """
        
        :return: 
        """
    @Action.setter
    def Action(self, value: MatchmakingAvatarAction) -> None: ...
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
class MatchmakingAvatarActionRequest(MatchUserRequest):
    """"""
    def __init__(self):
        """"""
    @property
    def Action(self) -> MatchmakingAvatarAction:
        """
        
        :return: 
        """
    @Action.setter
    def Action(self, value: MatchmakingAvatarAction) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""