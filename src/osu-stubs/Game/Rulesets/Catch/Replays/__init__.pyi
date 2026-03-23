from System.Collections.Generic import List
from System import Func
from System import IDisposable
from System import Type
from __future__ import annotations
from osu.Framework.Bindables import BindableBool
from osu.Framework.Bindables import IHasDescription
from osu.Framework.Input.StateChanges import IInput
from osu.Framework.Input.StateChanges import IInputStateChangeHandler
from osu.Framework.Input.States import InputState
from osu.Framework.Platform import GameHost
from osu.Game.Beatmaps import IBeatmap
from osu.Game.Input.Handlers.ReplayInputHandler import ReplayState
from osu.Game.Online.Spectator import FrameHeader
from osu.Game.Replays.Legacy import LegacyReplayFrame
from osu.Game.Replays import Replay
from osu.Game.Rulesets.Catch.Beatmaps import CatchBeatmap
from osu.Game.Rulesets.Catch import CatchAction
from osu.Game.Rulesets.Replays import AutoGenerator
from osu.Game.Rulesets.Replays import FramedReplayInputHandler
from osu.Game.Rulesets.Replays import ReplayFrame
from osu.Game.Rulesets.Replays.Types import IConvertibleReplayFrame
from osuTK import Vector2
from typing import Final
from typing import Optional
from typing import overload
class CatchAutoGenerator(AutoGenerator[CatchReplayFrame]):
    """"""
    def __init__(self, beatmap: IBeatmap):
        """
        
        :param beatmap: 
        """
    @property
    def Beatmap(self) -> CatchBeatmap:
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
class CatchFramedReplayInputHandler(FramedReplayInputHandler[CatchReplayFrame], IDisposable, IHasDescription):
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
    def CurrentFrame(self) -> CatchReplayFrame:
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
    def EndFrame(self) -> CatchReplayFrame:
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
    def NextFrame(self) -> CatchReplayFrame:
        """
        
        :return: 
        """
    @property
    def StartFrame(self) -> CatchReplayFrame:
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
    class CatchReplayState(ReplayInputHandler.ReplayState[CatchAction], IInput):
        """"""
        PressedActions: Final[List[CatchAction]] = ...
        """"""
        def __init__(self):
            """"""
        @property
        def CatcherX(self) -> Optional[float]:
            """"""
        @CatcherX.setter
        def CatcherX(self, value: Optional[float]) -> None: ...
        def Apply(self, state: InputState, handler: IInputStateChangeHandler) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
class CatchReplayFrame(ReplayFrame, IConvertibleReplayFrame):
    """"""
    Actions: Final[List[CatchAction]] = ...
    """
    
    :return: 
    """
    Dashing: Final[bool] = ...
    """
    
    :return: 
    """
    Header: Final[FrameHeader] = ...
    """
    
    :return: 
    """
    Position: Final[float] = ...
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
    def __init__(self, time: float, position: Optional[float] = ..., dashing: bool = ..., lastFrame: CatchReplayFrame = ...):
        """
        
        :param time: 
        :param position: 
        :param dashing: 
        :param lastFrame: 
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