from System import Array
from System.Collections.Generic import Dictionary
from System import Guid
from System import IEquatable
from System.Threading.Tasks import Task
from System import TimeSpan
from System import Type
from System import ValueType
from __future__ import annotations
from osu.Game.Online.Multiplayer import MatchServerEvent
from osu.Game.Online.Multiplayer.MatchTypes.RankedPlay import RankedPlayCardItem
from osu.Game.Online.Multiplayer.MatchTypes.RankedPlay import RankedPlayStage
from osu.Game.Online.Multiplayer import MatchUserRequest
from osu.Game.Online.Multiplayer import MultiplayerCountdown
from osu.Game.Online.Rooms import MultiplayerPlaylistItem
from osuTK import Vector2
from typing import overload
class IRankedPlayClient:
    """"""
    def RankedPlayCardAdded(self, userId: int, card: RankedPlayCardItem) -> Task:
        """
        
        :param userId: 
        :param card: 
        :return: 
        """
    def RankedPlayCardPlayed(self, card: RankedPlayCardItem) -> Task:
        """
        
        :param card: 
        :return: 
        """
    def RankedPlayCardRemoved(self, userId: int, card: RankedPlayCardItem) -> Task:
        """
        
        :param userId: 
        :param card: 
        :return: 
        """
    def RankedPlayCardRevealed(self, card: RankedPlayCardItem, item: MultiplayerPlaylistItem) -> Task:
        """
        
        :param card: 
        :param item: 
        :return: 
        """
class IRankedPlayServer:
    """"""
    def DiscardCards(self, cards: Array[RankedPlayCardItem]) -> Task:
        """
        
        :param cards: 
        :return: 
        """
    def PlayCard(self, card: RankedPlayCardItem) -> Task:
        """
        
        :param card: 
        :return: 
        """
class RankedPlayCardHandReplayEvent(MatchServerEvent):
    """"""
    def __init__(self):
        """"""
    @property
    def Frames(self) -> Array[RankedPlayCardHandReplayFrame]:
        """
        
        :return: 
        """
    @Frames.setter
    def Frames(self, value: Array[RankedPlayCardHandReplayFrame]) -> None: ...
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
class RankedPlayCardHandReplayFrame(ValueType, IEquatable[RankedPlayCardHandReplayFrame]):
    """"""
    @property
    def Cards(self) -> Dictionary[Guid, RankedPlayCardState]:
        """
        
        :return: 
        """
    @Cards.setter
    def Cards(self, value: Dictionary[Guid, RankedPlayCardState]) -> None: ...
    @property
    def Delay(self) -> float:
        """
        
        :return: 
        """
    @Delay.setter
    def Delay(self, value: float) -> None: ...
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: RankedPlayCardHandReplayFrame) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def RelativeTo(self, other: RankedPlayCardHandReplayFrame) -> RankedPlayCardHandReplayFrame:
        """
        
        :param other: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    def __eq__(self, other: RankedPlayCardHandReplayFrame) -> bool:
        """
        
        :param other: 
        :return: 
        """
    def __ne__(self, other: RankedPlayCardHandReplayFrame) -> bool:
        """
        
        :param other: 
        :return: 
        """
    @classmethod
    def op_Equality(cls, left: RankedPlayCardHandReplayFrame, right: RankedPlayCardHandReplayFrame) -> bool:
        """
        
        :param left: 
        :param right: 
        :return: 
        """
    @classmethod
    def op_Inequality(cls, left: RankedPlayCardHandReplayFrame, right: RankedPlayCardHandReplayFrame) -> bool:
        """
        
        :param left: 
        :param right: 
        :return: 
        """
class RankedPlayCardHandReplayRequest(MatchUserRequest):
    """"""
    def __init__(self):
        """"""
    @property
    def Frames(self) -> Array[RankedPlayCardHandReplayFrame]:
        """
        
        :return: 
        """
    @Frames.setter
    def Frames(self, value: Array[RankedPlayCardHandReplayFrame]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class RankedPlayCardState(ValueType, IEquatable[RankedPlayCardState]):
    """"""
    @property
    def DragPosition(self) -> Vector2:
        """
        
        :return: 
        """
    @DragPosition.setter
    def DragPosition(self, value: Vector2) -> None: ...
    @property
    def DragX(self) -> float:
        """
        
        :return: 
        """
    @DragX.setter
    def DragX(self, value: float) -> None: ...
    @property
    def DragY(self) -> float:
        """
        
        :return: 
        """
    @DragY.setter
    def DragY(self, value: float) -> None: ...
    @property
    def Dragged(self) -> bool:
        """
        
        :return: 
        """
    @Dragged.setter
    def Dragged(self, value: bool) -> None: ...
    @property
    def Hovered(self) -> bool:
        """
        
        :return: 
        """
    @Hovered.setter
    def Hovered(self, value: bool) -> None: ...
    @property
    def Order(self) -> int:
        """
        
        :return: 
        """
    @Order.setter
    def Order(self, value: int) -> None: ...
    @property
    def Pressed(self) -> bool:
        """
        
        :return: 
        """
    @Pressed.setter
    def Pressed(self, value: bool) -> None: ...
    @property
    def Selected(self) -> bool:
        """
        
        :return: 
        """
    @Selected.setter
    def Selected(self, value: bool) -> None: ...
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: RankedPlayCardState) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __eq__(self, other: RankedPlayCardState) -> bool:
        """
        
        :param other: 
        :return: 
        """
    def __ne__(self, other: RankedPlayCardState) -> bool:
        """
        
        :param other: 
        :return: 
        """
    @classmethod
    def op_Equality(cls, left: RankedPlayCardState, right: RankedPlayCardState) -> bool:
        """
        
        :param left: 
        :param right: 
        :return: 
        """
    @classmethod
    def op_Inequality(cls, left: RankedPlayCardState, right: RankedPlayCardState) -> bool:
        """
        
        :param left: 
        :param right: 
        :return: 
        """
class RankedPlayStageCountdown(MultiplayerCountdown):
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
    def IsExclusive(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Stage(self) -> RankedPlayStage:
        """
        
        :return: 
        """
    @Stage.setter
    def Stage(self, value: RankedPlayStage) -> None: ...
    @property
    def TimeRemaining(self) -> TimeSpan:
        """
        
        :return: 
        """
    @TimeRemaining.setter
    def TimeRemaining(self, value: TimeSpan) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""