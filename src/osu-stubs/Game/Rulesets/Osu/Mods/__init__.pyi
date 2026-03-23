from System import Action
from System import Array
from System.Collections.Generic import ICollection
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IReadOnlyCollection
from System.Collections.Generic import IReadOnlyList
from System.Collections import IEnumerable
from System import Enum
from System import IDisposable
from System import IEquatable
from System import Predicate
from System import Type
from System import ValueTuple
from __future__ import annotations
from abc import ABC
from osu.Framework.Allocation import IDependencyActivatorRegistry
from osu.Framework.Allocation import IDependencyInjectionCandidate
from osu.Framework.Allocation import IReadOnlyDependencyContainer
from osu.Framework.Allocation import ISourceGeneratedDependencyActivator
from osu.Framework.Allocation import ISourceGeneratedLongRunningLoadCache
from osu.Framework.Audio import IAdjustableAudioComponent
from osu.Framework.Bindables import Bindable
from osu.Framework.Bindables import BindableBool
from osu.Framework.Bindables import BindableDouble
from osu.Framework.Bindables import BindableFloat
from osu.Framework.Bindables import BindableInt
from osu.Framework.Bindables import BindableNumber
from osu.Framework.Graphics import Anchor
from osu.Framework.Graphics import Axes
from osu.Framework.Graphics import BlendingParameters
from osu.Framework.Graphics.Colour import ColourInfo
from osu.Framework.Graphics.Containers import CompositeDrawable
from osu.Framework.Graphics.Containers import Container
from osu.Framework.Graphics.Containers.Container import Enumerator
from osu.Framework.Graphics.Containers import IContainer
from osu.Framework.Graphics.Containers import IContainerCollection
from osu.Framework.Graphics.Containers import IContainerEnumerable
from osu.Framework.Graphics import DrawColourInfo
from osu.Framework.Graphics import DrawInfo
from osu.Framework.Graphics import Drawable
from osu.Framework.Graphics import Easing
from osu.Framework.Graphics.Effects import EdgeEffectParameters
from osu.Framework.Graphics.Effects import IEffect
from osu.Framework.Graphics import FillMode
from osu.Framework.Graphics import IDrawable
from osu.Framework.Graphics import ITexturedShaderDrawable
from osu.Framework.Graphics import Invalidation
from osu.Framework.Graphics import LoadState
from osu.Framework.Graphics import MarginPadding
from osu.Framework.Graphics.Primitives import Quad
from osu.Framework.Graphics.Primitives import RectangleF
from osu.Framework.Graphics import RotationDirection
from osu.Framework.Graphics.Shaders import IShader
from osu.Framework.Graphics.Sprites import IconUsage
from osu.Framework.Graphics.Sprites import Sprite
from osu.Framework.Graphics.Textures import Texture
from osu.Framework.Graphics.Transforms import ITransformable
from osu.Framework.Graphics.Transforms import Transform
from osu.Framework.Input.Events import UIEvent
from osu.Framework.Input import ISourceGeneratedHandleInputCache
from osu.Framework.Layout import InvalidationSource
from osu.Framework.Localisation import LocalisableString
from osu.Framework.Timing import FrameTimeInfo
from osu.Framework.Timing import IFrameBasedClock
from osu.Game.Beatmaps import Beatmap
from osu.Game.Beatmaps import BeatmapDifficulty
from osu.Game.Beatmaps import IBeatmap
from osu.Game.Configuration import OsuConfigManager
from osu.Game.Rulesets.Judgements import JudgementResult
from osu.Game.Rulesets.Mods import DifficultyBindable
from osu.Game.Rulesets.Mods import IApplicableAfterBeatmapConversion
from osu.Game.Rulesets.Mods import IApplicableFailOverride
from osu.Game.Rulesets.Mods import IApplicableHealthProcessor
from osu.Game.Rulesets.Mods import IApplicableMod
from osu.Game.Rulesets.Mods import IApplicableToAudio
from osu.Game.Rulesets.Mods import IApplicableToBeatmap
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
from osu.Game.Rulesets.Mods import IHasNoTimedInputs
from osu.Game.Rulesets.Mods import IHasSeed
from osu.Game.Rulesets.Mods import IMod
from osu.Game.Rulesets.Mods import IReadFromConfig
from osu.Game.Rulesets.Mods import IUpdatableByPlayfield
from osu.Game.Rulesets.Mods import Mod
from osu.Game.Rulesets.Mods import ModAccuracyChallenge
from osu.Game.Rulesets.Mods.ModAccuracyChallenge import AccuracyMode
from osu.Game.Rulesets.Mods import ModAutoplay
from osu.Game.Rulesets.Mods import ModBarrelRoll
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
from osu.Game.Rulesets.Mods import ModRandom
from osu.Game.Rulesets.Mods import ModRelax
from osu.Game.Rulesets.Mods import ModReplayData
from osu.Game.Rulesets.Mods import ModSuddenDeath
from osu.Game.Rulesets.Mods import ModSynesthesia
from osu.Game.Rulesets.Mods import ModTouchDevice
from osu.Game.Rulesets.Mods import ModType
from osu.Game.Rulesets.Mods import ModWithVisibilityAdjustment
from osu.Game.Rulesets.Objects.Drawables import DrawableHitObject
from osu.Game.Rulesets.Objects import HitObject
from osu.Game.Rulesets.Osu.Mods.OsuModApproachDifferent import AnimationStyle
from osu.Game.Rulesets.Osu.Mods.OsuModMirror import MirrorType
from osu.Game.Rulesets.Osu.Objects import OsuHitObject
from osu.Game.Rulesets.Osu.Objects.SliderTailCircle import TailJudgement
from osu.Game.Rulesets.Scoring import HealthProcessor
from osu.Game.Rulesets.Scoring import HitResult
from osu.Game.Rulesets.Scoring import ScoreProcessor
from osu.Game.Rulesets.UI import DrawableRuleset
from osu.Game.Rulesets.UI import Playfield
from osu.Game.Scoring import ScoreRank
from osu.Game.Screens.Play import HUDOverlay
from osu.Game.Screens.Play import Player
from osu.Game.Utils import IDeepCloneable
from osuTK import Vector2
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Iterator
from typing import Optional
from typing import TypeVar
from typing import overload
T = TypeVar("T")
class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...
class IHidesApproachCircles:
    """"""
class IRequiresApproachCircles:
    """"""
