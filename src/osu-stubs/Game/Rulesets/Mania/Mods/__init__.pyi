from System import Array
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IReadOnlyList
from System import IEquatable
from System import Type
from System import ValueTuple
from __future__ import annotations
from abc import ABC
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
from osu.Game.Beatmaps import IBeatmapConverter
from osu.Game.Configuration import OsuConfigManager
from osu.Game.Rulesets.Mania.Objects import ManiaHitObject
from osu.Game.Rulesets.Mania import PlayfieldType
from osu.Game.Rulesets.Mania.UI import CoverExpandDirection
from osu.Game.Rulesets.Mods import DifficultyBindable
from osu.Game.Rulesets.Mods import IApplicableAfterBeatmapConversion
from osu.Game.Rulesets.Mods import IApplicableFailOverride
from osu.Game.Rulesets.Mods import IApplicableMod
from osu.Game.Rulesets.Mods import IApplicableToAudio
from osu.Game.Rulesets.Mods import IApplicableToBeatmap
from osu.Game.Rulesets.Mods import IApplicableToBeatmapConverter
from osu.Game.Rulesets.Mods import IApplicableToDifficulty
from osu.Game.Rulesets.Mods import IApplicableToDrawableHitObject
from osu.Game.Rulesets.Mods import IApplicableToDrawableRuleset
from osu.Game.Rulesets.Mods import IApplicableToHUD
from osu.Game.Rulesets.Mods import IApplicableToHealthProcessor
from osu.Game.Rulesets.Mods import IApplicableToHitObject
from osu.Game.Rulesets.Mods import IApplicableToPlayer
from osu.Game.Rulesets.Mods import IApplicableToRate
from osu.Game.Rulesets.Mods import IApplicableToSample
from osu.Game.Rulesets.Mods import IApplicableToScoreProcessor
from osu.Game.Rulesets.Mods import IApplicableToTrack
from osu.Game.Rulesets.Mods import ICreateReplayData
from osu.Game.Rulesets.Mods import IHasSeed
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
from osu.Game.Rulesets.Mods import ModPerfect
from osu.Game.Rulesets.Mods import ModRandom
from osu.Game.Rulesets.Mods import ModReplayData
from osu.Game.Rulesets.Mods import ModScoreV2
from osu.Game.Rulesets.Mods import ModSuddenDeath
from osu.Game.Rulesets.Mods import ModType
from osu.Game.Rulesets.Objects.Drawables import DrawableHitObject
from osu.Game.Rulesets.Objects import HitObject
from osu.Game.Rulesets.Scoring import HealthProcessor
from osu.Game.Rulesets.Scoring import ScoreProcessor
from osu.Game.Rulesets.UI import DrawableRuleset
from osu.Game.Rulesets.UI import Playfield
from osu.Game.Scoring import ScoreRank
from osu.Game.Screens.Play import HUDOverlay
from osu.Game.Screens.Play import Player
from osu.Game.Utils import IDeepCloneable
from typing import ClassVar
from typing import Final
from typing import Optional
from typing import overload
class IManiaRateAdjustmentMod(IApplicableMod, IApplicableToHitObject):
    """"""
    @property
    def SpeedChange(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    def ApplyToHitObject(self, hitObject: HitObject) -> None:
        """
        
        :param hitObject: 
        """
class IPlayfieldTypeMod(IApplicableMod):
    """"""
    @property
    def PlayfieldType(self) -> PlayfieldType:
        """
        
        :return: 
        """
class ManiaKeyMod(ABC, Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmapConverter, IMod, IDeepCloneable[Mod]):
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
    def KeyCount(self) -> int:
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
    def ApplyToBeatmapConverter(self, beatmapConverter: IBeatmapConverter) -> None:
        """
        
        :param beatmapConverter: 
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
class ManiaModAutoplay(ModAutoplay, IEquatable[IMod], IEquatable[Mod], ICreateReplayData, IMod, IDeepCloneable[Mod]):
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
class ManiaModCinema(ModCinema[ManiaHitObject], IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToDrawableRuleset[ManiaHitObject], IApplicableToHUD, IApplicableToPlayer, ICreateReplayData, IMod, IDeepCloneable[Mod]):
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
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[ManiaHitObject]) -> None:
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
class ManiaModClassic(ModClassic, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IMod, IDeepCloneable[Mod]):
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
class ManiaModConstantSpeed(Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableRuleset[ManiaHitObject], IMod, IDeepCloneable[Mod]):
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
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[ManiaHitObject]) -> None:
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
class ManiaModCover(ManiaModWithPlayfieldCover, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IApplicableToDrawableHitObject, IApplicableToDrawableRuleset[ManiaHitObject], IApplicableToScoreProcessor, IMod, IReadFromConfig, IDeepCloneable[Mod]):
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
    def Coverage(self) -> BindableNumber[float]:
        """
        
        :return: 
        """
    @property
    def Description(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def Direction(self) -> Bindable[CoverExpandDirection]:
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
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[ManiaHitObject]) -> None:
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
class ManiaModDaycore(ModDaycore, IEquatable[IMod], IEquatable[Mod], IManiaRateAdjustmentMod, IApplicableMod, IApplicableToAudio, IApplicableToHitObject, IApplicableToRate, IApplicableToSample, IApplicableToTrack, IMod, IDeepCloneable[Mod]):
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
    def ApplyToHitObject(self, hitObject: HitObject) -> None:
        """
        
        :param hitObject: 
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
class ManiaModDifficultyAdjust(ModDifficultyAdjust, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDifficulty, IMod, IDeepCloneable[Mod]):
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
class ManiaModDoubleTime(ModDoubleTime, IEquatable[IMod], IEquatable[Mod], IManiaRateAdjustmentMod, IApplicableMod, IApplicableToAudio, IApplicableToHitObject, IApplicableToRate, IApplicableToSample, IApplicableToTrack, IMod, IDeepCloneable[Mod]):
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
    def ApplyToHitObject(self, hitObject: HitObject) -> None:
        """
        
        :param hitObject: 
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
class ManiaModDualStages(Mod, IEquatable[IMod], IEquatable[Mod], IPlayfieldTypeMod, IApplicableMod, IApplicableToBeatmapConverter, IMod, IDeepCloneable[Mod]):
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
    def PlayfieldType(self) -> PlayfieldType:
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
    def ApplyToBeatmapConverter(self, beatmapConverter: IBeatmapConverter) -> None:
        """
        
        :param beatmapConverter: 
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
class ManiaModEasy(ModEasyWithExtraLives, IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToDifficulty, IApplicableToHealthProcessor, IApplicableToHitObject, IApplicableToPlayer, IMod, IDeepCloneable[Mod]):
    """"""
    HIT_WINDOW_DIFFICULTY_MULTIPLIER: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
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
    def ApplyToHitObject(self, hitObject: HitObject) -> None:
        """
        
        :param hitObject: 
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
    def PerformFail(self) -> bool:
        """
        
        :return: 
        """
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class ManiaModFadeIn(ManiaModHidden, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IApplicableToDrawableHitObject, IApplicableToDrawableRuleset[ManiaHitObject], IApplicableToPlayer, IApplicableToScoreProcessor, IMod, IReadFromConfig, IUpdatableByPlayfield, IDeepCloneable[Mod]):
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
    def Coverage(self) -> BindableNumber[float]:
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
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[ManiaHitObject]) -> None:
        """
        
        :param drawableRuleset: 
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
    def ReadFromConfig(self, config: OsuConfigManager) -> None:
        """
        
        :param config: 
        """
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, playfield: Playfield) -> None:
        """
        
        :param playfield: 
        """
