from System import Array
from System.Collections.Generic import List
from System import Func
from System import IDisposable
from System import Type
from __future__ import annotations
from osu.Framework.Bindables import BindableBool
from osu.Framework.Bindables import IHasDescription
from osu.Framework.Input.StateChanges import IInput
from osu.Framework.Platform import GameHost
from osu.Game.Beatmaps import IBeatmap
from osu.Game.Online.Spectator import FrameHeader
from osu.Game.Replays.Legacy import LegacyReplayFrame
from osu.Game.Replays import Replay
from osu.Game.Rulesets.Replays import AutoGenerator
from osu.Game.Rulesets.Replays import FramedReplayInputHandler
from osu.Game.Rulesets.Replays import ReplayFrame
from osu.Game.Rulesets.Replays.Types import IConvertibleReplayFrame
from osu.Game.Rulesets.Taiko.Beatmaps import TaikoBeatmap
from osu.Game.Rulesets.Taiko import TaikoAction
from osuTK import Vector2
from typing import Final
from typing import Optional
from typing import overload
class TaikoAutoGenerator(AutoGenerator[TaikoReplayFrame]):
    """"""
    def __init__(self, beatmap: IBeatmap):
        """
        
        :param beatmap: 
        """
    @property
    def Beatmap(self) -> TaikoBeatmap:
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
class TaikoFramedReplayInputHandler(FramedReplayInputHandler[TaikoReplayFrame], IDisposable, IHasDescription):
    """"""
    FrameAccuratePlayback: Final[bool] = ...
    """
    
    :return: 
    """
    def __init__(self, replay: Replay):
        """
        
        :param replay: 
        """
    @property
    def CurrentFrame(self) -> TaikoReplayFrame:
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
    def EndFrame(self) -> TaikoReplayFrame:
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
    def NextFrame(self) -> TaikoReplayFrame:
        """
        
        :return: 
        """
    @property
    def StartFrame(self) -> TaikoReplayFrame:
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
class TaikoReplayFrame(ReplayFrame, IConvertibleReplayFrame):
    """"""
    Actions: Final[List[TaikoAction]] = ...
    """
    
    :return: 
    """
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
    def __init__(self, time: float, actions: Array[TaikoAction]):
        """
        
        :param time: 
        :param actions: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def FromLegacy(self, currentFrame: LegacyReplayFrame, beatmap: IBeatmap, lastFrame: ReplayFrame = ...) -> None:
        """
        
        :param currentFrame: 
        :param beatmap: 
        :param lastFrame: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsEquivalentTo(self, other: ReplayFrame) -> bool:
        """
        
        :param other: 
        :return: 
        """
    def ToLegacy(self, beatmap: IBeatmap) -> LegacyReplayFrame:
        """
        
        :param beatmap: 
        :return: 
        """
    def ToString(self) -> str:
        """"""