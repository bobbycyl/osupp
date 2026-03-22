from System import Array
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IReadOnlyList
from System import IEquatable
from System import Type
from System import ValueTuple
from __future__ import annotations
from osu.Framework.Audio import IAdjustableAudioComponent
from osu.Framework.Bindables import Bindable
from osu.Framework.Bindables import BindableBool
from osu.Framework.Bindables import BindableFloat
from osu.Framework.Bindables import BindableInt
from osu.Framework.Bindables import BindableNumber
from osu.Framework.Graphics.Sprites import IconUsage
from osu.Framework.Localisation import LocalisableString
from osu.Game.Beatmaps import BeatmapDifficulty
from osu.Game.Beatmaps import IBeatmap
from osu.Game.Beatmaps import IBeatmapProcessor
from osu.Game.Configuration import OsuConfigManager
from osu.Game.Rulesets.Catch.Objects import CatchHitObject
from osu.Game.Rulesets.Mods import DifficultyBindable
from osu.Game.Rulesets.Mods import IApplicableFailOverride
from osu.Game.Rulesets.Mods import IApplicableMod
from osu.Game.Rulesets.Mods import IApplicableToAudio
from osu.Game.Rulesets.Mods import IApplicableToBeatmap
from osu.Game.Rulesets.Mods import IApplicableToBeatmapProcessor
from osu.Game.Rulesets.Mods import IApplicableToDifficulty
from osu.Game.Rulesets.Mods import IApplicableToDrawableHitObject
from osu.Game.Rulesets.Mods import IApplicableToDrawableRuleset
from osu.Game.Rulesets.Mods import IApplicableToHUD
from osu.Game.Rulesets.Mods import IApplicableToHealthProcessor
from osu.Game.Rulesets.Mods import IApplicableToPlayer
from osu.Game.Rulesets.Mods import IApplicableToRate
from osu.Game.Rulesets.Mods import IApplicableToSample
from osu.Game.Rulesets.Mods import IApplicableToScoreProcessor
from osu.Game.Rulesets.Mods import IApplicableToTrack
from osu.Game.Rulesets.Mods import ICreateReplayData
from osu.Game.Rulesets.Mods import IMod
from osu.Game.Rulesets.Mods import IReadFromConfig
from osu.Game.Rulesets.Mods import IUpdatableByPlayfield
from osu.Game.Rulesets.Mods import Mod
from osu.Game.Rulesets.Mods import ModAutoplay
from osu.Game.Rulesets.Mods import ModCinema
from osu.Game.Rulesets.Mods import ModClassic
from osu.Game.Rulesets.Mods import ModDaycore
from osu.Game.Rulesets.Mods import ModDifficultyAdjust
from osu.Game.Rulesets.Mods import ModDoubleTime
from osu.Game.Rulesets.Mods import ModEasyWithExtraLives
from osu.Game.Rulesets.Mods import ModFlashlight
from osu.Game.Rulesets.Mods import ModHalfTime
from osu.Game.Rulesets.Mods import ModHardRock
from osu.Game.Rulesets.Mods import ModHidden
from osu.Game.Rulesets.Mods import ModMirror
from osu.Game.Rulesets.Mods import ModMuted
from osu.Game.Rulesets.Mods import ModNightcore
from osu.Game.Rulesets.Mods import ModNoFail
from osu.Game.Rulesets.Mods import ModNoScope
from osu.Game.Rulesets.Mods import ModPerfect
from osu.Game.Rulesets.Mods import ModRelax
from osu.Game.Rulesets.Mods import ModReplayData
from osu.Game.Rulesets.Mods import ModSuddenDeath
from osu.Game.Rulesets.Mods import ModType
from osu.Game.Rulesets.Objects.Drawables import DrawableHitObject
from osu.Game.Rulesets.Scoring import HealthProcessor
from osu.Game.Rulesets.Scoring import ScoreProcessor
from osu.Game.Rulesets.UI import DrawableRuleset
from osu.Game.Rulesets.UI import Playfield
from osu.Game.Scoring import ScoreRank
from osu.Game.Screens.Play import HUDOverlay
from osu.Game.Screens.Play import Player
from osu.Game.Utils import IDeepCloneable
from typing import Optional
from typing import overload
class CatchModAutoplay(ModAutoplay, IEquatable[IMod], IEquatable[Mod], ICreateReplayData, IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def CreateReplayData(self, beatmap: IBeatmap, mods: IReadOnlyList[Mod]) -> ModReplayData:
        """
        
        :param beatmap: 
        :param mods: 
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class CatchModCinema(ModCinema[CatchHitObject], IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToDrawableRuleset[CatchHitObject], IApplicableToHUD, IApplicableToPlayer, ICreateReplayData, IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RestartOnFail(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[CatchHitObject]) -> None:
        """
        
        :param drawableRuleset: 
        """
    def ApplyToHUD(self, overlay: HUDOverlay) -> None:
        """
        
        :param overlay: 
        """
    def ApplyToPlayer(self, player: Player) -> None:
        """
        
        :param player: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def CreateReplayData(self, beatmap: IBeatmap, mods: IReadOnlyList[Mod]) -> ModReplayData:
        """
        
        :param beatmap: 
        :param mods: 
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PerformFail(self) -> bool:
        """
        
        :return: 
        """
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class CatchModClassic(ModClassic, IEquatable[IMod], IEquatable[Mod], IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class CatchModDaycore(ModDaycore, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToAudio, IApplicableToRate, IApplicableToSample, IApplicableToTrack, IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def SpeedChange(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToRate(self, time: float, rate: float) -> float:
        """
        
        :param time: 
        :param rate: 
        :return: 
        """
    def ApplyToSample(self, sample: IAdjustableAudioComponent) -> None:
        """
        
        :param sample: 
        """
    def ApplyToTrack(self, track: IAdjustableAudioComponent) -> None:
        """
        
        :param track: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class CatchModDifficultyAdjust(ModDifficultyAdjust, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmapProcessor, IApplicableToDifficulty, IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ApproachRate(self) -> DifficultyBindable:
        """
        
        :return: 
        """
    @property
    def CircleSize(self) -> DifficultyBindable:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def DrainRate(self) -> DifficultyBindable:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def ExtendedLimits(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def HardRockOffsets(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def OverallDifficulty(self) -> DifficultyBindable:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToBeatmapProcessor(self, beatmapProcessor: IBeatmapProcessor) -> None:
        """
        
        :param beatmapProcessor: 
        """
    def ApplyToDifficulty(self, difficulty: BeatmapDifficulty) -> None:
        """
        
        :param difficulty: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class CatchModDoubleTime(ModDoubleTime, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToAudio, IApplicableToRate, IApplicableToSample, IApplicableToTrack, IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AdjustPitch(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def SpeedChange(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToRate(self, time: float, rate: float) -> float:
        """
        
        :param time: 
        :param rate: 
        :return: 
        """
    def ApplyToSample(self, sample: IAdjustableAudioComponent) -> None:
        """
        
        :param sample: 
        """
    def ApplyToTrack(self, track: IAdjustableAudioComponent) -> None:
        """
        
        :param track: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class CatchModEasy(ModEasyWithExtraLives, IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToDifficulty, IApplicableToHealthProcessor, IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RestartOnFail(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Retries(self) -> Bindable[int]:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToDifficulty(self, difficulty: BeatmapDifficulty) -> None:
        """
        
        :param difficulty: 
        """
    def ApplyToHealthProcessor(self, healthProcessor: HealthProcessor) -> None:
        """
        
        :param healthProcessor: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PerformFail(self) -> bool:
        """
        
        :return: 
        """
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class CatchModFlashlight(ModFlashlight[CatchHitObject], IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableRuleset[CatchHitObject], IApplicableToScoreProcessor, IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ComboBasedSize(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def DefaultFlashlightSize(self) -> float:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def SizeMultiplier(self) -> BindableFloat:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def AdjustRank(self, rank: ScoreRank, accuracy: float) -> ScoreRank:
        """
        
        :param rank: 
        :param accuracy: 
        :return: 
        """
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[CatchHitObject]) -> None:
        """
        
        :param drawableRuleset: 
        """
    def ApplyToScoreProcessor(self, scoreProcessor: ScoreProcessor) -> None:
        """
        
        :param scoreProcessor: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class CatchModFloatingFruits(Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableRuleset[CatchHitObject], IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[CatchHitObject]) -> None:
        """
        
        :param drawableRuleset: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class CatchModHalfTime(ModHalfTime, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToAudio, IApplicableToRate, IApplicableToSample, IApplicableToTrack, IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AdjustPitch(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def SpeedChange(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToRate(self, time: float, rate: float) -> float:
        """
        
        :param time: 
        :param rate: 
        :return: 
        """
    def ApplyToSample(self, sample: IAdjustableAudioComponent) -> None:
        """
        
        :param sample: 
        """
    def ApplyToTrack(self, track: IAdjustableAudioComponent) -> None:
        """
        
        :param track: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class CatchModHardRock(ModHardRock, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmapProcessor, IApplicableToDifficulty, IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToBeatmapProcessor(self, beatmapProcessor: IBeatmapProcessor) -> None:
        """
        
        :param beatmapProcessor: 
        """
    def ApplyToDifficulty(self, difficulty: BeatmapDifficulty) -> None:
        """
        
        :param difficulty: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class CatchModHidden(ModHidden, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IApplicableToDrawableHitObject, IApplicableToDrawableRuleset[CatchHitObject], IApplicableToScoreProcessor, IMod, IReadFromConfig, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def AdjustRank(self, rank: ScoreRank, accuracy: float) -> ScoreRank:
        """
        
        :param rank: 
        :param accuracy: 
        :return: 
        """
    def ApplyToBeatmap(self, beatmap: IBeatmap) -> None:
        """
        
        :param beatmap: 
        """
    def ApplyToDrawableHitObject(self, dho: DrawableHitObject) -> None:
        """
        
        :param drawable: 
        """
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[CatchHitObject]) -> None:
        """
        
        :param drawableRuleset: 
        """
    def ApplyToScoreProcessor(self, scoreProcessor: ScoreProcessor) -> None:
        """
        
        :param scoreProcessor: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ReadFromConfig(self, config: OsuConfigManager) -> None:
        """
        
        :param config: 
        """
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class CatchModMirror(ModMirror, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToBeatmap(self, beatmap: IBeatmap) -> None:
        """
        
        :param beatmap: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class CatchModMovingFast(Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableRuleset[CatchHitObject], IApplicableToPlayer, IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[CatchHitObject]) -> None:
        """
        
        :param drawableRuleset: 
        """
    def ApplyToPlayer(self, player: Player) -> None:
        """
        
        :param player: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class CatchModMuted(ModMuted[CatchHitObject], IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableRuleset[CatchHitObject], IApplicableToScoreProcessor, IApplicableToTrack, IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AffectsHitSounds(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def EnableMetronome(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def InverseMuting(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def MuteComboCount(self) -> BindableInt:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def AdjustRank(self, rank: ScoreRank, accuracy: float) -> ScoreRank:
        """
        
        :param rank: 
        :param accuracy: 
        :return: 
        """
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[CatchHitObject]) -> None:
        """
        
        :param drawableRuleset: 
        """
    def ApplyToScoreProcessor(self, scoreProcessor: ScoreProcessor) -> None:
        """
        
        :param scoreProcessor: 
        """
    def ApplyToTrack(self, track: IAdjustableAudioComponent) -> None:
        """
        
        :param track: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class CatchModNightcore(ModNightcore[CatchHitObject], IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToAudio, IApplicableToDrawableRuleset[CatchHitObject], IApplicableToRate, IApplicableToSample, IApplicableToTrack, IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def SpeedChange(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[CatchHitObject]) -> None:
        """
        
        :param drawableRuleset: 
        """
    def ApplyToRate(self, time: float, rate: float) -> float:
        """
        
        :param time: 
        :param rate: 
        :return: 
        """
    def ApplyToSample(self, sample: IAdjustableAudioComponent) -> None:
        """
        
        :param sample: 
        """
    def ApplyToTrack(self, track: IAdjustableAudioComponent) -> None:
        """
        
        :param track: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class CatchModNoFail(ModNoFail, IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToHUD, IMod, IReadFromConfig, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RestartOnFail(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToHUD(self, overlay: HUDOverlay) -> None:
        """
        
        :param overlay: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PerformFail(self) -> bool:
        """
        
        :return: 
        """
    def ReadFromConfig(self, config: OsuConfigManager) -> None:
        """
        
        :param config: 
        """
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class CatchModNoScope(ModNoScope, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToPlayer, IApplicableToScoreProcessor, IMod, IUpdatableByPlayfield, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HiddenComboCount(self) -> BindableInt:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def AdjustRank(self, rank: ScoreRank, accuracy: float) -> ScoreRank:
        """
        
        :param rank: 
        :param accuracy: 
        :return: 
        """
    def ApplyToPlayer(self, player: Player) -> None:
        """
        
        :param player: 
        """
    def ApplyToScoreProcessor(self, scoreProcessor: ScoreProcessor) -> None:
        """
        
        :param scoreProcessor: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, playfield: Playfield) -> None:
        """
        
        :param playfield: 
        """
class CatchModPerfect(ModPerfect, IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToHealthProcessor, IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Restart(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def RestartOnFail(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToHealthProcessor(self, healthProcessor: HealthProcessor) -> None:
        """
        
        :param healthProcessor: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PerformFail(self) -> bool:
        """
        
        :return: 
        """
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class CatchModRelax(ModRelax, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableRuleset[CatchHitObject], IApplicableToPlayer, IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[CatchHitObject]) -> None:
        """
        
        :param drawableRuleset: 
        """
    def ApplyToPlayer(self, player: Player) -> None:
        """
        
        :param player: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class CatchModSuddenDeath(ModSuddenDeath, IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToHealthProcessor, IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def ExtendedIconInformation(self) -> str:
        """
        
        :return: 
        """
    @property
    def HasImplementation(self) -> bool:
        """
        
        :return: 
        """
    @property
    def HasNonDefaultSettings(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Icon(self) -> Optional[IconUsage]:
        """
        
        :return: 
        """
    @property
    def IncompatibleMods(self) -> Array[Type]:
        """
        
        :return: 
        """
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @property
    def RequiresConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Restart(self) -> BindableBool:
        """
        
        :return: 
        """
    @property
    def RestartOnFail(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ScoreMultiplier(self) -> float:
        """
        
        :return: 
        """
    @property
    def SettingDescription(self) -> IEnumerable[ValueTuple, LocalisableString]:
        """
        
        :return: 
        """
    @property
    def Type(self) -> ModType:
        """
        
        :return: 
        """
    @property
    def UserPlayable(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UsesDefaultConfiguration(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForFreestyleAsRequiredMod(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayer(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ValidForMultiplayerAsFreeMod(self) -> bool:
        """
        
        :return: 
        """
    def ApplyToHealthProcessor(self, healthProcessor: HealthProcessor) -> None:
        """
        
        :param healthProcessor: 
        """
    def CopyCommonSettingsFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CopyFrom(self, source: Mod) -> None:
        """
        
        :param source: 
        """
    def CreateInstance(self) -> Mod:
        """
        
        :return: 
        """
    def DeepClone(self) -> Mod:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IMod) -> bool:
        """"""
    @overload
    def Equals(self, other: Mod) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PerformFail(self) -> bool:
        """
        
        :return: 
        """
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""