class InputBlockingMod(ABC, Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableRuleset[OsuHitObject], IMod, IUpdatableByPlayfield, IDeepCloneable[Mod]):
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
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[OsuHitObject]) -> None:
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
    def Update(self, playfield: Playfield) -> None:
        """
        
        :param playfield: 
        """
class OsuModAccuracyChallenge(ModAccuracyChallenge, IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToHealthProcessor, IApplicableToScoreProcessor, IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def AccuracyJudgeMode(self) -> Bindable[ModAccuracyChallenge.AccuracyMode]:
        """
        
        :return: 
        """
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
    def MinimumAccuracy(self) -> BindableNumber[float]:
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
    def AdjustRank(self, rank: ScoreRank, accuracy: float) -> ScoreRank:
        """
        
        :param rank: 
        :param accuracy: 
        :return: 
        """
    def ApplyToHealthProcessor(self, healthProcessor: HealthProcessor) -> None:
        """
        
        :param healthProcessor: 
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
    def PerformFail(self) -> bool:
        """
        
        :return: 
        """
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class OsuModAlternate(InputBlockingMod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableRuleset[OsuHitObject], IMod, IUpdatableByPlayfield, IDeepCloneable[Mod]):
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
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[OsuHitObject]) -> None:
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
    def Update(self, playfield: Playfield) -> None:
        """
        
        :param playfield: 
        """
class OsuModApproachDifferent(Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableHitObject, IMod, IRequiresApproachCircles, IDeepCloneable[Mod]):
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
    def Scale(self) -> BindableFloat:
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
    def Style(self) -> Bindable[OsuModApproachDifferent.AnimationStyle]:
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
    def ApplyToDrawableHitObject(self, drawable: DrawableHitObject) -> None:
        """
        
        :param drawable: 
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
    class AnimationStyle(Enum):
        """"""
        Linear: AnimationStyle = ...
        """"""
        Gravity: AnimationStyle = ...
        """"""
        InOut1: AnimationStyle = ...
        """"""
        InOut2: AnimationStyle = ...
        """"""
        Accelerate1: AnimationStyle = ...
        """"""
        Accelerate2: AnimationStyle = ...
        """"""
        Accelerate3: AnimationStyle = ...
        """"""
        Decelerate1: AnimationStyle = ...
        """"""
        Decelerate2: AnimationStyle = ...
        """"""
        Decelerate3: AnimationStyle = ...
        """"""
class OsuModAutopilot(Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableRuleset[OsuHitObject], IMod, IUpdatableByPlayfield, IDeepCloneable[Mod]):
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
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[OsuHitObject]) -> None:
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
    def Update(self, playfield: Playfield) -> None:
        """
        
        :param playfield: 
        """
class OsuModAutoplay(ModAutoplay, IEquatable[IMod], IEquatable[Mod], ICreateReplayData, IMod, IDeepCloneable[Mod]):
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
class OsuModBarrelRoll(ModBarrelRoll[OsuHitObject], IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableHitObject, IApplicableToDrawableRuleset[OsuHitObject], IMod, IUpdatableByPlayfield, IDeepCloneable[Mod]):
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
    def Direction(self) -> Bindable[RotationDirection]:
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
    def SpinSpeed(self) -> BindableNumber[float]:
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
    def ApplyToDrawableHitObject(self, d: DrawableHitObject) -> None:
        """
        
        :param drawable: 
        """
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[OsuHitObject]) -> None:
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
    def Update(self, playfield: Playfield) -> None:
        """
        
        :param playfield: 
        """
