from Realms import DynamicObjectApi
from Realms import EmbeddedObject
from Realms import IEmbeddedObject
from Realms import IRealmAccessor
from Realms import IRealmObject
from Realms import IRealmObjectBase
from Realms import ISettableManagedAccessor
from Realms import Realm
from Realms import RealmObject
from Realms.Schema import ObjectSchema
from Realms.Weaving import IRealmObjectHelper
from System.ComponentModel import INotifyPropertyChanged
from System.ComponentModel import PropertyChangedEventHandler
from System import IEquatable
from System import Int32
from System.Linq import IQueryable
from System.Reflection import IReflectableType
from System.Reflection import TypeInfo
from System import Type
from __future__ import annotations
from osu.Game.Database import IHasOnlineID
from osu.Game.Database import INamedFile
from osu.Game.Database import INamedFileUsage
from osu.Game.IO import IFileInfo
from osu.Game.Users import CountryCode
from osu.Game.Users import IUser
from osu.Game.Utils import IDeepCloneable
from typing import Generic
from typing import TypeVar
from typing import overload
T = TypeVar("T")
class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...
class RealmFile(RealmObject, IRealmObject, IRealmObjectBase, ISettableManagedAccessor, INotifyPropertyChanged, IReflectableType, IFileInfo):
    """"""
    def __init__(self):
        """"""
    @property
    def Accessor(self) -> IRealmAccessor:
        """"""
    @property
    def BacklinksCount(self) -> int:
        """"""
    @property
    def DynamicApi(self) -> DynamicObjectApi:
        """"""
    @property
    def Hash(self) -> str:
        """
        
        :return: 
        """
    @Hash.setter
    def Hash(self, value: str) -> None: ...
    @property
    def IsFrozen(self) -> bool:
        """"""
    @property
    def IsManaged(self) -> bool:
        """"""
    @property
    def IsValid(self) -> bool:
        """"""
    @property
    def ObjectSchema(self) -> ObjectSchema:
        """"""
    @property
    def Realm(self) -> Realm:
        """"""
    @property
    def Usages(self) -> IQueryable[RealmNamedFileUsage]:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self) -> TypeInfo:
        """"""
    def SetManagedAccessor(self, accessor: IRealmAccessor, helper: IRealmObjectHelper = ..., update: bool = ..., skipDefaults: bool = ...) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    PropertyChanged: EventType[PropertyChangedEventHandler] = ...
    """"""
class RealmNamedFileUsage(EmbeddedObject, IEmbeddedObject, IRealmObjectBase, ISettableManagedAccessor, INotifyPropertyChanged, IReflectableType, INamedFile, INamedFileUsage):
    """"""
    def __init__(self, file: RealmFile, filename: str):
        """
        
        :param file: 
        :param filename: 
        """
    @property
    def Accessor(self) -> IRealmAccessor:
        """"""
    @property
    def BacklinksCount(self) -> int:
        """"""
    @property
    def DynamicApi(self) -> DynamicObjectApi:
        """"""
    @property
    def File(self) -> RealmFile:
        """
        
        :return: 
        """
    @File.setter
    def File(self, value: RealmFile) -> None: ...
    @property
    def Filename(self) -> str:
        """
        
        :return: 
        """
    @Filename.setter
    def Filename(self, value: str) -> None: ...
    @property
    def IsFrozen(self) -> bool:
        """"""
    @property
    def IsManaged(self) -> bool:
        """"""
    @property
    def IsValid(self) -> bool:
        """"""
    @property
    def ObjectSchema(self) -> ObjectSchema:
        """"""
    @property
    def Parent(self) -> IRealmObjectBase:
        """"""
    @property
    def Realm(self) -> Realm:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self) -> TypeInfo:
        """"""
    def SetManagedAccessor(self, accessor: IRealmAccessor, helper: IRealmObjectHelper = ..., update: bool = ..., skipDefaults: bool = ...) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    PropertyChanged: EventType[PropertyChangedEventHandler] = ...
    """"""
class RealmUser(EmbeddedObject, IEmbeddedObject, IRealmObjectBase, ISettableManagedAccessor, INotifyPropertyChanged, IReflectableType, IEquatable[RealmUser], IEquatable[IUser], IHasOnlineID[Int32], IUser, IDeepCloneable[RealmUser]):
    """"""
    def __init__(self):
        """"""
    @property
    def Accessor(self) -> IRealmAccessor:
        """"""
    @property
    def BacklinksCount(self) -> int:
        """"""
    @property
    def CountryCode(self) -> CountryCode:
        """
        
        :return: 
        """
    @CountryCode.setter
    def CountryCode(self, value: CountryCode) -> None: ...
    @property
    def CountryString(self) -> str:
        """
        
        :return: 
        """
    @CountryString.setter
    def CountryString(self, value: str) -> None: ...
    @property
    def DynamicApi(self) -> DynamicObjectApi:
        """"""
    @property
    def IsBot(self) -> bool:
        """
        
        :return: 
        """
    @property
    def IsFrozen(self) -> bool:
        """"""
    @property
    def IsManaged(self) -> bool:
        """"""
    @property
    def IsValid(self) -> bool:
        """"""
    @property
    def ObjectSchema(self) -> ObjectSchema:
        """"""
    @property
    def OnlineID(self) -> int:
        """
        
        :return: 
        """
    @OnlineID.setter
    def OnlineID(self, value: int) -> None: ...
    @property
    def Parent(self) -> IRealmObjectBase:
        """"""
    @property
    def Realm(self) -> Realm:
        """"""
    @property
    def Username(self) -> str:
        """
        
        :return: 
        """
    @Username.setter
    def Username(self, value: str) -> None: ...
    def DeepClone(self) -> RealmUser:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: RealmUser) -> bool:
        """"""
    @overload
    def Equals(self, other: IUser) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self) -> TypeInfo:
        """"""
    def SetManagedAccessor(self, accessor: IRealmAccessor, helper: IRealmObjectHelper = ..., update: bool = ..., skipDefaults: bool = ...) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    PropertyChanged: EventType[PropertyChangedEventHandler] = ...
    """"""