from System import Action
from System.Collections.Generic import ICollection
from System.Collections.Generic import IEnumerable
from System import DateTimeOffset
from System import Func
from System import Object
from System.Threading import CancellationToken
from System.Threading.Tasks import Task
from System import TimeSpan
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Framework.Graphics import Drawable
from osu.Framework.IO.Network import WebRequest
from osu.Framework.Localisation import LocalisableString
from osu.Framework.Localisation import LocalisationParameters
from osu.Framework.Platform import GameHost
from osu.Game.Beatmaps import IBeatmapInfo
from osu.Game.Beatmaps import IBeatmapSetInfo
from osu.Game.IO import IFileInfo
from osu.Game.Localisation import Language
from osu.Game.Online.API.Requests import Cursor
from osu.Game.Online.API.Requests.Responses import APIUser
from osu.Game.Rulesets import IRulesetInfo
from osu.Game.Scoring import IScoreInfo
from osu.Game.Screens.Play.Leaderboards import BeatmapLeaderboardScope
from osuTK import Vector2
from typing import Optional
from typing import Tuple
from typing import TypeVar
from typing import overload
T = TypeVar("T")
class CollectionExtensions(ABC, Object):
    """"""
    @classmethod
    def AddRange(cls, collection: ICollection[T], items: IEnumerable[T]) -> None:
        """
        
        :param collection: 
        :param items: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class DrawableExtensions(ABC, Object):
    """"""
    @classmethod
    def ApplyGameWideClock(cls, drawable: Drawable, host: GameHost) -> None:
        """
        
        :param drawable: 
        :param host: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ScreenSpaceDeltaToParentSpace(cls, drawable: Drawable, delta: Vector2) -> Vector2:
        """
        
        :param drawable: 
        :param delta: 
        :return: 
        """
    @classmethod
    def Shake(cls, target: Drawable, shakeDuration: float = ..., shakeMagnitude: float = ..., maximumLength: Optional[float] = ...) -> None:
        """
        
        :param target: 
        :param shakeDuration: 
        :param shakeMagnitude: 
        :param maximumLength: 
        """
    def ToString(self) -> str:
        """"""
class LanguageExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetLanguageFor(cls, frameworkLocale: str, localisationParameters: LocalisationParameters) -> Language:
        """
        
        :param frameworkLocale: 
        :param localisationParameters: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ToCultureCode(cls, language: Language) -> str:
        """
        
        :param language: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
    @classmethod
    def TryParseCultureCode(cls, cultureCode: str, language: Language) -> Tuple[bool, Language]:
        """
        
        :param cultureCode: 
        :param language: 
        :return: 
        """
class ModelExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetDisplayString(cls, model: object) -> str:
        """
        
        :param model: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetStoragePath(cls, fileInfo: IFileInfo) -> str:
        """
        
        :param fileInfo: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetValidFilename(cls, filename: str) -> str:
        """
        
        :param filename: 
        :return: 
        """
    @classmethod
    def IsLegacyRuleset(cls, ruleset: IRulesetInfo) -> bool:
        """
        
        :param ruleset: 
        :return: 
        """
    @classmethod
    @overload
    def MatchesOnlineID(cls, instance: IBeatmapInfo, other: IBeatmapInfo) -> bool:
        """
        
        :param instance: 
        :param other: 
        :return: 
        """
    @classmethod
    @overload
    def MatchesOnlineID(cls, instance: IBeatmapSetInfo, other: IBeatmapSetInfo) -> bool:
        """
        
        :param instance: 
        :param other: 
        :return: 
        """
    @classmethod
    @overload
    def MatchesOnlineID(cls, instance: APIUser, other: APIUser) -> bool:
        """
        
        :param instance: 
        :param other: 
        :return: 
        """
    @classmethod
    @overload
    def MatchesOnlineID(cls, instance: IRulesetInfo, other: IRulesetInfo) -> bool:
        """
        
        :param instance: 
        :param other: 
        :return: 
        """
    @classmethod
    @overload
    def MatchesOnlineID(cls, instance: IScoreInfo, other: IScoreInfo) -> bool:
        """
        
        :param instance: 
        :param other: 
        :return: 
        """
    @classmethod
    def RequiresSupporter(cls, scope: BeatmapLeaderboardScope, filterMods: bool) -> bool:
        """
        
        :param scope: 
        :param filterMods: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class NumberFormattingExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ToStandardFormattedString(cls, value: T, maxDecimalDigits: int, asPercentage: bool = ...) -> str:
        """
        
        :param value: 
        :param maxDecimalDigits: 
        :param asPercentage: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class StringDehumanizeExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ToCamelCase(cls, input: str) -> str:
        """
        
        :param input: 
        :return: 
        """
    @classmethod
    def ToKebabCase(cls, input: str) -> str:
        """
        
        :param input: 
        :return: 
        """
    @classmethod
    def ToPascalCase(cls, input: str) -> str:
        """
        
        :param input: 
        :return: 
        """
    @classmethod
    def ToSnakeCase(cls, input: str) -> str:
        """
        
        :param input: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class TaskExtensions(ABC, Object):
    """"""
    @classmethod
    @overload
    def ContinueWithSequential(cls, task: Task, action: Action, cancellationToken: CancellationToken = ...) -> Task:
        """
        
        :param task: 
        :param action: 
        :param cancellationToken: 
        :return: 
        """
    @classmethod
    @overload
    def ContinueWithSequential(cls, task: Task, continuationFunction: Func[Task], cancellationToken: CancellationToken = ...) -> Task:
        """
        
        :param task: 
        :param continuationFunction: 
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
class TimeDisplayExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def ToEditorFormattedString(cls, milliseconds: float) -> str:
        """
        
        :param milliseconds: 
        :return: 
        """
    @classmethod
    @overload
    def ToEditorFormattedString(cls, timeSpan: TimeSpan) -> str:
        """
        
        :param timeSpan: 
        :return: 
        """
    @classmethod
    @overload
    def ToFormattedDuration(cls, milliseconds: float) -> LocalisableString:
        """
        
        :param milliseconds: 
        :return: 
        """
    @classmethod
    @overload
    def ToFormattedDuration(cls, timeSpan: TimeSpan) -> LocalisableString:
        """
        
        :param timeSpan: 
        :return: 
        """
    @classmethod
    def ToShortRelativeTime(cls, time: DateTimeOffset, lowerCutoff: TimeSpan) -> str:
        """
        
        :param time: 
        :param lowerCutoff: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class TypeExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class WebRequestExtensions(ABC, Object):
    """"""
    @classmethod
    def AddCursor(cls, webRequest: WebRequest, cursor: Cursor) -> None:
        """
        
        :param webRequest: 
        :param cursor: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""