from System.Collections.Generic import List
from System import Type
from __future__ import annotations
from osu.Game.Beatmaps.ControlPoints import ControlPointInfo
from osu.Game.Rulesets.Difficulty.Preprocessing import DifficultyHitObject
from osu.Game.Rulesets.Objects import HitObject
from osu.Game.Rulesets.Taiko.Difficulty.Preprocessing.Colour import TaikoColourData
from osu.Game.Rulesets.Taiko.Difficulty.Preprocessing.Rhythm import TaikoRhythmData
from osu.Game.Rulesets.Taiko.Difficulty.Utils import IHasInterval
from typing import Final
class TaikoDifficultyHitObject(DifficultyHitObject, IHasInterval):
    """"""
    BaseObject: Final[HitObject] = ...
    """
    
    :return: 
    """
    ColourData: Final[TaikoColourData] = ...
    """
    
    :return: 
    """
    DeltaTime: Final[float] = ...
    """
    
    :return: 
    """
    EffectiveBPM: Final[float] = ...
    """
    
    :return: 
    """
    EndTime: Final[float] = ...
    """
    
    :return: 
    """
    Index: Final[int] = ...
    """
    
    :return: 
    """
    LastObject: Final[HitObject] = ...
    """
    
    :return: 
    """
    MonoIndex: Final[int] = ...
    """
    
    :return: 
    """
    NoteIndex: Final[int] = ...
    """
    
    :return: 
    """
    RhythmData: Final[TaikoRhythmData] = ...
    """
    
    :return: 
    """
    StartTime: Final[float] = ...
    """
    
    :return: 
    """
    def __init__(self, hitObject: HitObject, lastObject: HitObject, clockRate: float, objects: List[DifficultyHitObject], centreHitObjects: List[TaikoDifficultyHitObject], rimHitObjects: List[TaikoDifficultyHitObject], noteObjects: List[TaikoDifficultyHitObject], index: int, controlPointInfo: ControlPointInfo, globalSliderVelocity: float):
        """
        
        :param hitObject: 
        :param lastObject: 
        :param clockRate: 
        :param objects: 
        :param centreHitObjects: 
        :param rimHitObjects: 
        :param noteObjects: 
        :param index: 
        :param controlPointInfo: 
        :param globalSliderVelocity: 
        """
    @property
    def Interval(self) -> float:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Next(self, forwardsIndex: int) -> DifficultyHitObject:
        """
        
        :param forwardsIndex: 
        :return: 
        """
    def NextMono(self, forwardsIndex: int) -> TaikoDifficultyHitObject:
        """
        
        :param forwardsIndex: 
        :return: 
        """
    def NextNote(self, forwardsIndex: int) -> TaikoDifficultyHitObject:
        """
        
        :param forwardsIndex: 
        :return: 
        """
    def Previous(self, backwardsIndex: int) -> DifficultyHitObject:
        """
        
        :param backwardsIndex: 
        :return: 
        """
    def PreviousMono(self, backwardsIndex: int) -> TaikoDifficultyHitObject:
        """
        
        :param backwardsIndex: 
        :return: 
        """
    def PreviousNote(self, backwardsIndex: int) -> TaikoDifficultyHitObject:
        """
        
        :param backwardsIndex: 
        :return: 
        """
    def ToString(self) -> str:
        """"""