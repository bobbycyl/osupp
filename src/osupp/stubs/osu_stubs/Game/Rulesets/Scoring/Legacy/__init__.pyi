from System.Collections.Generic import IReadOnlyList
from System import Object
from System import Type
from System import ValueType
from __future__ import annotations
from osu.Game.Beatmaps import IBeatmap
from osu.Game.Beatmaps import IBeatmapDifficultyInfo
from osu.Game.Beatmaps import IBeatmapInfo
from osu.Game.Beatmaps import IWorkingBeatmap
from osu.Game.Online.API.Requests.Responses import APIBeatmap
from osu.Game.Rulesets import IRulesetInfo
from osu.Game.Rulesets.Mods import Mod
from typing import Final
class ILegacyScoreSimulator:
    """"""
    def GetLegacyScoreMultiplier(self, mods: IReadOnlyList[Mod], difficulty: LegacyBeatmapConversionDifficultyInfo) -> float:
        """
        
        :param mods: 
        :param difficulty: 
        :return: 
        """
    def Simulate(self, workingBeatmap: IWorkingBeatmap, playableBeatmap: IBeatmap) -> LegacyScoreAttributes:
        """
        
        :param workingBeatmap: 
        :param playableBeatmap: 
        :return: 
        """
class LegacyBeatmapConversionDifficultyInfo(Object, IBeatmapDifficultyInfo):
    """"""
    def __init__(self):
        """"""
    @property
    def ApproachRate(self) -> float:
        """
        
        :return: 
        """
    @ApproachRate.setter
    def ApproachRate(self, value: float) -> None: ...
    @property
    def CircleSize(self) -> float:
        """
        
        :return: 
        """
    @CircleSize.setter
    def CircleSize(self, value: float) -> None: ...
    @property
    def DrainRate(self) -> float:
        """
        
        :return: 
        """
    @DrainRate.setter
    def DrainRate(self, value: float) -> None: ...
    @property
    def EndTimeObjectCount(self) -> int:
        """
        
        :return: 
        """
    @EndTimeObjectCount.setter
    def EndTimeObjectCount(self, value: int) -> None: ...
    @property
    def OverallDifficulty(self) -> float:
        """
        
        :return: 
        """
    @OverallDifficulty.setter
    def OverallDifficulty(self, value: float) -> None: ...
    @property
    def SliderMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SliderTickRate(self) -> float:
        """
        
        :return: 
        """
    @property
    def SourceRuleset(self) -> IRulesetInfo:
        """
        
        :return: 
        """
    @SourceRuleset.setter
    def SourceRuleset(self, value: IRulesetInfo) -> None: ...
    @property
    def TotalObjectCount(self) -> int:
        """
        
        :return: 
        """
    @TotalObjectCount.setter
    def TotalObjectCount(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FromAPIBeatmap(cls, apiBeatmap: APIBeatmap) -> LegacyBeatmapConversionDifficultyInfo:
        """
        
        :param apiBeatmap: 
        :return: 
        """
    @classmethod
    def FromBeatmap(cls, beatmap: IBeatmap) -> LegacyBeatmapConversionDifficultyInfo:
        """
        
        :param beatmap: 
        :return: 
        """
    @classmethod
    def FromBeatmapInfo(cls, beatmapInfo: IBeatmapInfo) -> LegacyBeatmapConversionDifficultyInfo:
        """
        
        :param beatmapInfo: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class LegacyScoreAttributes(ValueType):
    """"""
    AccuracyScore: Final[int] = ...
    """
    
    :return: 
    """
    BonusScore: Final[int] = ...
    """
    
    :return: 
    """
    BonusScoreRatio: Final[float] = ...
    """
    
    :return: 
    """
    ComboScore: Final[int] = ...
    """
    
    :return: 
    """
    MaxCombo: Final[int] = ...
    """
    
    :return: 
    """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""