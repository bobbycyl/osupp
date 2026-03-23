from System import IDisposable
from __future__ import annotations
class IHighPerformanceSessionManager:
    """"""
    @property
    def IsSessionActive(self) -> bool:
        """
        
        :return: 
        """
    def BeginSession(self) -> IDisposable:
        """
        
        :return: 
        """