from System.Collections.Generic import List
from System import Func
from System import IDisposable
from System import Object
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Framework.Bindables import BindableBool
from osu.Framework.Bindables import IHasDescription
from osu.Framework.Input.StateChanges import IInput
from osu.Framework.Platform import GameHost
from osu.Game.Input.Handlers import ReplayInputHandler
from osu.Game.Online.Spectator import FrameHeader
from osu.Game.Replays import Replay
from osuTK import Vector2
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Optional
from typing import TypeVar
from typing import overload
TFrame = TypeVar("TFrame")
class AutoGenerator(ABC, Object):
    """"""
    KEY_UP_DELAY: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    def Equals(self, obj: object) -> bool:
        """"""
    def Generate(self) -> Replay:
        """
        
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class AutoGenerator(ABC, Generic[TFrame], AutoGenerator):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Generate(self) -> Replay:
        """
        
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class FramedReplayInputHandler(ABC, Generic[TFrame], ReplayInputHandler, IDisposable, IHasDescription):
    """"""
    FrameAccuratePlayback: Final[bool] = ...
    """
    
    :return: 
    """
    @property
    def CurrentFrame(self) -> TFrame:
        """
        
        :return: 
        """
    @property
    def Description(self) -> str:
        """"""
    @property
    def Enabled(self) -> BindableBool:
        """"""
    @property
    def EndFrame(self) -> TFrame:
        """
        
        :return: 
        """
    @property
    def GamefieldToScreenSpace(self) -> Func[Vector2, Vector2]:
        """
        
        :return: 
        """
    @GamefieldToScreenSpace.setter
    def GamefieldToScreenSpace(self, value: Func[Vector2, Vector2]) -> None: ...
    @property
    def HasFrames(self) -> bool:
        """
        
        :return: 
        """
    @property
    def IsActive(self) -> bool:
        """"""
    @property
    def NextFrame(self) -> TFrame:
        """
        
        :return: 
        """
    @property
    def StartFrame(self) -> TFrame:
        """
        
        :return: 
        """
    @property
    def WaitingForFrame(self) -> bool:
        """
        
        :return: 
        """
    def CollectPendingInputs(self, inputs: List[IInput]) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self, host: GameHost) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def SetFrameFromTime(self, time: float) -> Optional[float]:
        """
        
        :param time: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class ReplayFrame(Object):
    """"""
    Header: Final[FrameHeader] = ...
    """
    
    :return: 
    """
    Time: Final[float] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, time: float):
        """
        
        :param time: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsEquivalentTo(self, other: ReplayFrame) -> bool:
        """
        
        :param other: 
        :return: 
        """
    def ToString(self) -> str:
        """"""