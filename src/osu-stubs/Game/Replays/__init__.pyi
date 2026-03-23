from System.Collections.Generic import List
from System import Object
from System import Type
from __future__ import annotations
from osu.Game.Rulesets.Replays import ReplayFrame
from osu.Game.Utils import IDeepCloneable
from typing import Final
class Replay(Object, IDeepCloneable[Replay]):
    """"""
    Frames: Final[List[ReplayFrame]] = ...
    """
    
    :return: 
    """
    HasReceivedAllFrames: Final[bool] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    def DeepClone(self) -> Replay:
        """
        
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