from System import Array
from System.Collections.Generic import IEnumerable
from System import Enum
from System import IDisposable
from System.IO import FileAccess
from System.IO import FileMode
from System.IO import Stream
from System import IntPtr
from System import Object
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Framework.Audio import AudioManager
from osu.Framework.Graphics.Rendering import IRenderer
from osu.Framework.Graphics.Textures import TextureUpload
from osu.Framework.IO.Stores import IResourceStore
from osu.Framework.Platform import DesktopGameHost
from osu.Framework.Platform import DesktopStorage
from osu.Framework.Platform import GameHost
from osu.Framework.Platform import Storage
from osu.Game.Database import IHasPrimaryKey
from osu.Game.Database import RealmAccess
from typing import ClassVar
from typing import Final
from typing import Tuple
class FileInfo(Object, IHasPrimaryKey, IFileInfo):
    """"""
    def __init__(self):
        """"""
    @property
    def Hash(self) -> str:
        """
        
        :return: 
        """
    @Hash.setter
    def Hash(self, value: str) -> None: ...
    @property
    def ID(self) -> int:
        """
        
        :return: 
        """
    @ID.setter
    def ID(self, value: int) -> None: ...
    @property
    def IsManaged(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ReferenceCount(self) -> int:
        """
        
        :return: 
        """
    @ReferenceCount.setter
    def ReferenceCount(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class HardLinkHelper(ABC, Object):
    """"""
    @classmethod
    def CheckAvailability(cls, testDestinationPath: str, testSourcePath: str) -> bool:
        """
        
        :param testDestinationPath: 
        :param testSourcePath: 
        :return: 
        """
    @classmethod
    def CreateHardLink(cls, lpFileName: str, lpExistingFileName: str, lpSecurityAttributes: IntPtr) -> bool:
        """
        
        :param lpFileName: 
        :param lpExistingFileName: 
        :param lpSecurityAttributes: 
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetFileLinkCount(cls, filePath: str) -> int:
        """
        
        :param filePath: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def TryCreateHardLink(cls, destinationPath: str, sourcePath: str) -> bool:
        """
        
        :param destinationPath: 
        :param sourcePath: 
        :return: 
        """
    @classmethod
    def link(cls, oldpath: str, newpath: str) -> int:
        """
        
        :param oldpath: 
        :param newpath: 
        :return: 
        """
class IFileInfo:
    """"""
    @property
    def Hash(self) -> str:
        """
        
        :return: 
        """
class IStorageResourceProvider:
    """"""
    @property
    def AudioManager(self) -> AudioManager:
        """
        
        :return: 
        """
    @property
    def Files(self) -> IResourceStore[Array[int]]:
        """
        
        :return: 
        """
    @property
    def RealmAccess(self) -> RealmAccess:
        """
        
        :return: 
        """
    @property
    def Renderer(self) -> IRenderer:
        """
        
        :return: 
        """
    @property
    def Resources(self) -> IResourceStore[Array[int]]:
        """
        
        :return: 
        """
    def CreateTextureLoaderStore(self, underlyingStore: IResourceStore[Array[int]]) -> IResourceStore[TextureUpload]:
        """
        
        :param underlyingStore: 
        :return: 
        """
class LineBufferedReader(Object, IDisposable):
    """"""
    def __init__(self, stream: Stream, leaveOpen: bool = ...):
        """
        
        :param stream: 
        :param leaveOpen: 
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PeekLine(self) -> str:
        """
        
        :return: 
        """
    def ReadLine(self) -> str:
        """
        
        :return: 
        """
    def ReadToEnd(self) -> str:
        """
        
        :return: 
        """
    def ToString(self) -> str:
        """"""
class MigratableStorage(ABC, WrappedStorage):
    """"""
    @property
    def IgnoreDirectories(self) -> Array[str]:
        """
        
        :return: 
        """
    @property
    def IgnoreFiles(self) -> Array[str]:
        """
        
        :return: 
        """
    @property
    def IgnoreSuffixes(self) -> Array[str]:
        """
        
        :return: 
        """
    def CreateFileSafely(self, path: str) -> Stream:
        """"""
    def Delete(self, path: str) -> None:
        """"""
    def DeleteDirectory(self, path: str) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Exists(self, path: str) -> bool:
        """"""
    def ExistsDirectory(self, path: str) -> bool:
        """"""
    def GetDirectories(self, path: str) -> IEnumerable[str]:
        """"""
    def GetFiles(self, path: str, pattern: str = ...) -> IEnumerable[str]:
        """"""
    def GetFullPath(self, path: str, createIfNotExisting: bool = ...) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetStorageForDirectory(self, path: str) -> Storage:
        """"""
    def GetStream(self, path: str, access: FileAccess = ..., mode: FileMode = ...) -> Stream:
        """"""
    def GetType(self) -> Type:
        """"""
    def Migrate(self, newStorage: Storage) -> bool:
        """
        
        :param newStorage: 
        :return: 
        """
    def Move(self, _from: str, to: str) -> None:
        """"""
    def OpenFileExternally(self, filename: str) -> bool:
        """"""
    def PresentExternally(self) -> bool:
        """"""
    def PresentFileExternally(self, filename: str) -> bool:
        """"""
    def ToLocalRelative(self, paths: IEnumerable[str]) -> IEnumerable[str]:
        """
        
        :param paths: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class OsuStorage(MigratableStorage):
    """"""
    Error: Final[OsuStorageError] = ...
    """
    
    :return: 
    """
    def __init__(self, host: GameHost, defaultStorage: Storage):
        """
        
        :param host: 
        :param defaultStorage: 
        """
    @property
    def CustomStoragePath(self) -> str:
        """
        
        :return: 
        """
    @property
    def DefaultStoragePath(self) -> str:
        """
        
        :return: 
        """
    @property
    def IgnoreDirectories(self) -> Array[str]:
        """
        
        :return: 
        """
    @property
    def IgnoreFiles(self) -> Array[str]:
        """
        
        :return: 
        """
    @property
    def IgnoreSuffixes(self) -> Array[str]:
        """
        
        :return: 
        """
    def ChangeDataPath(self, newPath: str) -> None:
        """
        
        :param newPath: 
        """
    def CreateFileSafely(self, path: str) -> Stream:
        """"""
    def Delete(self, path: str) -> None:
        """"""
    def DeleteDirectory(self, path: str) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Exists(self, path: str) -> bool:
        """"""
    def ExistsDirectory(self, path: str) -> bool:
        """"""
    def GetDirectories(self, path: str) -> IEnumerable[str]:
        """"""
    def GetExportStorage(self) -> Storage:
        """
        
        :return: 
        """
    def GetFiles(self, path: str, pattern: str = ...) -> IEnumerable[str]:
        """"""
    def GetFullPath(self, path: str, createIfNotExisting: bool = ...) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetStorageForDirectory(self, path: str) -> Storage:
        """"""
    def GetStream(self, path: str, access: FileAccess = ..., mode: FileMode = ...) -> Stream:
        """"""
    def GetType(self) -> Type:
        """"""
    def Migrate(self, newStorage: Storage) -> bool:
        """
        
        :param newStorage: 
        :return: 
        """
    def Move(self, _from: str, to: str) -> None:
        """"""
    def OpenFileExternally(self, filename: str) -> bool:
        """"""
    def PresentExternally(self) -> bool:
        """"""
    def PresentFileExternally(self, filename: str) -> bool:
        """"""
    def ResetCustomStoragePath(self) -> None:
        """"""
    def ToLocalRelative(self, paths: IEnumerable[str]) -> IEnumerable[str]:
        """
        
        :param paths: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    def TryChangeToCustomStorage(self, error: OsuStorageError) -> Tuple[bool, OsuStorageError]:
        """
        
        :param error: 
        :return: 
        """
class OsuStorageError(Enum):
    """"""
    _None: OsuStorageError = ...
    """"""
    AccessibleButEmpty: OsuStorageError = ...
    """"""
    NotAccessible: OsuStorageError = ...
    """"""
class StableStorage(DesktopStorage):
    """"""
    STABLE_DEFAULT_SONGS_PATH: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    def __init__(self, path: str, host: DesktopGameHost):
        """
        
        :param path: 
        :param host: 
        """
    def CreateFileSafely(self, path: str) -> Stream:
        """"""
    def Delete(self, path: str) -> None:
        """"""
    def DeleteDirectory(self, path: str) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Exists(self, path: str) -> bool:
        """"""
    def ExistsDirectory(self, path: str) -> bool:
        """"""
    def GetDirectories(self, path: str) -> IEnumerable[str]:
        """"""
    def GetFiles(self, path: str, pattern: str = ...) -> IEnumerable[str]:
        """"""
    def GetFullPath(self, path: str, createIfNotExisting: bool = ...) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetSongStorage(self) -> Storage:
        """
        
        :return: 
        """
    def GetStorageForDirectory(self, path: str) -> Storage:
        """"""
    def GetStream(self, path: str, access: FileAccess = ..., mode: FileMode = ...) -> Stream:
        """"""
    def GetType(self) -> Type:
        """"""
    def Move(self, _from: str, to: str) -> None:
        """"""
    def OpenFileExternally(self, filename: str) -> bool:
        """"""
    def PresentExternally(self) -> bool:
        """"""
    def PresentFileExternally(self, filename: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
class WrappedStorage(Storage):
    """"""
    def __init__(self, underlyingStorage: Storage, subPath: str = ...):
        """
        
        :param underlyingStorage: 
        :param subPath: 
        """
    def CreateFileSafely(self, path: str) -> Stream:
        """"""
    def Delete(self, path: str) -> None:
        """"""
    def DeleteDirectory(self, path: str) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Exists(self, path: str) -> bool:
        """"""
    def ExistsDirectory(self, path: str) -> bool:
        """"""
    def GetDirectories(self, path: str) -> IEnumerable[str]:
        """"""
    def GetFiles(self, path: str, pattern: str = ...) -> IEnumerable[str]:
        """"""
    def GetFullPath(self, path: str, createIfNotExisting: bool = ...) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetStorageForDirectory(self, path: str) -> Storage:
        """"""
    def GetStream(self, path: str, access: FileAccess = ..., mode: FileMode = ...) -> Stream:
        """"""
    def GetType(self) -> Type:
        """"""
    def Move(self, _from: str, to: str) -> None:
        """"""
    def OpenFileExternally(self, filename: str) -> bool:
        """"""
    def PresentExternally(self) -> bool:
        """"""
    def PresentFileExternally(self, filename: str) -> bool:
        """"""
    def ToLocalRelative(self, paths: IEnumerable[str]) -> IEnumerable[str]:
        """
        
        :param paths: 
        :return: 
        """
    def ToString(self) -> str:
        """"""