class ManiaModFlashlight(ModFlashlight[ManiaHitObject], IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableRuleset[ManiaHitObject], IApplicableToScoreProcessor, IMod, IDeepCloneable[Mod]):
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
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[ManiaHitObject]) -> None:
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
class ManiaModHalfTime(ModHalfTime, IEquatable[IMod], IEquatable[Mod], IManiaRateAdjustmentMod, IApplicableMod, IApplicableToAudio, IApplicableToHitObject, IApplicableToRate, IApplicableToSample, IApplicableToTrack, IMod, IDeepCloneable[Mod]):
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
    def ApplyToHitObject(self, hitObject: HitObject) -> None:
        """
        
        :param hitObject: 
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
class ManiaModHardRock(ModHardRock, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDifficulty, IApplicableToHitObject, IMod, IDeepCloneable[Mod]):
    """"""
    HIT_WINDOW_DIFFICULTY_MULTIPLIER: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
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
    def ApplyToDifficulty(self, difficulty: BeatmapDifficulty) -> None:
        """
        
        :param difficulty: 
        """
    def ApplyToHitObject(self, hitObject: HitObject) -> None:
        """
        
        :param hitObject: 
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
class ManiaModHidden(ManiaModWithPlayfieldCover, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IApplicableToDrawableHitObject, IApplicableToDrawableRuleset[ManiaHitObject], IApplicableToPlayer, IApplicableToScoreProcessor, IMod, IReadFromConfig, IUpdatableByPlayfield, IDeepCloneable[Mod]):
    """"""
    MAX_COVERAGE: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    MIN_COVERAGE: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
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
    def Coverage(self) -> BindableNumber[float]:
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
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[ManiaHitObject]) -> None:
        """
        
        :param drawableRuleset: 
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
    def ReadFromConfig(self, config: OsuConfigManager) -> None:
        """
        
        :param config: 
        """
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Update(self, playfield: Playfield) -> None:
        """
        
        :param playfield: 
        """
class ManiaModHoldOff(Mod, IEquatable[IMod], IEquatable[Mod], IApplicableAfterBeatmapConversion, IApplicableMod, IMod, IDeepCloneable[Mod]):
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
class ManiaModInvert(Mod, IEquatable[IMod], IEquatable[Mod], IApplicableAfterBeatmapConversion, IApplicableMod, IMod, IDeepCloneable[Mod]):
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
class ManiaModKey1(ManiaKeyMod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmapConverter, IMod, IDeepCloneable[Mod]):
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
    def KeyCount(self) -> int:
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
    def ApplyToBeatmapConverter(self, beatmapConverter: IBeatmapConverter) -> None:
        """
        
        :param beatmapConverter: 
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
class ManiaModKey10(ManiaKeyMod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmapConverter, IMod, IDeepCloneable[Mod]):
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
    def KeyCount(self) -> int:
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
    def ApplyToBeatmapConverter(self, beatmapConverter: IBeatmapConverter) -> None:
        """
        
        :param beatmapConverter: 
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
class ManiaModKey2(ManiaKeyMod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmapConverter, IMod, IDeepCloneable[Mod]):
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
    def KeyCount(self) -> int:
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
    def ApplyToBeatmapConverter(self, beatmapConverter: IBeatmapConverter) -> None:
        """
        
        :param beatmapConverter: 
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
class ManiaModKey3(ManiaKeyMod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmapConverter, IMod, IDeepCloneable[Mod]):
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
    def KeyCount(self) -> int:
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
    def ApplyToBeatmapConverter(self, beatmapConverter: IBeatmapConverter) -> None:
        """
        
        :param beatmapConverter: 
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
class ManiaModKey4(ManiaKeyMod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmapConverter, IMod, IDeepCloneable[Mod]):
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
    def KeyCount(self) -> int:
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
    def ApplyToBeatmapConverter(self, beatmapConverter: IBeatmapConverter) -> None:
        """
        
        :param beatmapConverter: 
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
class ManiaModKey5(ManiaKeyMod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmapConverter, IMod, IDeepCloneable[Mod]):
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
    def KeyCount(self) -> int:
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
    def ApplyToBeatmapConverter(self, beatmapConverter: IBeatmapConverter) -> None:
        """
        
        :param beatmapConverter: 
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
class ManiaModKey6(ManiaKeyMod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmapConverter, IMod, IDeepCloneable[Mod]):
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
    def KeyCount(self) -> int:
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
    def ApplyToBeatmapConverter(self, beatmapConverter: IBeatmapConverter) -> None:
        """
        
        :param beatmapConverter: 
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
class ManiaModKey7(ManiaKeyMod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmapConverter, IMod, IDeepCloneable[Mod]):
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
    def KeyCount(self) -> int:
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
    def ApplyToBeatmapConverter(self, beatmapConverter: IBeatmapConverter) -> None:
        """
        
        :param beatmapConverter: 
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
class ManiaModKey8(ManiaKeyMod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmapConverter, IMod, IDeepCloneable[Mod]):
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
    def KeyCount(self) -> int:
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
    def ApplyToBeatmapConverter(self, beatmapConverter: IBeatmapConverter) -> None:
        """
        
        :param beatmapConverter: 
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
class ManiaModKey9(ManiaKeyMod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmapConverter, IMod, IDeepCloneable[Mod]):
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
    def KeyCount(self) -> int:
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
    def ApplyToBeatmapConverter(self, beatmapConverter: IBeatmapConverter) -> None:
        """
        
        :param beatmapConverter: 
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
class ManiaModMirror(ModMirror, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IMod, IDeepCloneable[Mod]):
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
class ManiaModMuted(ModMuted[ManiaHitObject], IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableRuleset[ManiaHitObject], IApplicableToScoreProcessor, IApplicableToTrack, IMod, IDeepCloneable[Mod]):
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
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[ManiaHitObject]) -> None:
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
class ManiaModNightcore(ModNightcore[ManiaHitObject], IEquatable[IMod], IEquatable[Mod], IManiaRateAdjustmentMod, IApplicableMod, IApplicableToAudio, IApplicableToDrawableRuleset[ManiaHitObject], IApplicableToHitObject, IApplicableToRate, IApplicableToSample, IApplicableToTrack, IMod, IDeepCloneable[Mod]):
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
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[ManiaHitObject]) -> None:
        """
        
        :param drawableRuleset: 
        """
    def ApplyToHitObject(self, hitObject: HitObject) -> None:
        """
        
        :param hitObject: 
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
class ManiaModNoFail(ModNoFail, IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToHUD, IMod, IReadFromConfig, IDeepCloneable[Mod]):
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
class ManiaModNoRelease(Mod, IEquatable[IMod], IEquatable[Mod], IApplicableAfterBeatmapConversion, IApplicableMod, IApplicableToDrawableRuleset[ManiaHitObject], IMod, IDeepCloneable[Mod]):
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
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[ManiaHitObject]) -> None:
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
class ManiaModPerfect(ModPerfect, IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToHealthProcessor, IMod, IDeepCloneable[Mod]):
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
    def RequirePerfectHits(self) -> BindableBool:
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
class ManiaModRandom(ModRandom, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IHasSeed, IMod, IDeepCloneable[Mod]):
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
    def Seed(self) -> Bindable[Optional[int]]:
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
class ManiaModScoreV2(ModScoreV2, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IMod, IDeepCloneable[Mod]):
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
class ManiaModSuddenDeath(ModSuddenDeath, IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToHealthProcessor, IMod, IDeepCloneable[Mod]):
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
class ManiaModWithPlayfieldCover(ABC, ModHidden, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IApplicableToDrawableHitObject, IApplicableToDrawableRuleset[ManiaHitObject], IApplicableToScoreProcessor, IMod, IReadFromConfig, IDeepCloneable[Mod]):
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
    def Coverage(self) -> BindableNumber[float]:
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
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[ManiaHitObject]) -> None:
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