class OsuModBlinds(Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableRuleset[OsuHitObject], IApplicableToHealthProcessor, IMod, IDeepCloneable[Mod]):
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
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[OsuHitObject]) -> None:
        """
        
        :param drawableRuleset: 
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
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    class DrawableOsuBlinds(Container, ICollection[Drawable], IEnumerable[Drawable], IReadOnlyCollection[Drawable], IReadOnlyList[Drawable], IEnumerable, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, IContainer, IContainerCollection[Drawable], IContainerEnumerable[Drawable], ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
        """"""
        Name: Final[str] = ...
        """"""
        ProcessCustomClock: Final[bool] = ...
        """"""
        def __init__(self, restrictTo: CompositeDrawable, beatmap: Beatmap[OsuHitObject]):
            """"""
        @property
        def AcceptsFocus(self) -> bool:
            """"""
        @property
        def AliveChildren(self) -> IReadOnlyList[Drawable]:
            """"""
        @property
        def Alpha(self) -> float:
            """"""
        @Alpha.setter
        def Alpha(self, value: float) -> None: ...
        @property
        def AlwaysPresent(self) -> bool:
            """"""
        @AlwaysPresent.setter
        def AlwaysPresent(self, value: bool) -> None: ...
        @property
        def Anchor(self) -> Anchor:
            """"""
        @Anchor.setter
        def Anchor(self, value: Anchor) -> None: ...
        @property
        def AnchorPosition(self) -> Vector2:
            """"""
        @property
        def AutoSizeAxes(self) -> Axes:
            """"""
        @AutoSizeAxes.setter
        def AutoSizeAxes(self, value: Axes) -> None: ...
        @property
        def AutoSizeDuration(self) -> float:
            """"""
        @AutoSizeDuration.setter
        def AutoSizeDuration(self, value: float) -> None: ...
        @property
        def AutoSizeEasing(self) -> Easing:
            """"""
        @AutoSizeEasing.setter
        def AutoSizeEasing(self, value: Easing) -> None: ...
        @property
        def Blending(self) -> BlendingParameters:
            """"""
        @Blending.setter
        def Blending(self, value: BlendingParameters) -> None: ...
        @property
        def BorderColour(self) -> ColourInfo:
            """"""
        @BorderColour.setter
        def BorderColour(self, value: ColourInfo) -> None: ...
        @property
        def BorderThickness(self) -> float:
            """"""
        @BorderThickness.setter
        def BorderThickness(self, value: float) -> None: ...
        @property
        def BoundingBox(self) -> RectangleF:
            """"""
        @property
        def BypassAutoSizeAxes(self) -> Axes:
            """"""
        @BypassAutoSizeAxes.setter
        def BypassAutoSizeAxes(self, value: Axes) -> None: ...
        @property
        def ChangeFocusOnClick(self) -> bool:
            """"""
        @property
        def Child(self) -> Drawable:
            """"""
        @Child.setter
        def Child(self, value: Drawable) -> None: ...
        @property
        def ChildMaskingBounds(self) -> RectangleF:
            """"""
        @property
        def ChildOffset(self) -> Vector2:
            """"""
        @property
        def ChildSize(self) -> Vector2:
            """"""
        @property
        def Children(self) -> IReadOnlyList[Drawable]:
            """"""
        @Children.setter
        def Children(self, value: IReadOnlyList[Drawable]) -> None: ...
        @property
        def ChildrenEnumerable(self) -> IEnumerable[Drawable]:
            """"""
        @ChildrenEnumerable.setter
        def ChildrenEnumerable(self, value: IEnumerable[Drawable]) -> None: ...
        @property
        def Clock(self) -> IFrameBasedClock:
            """"""
        @Clock.setter
        def Clock(self, value: IFrameBasedClock) -> None: ...
        @property
        def Colour(self) -> ColourInfo:
            """"""
        @Colour.setter
        def Colour(self, value: ColourInfo) -> None: ...
        @property
        def CornerExponent(self) -> float:
            """"""
        @CornerExponent.setter
        def CornerExponent(self, value: float) -> None: ...
        @property
        def CornerRadius(self) -> float:
            """"""
        @CornerRadius.setter
        def CornerRadius(self, value: float) -> None: ...
        @property
        def Count(self) -> int:
            """"""
        @property
        def Dependencies(self) -> IReadOnlyDependencyContainer:
            """"""
        @property
        def Depth(self) -> float:
            """"""
        @Depth.setter
        def Depth(self, value: float) -> None: ...
        @property
        def DisposeOnDeathRemoval(self) -> bool:
            """"""
        @property
        def DragBlocksClick(self) -> bool:
            """"""
        @property
        def DrawColourInfo(self) -> DrawColourInfo:
            """"""
        @property
        def DrawHeight(self) -> float:
            """"""
        @property
        def DrawInfo(self) -> DrawInfo:
            """"""
        @property
        def DrawPosition(self) -> Vector2:
            """"""
        @property
        def DrawRectangle(self) -> RectangleF:
            """"""
        @property
        def DrawSize(self) -> Vector2:
            """"""
        @property
        def DrawWidth(self) -> float:
            """"""
        @property
        def EdgeEffect(self) -> EdgeEffectParameters:
            """"""
        @EdgeEffect.setter
        def EdgeEffect(self, value: EdgeEffectParameters) -> None: ...
        @property
        def FillAspectRatio(self) -> float:
            """"""
        @FillAspectRatio.setter
        def FillAspectRatio(self, value: float) -> None: ...
        @property
        def FillMode(self) -> FillMode:
            """"""
        @FillMode.setter
        def FillMode(self, value: FillMode) -> None: ...
        @property
        def ForceLocalVertexBatch(self) -> bool:
            """"""
        @ForceLocalVertexBatch.setter
        def ForceLocalVertexBatch(self, value: bool) -> None: ...
        @property
        def HandleNonPositionalInput(self) -> bool:
            """"""
        @property
        def HandlePositionalInput(self) -> bool:
            """"""
        @property
        def HasFocus(self) -> bool:
            """"""
        @property
        def HasProxy(self) -> bool:
            """"""
        @property
        def Height(self) -> float:
            """"""
        @Height.setter
        def Height(self, value: float) -> None: ...
        @property
        def InvalidationFromParentSize(self) -> Invalidation:
            """"""
        @property
        def InvalidationID(self) -> int:
            """"""
        @property
        def IsAlive(self) -> bool:
            """"""
        @property
        def IsDragged(self) -> bool:
            """"""
        @property
        def IsHovered(self) -> bool:
            """"""
        @property
        def IsLoaded(self) -> bool:
            """"""
        @property
        def IsPresent(self) -> bool:
            """"""
        @property
        def IsProxy(self) -> bool:
            """"""
        @property
        def IsReadOnly(self) -> bool:
            """"""
        @property
        def LatestTransformEndTime(self) -> float:
            """"""
        @property
        def LayoutRectangle(self) -> RectangleF:
            """"""
        @property
        def LayoutSize(self) -> Vector2:
            """"""
        @property
        def LifetimeEnd(self) -> float:
            """"""
        @LifetimeEnd.setter
        def LifetimeEnd(self, value: float) -> None: ...
        @property
        def LifetimeStart(self) -> float:
            """"""
        @LifetimeStart.setter
        def LifetimeStart(self, value: float) -> None: ...
        @property
        def LoadState(self) -> LoadState:
            """"""
        @property
        def Margin(self) -> MarginPadding:
            """"""
        @Margin.setter
        def Margin(self, value: MarginPadding) -> None: ...
        @property
        def Masking(self) -> bool:
            """"""
        @Masking.setter
        def Masking(self, value: bool) -> None: ...
        @property
        def MaskingSmoothness(self) -> float:
            """"""
        @MaskingSmoothness.setter
        def MaskingSmoothness(self, value: float) -> None: ...
        @property
        def Origin(self) -> Anchor:
            """"""
        @Origin.setter
        def Origin(self, value: Anchor) -> None: ...
        @property
        def OriginPosition(self) -> Vector2:
            """"""
        @OriginPosition.setter
        def OriginPosition(self, value: Vector2) -> None: ...
        @property
        def Padding(self) -> MarginPadding:
            """"""
        @Padding.setter
        def Padding(self, value: MarginPadding) -> None: ...
        @property
        def Parent(self) -> CompositeDrawable:
            """"""
        @property
        def Position(self) -> Vector2:
            """"""
        @Position.setter
        def Position(self, value: Vector2) -> None: ...
        @property
        def PropagateNonPositionalInputSubTree(self) -> bool:
            """"""
        @property
        def PropagatePositionalInputSubTree(self) -> bool:
            """"""
        @property
        def RelativeAnchorPosition(self) -> Vector2:
            """"""
        @RelativeAnchorPosition.setter
        def RelativeAnchorPosition(self, value: Vector2) -> None: ...
        @property
        def RelativeChildOffset(self) -> Vector2:
            """"""
        @RelativeChildOffset.setter
        def RelativeChildOffset(self, value: Vector2) -> None: ...
        @property
        def RelativeChildSize(self) -> Vector2:
            """"""
        @RelativeChildSize.setter
        def RelativeChildSize(self, value: Vector2) -> None: ...
        @property
        def RelativeOriginPosition(self) -> Vector2:
            """"""
        @property
        def RelativePositionAxes(self) -> Axes:
            """"""
        @RelativePositionAxes.setter
        def RelativePositionAxes(self, value: Axes) -> None: ...
        @property
        def RelativeSizeAxes(self) -> Axes:
            """"""
        @RelativeSizeAxes.setter
        def RelativeSizeAxes(self, value: Axes) -> None: ...
        @property
        def RelativeToAbsoluteFactor(self) -> Vector2:
            """"""
        @property
        def RemoveCompletedTransforms(self) -> bool:
            """"""
        @property
        def RemoveWhenNotAlive(self) -> bool:
            """"""
        @property
        def RequestsFocus(self) -> bool:
            """"""
        @property
        def Rotation(self) -> float:
            """"""
        @Rotation.setter
        def Rotation(self, value: float) -> None: ...
        @property
        def Scale(self) -> Vector2:
            """"""
        @Scale.setter
        def Scale(self, value: Vector2) -> None: ...
        @property
        def ScreenSpaceDrawQuad(self) -> Quad:
            """"""
        @property
        def Shear(self) -> Vector2:
            """"""
        @Shear.setter
        def Shear(self, value: Vector2) -> None: ...
        @property
        def Size(self) -> Vector2:
            """"""
        @Size.setter
        def Size(self, value: Vector2) -> None: ...
        @property
        def Time(self) -> FrameTimeInfo:
            """"""
        @property
        def TransformStartTime(self) -> float:
            """"""
        @property
        def Transforms(self) -> IEnumerable[Transform]:
            """"""
        @property
        def Width(self) -> float:
            """"""
        @Width.setter
        def Width(self, value: float) -> None: ...
        @property
        def X(self) -> float:
            """"""
        @X.setter
        def X(self, value: float) -> None: ...
        @property
        def Y(self) -> float:
            """"""
        @Y.setter
        def Y(self, value: float) -> None: ...
        def Add(self, drawable: Drawable) -> None:
            """"""
        def AddRange(self, range: IEnumerable[Drawable]) -> None:
            """"""
        def AddTransform(self, transform: Transform, customTransformID: Optional[int] = ...) -> None:
            """"""
        def AnimateClosedness(self, value: float) -> None:
            """"""
        def ApplyTransformsAt(self, time: float, propagateChildren: bool = ...) -> None:
            """"""
        def BeginAbsoluteSequence(self, newTransformStartTime: float, recursive: bool = ...) -> IDisposable:
            """"""
        def BeginDelayedSequence(self, delay: float, recursive: bool = ...) -> IDisposable:
            """"""
        def ChangeChildDepth(self, child: Drawable, newDepth: float) -> None:
            """"""
        @overload
        def Clear(self) -> None:
            """"""
        @overload
        def Clear(self, disposeChildren: bool) -> None:
            """"""
        def ClearTransforms(self, propagateChildren: bool = ..., targetMember: str = ...) -> None:
            """"""
        def ClearTransformsAfter(self, time: float, propagateChildren: bool = ..., targetMember: str = ...) -> None:
            """"""
        def ComputeMaskingBounds(self) -> RectangleF:
            """"""
        @overload
        def Contains(self, drawable: Drawable) -> bool:
            """"""
        @overload
        def Contains(self, screenSpacePos: Vector2) -> bool:
            """"""
        def CopyTo(self, array: Array[Drawable], arrayIndex: int) -> None:
            """"""
        def CreateProxy(self) -> Drawable:
            """"""
        def Dispose(self) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def Expire(self, calculateLifetimeStart: bool = ...) -> None:
            """"""
        def FinishTransforms(self, propagateChildren: bool = ..., targetMember: str = ...) -> None:
            """"""
        def GetEnumerator(self) -> Container.Enumerator[Drawable]:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def Hide(self) -> None:
            """"""
        def IndexOf(self, drawable: Drawable) -> int:
            """"""
        def Invalidate(self, invalidation: Invalidation = ..., source: InvalidationSource = ...) -> bool:
            """"""
        def ReceivePositionalInputAt(self, screenSpacePos: Vector2) -> bool:
            """"""
        def RegisterForDependencyActivation(self, registry: IDependencyActivatorRegistry) -> None:
            """"""
        @overload
        def Remove(self, item: Drawable) -> bool:
            """"""
        @overload
        def Remove(self, drawable: Drawable, disposeImmediately: bool) -> bool:
            """"""
        def RemoveAll(self, pred: Predicate[Drawable], disposeImmediately: bool) -> int:
            """"""
        def RemoveRange(self, range: IEnumerable[Drawable], disposeImmediately: bool) -> None:
            """"""
        def RemoveTransform(self, toRemove: Transform) -> None:
            """"""
        def Show(self) -> None:
            """"""
        @overload
        def ToLocalSpace(self, screenSpaceQuad: Quad) -> Quad:
            """"""
        @overload
        def ToLocalSpace(self, screenSpacePos: Vector2) -> Vector2:
            """"""
        @overload
        def ToParentSpace(self, input: RectangleF) -> Quad:
            """"""
        @overload
        def ToParentSpace(self, input: Vector2) -> Vector2:
            """"""
        @overload
        def ToScreenSpace(self, input: RectangleF) -> Quad:
            """"""
        @overload
        def ToScreenSpace(self, input: Vector2) -> Vector2:
            """"""
        @overload
        def ToSpaceOfOtherDrawable(self, input: RectangleF, other: IDrawable) -> Quad:
            """"""
        @overload
        def ToSpaceOfOtherDrawable(self, input: Vector2, other: IDrawable) -> Vector2:
            """"""
        def ToString(self) -> str:
            """"""
        def TransformsForTargetMember(self, targetMember: str) -> IEnumerable[Transform]:
            """"""
        def TriggerClick(self) -> bool:
            """"""
        def TriggerEvent(self, e: UIEvent) -> bool:
            """"""
        def UpdateSubTree(self) -> bool:
            """"""
        def UpdateSubTreeMasking(self) -> bool:
            """"""
        def WithEffect(self, effect: IEffect[T], initializationAction: Action[T] = ...) -> T:
            """"""
        @overload
        def __contains__(self, drawable: Drawable) -> bool:
            """"""
        @overload
        def __contains__(self, screenSpacePos: Vector2) -> bool:
            """"""
        @overload
        def __delitem__(self, item: Drawable) -> bool:
            """"""
        @overload
        def __delitem__(self, drawable: Drawable, disposeImmediately: bool) -> bool:
            """"""
        def __getitem__(self, index: int) -> Drawable:
            """"""
        def __iter__(self) -> Iterator[Drawable]:
            """"""
        def __len__(self) -> int:
            """"""
        OnLoadComplete: EventType[Action[Drawable]] = ...
        """"""
        OnUpdate: EventType[Action[Drawable]] = ...
        """"""
        class ModBlindsPanel(Sprite, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ITexturedShaderDrawable, ISourceGeneratedHandleInputCache):
            """"""
            Name: Final[str] = ...
            """"""
            ProcessCustomClock: Final[bool] = ...
            """"""
            def __init__(self):
                """"""
            @property
            def AcceptsFocus(self) -> bool:
                """"""
            @property
            def Alpha(self) -> float:
                """"""
            @Alpha.setter
            def Alpha(self, value: float) -> None: ...
            @property
            def AlwaysPresent(self) -> bool:
                """"""
            @AlwaysPresent.setter
            def AlwaysPresent(self, value: bool) -> None: ...
            @property
            def Anchor(self) -> Anchor:
                """"""
            @Anchor.setter
            def Anchor(self, value: Anchor) -> None: ...
            @property
            def AnchorPosition(self) -> Vector2:
                """"""
            @property
            def Blending(self) -> BlendingParameters:
                """"""
            @Blending.setter
            def Blending(self, value: BlendingParameters) -> None: ...
            @property
            def BoundingBox(self) -> RectangleF:
                """"""
            @property
            def BypassAutoSizeAxes(self) -> Axes:
                """"""
            @BypassAutoSizeAxes.setter
            def BypassAutoSizeAxes(self, value: Axes) -> None: ...
            @property
            def ChangeFocusOnClick(self) -> bool:
                """"""
            @property
            def Clock(self) -> IFrameBasedClock:
                """"""
            @Clock.setter
            def Clock(self, value: IFrameBasedClock) -> None: ...
            @property
            def Colour(self) -> ColourInfo:
                """"""
            @Colour.setter
            def Colour(self, value: ColourInfo) -> None: ...
            @property
            def ConservativeScreenSpaceDrawQuad(self) -> Quad:
                """"""
            @property
            def Depth(self) -> float:
                """"""
            @Depth.setter
            def Depth(self, value: float) -> None: ...
            @property
            def DisposeOnDeathRemoval(self) -> bool:
                """"""
            @property
            def DragBlocksClick(self) -> bool:
                """"""
            @property
            def DrawColourInfo(self) -> DrawColourInfo:
                """"""
            @property
            def DrawHeight(self) -> float:
                """"""
            @property
            def DrawInfo(self) -> DrawInfo:
                """"""
            @property
            def DrawPosition(self) -> Vector2:
                """"""
            @property
            def DrawRectangle(self) -> RectangleF:
                """"""
            @property
            def DrawSize(self) -> Vector2:
                """"""
            @property
            def DrawTextureRectangle(self) -> RectangleF:
                """"""
            @property
            def DrawWidth(self) -> float:
                """"""
            @property
            def EdgeSmoothness(self) -> Vector2:
                """"""
            @EdgeSmoothness.setter
            def EdgeSmoothness(self, value: Vector2) -> None: ...
            @property
            def FillAspectRatio(self) -> float:
                """"""
            @FillAspectRatio.setter
            def FillAspectRatio(self, value: float) -> None: ...
            @property
            def FillMode(self) -> FillMode:
                """"""
            @FillMode.setter
            def FillMode(self, value: FillMode) -> None: ...
            @property
            def HandleNonPositionalInput(self) -> bool:
                """"""
            @property
            def HandlePositionalInput(self) -> bool:
                """"""
            @property
            def HasFocus(self) -> bool:
                """"""
            @property
            def HasProxy(self) -> bool:
                """"""
            @property
            def Height(self) -> float:
                """"""
            @Height.setter
            def Height(self, value: float) -> None: ...
            @property
            def InflationAmount(self) -> Vector2:
                """"""
            @property
            def InvalidationFromParentSize(self) -> Invalidation:
                """"""
            @property
            def InvalidationID(self) -> int:
                """"""
            @property
            def IsAlive(self) -> bool:
                """"""
            @property
            def IsDragged(self) -> bool:
                """"""
            @property
            def IsHovered(self) -> bool:
                """"""
            @property
            def IsLoaded(self) -> bool:
                """"""
            @property
            def IsPresent(self) -> bool:
                """"""
            @property
            def IsProxy(self) -> bool:
                """"""
            @property
            def LatestTransformEndTime(self) -> float:
                """"""
            @property
            def LayoutRectangle(self) -> RectangleF:
                """"""
            @property
            def LayoutSize(self) -> Vector2:
                """"""
            @property
            def LifetimeEnd(self) -> float:
                """"""
            @LifetimeEnd.setter
            def LifetimeEnd(self, value: float) -> None: ...
            @property
            def LifetimeStart(self) -> float:
                """"""
            @LifetimeStart.setter
            def LifetimeStart(self, value: float) -> None: ...
            @property
            def LoadState(self) -> LoadState:
                """"""
            @property
            def Margin(self) -> MarginPadding:
                """"""
            @Margin.setter
            def Margin(self, value: MarginPadding) -> None: ...
            @property
            def Origin(self) -> Anchor:
                """"""
            @Origin.setter
            def Origin(self, value: Anchor) -> None: ...
            @property
            def OriginPosition(self) -> Vector2:
                """"""
            @OriginPosition.setter
            def OriginPosition(self, value: Vector2) -> None: ...
            @property
            def Parent(self) -> CompositeDrawable:
                """"""
            @property
            def Position(self) -> Vector2:
                """"""
            @Position.setter
            def Position(self, value: Vector2) -> None: ...
            @property
            def PropagateNonPositionalInputSubTree(self) -> bool:
                """"""
            @property
            def PropagatePositionalInputSubTree(self) -> bool:
                """"""
            @property
            def RelativeAnchorPosition(self) -> Vector2:
                """"""
            @RelativeAnchorPosition.setter
            def RelativeAnchorPosition(self, value: Vector2) -> None: ...
            @property
            def RelativeOriginPosition(self) -> Vector2:
                """"""
            @property
            def RelativePositionAxes(self) -> Axes:
                """"""
            @RelativePositionAxes.setter
            def RelativePositionAxes(self, value: Axes) -> None: ...
            @property
            def RelativeSizeAxes(self) -> Axes:
                """"""
            @RelativeSizeAxes.setter
            def RelativeSizeAxes(self, value: Axes) -> None: ...
            @property
            def RemoveCompletedTransforms(self) -> bool:
                """"""
            @property
            def RemoveWhenNotAlive(self) -> bool:
                """"""
            @property
            def RequestsFocus(self) -> bool:
                """"""
            @property
            def Rotation(self) -> float:
                """"""
            @Rotation.setter
            def Rotation(self, value: float) -> None: ...
            @property
            def Scale(self) -> Vector2:
                """"""
            @Scale.setter
            def Scale(self, value: Vector2) -> None: ...
            @property
            def ScreenSpaceDrawQuad(self) -> Quad:
                """"""
            @property
            def Shear(self) -> Vector2:
                """"""
            @Shear.setter
            def Shear(self, value: Vector2) -> None: ...
            @property
            def Size(self) -> Vector2:
                """"""
            @Size.setter
            def Size(self, value: Vector2) -> None: ...
            @property
            def Texture(self) -> Texture:
                """"""
            @Texture.setter
            def Texture(self, value: Texture) -> None: ...
            @property
            def TextureRectangle(self) -> RectangleF:
                """"""
            @TextureRectangle.setter
            def TextureRectangle(self, value: RectangleF) -> None: ...
            @property
            def TextureRelativeSizeAxes(self) -> Axes:
                """"""
            @TextureRelativeSizeAxes.setter
            def TextureRelativeSizeAxes(self, value: Axes) -> None: ...
            @property
            def TextureShader(self) -> IShader:
                """"""
            @property
            def Time(self) -> FrameTimeInfo:
                """"""
            @property
            def TransformStartTime(self) -> float:
                """"""
            @property
            def Transforms(self) -> IEnumerable[Transform]:
                """"""
            @property
            def Width(self) -> float:
                """"""
            @Width.setter
            def Width(self, value: float) -> None: ...
            @property
            def X(self) -> float:
                """"""
            @X.setter
            def X(self, value: float) -> None: ...
            @property
            def Y(self) -> float:
                """"""
            @Y.setter
            def Y(self, value: float) -> None: ...
            def AddTransform(self, transform: Transform, customTransformID: Optional[int] = ...) -> None:
                """"""
            def ApplyTransformsAt(self, time: float, propagateChildren: bool = ...) -> None:
                """"""
            def BeginAbsoluteSequence(self, newTransformStartTime: float, recursive: bool = ...) -> IDisposable:
                """"""
            def BeginDelayedSequence(self, delay: float, recursive: bool = ...) -> IDisposable:
                """"""
            def ClearTransforms(self, propagateChildren: bool = ..., targetMember: str = ...) -> None:
                """"""
            def ClearTransformsAfter(self, time: float, propagateChildren: bool = ..., targetMember: str = ...) -> None:
                """"""
            def ComputeMaskingBounds(self) -> RectangleF:
                """"""
            def Contains(self, screenSpacePos: Vector2) -> bool:
                """"""
            def CreateProxy(self) -> Drawable:
                """"""
            def Dispose(self) -> None:
                """"""
            def Equals(self, obj: object) -> bool:
                """"""
            def Expire(self, calculateLifetimeStart: bool = ...) -> None:
                """"""
            def FinishTransforms(self, propagateChildren: bool = ..., targetMember: str = ...) -> None:
                """"""
            def GetHashCode(self) -> int:
                """"""
            def GetType(self) -> Type:
                """"""
            def Hide(self) -> None:
                """"""
            def Invalidate(self, invalidation: Invalidation = ..., source: InvalidationSource = ...) -> bool:
                """"""
            def ReceivePositionalInputAt(self, screenSpacePos: Vector2) -> bool:
                """"""
            def RegisterForDependencyActivation(self, registry: IDependencyActivatorRegistry) -> None:
                """"""
            def RemoveTransform(self, toRemove: Transform) -> None:
                """"""
            def Show(self) -> None:
                """"""
            @overload
            def ToLocalSpace(self, screenSpaceQuad: Quad) -> Quad:
                """"""
            @overload
            def ToLocalSpace(self, screenSpacePos: Vector2) -> Vector2:
                """"""
            @overload
            def ToParentSpace(self, input: RectangleF) -> Quad:
                """"""
            @overload
            def ToParentSpace(self, input: Vector2) -> Vector2:
                """"""
            @overload
            def ToScreenSpace(self, input: RectangleF) -> Quad:
                """"""
            @overload
            def ToScreenSpace(self, input: Vector2) -> Vector2:
                """"""
            @overload
            def ToSpaceOfOtherDrawable(self, input: RectangleF, other: IDrawable) -> Quad:
                """"""
            @overload
            def ToSpaceOfOtherDrawable(self, input: Vector2, other: IDrawable) -> Vector2:
                """"""
            def ToString(self) -> str:
                """"""
            def TransformsForTargetMember(self, targetMember: str) -> IEnumerable[Transform]:
                """"""
            def TriggerClick(self) -> bool:
                """"""
            def TriggerEvent(self, e: UIEvent) -> bool:
                """"""
            def UpdateSubTree(self) -> bool:
                """"""
            def UpdateSubTreeMasking(self) -> bool:
                """"""
            def WithEffect(self, effect: IEffect[T], initializationAction: Action[T] = ...) -> T:
                """"""
            def __contains__(self, screenSpacePos: Vector2) -> bool:
                """"""
            OnLoadComplete: EventType[Action[Drawable]] = ...
            """"""
            OnUpdate: EventType[Action[Drawable]] = ...
            """"""
class OsuModBloom(Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToPlayer, IApplicableToScoreProcessor, IMod, IUpdatableByPlayfield, IDeepCloneable[Mod]):
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
    def MaxCursorSize(self) -> BindableFloat:
        """
        
        :return: 
        """
    @property
    def MaxSizeComboCount(self) -> BindableInt:
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
class OsuModBubbles(Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableHitObject, IApplicableToDrawableRuleset[OsuHitObject], IApplicableToScoreProcessor, IMod, IDeepCloneable[Mod]):
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
    def ApplyToDrawableHitObject(self, drawableObject: DrawableHitObject) -> None:
        """
        
        :param drawable: 
        """
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[OsuHitObject]) -> None:
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
class OsuModCinema(ModCinema[OsuHitObject], IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToDrawableRuleset[OsuHitObject], IApplicableToHUD, IApplicableToPlayer, ICreateReplayData, IMod, IDeepCloneable[Mod]):
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
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[OsuHitObject]) -> None:
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
class OsuModClassic(ModClassic, IEquatable[IMod], IEquatable[Mod], IApplicableHealthProcessor, IApplicableMod, IApplicableToDrawableHitObject, IApplicableToDrawableRuleset[OsuHitObject], IApplicableToHitObject, IMod, IDeepCloneable[Mod]):
    """"""
    def __init__(self):
        """"""
    @property
    def Acronym(self) -> str:
        """
        
        :return: 
        """
    @property
    def AlwaysPlayTailSample(self) -> Bindable[bool]:
        """
        
        :return: 
        """
    @property
    def AlwaysValidForSubmission(self) -> bool:
        """
        
        :return: 
        """
    @property
    def ClassicHealth(self) -> Bindable[bool]:
        """
        
        :return: 
        """
    @property
    def ClassicNoteLock(self) -> Bindable[bool]:
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
    def FadeHitCircleEarly(self) -> Bindable[bool]:
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
    def NoSliderHeadAccuracy(self) -> Bindable[bool]:
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
    def ApplyToDrawableHitObject(self, obj: DrawableHitObject) -> None:
        """
        
        :param drawable: 
        """
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[OsuHitObject]) -> None:
        """
        
        :param drawableRuleset: 
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
    def CreateHealthProcessor(self, drainStartTime: float) -> HealthProcessor:
        """
        
        :param drainStartTime: 
        :return: 
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
class OsuModDaycore(ModDaycore, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToAudio, IApplicableToRate, IApplicableToSample, IApplicableToTrack, IMod, IDeepCloneable[Mod]):
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
class OsuModDeflate(OsuModObjectScaleTween, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IApplicableToDrawableHitObject, IMod, IReadFromConfig, IHidesApproachCircles, IDeepCloneable[Mod]):
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
    def StartScale(self) -> BindableNumber[float]:
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
    def ApplyToDrawableHitObject(self, dho: DrawableHitObject) -> None:
        """
        
        :param drawable: 
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
class OsuModDepth(ModWithVisibilityAdjustment, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IApplicableToDrawableHitObject, IApplicableToDrawableRuleset[OsuHitObject], IMod, IReadFromConfig, IUpdatableByPlayfield, IDeepCloneable[Mod]):
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
    def MaxDepth(self) -> BindableFloat:
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
    def ShowApproachCircles(self) -> BindableBool:
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
    def ApplyToDrawableHitObject(self, dho: DrawableHitObject) -> None:
        """
        
        :param drawable: 
        """
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[OsuHitObject]) -> None:
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
class OsuModDifficultyAdjust(ModDifficultyAdjust, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDifficulty, IMod, IDeepCloneable[Mod]):
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
class OsuModDoubleTime(ModDoubleTime, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToAudio, IApplicableToRate, IApplicableToSample, IApplicableToTrack, IMod, IDeepCloneable[Mod]):
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
class OsuModEasy(ModEasyWithExtraLives, IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToDifficulty, IApplicableToHealthProcessor, IMod, IDeepCloneable[Mod]):
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
class OsuModFlashlight(ModFlashlight[OsuHitObject], IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableHitObject, IApplicableToDrawableRuleset[OsuHitObject], IApplicableToScoreProcessor, IMod, IDeepCloneable[Mod]):
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
    def FollowDelay(self) -> BindableNumber[float]:
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
    def ApplyToDrawableHitObject(self, drawable: DrawableHitObject) -> None:
        """
        
        :param drawable: 
        """
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[OsuHitObject]) -> None:
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
class OsuModFreezeFrame(Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IApplicableToDrawableHitObject, IMod, IDeepCloneable[Mod]):
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
    def ApplyToDrawableHitObject(self, drawableObject: DrawableHitObject) -> None:
        """
        
        :param drawable: 
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
class OsuModGrow(OsuModObjectScaleTween, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IApplicableToDrawableHitObject, IMod, IReadFromConfig, IHidesApproachCircles, IDeepCloneable[Mod]):
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
    def StartScale(self) -> BindableNumber[float]:
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
    def ApplyToDrawableHitObject(self, dho: DrawableHitObject) -> None:
        """
        
        :param drawable: 
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
class OsuModHalfTime(ModHalfTime, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToAudio, IApplicableToRate, IApplicableToSample, IApplicableToTrack, IMod, IDeepCloneable[Mod]):
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
class OsuModHardRock(ModHardRock, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDifficulty, IApplicableToHitObject, IMod, IDeepCloneable[Mod]):
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
class OsuModHidden(ModHidden, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IApplicableToDrawableHitObject, IApplicableToScoreProcessor, IMod, IReadFromConfig, IHidesApproachCircles, IDeepCloneable[Mod]):
    """"""
    FADE_IN_DURATION_MULTIPLIER: Final[ClassVar[float]] = ...
    """
    
    :return: 
    """
    FADE_OUT_DURATION_MULTIPLIER: Final[ClassVar[float]] = ...
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
    def OnlyFadeApproachCircles(self) -> Bindable[bool]:
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
class OsuModMagnetised(Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableRuleset[OsuHitObject], IMod, IUpdatableByPlayfield, IDeepCloneable[Mod]):
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
    def AttractionStrength(self) -> BindableFloat:
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
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[OsuHitObject]) -> None:
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
    def Update(self, playfield: Playfield) -> None:
        """
        
        :param playfield: 
        """
