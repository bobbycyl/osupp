from System import Exception
from System import Type
from __future__ import annotations
from osu.Game.Beatmaps import BeatmapInfo
from osu.Game.Online.API import APIFailureHandler
from osu.Game.Online.API import APIRequest
from osu.Game.Online.API import APIRequestCompletionState
from osu.Game.Online.API import APISuccessHandler
from osu.Game.Online.API import IAPIProvider
from osu.Game.Online.API.Requests.Responses import SoloScoreInfo
from osu.Game.Online.Rooms import APIScoreToken
from osu.Game.Online.Rooms import MultiplayerScore
from osu.Game.Online.Rooms import SubmitScoreRequest
from osu.Game.Scoring import ScoreInfo
from typing import Final
from typing import Generic
from typing import TypeVar
T = TypeVar("T")
class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...
class CreateSoloScoreRequest(APIRequest[APIScoreToken]):
    """"""
    def __init__(self, beatmapInfo: BeatmapInfo, rulesetId: int, versionHash: str):
        """
        
        :param beatmapInfo: 
        :param rulesetId: 
        :param versionHash: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> APIScoreToken:
        """
        
        :return: 
        """
    def AttachAPI(self, apiAccess: IAPIProvider) -> None:
        """
        
        :param apiAccess: 
        """
    def Cancel(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Fail(self, e: Exception) -> None:
        """
        
        :param e: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Perform(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    Failure: EventType[APIFailureHandler] = ...
    """"""
    Success: EventType[APISuccessHandler[APIScoreToken]] = ...
    """"""
class SubmitSoloScoreRequest(SubmitScoreRequest):
    """"""
    Score: Final[SoloScoreInfo] = ...
    """
    
    :return: 
    """
    def __init__(self, scoreInfo: ScoreInfo, scoreId: int, beatmapId: int):
        """
        
        :param scoreInfo: 
        :param scoreId: 
        :param beatmapId: 
        """
    @property
    def CompletionState(self) -> APIRequestCompletionState:
        """
        
        :return: 
        """
    @property
    def Response(self) -> MultiplayerScore:
        """
        
        :return: 
        """
    def AttachAPI(self, apiAccess: IAPIProvider) -> None:
        """
        
        :param apiAccess: 
        """
    def Cancel(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Fail(self, e: Exception) -> None:
        """
        
        :param e: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Perform(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    Failure: EventType[APIFailureHandler] = ...
    """"""
    Success: EventType[APISuccessHandler[MultiplayerScore]] = ...
    """"""