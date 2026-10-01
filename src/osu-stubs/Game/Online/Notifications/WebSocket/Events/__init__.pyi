from Newtonsoft.Json.Linq import JObject
from System.Collections.Generic import List
from System import DateTimeOffset
from System import Object
from System import Type
from __future__ import annotations
from osu.Game.Online.Chat import Message
class NewChatMessageData(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Messages(self) -> List[Message]:
        """
        
        :return: 
        """
    @Messages.setter
    def Messages(self, value: List[Message]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class NewPrivateNotificationEvent(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def CreatedAt(self) -> DateTimeOffset:
        """
        
        :return: 
        """
    @CreatedAt.setter
    def CreatedAt(self, value: DateTimeOffset) -> None: ...
    @property
    def Details(self) -> JObject:
        """
        
        :return: 
        """
    @Details.setter
    def Details(self, value: JObject) -> None: ...
    @property
    def ID(self) -> int:
        """
        
        :return: 
        """
    @ID.setter
    def ID(self, value: int) -> None: ...
    @property
    def IsRead(self) -> bool:
        """
        
        :return: 
        """
    @IsRead.setter
    def IsRead(self, value: bool) -> None: ...
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def ObjectId(self) -> int:
        """
        
        :return: 
        """
    @ObjectId.setter
    def ObjectId(self, value: int) -> None: ...
    @property
    def ObjectType(self) -> str:
        """
        
        :return: 
        """
    @ObjectType.setter
    def ObjectType(self, value: str) -> None: ...
    @property
    def SourceUserID(self) -> int:
        """
        
        :return: 
        """
    @SourceUserID.setter
    def SourceUserID(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class UserAchievementUnlock(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def AchievementId(self) -> int:
        """
        
        :return: 
        """
    @AchievementId.setter
    def AchievementId(self, value: int) -> None: ...
    @property
    def AchievementMode(self) -> str:
        """
        
        :return: 
        """
    @AchievementMode.setter
    def AchievementMode(self, value: str) -> None: ...
    @property
    def CoverUrl(self) -> str:
        """
        
        :return: 
        """
    @CoverUrl.setter
    def CoverUrl(self, value: str) -> None: ...
    @property
    def Description(self) -> str:
        """
        
        :return: 
        """
    @Description.setter
    def Description(self, value: str) -> None: ...
    @property
    def Slug(self) -> str:
        """
        
        :return: 
        """
    @Slug.setter
    def Slug(self, value: str) -> None: ...
    @property
    def Title(self) -> str:
        """
        
        :return: 
        """
    @Title.setter
    def Title(self, value: str) -> None: ...
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