class OsuModMirror(ModMirror, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToHitObject, IMod, IDeepCloneable[Mod]):
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
    def Reflection(self) -> Bindable[OsuModMirror.MirrorType]:
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
    class MirrorType(Enum):
        """"""
        Horizontal: MirrorType = ...
        """"""
        Vertical: MirrorType = ...
        """"""
        Both: MirrorType = ...
        """"""
class OsuModMuted(ModMuted[OsuHitObject], IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableRuleset[OsuHitObject], IApplicableToScoreProcessor, IApplicableToTrack, IMod, IDeepCloneable[Mod]):
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
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[OsuHitObject]) -> None:
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
class OsuModNightcore(ModNightcore[OsuHitObject], IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToAudio, IApplicableToDrawableRuleset[OsuHitObject], IApplicableToRate, IApplicableToSample, IApplicableToTrack, IMod, IDeepCloneable[Mod]):
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
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[OsuHitObject]) -> None:
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
class OsuModNoFail(ModNoFail, IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToHUD, IMod, IReadFromConfig, IDeepCloneable[Mod]):
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
class OsuModNoScope(ModNoScope, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IApplicableToPlayer, IApplicableToScoreProcessor, IMod, IUpdatableByPlayfield, IDeepCloneable[Mod]):
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
    def ApplyToBeatmap(self, beatmap: IBeatmap) -> None:
        """
        
        :param beatmap: 
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
class OsuModObjectScaleTween(ABC, ModWithVisibilityAdjustment, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IApplicableToDrawableHitObject, IMod, IReadFromConfig, IHidesApproachCircles, IDeepCloneable[Mod]):
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
    def StartScale(self) -> BindableNumber[float]:
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
    def ApplyToDrawableHitObject(self, dho: DrawableHitObject) -> None:
        """
        
        :param drawable: 
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
class OsuModPerfect(ModPerfect, IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToHealthProcessor, IMod, IDeepCloneable[Mod]):
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
class OsuModRandom(ModRandom, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IHasSeed, IMod, IDeepCloneable[Mod]):
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
    def AngleSharpness(self) -> BindableFloat:
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
class OsuModRelax(ModRelax, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableRuleset[OsuHitObject], IApplicableToPlayer, IHasNoTimedInputs, IMod, IUpdatableByPlayfield, IDeepCloneable[Mod]):
    """"""
    RELAX_LENIENCY: Final[ClassVar[float]] = ...
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
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[OsuHitObject]) -> None:
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
    def Update(self, playfield: Playfield) -> None:
        """
        
        :param playfield: 
        """
