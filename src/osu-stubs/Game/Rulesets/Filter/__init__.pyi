from System.Collections.Generic import IReadOnlyList
from __future__ import annotations
from osu.Framework.Bindables import ValueChangedEvent
from osu.Game.Beatmaps import BeatmapInfo
from osu.Game.Rulesets.Mods import Mod
from osu.Game.Screens.Select.Filter import Operator
from osu.Game.Screens.Select import FilterCriteria
class IRulesetFilterCriteria:
    """"""
    def FilterMayChangeFromMods(self, mods: ValueChangedEvent[IReadOnlyList[Mod]]) -> bool:
        """
        
        :param mods: 
        :return: 
        """
    def Matches(self, beatmapInfo: BeatmapInfo, criteria: FilterCriteria) -> bool:
        """
        
        :param beatmapInfo: 
        :param criteria: 
        :return: 
        """
    def TryParseCustomKeywordCriteria(self, key: str, op: Operator, value: str) -> bool:
        """
        
        :param key: 
        :param op: 
        :param value: 
        :return: 
        """