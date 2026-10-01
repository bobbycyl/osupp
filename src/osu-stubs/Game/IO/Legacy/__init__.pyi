from System import Array
from System import Char
from System.Collections.Generic import IDictionary
from System.Collections.Generic import IList
from System.Collections.Generic import List
from System import DateTime
from System import Decimal
from System import Enum
from System import Half
from System import IAsyncDisposable
from System import IDisposable
from System.IO import BinaryReader
from System.IO import BinaryWriter
from System.IO import SeekOrigin
from System.IO import Stream
from System import ReadOnlySpan
from System import Span
from System.Threading.Tasks import ValueTask
from System import Type
from __future__ import annotations
from typing import TypeVar
from typing import overload
T = TypeVar("T")
TKey = TypeVar("TKey")
TValue = TypeVar("TValue")
class ILegacySerializable:
    """"""
    def ReadFromStream(self, sr: SerializationReader) -> None:
        """
        
        :param sr: 
        """
    def WriteToStream(self, sw: SerializationWriter) -> None:
        """
        
        :param sw: 
        """
class ObjType(Enum):
    """"""
    NullType: ObjType = ...
    """"""
    BoolType: ObjType = ...
    """"""
    ByteType: ObjType = ...
    """"""
    UInt16Type: ObjType = ...
    """"""
    UInt32Type: ObjType = ...
    """"""
    UInt64Type: ObjType = ...
    """"""
    SByteType: ObjType = ...
    """"""
    Int16Type: ObjType = ...
    """"""
    Int32Type: ObjType = ...
    """"""
    Int64Type: ObjType = ...
    """"""
    CharType: ObjType = ...
    """"""
    StringType: ObjType = ...
    """"""
    SingleType: ObjType = ...
    """"""
    DoubleType: ObjType = ...
    """"""
    DecimalType: ObjType = ...
    """"""
    DateTimeType: ObjType = ...
    """"""
    ByteArrayType: ObjType = ...
    """"""
    CharArrayType: ObjType = ...
    """"""
    OtherType: ObjType = ...
    """"""
    LegacySerializableType: ObjType = ...
    """"""
class SerializationReader(BinaryReader, IDisposable):
    """"""
    def __init__(self, s: Stream):
        """
        
        :param s: 
        """
    @property
    def BaseStream(self) -> Stream:
        """"""
    @property
    def RemainingBytes(self) -> int:
        """
        
        :return: 
        """
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PeekChar(self) -> int:
        """"""
    @overload
    def Read(self) -> int:
        """"""
    @overload
    def Read(self, buffer: Span[int]) -> int:
        """"""
    @overload
    def Read(self, buffer: Span[Char]) -> int:
        """"""
    @overload
    def Read(self, buffer: Array[int], index: int, count: int) -> int:
        """"""
    @overload
    def Read(self, buffer: Array[Char], index: int, count: int) -> int:
        """"""
    def Read7BitEncodedInt(self) -> int:
        """"""
    def Read7BitEncodedInt64(self) -> int:
        """"""
    def ReadBList(self, skipErrors: bool = ...) -> IList[T]:
        """
        
        :param skipErrors: 
        :return: 
        """
    def ReadBoolean(self) -> bool:
        """"""
    def ReadByte(self) -> int:
        """"""
    def ReadByteArray(self) -> Array[int]:
        """
        
        :return: 
        """
    def ReadBytes(self, count: int) -> Array[int]:
        """"""
    def ReadChar(self) -> Char:
        """"""
    def ReadCharArray(self) -> Array[Char]:
        """
        
        :return: 
        """
    def ReadChars(self, count: int) -> Array[Char]:
        """"""
    def ReadDateTime(self) -> DateTime:
        """
        
        :return: 
        """
    def ReadDecimal(self) -> Decimal:
        """"""
    def ReadDictionary(self) -> IDictionary[TKey, TValue]:
        """
        
        :return: 
        """
    def ReadDouble(self) -> float:
        """"""
    def ReadExactly(self, buffer: Span[int]) -> None:
        """"""
    def ReadHalf(self) -> Half:
        """"""
    def ReadInt16(self) -> int:
        """"""
    def ReadInt32(self) -> int:
        """"""
    def ReadInt64(self) -> int:
        """"""
    def ReadList(self) -> IList[T]:
        """
        
        :return: 
        """
    def ReadObject(self) -> object:
        """
        
        :return: 
        """
    def ReadSByte(self) -> int:
        """"""
    def ReadSingle(self) -> float:
        """"""
    def ReadString(self) -> str:
        """"""
    def ReadUInt16(self) -> int:
        """"""
    def ReadUInt32(self) -> int:
        """"""
    def ReadUInt64(self) -> int:
        """"""
    def ToString(self) -> str:
        """"""
class SerializationWriter(BinaryWriter, IAsyncDisposable, IDisposable):
    """"""
    def __init__(self, s: Stream, leaveOpen: bool = ...):
        """
        
        :param s: 
        :param leaveOpen: 
        """
    @property
    def BaseStream(self) -> Stream:
        """"""
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def DisposeAsync(self) -> ValueTask:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetWriter(cls) -> SerializationWriter:
        """
        
        :return: 
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Write(self, d: IDictionary[TKey, TValue]) -> None:
        """
        
        :param d: 
        """
    @overload
    def Write(self, c: List[T]) -> None:
        """
        
        :param c: 
        """
    @overload
    def Write(self, b: Array[int]) -> None:
        """"""
    @overload
    def Write(self, c: Array[Char]) -> None:
        """"""
    @overload
    def Write(self, value: bool) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, ch: Char) -> None:
        """"""
    @overload
    def Write(self, dt: DateTime) -> None:
        """
        
        :param dt: 
        """
    @overload
    def Write(self, value: Decimal) -> None:
        """"""
    @overload
    def Write(self, value: float) -> None:
        """"""
    @overload
    def Write(self, value: Half) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, buffer: ReadOnlySpan[int]) -> None:
        """"""
    @overload
    def Write(self, chars: ReadOnlySpan[Char]) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, value: float) -> None:
        """"""
    @overload
    def Write(self, str: str) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, buffer: Array[int], index: int, count: int) -> None:
        """"""
    @overload
    def Write(self, chars: Array[Char], index: int, count: int) -> None:
        """"""
    def Write7BitEncodedInt(self, value: int) -> None:
        """"""
    def Write7BitEncodedInt64(self, value: int) -> None:
        """"""
    def WriteByteArray(self, b: Array[int]) -> None:
        """
        
        :param b: 
        """
    def WriteObject(self, obj: object) -> None:
        """
        
        :param obj: 
        """
    def WriteRawBytes(self, b: Array[int]) -> None:
        """
        
        :param b: 
        """
    def WriteUtf8(self, str: str) -> None:
        """
        
        :param str: 
        """