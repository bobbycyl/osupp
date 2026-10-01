from System.Collections.Generic import List
from System import Object
from System import Type
from __future__ import annotations
from osu.Game.Online.Multiplayer import MatchUserRequest
from osu.Game.Online.Multiplayer import MatchUserState
from osu.Game.Online.Multiplayer import StandardMatchRoomState
from typing import Optional
class ChangeTeamRequest(MatchUserRequest):
    """"""
    def __init__(self):
        """"""
    @property
    def TeamID(self) -> int:
        """
        
        :return: 
        """
    @TeamID.setter
    def TeamID(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class MultiplayerTeam(Object):
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
    def Name(self) -> str:
        """
        
        :return: 
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class TeamVersusRoomState(StandardMatchRoomState):
    """"""
    def __init__(self):
        """"""
    @property
    def Locked(self) -> bool:
        """
        
        :return: 
        """
    @Locked.setter
    def Locked(self, value: bool) -> None: ...
    @property
    def Slots(self) -> Optional[int]:
        """
        
        :return: 
        """
    @Slots.setter
    def Slots(self, value: Optional[int]) -> None: ...
    @property
    def Teams(self) -> List[MultiplayerTeam]:
        """
        
        :return: 
        """
    @Teams.setter
    def Teams(self, value: List[MultiplayerTeam]) -> None: ...
    @classmethod
    def CreateDefault(cls, maxParticipants: Optional[int] = ...) -> TeamVersusRoomState:
        """
        
        :param maxParticipants: 
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
class TeamVersusUserState(MatchUserState):
    """"""
    def __init__(self):
        """"""
    @property
    def TeamID(self) -> int:
        """
        
        :return: 
        """
    @TeamID.setter
    def TeamID(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""