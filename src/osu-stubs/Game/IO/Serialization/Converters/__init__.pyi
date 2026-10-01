from Newtonsoft.Json.Converters import StringEnumConverter
from Newtonsoft.Json import JsonConverter
from Newtonsoft.Json import JsonReader
from Newtonsoft.Json import JsonSerializer
from Newtonsoft.Json import JsonWriter
from Newtonsoft.Json.Serialization import NamingStrategy
from System.Collections.Generic import IReadOnlyList
from System import Type
from __future__ import annotations
from typing import Generic
from typing import TypeVar
from typing import overload
T = TypeVar("T")
class SnakeCaseStringEnumConverter(StringEnumConverter):
    """"""
    def __init__(self):
        """"""
    @property
    def AllowIntegerValues(self) -> bool:
        """"""
    @AllowIntegerValues.setter
    def AllowIntegerValues(self, value: bool) -> None: ...
    @property
    def CamelCaseText(self) -> bool:
        """"""
    @CamelCaseText.setter
    def CamelCaseText(self, value: bool) -> None: ...
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def NamingStrategy(self) -> NamingStrategy:
        """"""
    @NamingStrategy.setter
    def NamingStrategy(self, value: NamingStrategy) -> None: ...
    def CanConvert(self, objectType: Type) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ReadJson(self, reader: JsonReader, objectType: Type, existingValue: object, serializer: JsonSerializer) -> object:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteJson(self, writer: JsonWriter, value: object, serializer: JsonSerializer) -> None:
        """"""
class TypedListConverter(Generic[T], JsonConverter[IReadOnlyList[T]]):
    """"""
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, requiresTypeVersion: bool):
        """
        
        :param requiresTypeVersion: 
        """
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    def CanConvert(self, objectType: Type) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def ReadJson(self, reader: JsonReader, objectType: Type, existingValue: object, serializer: JsonSerializer) -> object:
        """"""
    @overload
    def ReadJson(self, reader: JsonReader, objectType: Type, existingValue: IReadOnlyList[T], hasExistingValue: bool, serializer: JsonSerializer) -> IReadOnlyList[T]:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def WriteJson(self, writer: JsonWriter, value: IReadOnlyList[T], serializer: JsonSerializer) -> None:
        """"""
    @overload
    def WriteJson(self, writer: JsonWriter, value: object, serializer: JsonSerializer) -> None:
        """"""