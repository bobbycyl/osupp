from System.Collections.Generic import IDictionary
from System import Enum
from System import IDisposable
from System import Type
from __future__ import annotations
from osu.Framework.Bindables import Bindable
from osu.Framework.Configuration import IConfigManager
from osu.Framework.Configuration.Tracking import ITrackableConfigManager
from osu.Framework.Configuration.Tracking import TrackedSettings
from osu.Game.Configuration import SettingsStore
from osu.Game.Rulesets.Configuration import IRulesetConfigManager
from osu.Game.Rulesets.Configuration import RulesetConfigManager
from osu.Game.Rulesets import RulesetInfo
from typing import Optional
from typing import TypeVar
TValue = TypeVar("TValue")
class OsuRulesetConfigManager(RulesetConfigManager[OsuRulesetSetting], IDisposable, ITrackableConfigManager, IConfigManager, IRulesetConfigManager):
    """"""
    def __init__(self, settings: SettingsStore, ruleset: RulesetInfo, variant: Optional[int] = ...):
        """
        
        :param settings: 
        :param ruleset: 
        :param variant: 
        """
    def BindWith(self, lookup: OsuRulesetSetting, bindable: Bindable[TValue]) -> None:
        """"""
    def CreateTrackedSettings(self) -> TrackedSettings:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Get(self, lookup: OsuRulesetSetting) -> TValue:
        """"""
    def GetBindable(self, lookup: OsuRulesetSetting) -> Bindable[TValue]:
        """"""
    def GetCurrentConfigurationForLogging(self) -> IDictionary[OsuRulesetSetting, str]:
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
    def SetValue(self, lookup: OsuRulesetSetting, value: TValue) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class OsuRulesetSetting(Enum):
    """"""
    SnakingInSliders: OsuRulesetSetting = ...
    """"""
    SnakingOutSliders: OsuRulesetSetting = ...
    """"""
    ShowCursorTrail: OsuRulesetSetting = ...
    """"""
    ShowCursorRipples: OsuRulesetSetting = ...
    """"""
    PlayfieldBorderStyle: OsuRulesetSetting = ...
    """"""
    ReplayClickMarkersEnabled: OsuRulesetSetting = ...
    """"""
    ReplayFrameMarkersEnabled: OsuRulesetSetting = ...
    """"""
    ReplayCursorPathEnabled: OsuRulesetSetting = ...
    """"""
    ReplayCursorHideEnabled: OsuRulesetSetting = ...
    """"""
    ReplayAnalysisDisplayLength: OsuRulesetSetting = ...
    """"""