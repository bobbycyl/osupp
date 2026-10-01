from SharpCompress.Common import ArchiveEncoding
from System import Array
from System import Byte
from System.Collections.Generic import IEnumerable
from System import IDisposable
from System.IO import MemoryStream
from System.IO import Stream
from System import Object
from System.Threading import CancellationToken
from System.Threading.Tasks import Task
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Framework.IO.Stores import IResourceStore
from typing import ClassVar
from typing import Final
class ArchiveReader(ABC, Object, IDisposable, IResourceStore[Array[Byte]]):
    """"""
    Name: Final[str] = ...
    """
    
    :return: 
    """
    @property
    def Filenames(self) -> IEnumerable[str]:
        """
        
        :return: 
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Get(self, name: str) -> Array[int]:
        """"""
    def GetAsync(self, name: str, cancellationToken: CancellationToken = ...) -> Task[Array[int]]:
        """"""
    def GetAvailableResources(self) -> IEnumerable[str]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetStream(self, name: str) -> Stream:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class ByteArrayArchiveReader(ArchiveReader, IDisposable, IResourceStore[Array[Byte]]):
    """"""
    Name: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self, content: Array[int], filename: str):
        """
        
        :param content: 
        :param filename: 
        """
    @property
    def Filenames(self) -> IEnumerable[str]:
        """
        
        :return: 
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Get(self, name: str) -> Array[int]:
        """"""
    def GetAsync(self, name: str, cancellationToken: CancellationToken = ...) -> Task[Array[int]]:
        """"""
    def GetAvailableResources(self) -> IEnumerable[str]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetStream(self, name: str) -> Stream:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class DirectoryArchiveReader(ArchiveReader, IDisposable, IResourceStore[Array[Byte]]):
    """"""
    Name: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self, path: str):
        """
        
        :param path: 
        """
    @property
    def Filenames(self) -> IEnumerable[str]:
        """
        
        :return: 
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Get(self, name: str) -> Array[int]:
        """"""
    def GetAsync(self, name: str, cancellationToken: CancellationToken = ...) -> Task[Array[int]]:
        """"""
    def GetAvailableResources(self) -> IEnumerable[str]:
        """"""
    def GetFullPath(self, filename: str) -> str:
        """
        
        :param filename: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetStream(self, name: str) -> Stream:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class MemoryStreamArchiveReader(ArchiveReader, IDisposable, IResourceStore[Array[Byte]]):
    """"""
    Name: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self, stream: MemoryStream, filename: str):
        """
        
        :param stream: 
        :param filename: 
        """
    @property
    def Filenames(self) -> IEnumerable[str]:
        """
        
        :return: 
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Get(self, name: str) -> Array[int]:
        """"""
    def GetAsync(self, name: str, cancellationToken: CancellationToken = ...) -> Task[Array[int]]:
        """"""
    def GetAvailableResources(self) -> IEnumerable[str]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetStream(self, name: str) -> Stream:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class SingleFileArchiveReader(ArchiveReader, IDisposable, IResourceStore[Array[Byte]]):
    """"""
    Name: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self, path: str):
        """
        
        :param path: 
        """
    @property
    def Filenames(self) -> IEnumerable[str]:
        """
        
        :return: 
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Get(self, name: str) -> Array[int]:
        """"""
    def GetAsync(self, name: str, cancellationToken: CancellationToken = ...) -> Task[Array[int]]:
        """"""
    def GetAvailableResources(self) -> IEnumerable[str]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetStream(self, name: str) -> Stream:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class ZipArchiveReader(ArchiveReader, IDisposable, IResourceStore[Array[Byte]]):
    """"""
    DEFAULT_ENCODING: Final[ClassVar[ArchiveEncoding]] = ...
    """
    
    :return: 
    """
    Name: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self, archiveStream: Stream, name: str = ...):
        """
        
        :param archiveStream: 
        :param name: 
        """
    @property
    def Filenames(self) -> IEnumerable[str]:
        """
        
        :return: 
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Get(self, name: str) -> Array[int]:
        """"""
    def GetAsync(self, name: str, cancellationToken: CancellationToken = ...) -> Task[Array[int]]:
        """"""
    def GetAvailableResources(self) -> IEnumerable[str]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetStream(self, name: str) -> Stream:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""