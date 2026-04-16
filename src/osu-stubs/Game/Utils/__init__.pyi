from __future__ import annotations

from abc import ABC
from typing import ClassVar, Final, Generic, Iterator, Optional, Tuple, TypeVar, overload

from Humanizer.Localisation import TimeUnit
from System import Action, Array, Attribute, DateTimeOffset, Decimal, Enum, Exception, Func, IDisposable, Object, String, TimeSpan, Type, ValueTuple, ValueType
from System.Collections import IDictionary, IEnumerable
from System.Collections.Generic import IComparer, IEnumerable, IEnumerator, IReadOnlyList, List
from System.IO import MemoryStream, Stream
from System.Reflection import MethodBase
from System.Runtime.Serialization import ISerializable, SerializationInfo, StreamingContext
from System.Threading import CancellationToken
from System.Threading.Tasks import Task
from TagLib import File
from osu.Framework.Bindables import IBindable
from osu.Framework.Graphics import Anchor, Colour4, Direction, Easing
from osu.Framework.Graphics.Primitives import Quad
from osu.Framework.Localisation import LocalisableString
from osu.Framework.Platform import Storage
from osu.Game.Online.API import APIMod
from osu.Game.Online.API.Requests.Responses import APIUser
from osu.Game.Online.Rooms import MatchType
from osu.Game.Screens import IOsuScreen
from osu.Game.Screens.Play import ILocalUserPlayInfo
from osu.Game.Utils.MobileUtils import Orientation
from osuTK import Vector2
from osuTK.Graphics import Color4

from osu.Game import OsuGame
from osu.Game.Rulesets import Ruleset
from osu.Game.Rulesets.Mods import Mod
from osu.Game.Rulesets.Objects.Types import IHasPosition

T = TypeVar("T")
TEasing = TypeVar("TEasing")


class BatteryInfo(ABC, Object):
    """"""

    @property
    def ChargeLevel(self) -> Optional[float]:
        """
        
        :return: 
        """

    @property
    def OnBattery(self) -> bool:
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