class OsuModRepel(Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableRuleset[OsuHitObject], IMod, IUpdatableByPlayfield, IDeepCloneable[Mod]):
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
    def RepulsionStrength(self) -> BindableFloat:
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
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[OsuHitObject]) -> None:
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
    def Update(self, playfield: Playfield) -> None:
        """
        
        :param playfield: 
        """
class OsuModSingleTap(InputBlockingMod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableRuleset[OsuHitObject], IMod, IUpdatableByPlayfield, IDeepCloneable[Mod]):
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
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[OsuHitObject]) -> None:
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
    def Update(self, playfield: Playfield) -> None:
        """
        
        :param playfield: 
        """
class OsuModSpinIn(ModWithVisibilityAdjustment, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IApplicableToDrawableHitObject, IMod, IReadFromConfig, IHidesApproachCircles, IDeepCloneable[Mod]):
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
    def ApplyToDrawableHitObject(self, dho: DrawableHitObject) -> None:
        """
        
        :param drawable: 
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
class OsuModSpunOut(Mod, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToDrawableHitObject, IMod, IDeepCloneable[Mod]):
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
    def ApplyToDrawableHitObject(self, hitObject: DrawableHitObject) -> None:
        """
        
        :param drawable: 
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
class OsuModStrictTracking(Mod, IEquatable[IMod], IEquatable[Mod], IApplicableAfterBeatmapConversion, IApplicableMod, IApplicableToDrawableHitObject, IApplicableToDrawableRuleset[OsuHitObject], IMod, IDeepCloneable[Mod]):
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
    def ApplyToDrawableHitObject(self, drawable: DrawableHitObject) -> None:
        """
        
        :param drawable: 
        """
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[OsuHitObject]) -> None:
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
    class StrictTrackingTailJudgement(SliderTailCircle.TailJudgement):
        """"""
        def __init__(self):
            """"""
        @property
        def MaxHealthIncrease(self) -> float:
            """
            
            :return: 
            """
        @property
        def MaxResult(self) -> HitResult:
            """
            
            :return: 
            """
        @property
        def MinResult(self) -> HitResult:
            """
            
            :return: 
            """
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def HealthIncreaseFor(self, result: JudgementResult) -> float:
            """
            
            :param result: 
            :return: 
            """
        def ToString(self) -> str:
            """"""
