from Newtonsoft.Json.Linq import JObject
from System import Action
from System import Exception
from System import Func
from System import IAsyncDisposable
from System import IDisposable
from System.Net.WebSockets import ClientWebSocket
from System import Object
from System.Threading import CancellationToken
from System.Threading.Tasks import Task
from System.Threading.Tasks import ValueTask
from System import Type
from __future__ import annotations
from osu.Framework.Bindables import IBindable
from osu.Game.Online.API import IAPIProvider
from osu.Game.Online import PersistentEndpointClient
from osu.Game.Online import PersistentEndpointClientConnector
from typing import Final
from typing import Generic
from typing import Optional
from typing import TypeVar
T = TypeVar("T")
class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...
class DummyNotificationsClient(Object, INotificationsClient):
    """"""
    HandleMessage: Final[Func[SocketMessage, bool]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def IsConnected(self) -> IBindable[bool]:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Receive(self, message: SocketMessage) -> None:
        """
        
        :param message: 
        """
    def SendAsync(self, message: SocketMessage, cancellationToken: Optional[CancellationToken] = ...) -> Task:
        """
        
        :param message: 
        :param cancellationToken: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    MessageReceived: EventType[Action[SocketMessage]] = ...
    """"""
class INotificationsClient:
    """"""
    @property
    def IsConnected(self) -> IBindable[bool]:
        """
        
        :return: 
        """
    def SendAsync(self, message: SocketMessage, cancellationToken: Optional[CancellationToken] = ...) -> Task:
        """
        
        :param message: 
        :param cancellationToken: 
        :return: 
        """
    MessageReceived: EventType[Action[SocketMessage]] = ...
    """"""
class SocketMessage(Object):
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
class WebSocketNotificationsClient(PersistentEndpointClient, IAsyncDisposable):
    """"""
    def __init__(self, socket: ClientWebSocket, endpoint: str):
        """
        
        :param socket: 
        :param endpoint: 
        """
    def ConnectAsync(self, cancellationToken: CancellationToken) -> Task:
        """
        
        :param cancellationToken: 
        :return: 
        """
    def DisposeAsync(self) -> ValueTask:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SendAsync(self, message: SocketMessage, cancellationToken: Optional[CancellationToken] = ...) -> Task:
        """
        
        :param message: 
        :param cancellationToken: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    Closed: EventType[Func[Exception, Task]] = ...
    """"""
    MessageReceived: EventType[Action[SocketMessage]] = ...
    """"""
class WebSocketNotificationsClientConnector(PersistentEndpointClientConnector, IDisposable, INotificationsClient):
    """"""
    def __init__(self, api: IAPIProvider):
        """
        
        :param api: 
        """
    @property
    def CurrentConnection(self) -> PersistentEndpointClient:
        """
        
        :return: 
        """
    @property
    def IsConnected(self) -> IBindable[bool]:
        """
        
        :return: 
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Reconnect(self) -> Task:
        """
        
        :return: 
        """
    def SendAsync(self, message: SocketMessage, cancellationToken: Optional[CancellationToken] = ...) -> Task:
        """
        
        :param message: 
        :param cancellationToken: 
        :return: 
        """
    def Start(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    MessageReceived: EventType[Action[SocketMessage]] = ...
    """"""