from System import TimeSpan
from System import Type
from __future__ import annotations
from osu.Game.Online.Multiplayer import MatchServerEvent
from osu.Game.Online.Multiplayer import MatchUserRequest
from osu.Game.Online.Multiplayer import MultiplayerCountdown
from typing import Final
class CountdownStartedEvent(MatchServerEvent):
    """"""
    Countdown: Final[MultiplayerCountdown] = ...
    """
    
    :return: 
    """
    def __init__(self, countdown: MultiplayerCountdown):
        """
        
        :param countdown: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class CountdownStoppedEvent(MatchServerEvent):
    """"""
    ID: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self, id: int):
        """
        
        :param id: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class StartMatchCountdownRequest(MatchUserRequest):
    """"""
    def __init__(self):
        """"""
    @property
    def Duration(self) -> TimeSpan:
        """
        
        :return: 
        """
    @Duration.setter
    def Duration(self, value: TimeSpan) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class StopCountdownRequest(MatchUserRequest):
    """"""
    ID: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self, id: int):
        """
        
        :param id: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""