class OsuModSuddenDeath(ModSuddenDeath, IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToHealthProcessor, IMod, IDeepCloneable[Mod]):
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
    def FailOnSliderTail(self) -> BindableBool:
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
class OsuModSynesthesia(ModSynesthesia, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IApplicableToDrawableHitObject, IMod, IDeepCloneable[Mod]):
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
    def ApplyToDrawableHitObject(self, d: DrawableHitObject) -> None:
        """
        
        :param drawable: 
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
class OsuModTargetPractice(ModWithVisibilityAdjustment, IEquatable[IMod], IEquatable[Mod], IApplicableFailOverride, IApplicableMod, IApplicableToBeatmap, IApplicableToDifficulty, IApplicableToDrawableHitObject, IApplicableToDrawableRuleset[OsuHitObject], IApplicableToHealthProcessor, IHasSeed, IMod, IReadFromConfig, IHidesApproachCircles, IDeepCloneable[Mod]):
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
    def Metronome(self) -> Bindable[bool]:
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
    def ApplyToDifficulty(self, difficulty: BeatmapDifficulty) -> None:
        """
        
        :param difficulty: 
        """
    def ApplyToDrawableHitObject(self, dho: DrawableHitObject) -> None:
        """
        
        :param drawable: 
        """
    def ApplyToDrawableRuleset(self, drawableRuleset: DrawableRuleset[OsuHitObject]) -> None:
        """
        
        :param drawableRuleset: 
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
    def ReadFromConfig(self, config: OsuConfigManager) -> None:
        """
        
        :param config: 
        """
    def ResetSettingsToDefaults(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
class OsuModTouchDevice(ModTouchDevice, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IMod, IDeepCloneable[Mod]):
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
class OsuModTraceable(ModWithVisibilityAdjustment, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IApplicableToDrawableHitObject, IMod, IReadFromConfig, IRequiresApproachCircles, IDeepCloneable[Mod]):
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
    def ApplyToDrawableHitObject(self, dho: DrawableHitObject) -> None:
        """
        
        :param drawable: 
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
class OsuModTransform(ModWithVisibilityAdjustment, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IApplicableToDrawableHitObject, IMod, IReadFromConfig, IDeepCloneable[Mod]):
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
    def ApplyToDrawableHitObject(self, dho: DrawableHitObject) -> None:
        """
        
        :param drawable: 
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
class OsuModWiggle(ModWithVisibilityAdjustment, IEquatable[IMod], IEquatable[Mod], IApplicableMod, IApplicableToBeatmap, IApplicableToDrawableHitObject, IMod, IReadFromConfig, IDeepCloneable[Mod]):
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
    def Strength(self) -> BindableDouble:
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
    def ApplyToDrawableHitObject(self, dho: DrawableHitObject) -> None:
        """
        
        :param drawable: 
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