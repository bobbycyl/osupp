from Newtonsoft.Json import JsonSerializerSettings
from Newtonsoft.Json.Serialization import DefaultContractResolver
from Newtonsoft.Json.Serialization import IContractResolver
from Newtonsoft.Json.Serialization import JsonContract
from Newtonsoft.Json.Serialization import NamingStrategy
from System import Object
from System.Reflection import BindingFlags
from System import Type
from __future__ import annotations
from abc import ABC
from typing import TypeVar
T = TypeVar("T")
class JsonSerializableExtensions(ABC, Object):
    """"""
    @classmethod
    def CreateGlobalSettings(cls) -> JsonSerializerSettings:
        """
        
        :return: 
        """
    @classmethod
    def Deserialize(cls, objString: str) -> T:
        """
        
        :param objString: 
        :return: 
        """
    @classmethod
    def DeserializeInto(cls, objString: str, target: T) -> None:
        """
        
        :param objString: 
        :param target: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Serialize(cls, obj: object) -> str:
        """
        
        :param obj: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class SnakeCaseKeyContractResolver(DefaultContractResolver, IContractResolver):
    """"""
    def __init__(self):
        """"""
    @property
    def DefaultMembersSearchFlags(self) -> BindingFlags:
        """"""
    @DefaultMembersSearchFlags.setter
    def DefaultMembersSearchFlags(self, value: BindingFlags) -> None: ...
    @property
    def DynamicCodeGeneration(self) -> bool:
        """"""
    @property
    def IgnoreIsSpecifiedMembers(self) -> bool:
        """"""
    @IgnoreIsSpecifiedMembers.setter
    def IgnoreIsSpecifiedMembers(self, value: bool) -> None: ...
    @property
    def IgnoreSerializableAttribute(self) -> bool:
        """"""
    @IgnoreSerializableAttribute.setter
    def IgnoreSerializableAttribute(self, value: bool) -> None: ...
    @property
    def IgnoreSerializableInterface(self) -> bool:
        """"""
    @IgnoreSerializableInterface.setter
    def IgnoreSerializableInterface(self, value: bool) -> None: ...
    @property
    def IgnoreShouldSerializeMembers(self) -> bool:
        """"""
    @IgnoreShouldSerializeMembers.setter
    def IgnoreShouldSerializeMembers(self, value: bool) -> None: ...
    @property
    def NamingStrategy(self) -> NamingStrategy:
        """"""
    @NamingStrategy.setter
    def NamingStrategy(self, value: NamingStrategy) -> None: ...
    @property
    def SerializeCompilerGeneratedMembers(self) -> bool:
        """"""
    @SerializeCompilerGeneratedMembers.setter
    def SerializeCompilerGeneratedMembers(self, value: bool) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetResolvedPropertyName(self, propertyName: str) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResolveContract(self, type: Type) -> JsonContract:
        """"""
    def ToString(self) -> str:
        """"""