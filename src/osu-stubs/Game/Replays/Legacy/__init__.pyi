from System import Enum
from System import Type
from __future__ import annotations
from osu.Game.Online.Spectator import FrameHeader
from osu.Game.Rulesets.Replays import ReplayFrame
from osuTK import Vector2
from typing import Final
from typing import Optional
class LegacyReplayFrame(ReplayFrame):
    """"""
    ButtonState: Final[ReplayButtonState] = ...
    """
    
    :return: 
    """
    Header: Final[FrameHeader] = ...
    """
    
    :return: 
    """
    MouseX: Final[Optional[float]] = ...
    """
    
    :return: 
    """
    MouseY: Final[Optional[float]] = ...
    """
    
    :return: 
    """
    Time: Final[float] = ...
    """
    
    :return: 
    """
    def __init__(self, time: float, mouseX: Optional[float], mouseY: Optional[float], buttonState: ReplayButtonState):
        """
        
        :param time: 
        :param mouseX: 
        :param mouseY: 
        :param buttonState: 
        """
    @property
    def MouseLeft(self) -> bool:
        """
        
        :return: 
        """
    @property
    def MouseLeft1(self) -> bool:
        """
        
        :return: 
        """
    @property
    def MouseLeft2(self) -> bool:
        """
        
        :return: 
        """
    @property
    def MouseRight(self) -> bool:
        """
        
        :return: 
        """
    @property
    def MouseRight1(self) -> bool:
        """
        
        :return: 
        """
    @property
    def MouseRight2(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Position(self) -> Vector2:
        """
        
        :return: 
        """
    @property
    def Smoke(self) -> bool:
        """
        
        :return: 
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
class ReplayButtonState(Enum):
    """"""
    _None: ReplayButtonState = ...
    """"""
    Left1: ReplayButtonState = ...
    """"""
    Right1: ReplayButtonState = ...
    """"""
    Left2: ReplayButtonState = ...
    """"""
    Right2: ReplayButtonState = ...
    """"""
    Smoke: ReplayButtonState = ...
    """"""