class BindableValueAccessor(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """"""

    def GetHashCode(self) -> int:
        """"""

    def GetType(self) -> Type:
        """"""

    @classmethod
    def GetValue(cls, bindable: IBindable) -> object:
        """
        
        :param bindable: 
        :return: 
        """

    @classmethod
    def SetValue(cls, bindable: IBindable, value: object) -> None:
        """
        
        :param bindable: 
        :param value: 
        """

    def ToString(self) -> str:
        """"""


class ColourUtils(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """"""

    def GetHashCode(self) -> int:
        """"""

    def GetType(self) -> Type:
        """"""

    @classmethod
    def SampleFromLinearGradient(cls, gradient: IReadOnlyList[ValueTuple, Color4], point: float) -> Color4:
        """"""

    def ToString(self) -> str:
        """"""


class FileUtils(ABC, Object):
    """"""

    @classmethod
    @overload
    def AttemptOperation(cls, action: Action, attempts: int = ..., throwOnFailure: bool = ...) -> bool:
        """
        
        :param action: 
        :param attempts: 
        :param throwOnFailure: 
        :return: 
        """

    @classmethod
    @overload
    def AttemptOperation(cls, action: Action[T], state: T, attempts: int = ..., throwOnFailure: bool = ...) -> bool:
        """
        
        :param action: 
        :param state: 
        :param attempts: 
        :param throwOnFailure: 
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


class FilesystemSanityCheckHelpers(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """"""

    def GetHashCode(self) -> int:
        """"""

    def GetType(self) -> Type:
        """"""

    @classmethod
    def IncursPathTraversalRisk(cls, path: str) -> bool:
        """
        
        :param path: 
        :return: 
        """

    @classmethod
    def IsSubDirectory(cls, parent: str, child: str) -> bool:
        """
        
        :param parent: 
        :param child: 
        :return: 
        """

    def ToString(self) -> str:
        """"""


class FormatUtils(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """"""

    @classmethod
    def FindPrecision(cls, d: Decimal) -> int:
        """
        
        :param d: 
        :return: 
        """

    @classmethod
    def FloorToDecimalDigits(cls, value: float, digits: int) -> float:
        """
        
        :param value: 
        :param digits: 
        :return: 
        """

    @classmethod
    def FormatAccuracy(cls, accuracy: float) -> LocalisableString:
        """
        
        :param accuracy: 
        :return: 
        """

    @classmethod
    def FormatRank(cls, rank: int) -> str:
        """
        
        :param rank: 
        :return: 
        """

    @classmethod
    def FormatStarRating(cls, starRating: float) -> LocalisableString:
        """
        
        :param starRating: 
        :return: 
        """

    def GetHashCode(self) -> int:
        """"""

    def GetType(self) -> Type:
        """"""

    @classmethod
    def RoundBPM(cls, baseBpm: float, rate: float = ...) -> int:
        """
        
        :param baseBpm: 
        :param rate: 
        :return: 
        """

    @classmethod
    def ToLocalisedMediumDate(cls, dateTime: DateTimeOffset) -> LocalisableString:
        """
        
        :param dateTime: 
        :return: 
        """

    def ToString(self) -> str:
        """"""


class GeometryUtils(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """"""

    @classmethod
    @overload
    def GetConvexHull(cls, hitObjects: IEnumerable[IHasPosition]) -> List[Vector2]:
        """
        
        :param hitObjects: 
        :return: 
        """

    @classmethod
    @overload
    def GetConvexHull(cls, points: IEnumerable[Vector2]) -> List[Vector2]:
        """
        
        :param points: 
        :return: 
        """

    @classmethod
    @overload
    def GetFlippedPosition(cls, direction: Direction, quad: Quad, position: Vector2) -> Vector2:
        """
        
        :param direction: 
        :param quad: 
        :param position: 
        :return: 
        """

    @classmethod
    @overload
    def GetFlippedPosition(cls, axis: Vector2, quad: Quad, position: Vector2) -> Vector2:
        """
        
        :param axis: 
        :param quad: 
        :param position: 
        :return: 
        """

    def GetHashCode(self) -> int:
        """"""

    @classmethod
    @overload
    def GetScaledPosition(cls, reference: Anchor, scale: Vector2, selectionQuad: Quad, position: Vector2) -> Vector2:
        """
        
        :param reference: 
        :param scale: 
        :param selectionQuad: 
        :param position: 
        :return: 
        """

    @classmethod
    @overload
    def GetScaledPosition(cls, scale: Vector2, origin: Vector2, position: Vector2, axisRotation: float = ...) -> Vector2:
        """
        
        :param scale: 
        :param origin: 
        :param position: 
        :param axisRotation: 
        :return: 
        """

    @classmethod
    @overload
    def GetSurroundingQuad(cls, points: IEnumerable[Vector2]) -> Quad:
        """
        
        :param points: 
        :return: 
        """

    @classmethod
    @overload
    def GetSurroundingQuad(cls, hitObjects: IEnumerable[IHasPosition], startAndEndOnly: bool = ...) -> Quad:
        """
        
        :param hitObjects: 
        :param startAndEndOnly: 
        :return: 
        """

    def GetType(self) -> Type:
        """"""

    @classmethod
    @overload
    def MinimumEnclosingCircle(cls, hitObjects: IEnumerable[IHasPosition]) -> ValueTuple[Vector2, float]:
        """
        
        :param hitObjects: 
        :return: 
        """

    @classmethod
    @overload
    def MinimumEnclosingCircle(cls, points: IEnumerable[Vector2]) -> ValueTuple[Vector2, float]:
        """
        
        :param points: 
        :return: 
        """

    @classmethod
    def RotatePointAroundOrigin(cls, point: Vector2, origin: Vector2, angle: float) -> Vector2:
        """
        
        :param point: 
        :param origin: 
        :param angle: 
        :return: 
        """

    @classmethod
    def RotateVector(cls, vector: Vector2, angle: float) -> Vector2:
        """
        
        :param vector: 
        :param angle: 
        :return: 
        """

    def ToString(self) -> str:
        """"""


class HumanizerUtils(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """"""

    def GetHashCode(self) -> int:
        """"""

    def GetType(self) -> Type:
        """"""

    @classmethod
    @overload
    def Humanize(cls, input: DateTimeOffset) -> str:
        """
        
        :param input: 
        :return: 
        """

    @classmethod
    @overload
    def Humanize(cls, input: TimeSpan, precision: int = ..., maxUnit: TimeUnit = ..., minUnit: TimeUnit = ..., toWords: bool = ...) -> str:
        """
        
        :param input: 
        :param precision: 
        :param maxUnit: 
        :param minUnit: 
        :param toWords: 
        :return: 
        """

    def ToString(self) -> str:
        """"""


class IDeepCloneable(Generic[T]):
    """"""

    def DeepClone(self) -> T:
        """
        
        :return: 
        """


class LegacyRandom(Object):
    """"""

    @overload
    def __init__(self):
        """"""

    @overload
    def __init__(self, seed: int):
        """
        
        :param seed: 
        """

    @property
    def W(self) -> int:
        """
        
        :return: 
        """

    @property
    def X(self) -> int:
        """
        
        :return: 
        """

    @property
    def Y(self) -> int:
        """
        
        :return: 
        """

    @property
    def Z(self) -> int:
        """
        
        :return: 
        """

    def Equals(self, obj: object) -> bool:
        """"""

    def GetHashCode(self) -> int:
        """"""

    def GetType(self) -> Type:
        """"""

    @overload
    def Next(self) -> int:
        """
        
        :return: 
        """

    @overload
    def Next(self, upperBound: int) -> int:
        """
        
        :param upperBound: 
        :return: 
        """

    @overload
    def Next(self, lowerBound: float, upperBound: float) -> int:
        """
        
        :param lowerBound: 
        :param upperBound: 
        :return: 
        """

    @overload
    def Next(self, lowerBound: int, upperBound: int) -> int:
        """
        
        :param lowerBound: 
        :param upperBound: 
        :return: 
        """

    def NextBool(self) -> bool:
        """
        
        :return: 
        """

    def NextDouble(self) -> float:
        """
        
        :return: 
        """

    def NextUInt(self) -> int:
        """
        
        :return: 
        """

    def ToString(self) -> str:
        """"""


class LegacyUtils(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """"""

    def GetHashCode(self) -> int:
        """"""

    def GetType(self) -> Type:
        """"""

    @classmethod
    @overload
    def InterpolateNonLinear(cls, time: float, startColour: Colour4, endColour: Colour4, startTime: float, endTime: float, easing: TEasing) -> Colour4:
        """
        
        :param time: 
        :param startColour: 
        :param endColour: 
        :param startTime: 
        :param endTime: 
        :param easing: 
        :return: 
        """

    @classmethod
    @overload
    def InterpolateNonLinear(cls, time: float, startColour: Colour4, endColour: Colour4, startTime: float, endTime: float, easing: Easing = ...) -> Colour4:
        """
        
        :param time: 
        :param startColour: 
        :param endColour: 
        :param startTime: 
        :param endTime: 
        :param easing: 
        :return: 
        """

    @classmethod
    @overload
    def InterpolateNonLinear(cls, time: float, startColour: Color4, endColour: Color4, startTime: float, endTime: float, easing: TEasing) -> Color4:
        """
        
        :param time: 
        :param startColour: 
        :param endColour: 
        :param startTime: 
        :param endTime: 
        :param easing: 
        :return: 
        """

    @classmethod
    @overload
    def InterpolateNonLinear(cls, time: float, startColour: Color4, endColour: Color4, startTime: float, endTime: float, easing: Easing = ...) -> Color4:
        """
        
        :param time: 
        :param startColour: 
        :param endColour: 
        :param startTime: 
        :param endTime: 
        :param easing: 
        :return: 
        """

    def ToString(self) -> str:
        """"""


class LimitedCapacityQueue(Generic[T], Object, IEnumerable[T], IEnumerable):
    """"""

    def __init__(self, capacity: int):
        """
        
        :param capacity: 
        """

    @property
    def Count(self) -> int:
        """
        
        :return: 
        """

    @property
    def Full(self) -> bool:
        """
        
        :return: 
        """

    def Clear(self) -> None:
        """"""

    def Dequeue(self) -> T:
        """
        
        :return: 
        """

    def Enqueue(self, item: T) -> None:
        """
        
        :param item: 
        """

    def Equals(self, obj: object) -> bool:
        """"""

    def GetEnumerator(self) -> IEnumerator[T]:
        """"""

    def GetHashCode(self) -> int:
        """"""

    def GetType(self) -> Type:
        """"""

    def ToString(self) -> str:
        """"""

    def __getitem__(self, index: int) -> T:
        """
        
        :param index: 
        :return: 
        """

    def __iter__(self) -> Iterator[T]:
        """"""

    def __len__(self) -> int:
        """
        
        :return: 
        """


class MobileUtils(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """"""

    def GetHashCode(self) -> int:
        """"""

    @classmethod
    def GetOrientation(cls, userPlayInfo: ILocalUserPlayInfo, currentScreen: IOsuScreen, isTablet: bool) -> MobileUtils.Orientation:
        """
        
        :param userPlayInfo: 
        :param currentScreen: 
        :param isTablet: 
        :return: 
        """

    def GetType(self) -> Type:
        """"""

    def ToString(self) -> str:
        """"""

    class Orientation(Enum):
        """"""
        Locked: Orientation = ...
        """"""
        Portrait: Orientation = ...
        """"""
        Default: Orientation = ...
        """"""


class ModUtils(ABC, Object):
    """"""

    @classmethod
    def CalculateRateWithMods(cls, mods: IEnumerable[Mod]) -> float:
        """
        
        :param mods: 
        :return: 
        """

    @classmethod
    def CheckAllowed(cls, combination: IEnumerable[Mod], allowedTypes: IEnumerable[Type]) -> bool:
        """
        
        :param combination: 
        :param allowedTypes: 
        :return: 
        """

    @classmethod
    @overload
    def CheckCompatibleSet(cls, combination: IEnumerable[Mod]) -> bool:
        """
        
        :param combination: 
        :return: 
        """

    @classmethod
    @overload
    def CheckCompatibleSet(cls, combination: IEnumerable[Mod], invalidMods: List[Mod]) -> Tuple[bool, List[Mod]]:
        """
        
        :param combination: 
        :param invalidMods: 
        :return: 
        """

    @classmethod
    def CheckCompatibleSetAndAllowed(cls, combination: IEnumerable[Mod], allowedTypes: IEnumerable[Type]) -> bool:
        """
        
        :param combination: 
        :param allowedTypes: 
        :return: 
        """

    @classmethod
    def CheckModsBelongToRuleset(cls, ruleset: Ruleset, proposedMods: IEnumerable[Mod]) -> bool:
        """
        
        :param ruleset: 
        :param proposedMods: 
        :return: 
        """

    @classmethod
    def CheckValidAllowedModsForMultiplayer(cls, mods: IEnumerable[Mod], freestyle: bool, invalidMods: List[Mod]) -> Tuple[bool, List[Mod]]:
        """
        
        :param mods: 
        :param freestyle: 
        :param invalidMods: 
        :return: 
        """

    @classmethod
    def CheckValidForGameplay(cls, mods: IEnumerable[Mod], invalidMods: List[Mod]) -> Tuple[bool, List[Mod]]:
        """
        
        :param mods: 
        :param invalidMods: 
        :return: 
        """

    @classmethod
    def CheckValidRequiredModsForMultiplayer(cls, mods: IEnumerable[Mod], freestyle: bool, invalidMods: List[Mod]) -> Tuple[bool, List[Mod]]:
        """
        
        :param mods: 
        :param freestyle: 
        :param invalidMods: 
        :return: 
        """

    @classmethod
    def EnumerateUserSelectableFreeMods(cls, matchType: MatchType, requiredMods: IEnumerable[APIMod], allowedMods: IEnumerable[APIMod], freestyle: bool, userRuleset: Ruleset) -> Array[Mod]:
        """
        
        :param matchType: 
        :param requiredMods: 
        :param allowedMods: 
        :param freestyle: 
        :param userRuleset: 
        :return: 
        """

    def Equals(self, obj: object) -> bool:
        """"""

    @classmethod
    def FlattenMod(cls, mod: Mod) -> IEnumerable[Mod]:
        """
        
        :param mod: 
        :return: 
        """

    @classmethod
    def FlattenMods(cls, mods: IEnumerable[Mod]) -> IEnumerable[Mod]:
        """
        
        :param mods: 
        :return: 
        """

    @classmethod
    def FormatScoreMultiplier(cls, scoreMultiplier: float) -> LocalisableString:
        """
        
        :param scoreMultiplier: 
        :return: 
        """

    def GetHashCode(self) -> int:
        """"""

    def GetType(self) -> Type:
        """"""

    @classmethod
    def InstantiateValidModsForRuleset(cls, ruleset: Ruleset, proposedMods: IEnumerable[APIMod], valid: List[Mod]) -> Tuple[bool, List[Mod]]:
        """
        
        :param ruleset: 
        :param proposedMods: 
        :param valid: 
        :return: 
        """

    @classmethod
    def IsValidModForMatch(cls, mod: Mod, required: bool, matchType: MatchType, freestyle: bool) -> bool:
        """
        
        :param mod: 
        :param required: 
        :param matchType: 
        :param freestyle: 
        :return: 
        """

    def ToString(self) -> str:
        """"""


class NamingUtils(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """"""

    def GetHashCode(self) -> int:
        """"""

    @classmethod
    def GetNextBestFilename(cls, existingFilenames: IEnumerable[str], desiredFilename: str) -> str:
        """
        
        :param existingFilenames: 
        :param desiredFilename: 
        :return: 
        """

    @classmethod
    def GetNextBestName(cls, existingNames: IEnumerable[str], desiredName: str) -> str:
        """
        
        :param existingNames: 
        :param desiredName: 
        :return: 
        """

    def GetType(self) -> Type:
        """"""

    def ToString(self) -> str:
        """"""


class OfficialBuildAttribute(Attribute):
    """"""

    def __init__(self):
        """"""

    @property
    def TypeId(self) -> object:
        """"""

    def Equals(self, obj: object) -> bool:
        """"""

    def GetHashCode(self) -> int:
        """"""

    def GetType(self) -> Type:
        """"""

    def IsDefaultAttribute(self) -> bool:
        """"""

    def Match(self, obj: object) -> bool:
        """"""

    def ToString(self) -> str:
        """"""


class Optional(Generic[T], ValueType):
    """"""
    HasValue: Final[bool] = ...
    """
    
    :return: 
    """
    Value: Final[T] = ...
    """
    
    :return: 
    """

    def __init__(self, value: T):
        """
        
        :param value: 
        """

    def Equals(self, obj: object) -> bool:
        """"""

    def GetHashCode(self) -> int:
        """"""

    def GetOr(self, fallback: T) -> T:
        """
        
        :param fallback: 
        :return: 
        """

    def GetType(self) -> Type:
        """"""

    def ToString(self) -> str:
        """"""

    @classmethod
    def op_Implicit(cls, value: T) -> Optional[T]:
        """
        
        :param value: 
        :return: 
        """


class OrdinalSortByCaseStringComparer(Object, IComparer[String]):
    """"""
    DEFAULT: Final[ClassVar[OrdinalSortByCaseStringComparer]] = ...
    """
    
    :return: 
    """

    def Compare(self, a: str, b: str) -> int:
        """"""

    def Equals(self, obj: object) -> bool:
        """"""

    def GetHashCode(self) -> int:
        """"""

    def GetType(self) -> Type:
        """"""

    def ToString(self) -> str:
        """"""


class Period(ValueType):
    """"""
    End: Final[float] = ...
    """
    
    :return: 
    """
    Start: Final[float] = ...
    """
    
    :return: 
    """

    def __init__(self, start: float, end: float):
        """
        
        :param start: 
        :param end: 
        """

    @property
    def Duration(self) -> float:
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


class PeriodTracker(Object):
    """"""

    def __init__(self, periods: IEnumerable[Period]):
        """
        
        :param periods: 
        """

    def Equals(self, obj: object) -> bool:
        """"""

    def GetHashCode(self) -> int:
        """"""

    def GetType(self) -> Type:
        """"""

    @overload
    def IsInAny(self, time: float) -> bool:
        """
        
        :param time: 
        :return: 
        """

    @overload
    def IsInAny(self, time: float, period: Optional[Period]) -> Tuple[bool, Optional[Period]]:
        """
        
        :param time: 
        :param period: 
        :return: 
        """

    def ToString(self) -> str:
        """"""


class SentryLogger(Object, IDisposable):
    """"""

    def __init__(self, game: OsuGame, storage: Storage = ...):
        """
        
        :param game: 
        :param storage: 
        """

    def AttachUser(self, user: IBindable[APIUser]) -> None:
        """
        
        :param user: 
        """

    def Dispose(self) -> None:
        """"""

    def Equals(self, obj: object) -> bool:
        """"""

    def GetHashCode(self) -> int:
        """"""

    def GetType(self) -> Type:
        """"""

    @classmethod
    def IsLocalUserConnectivityException(cls, exception: Exception) -> bool:
        """
        
        :param exception: 
        :return: 
        """

    def ToString(self) -> str:
        """"""


class SentryOnlyDiagnosticsException(Exception, ISerializable):
    """"""

    def __init__(self, message: str):
        """
        
        :param message: 
        """

    @property
    def Data(self) -> IDictionary:
        """"""

    @property
    def HResult(self) -> int:
        """"""

    @HResult.setter
    def HResult(self, value: int) -> None: ...

    @property
    def HelpLink(self) -> str:
        """"""

    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...

    @property
    def InnerException(self) -> Exception:
        """"""

    @property
    def Message(self) -> str:
        """"""

    @property
    def Source(self) -> str:
        """"""

    @Source.setter
    def Source(self, value: str) -> None: ...

    @property
    def StackTrace(self) -> str:
        """"""

    @property
    def TargetSite(self) -> MethodBase:
        """"""

    def Equals(self, obj: object) -> bool:
        """"""

    def GetBaseException(self) -> Exception:
        """"""

    def GetHashCode(self) -> int:
        """"""

    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""

    def GetType(self) -> Type:
        """"""

    def ToString(self) -> str:
        """"""


class StatelessRNG(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """"""

    def GetHashCode(self) -> int:
        """"""

    def GetType(self) -> Type:
        """"""

    @classmethod
    def NextInt(cls, maxValue: int, seed: int, series: int = ...) -> int:
        """
        
        :param maxValue: 
        :param seed: 
        :param series: 
        :return: 
        """

    @classmethod
    @overload
    def NextSingle(cls, seed: int, series: int = ...) -> float:
        """
        
        :param seed: 
        :param series: 
        :return: 
        """

    @classmethod
    @overload
    def NextSingle(cls, min: float, max: float, seed: int, series: int = ...) -> float:
        """
        
        :param min: 
        :param max: 
        :param seed: 
        :param series: 
        :return: 
        """

    @classmethod
    def NextULong(cls, seed: int, series: int = ...) -> int:
        """
        
        :param seed: 
        :param series: 
        :return: 
        """

    def ToString(self) -> str:
        """"""


class SupportedExtensions(ABC, Object):
    """"""
    ALL_EXTENSIONS: Final[ClassVar[Array[str]]] = ...
    """
    
    :return: 
    """
    AUDIO_EXTENSIONS: Final[ClassVar[Array[str]]] = ...
    """
    
    :return: 
    """
    IMAGE_EXTENSIONS: Final[ClassVar[Array[str]]] = ...
    """
    
    :return: 
    """
    VIDEO_EXTENSIONS: Final[ClassVar[Array[str]]] = ...
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


class TagLibUtils(Object):
    """"""

    def __init__(self):
        """"""

    def Equals(self, obj: object) -> bool:
        """"""

    def GetHashCode(self) -> int:
        """"""

    @classmethod
    @overload
    def GetTagLibFile(cls, filePath: str) -> File:
        """
        
        :param filePath: 
        :return: 
        """

    @classmethod
    @overload
    def GetTagLibFile(cls, filename: str, stream: Stream) -> File:
        """
        
        :param filename: 
        :param stream: 
        :return: 
        """

    def GetType(self) -> Type:
        """"""

    def ToString(self) -> str:
        """"""


class TaskChain(Object):
    """"""

    def __init__(self):
        """"""

    @overload
    def Add(self, action: Action, cancellationToken: CancellationToken = ...) -> Task:
        """
        
        :param action: 
        :param cancellationToken: 
        :return: 
        """

    @overload
    def Add(self, task: Func[Task], cancellationToken: CancellationToken = ...) -> Task:
        """
        
        :param task: 
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


class ZipUtils(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """"""

    def GetHashCode(self) -> int:
        """"""

    def GetType(self) -> Type:
        """"""

    @classmethod
    @overload
    def IsZipArchive(cls, stream: MemoryStream) -> bool:
        """
        
        :param stream: 
        :return: 
        """

    @classmethod
    @overload
    def IsZipArchive(cls, path: str) -> bool:
        """
        
        :param path: 
        :return: 
        """

    def ToString(self) -> str:
        """"""
