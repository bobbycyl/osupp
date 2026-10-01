from Newtonsoft.Json.Linq import JObject
from System import Type
from __future__ import annotations
from osu.Game.Online.Notifications.WebSocket import SocketMessage
class EndChatRequest(SocketMessage):
    """"""
    def __init__(self):
        """"""
    @property
    def Data(self) -> JObject:
        """
        
        :return: 
        """
    @Data.setter
    def Data(self, value: JObject) -> None: ...
    @property
    def Error(self) -> str:
        """
        
        :return: 
        """
    @Error.setter
    def Error(self, value: str) -> None: ...
    @property
    def Event(self) -> str:
        """
        
        :return: 
        """
    @Event.setter
    def Event(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class StartChatRequest(SocketMessage):
    """"""
    def __init__(self):
        """"""
    @property
    def Data(self) -> JObject:
        """
        
        :return: 
        """
    @Data.setter
    def Data(self, value: JObject) -> None: ...
    @property
    def Error(self) -> str:
        """
        
        :return: 
        """
    @Error.setter
    def Error(self, value: str) -> None: ...
    @property
    def Event(self) -> str:
        """
        
        :return: 
        """
    @Event.setter
    def Event(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""