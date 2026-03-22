from System import Action
from System import Array
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import List
from System.Threading import CancellationToken
from System import Type
from __future__ import annotations
from osu.Framework.Lists import SortedList
from osu.Game.Beatmaps import Beatmap
from osu.Game.Beatmaps import BeatmapConverter
from osu.Game.Beatmaps import BeatmapDifficulty
from osu.Game.Beatmaps import BeatmapInfo
from osu.Game.Beatmaps import BeatmapMetadata
from osu.Game.Beatmaps import BeatmapProcessor
from osu.Game.Beatmaps import BeatmapStatistic
from osu.Game.Beatmaps.ControlPoints import ControlPointInfo
from osu.Game.Beatmaps import CountdownType
from osu.Game.Beatmaps import IBeatmap
from osu.Game.Beatmaps import IBeatmapConverter
from osu.Game.Beatmaps import IBeatmapProcessor
from osu.Game.Beatmaps.Timing import BreakPeriod
from osu.Game.Rulesets.Objects import HitObject
from osu.Game.Rulesets.Osu.Objects import OsuHitObject
from osu.Game.Rulesets import Ruleset
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import TypeVar
T = TypeVar("T")
class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...
class OsuBeatmap(Beatmap[OsuHitObject], IBeatmap, IBeatmap[OsuHitObject]):
    """"""
    def __init__(self):
        """"""
    @property
    def AudioLeadIn(self) -> float:
        """
        
        :return: 
        """
    @AudioLeadIn.setter
    def AudioLeadIn(self, value: float) -> None: ...
    @property
    def BeatmapInfo(self) -> BeatmapInfo:
        """
        
        :return: 
        """
    @BeatmapInfo.setter
    def BeatmapInfo(self, value: BeatmapInfo) -> None: ...
    @property
    def BeatmapVersion(self) -> int:
        """
        
        :return: 
        """
    @BeatmapVersion.setter
    def BeatmapVersion(self, value: int) -> None: ...
    @property
    def Bookmarks(self) -> Array[int]:
        """
        
        :return: 
        """
    @Bookmarks.setter
    def Bookmarks(self, value: Array[int]) -> None: ...
    @property
    def Breaks(self) -> SortedList[BreakPeriod]:
        """
        
        :return: 
        """
    @Breaks.setter
    def Breaks(self, value: SortedList[BreakPeriod]) -> None: ...
    @property
    def ControlPointInfo(self) -> ControlPointInfo:
        """
        
        :return: 
        """
    @ControlPointInfo.setter
    def ControlPointInfo(self, value: ControlPointInfo) -> None: ...
    @property
    def Countdown(self) -> CountdownType:
        """
        
        :return: 
        """
    @Countdown.setter
    def Countdown(self, value: CountdownType) -> None: ...
    @property
    def CountdownOffset(self) -> int:
        """
        
        :return: 
        """
    @CountdownOffset.setter
    def CountdownOffset(self, value: int) -> None: ...
    @property
    def Difficulty(self) -> BeatmapDifficulty:
        """
        
        :return: 
        """
    @Difficulty.setter
    def Difficulty(self, value: BeatmapDifficulty) -> None: ...
    @property
    def DistanceSpacing(self) -> float:
        """
        
        :return: 
        """
    @DistanceSpacing.setter
    def DistanceSpacing(self, value: float) -> None: ...
    @property
    def EpilepsyWarning(self) -> bool:
        """
        
        :return: 
        """
    @EpilepsyWarning.setter
    def EpilepsyWarning(self, value: bool) -> None: ...
    @property
    def GridSize(self) -> int:
        """
        
        :return: 
        """
    @GridSize.setter
    def GridSize(self, value: int) -> None: ...
    @property
    def HitObjects(self) -> List[OsuHitObject]:
        """
        
        :return: 
        """
    @HitObjects.setter
    def HitObjects(self, value: List[OsuHitObject]) -> None: ...
    @property
    def LetterboxInBreaks(self) -> bool:
        """
        
        :return: 
        """
    @LetterboxInBreaks.setter
    def LetterboxInBreaks(self, value: bool) -> None: ...
    @property
    def Metadata(self) -> BeatmapMetadata:
        """
        
        :return: 
        """
    @property
    def SamplesMatchPlaybackRate(self) -> bool:
        """
        
        :return: 
        """
    @SamplesMatchPlaybackRate.setter
    def SamplesMatchPlaybackRate(self, value: bool) -> None: ...
    @property
    def SpecialStyle(self) -> bool:
        """
        
        :return: 
        """
    @SpecialStyle.setter
    def SpecialStyle(self, value: bool) -> None: ...
    @property
    def StackLeniency(self) -> float:
        """
        
        :return: 
        """
    @StackLeniency.setter
    def StackLeniency(self, value: float) -> None: ...
    @property
    def TimelineZoom(self) -> float:
        """
        
        :return: 
        """
    @TimelineZoom.setter
    def TimelineZoom(self, value: float) -> None: ...
    @property
    def TotalBreakTime(self) -> float:
        """
        
        :return: 
        """
    @property
    def UnhandledEventLines(self) -> List[str]:
        """
        
        :return: 
        """
    @UnhandledEventLines.setter
    def UnhandledEventLines(self, value: List[str]) -> None: ...
    @property
    def WidescreenStoryboard(self) -> bool:
        """
        
        :return: 
        """
    @WidescreenStoryboard.setter
    def WidescreenStoryboard(self, value: bool) -> None: ...
    def Clone(self) -> Beatmap[OsuHitObject]:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMostCommonBeatLength(self) -> float:
        """
        
        :return: 
        """
    def GetStatistics(self) -> IEnumerable[BeatmapStatistic]:
        """
        
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class OsuBeatmapConverter(BeatmapConverter[OsuHitObject], IBeatmapConverter):
    """"""
    def __init__(self, beatmap: IBeatmap, ruleset: Ruleset):
        """
        
        :param beatmap: 
        :param ruleset: 
        """
    @property
    def Beatmap(self) -> IBeatmap:
        """
        
        :return: 
        """
    def CanConvert(self) -> bool:
        """
        
        :return: 
        """
    def Convert(self, cancellationToken: CancellationToken = ...) -> IBeatmap:
        """
        
        :param cancellationToken: 
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
    ObjectConverted: EventType[Action[HitObject, IEnumerable[HitObject]]] = ...
    """"""
class OsuBeatmapProcessor(BeatmapProcessor, IBeatmapProcessor):
    """"""
    STACK_DISTANCE: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    def __init__(self, beatmap: IBeatmap):
        """
        
        :param beatmap: 
        """
    @property
    def Beatmap(self) -> IBeatmap:
        """
        
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PostProcess(self) -> None:
        """"""
    def PreProcess(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""