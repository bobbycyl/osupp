from __future__ import annotations
from osu.Game.Beatmaps import IBeatmap
from osu.Game.Replays.Legacy import LegacyReplayFrame
from osu.Game.Rulesets.Replays import ReplayFrame
class IConvertibleReplayFrame:
    """"""
    def FromLegacy(self, currentFrame: LegacyReplayFrame, beatmap: IBeatmap, lastFrame: ReplayFrame = ...) -> None:
        """
        
        :param currentFrame: 
        :param beatmap: 
        :param lastFrame: 
        """
    def ToLegacy(self, beatmap: IBeatmap) -> LegacyReplayFrame:
        """
        
        :param beatmap: 
        :return: 
        """