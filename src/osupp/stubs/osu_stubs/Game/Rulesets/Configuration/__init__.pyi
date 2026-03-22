from System.Collections.Generic import IDictionary
from System import IDisposable
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Framework.Bindables import Bindable
from osu.Framework.Configuration import ConfigManager
from osu.Framework.Configuration import IConfigManager
from osu.Framework.Configuration.Tracking import ITrackableConfigManager
from osu.Framework.Configuration.Tracking import TrackedSettings
from typing import Generic
from typing import TypeVar
TLookup = TypeVar("TLookup")
TValue = TypeVar("TValue")
class IRulesetConfigManager(IDisposable, ITrackableConfigManager, IConfigManager):
    """"""
    def CreateTrackedSettings(self) -> TrackedSettings:
        """"""
    def Dispose(self) -> None:
        """"""
    def Load(self) -> None:
        """"""
    def LoadInto(self, settings: TrackedSettings) -> None:
        """"""
    def Save(self) -> bool:
        """"""
class RulesetConfigManager(ABC, Generic[TLookup], ConfigManager[TLookup], IDisposable, ITrackableConfigManager, IConfigManager, IRulesetConfigManager):
    """"""
    def BindWith(self, lookup: TLookup, bindable: Bindable[TValue]) -> None:
        """"""
    def CreateTrackedSettings(self) -> TrackedSettings:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Get(self, lookup: TLookup) -> TValue:
        """"""
    def GetBindable(self, lookup: TLookup) -> Bindable[TValue]:
        """"""
    def GetCurrentConfigurationForLogging(self) -> IDictionary[TLookup, str]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Load(self) -> None:
        """"""
    def LoadInto(self, settings: TrackedSettings) -> None:
        """"""
    def Save(self) -> bool:
        """"""
    def SetValue(self, lookup: TLookup, value: TValue) -> None:
        """"""
    def ToString(self) -> str:
        """"""