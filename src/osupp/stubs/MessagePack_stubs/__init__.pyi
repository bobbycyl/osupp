from MessagePack.Formatters import IMessagePackFormatter
from System import Object
from System import Type
from __future__ import annotations
from typing import ClassVar
from typing import Final
from typing import TypeVar
T = TypeVar("T")
class GeneratedMessagePackResolver(Object, IFormatterResolver):
    """"""
    Instance: Final[ClassVar[IFormatterResolver]] = ...
    """
    
    :return: 
    """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetFormatter(self) -> IMessagePackFormatter[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""