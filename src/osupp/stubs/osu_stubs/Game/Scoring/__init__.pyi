from Realms import DynamicObjectApi
from Realms import IRealmAccessor
from Realms import IRealmObject
from Realms import IRealmObjectBase
from Realms import ISettableManagedAccessor
from Realms import Realm
from Realms import RealmObject
from Realms.Schema import ObjectSchema
from Realms.Weaving import IRealmObjectHelper
from System import Action
from System import Array
from System.Collections.Generic import Dictionary
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IList
from System.Collections.Generic import List
from System.ComponentModel import INotifyPropertyChanged
from System.ComponentModel import PropertyChangedEventHandler
from System import DateTimeOffset
from System import Enum
from System import Func
from System import Guid
from System import IEquatable
from System.IO import Stream
from System import Int64
from System.Linq.Expressions import Expression
from System.Linq import IQueryable
from System import Object
from System.Reflection import IReflectableType
from System.Reflection import TypeInfo
from System.Threading import CancellationToken
from System.Threading.Tasks import Task
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Framework.Bindables import Bindable
from osu.Framework.IO.Stores import IResourceStore
from osu.Framework.Localisation import LocalisableString
from osu.Framework.Platform import Storage
from osu.Game.Beatmaps import BeatmapInfo
from osu.Game.Beatmaps import BeatmapManager
from osu.Game.Beatmaps import IBeatmapInfo
from osu.Game.Configuration import OsuConfigManager
from osu.Game.Database import ExternalEditOperation
from osu.Game.Database import ICanAcceptFiles
from osu.Game.Database import IHasGuidPrimaryKey
from osu.Game.Database import IHasNamedFiles
from osu.Game.Database import IHasOnlineID
from osu.Game.Database import IHasRealmFiles
from osu.Game.Database import IModelDownloader
from osu.Game.Database import IModelFileManager
from osu.Game.Database import IModelImporter
from osu.Game.Database import IModelManager
from osu.Game.Database import IPostNotifications
from osu.Game.Database import ISoftDelete
from osu.Game.Database import ImportParameters
from osu.Game.Database import ImportTask
from osu.Game.Database import Live
from osu.Game.Database import ModelDownloader
from osu.Game.Database import ModelManager
from osu.Game.Database import RealmAccess
from osu.Game.Database import RealmArchiveModelImporter
from osu.Game.IO.Archives import ArchiveReader
from osu.Game.Models import RealmNamedFileUsage
from osu.Game.Models import RealmUser
from osu.Game.Online.API import APIMod
from osu.Game.Online.API import ArchiveDownloadRequest
from osu.Game.Online.API import IAPIProvider
from osu.Game.Online.API.Requests.Responses import APIUser
from osu.Game.Overlays.Notifications import Notification
from osu.Game.Overlays.Notifications import ProgressNotification
from osu.Game.Replays import Replay
from osu.Game.Rulesets import IRulesetInfo
from osu.Game.Rulesets.Mods import Mod
from osu.Game.Rulesets import RulesetInfo
from osu.Game.Rulesets import RulesetStore
from osu.Game.Rulesets.Scoring import HitEvent
from osu.Game.Rulesets.Scoring import HitResult
from osu.Game.Screens.Select.Leaderboards import LeaderboardSortMode
from osu.Game.Users import IUser
from osu.Game.Utils import IDeepCloneable
from typing import Final
from typing import Generic
from typing import Optional
from typing import TypeVar
from typing import overload
T = TypeVar("T")
class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...
class HitResultDisplayStatistic(Object):
    """"""
    def __init__(self, result: HitResult, count: int, maxCount: Optional[int], displayName: LocalisableString):
        """
        
        :param result: 
        :param count: 
        :param maxCount: 
        :param displayName: 
        """
    @property
    def Count(self) -> int:
        """
        
        :return: 
        """
    @property
    def DisplayName(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def MaxCount(self) -> Optional[int]:
        """
        
        :return: 
        """
    @property
    def Result(self) -> HitResult:
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
    def __len__(self) -> int:
        """
        
        :return: 
        """
class IScoreInfo(IHasOnlineID[Int64]):
    """"""
    @property
    def Accuracy(self) -> float:
        """
        
        :return: 
        """
    @property
    def Beatmap(self) -> IBeatmapInfo:
        """
        
        :return: 
        """
    @property
    def Date(self) -> DateTimeOffset:
        """
        
        :return: 
        """
    @property
    def LegacyOnlineID(self) -> int:
        """
        
        :return: 
        """
    @property
    def MaxCombo(self) -> int:
        """
        
        :return: 
        """
    @property
    def OnlineID(self) -> int:
        """
        
        :return: 
        """
    @property
    def PP(self) -> Optional[float]:
        """
        
        :return: 
        """
    @property
    def Rank(self) -> ScoreRank:
        """
        
        :return: 
        """
    @property
    def Ruleset(self) -> IRulesetInfo:
        """
        
        :return: 
        """
    @property
    def TotalScore(self) -> int:
        """
        
        :return: 
        """
    @property
    def User(self) -> IUser:
        """
        
        :return: 
        """
class LegacyDatabasedScore(Score, IDeepCloneable[Score]):
    """"""
    Replay: Final[Replay] = ...
    """
    
    :return: 
    """
    ScoreInfo: Final[ScoreInfo] = ...
    """
    
    :return: 
    """
    def __init__(self, score: ScoreInfo, rulesets: RulesetStore, beatmaps: BeatmapManager, store: IResourceStore[Array[int]]):
        """
        
        :param score: 
        :param rulesets: 
        :param beatmaps: 
        :param store: 
        """
    def DeepClone(self) -> Score:
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
class RankingTier(Enum):
    """"""
    Iron: RankingTier = ...
    """"""
    Bronze: RankingTier = ...
    """"""
    Silver: RankingTier = ...
    """"""
    Gold: RankingTier = ...
    """"""
    Platinum: RankingTier = ...
    """"""
    Rhodium: RankingTier = ...
    """"""
    Radiant: RankingTier = ...
    """"""
    Lustrous: RankingTier = ...
    """"""
class Score(Object, IDeepCloneable[Score]):
    """"""
    Replay: Final[Replay] = ...
    """
    
    :return: 
    """
    ScoreInfo: Final[ScoreInfo] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    def DeepClone(self) -> Score:
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
class ScoreImporter(RealmArchiveModelImporter[ScoreInfo], ICanAcceptFiles, IModelImporter[ScoreInfo], IPostNotifications):
    """"""
    def __init__(self, rulesets: RulesetStore, beatmaps: Func[BeatmapManager], storage: Storage, realm: RealmAccess, api: IAPIProvider):
        """
        
        :param rulesets: 
        :param beatmaps: 
        :param storage: 
        :param realm: 
        :param api: 
        """
    @property
    def HandledExtensions(self) -> IEnumerable[str]:
        """
        
        :return: 
        """
    @property
    def HumanisedModelName(self) -> str:
        """
        
        :return: 
        """
    @property
    def PauseImports(self) -> bool:
        """
        
        :return: 
        """
    @PauseImports.setter
    def PauseImports(self, value: bool) -> None: ...
    @property
    def PostNotification(self) -> Action[Notification]:
        """
        
        :return: 
        """
    @PostNotification.setter
    def PostNotification(self, value: Action[Notification]) -> None: ...
    @property
    def PresentImport(self) -> Action[IEnumerable[Live[ScoreInfo]]]:
        """
        
        :return: 
        """
    @PresentImport.setter
    def PresentImport(self, value: Action[IEnumerable[Live[ScoreInfo]]]) -> None: ...
    def BeginExternalEditing(self, model: ScoreInfo) -> Task[ExternalEditOperation[ScoreInfo]]:
        """
        
        :param model: 
        :return: 
        """
    def ComputeHash(self, item: ScoreInfo) -> str:
        """
        
        :param item: 
        :return: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetScore(self, score: ScoreInfo) -> Score:
        """
        
        :param score: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    @overload
    def Import(self, paths: Array[str]) -> Task:
        """
        
        :param paths: 
        :return: 
        """
    @overload
    def Import(self, tasks: Array[ImportTask], parameters: ImportParameters = ...) -> Task:
        """
        
        :param tasks: 
        :param parameters: 
        :return: 
        """
    @overload
    def Import(self, task: ImportTask, parameters: ImportParameters = ..., cancellationToken: CancellationToken = ...) -> Task[Live[ScoreInfo]]:
        """
        
        :param task: 
        :param parameters: 
        :param cancellationToken: 
        :return: 
        """
    @overload
    def Import(self, notification: ProgressNotification, tasks: Array[ImportTask], parameters: ImportParameters = ...) -> Task[IEnumerable[Live[ScoreInfo]]]:
        """
        
        :param notification: 
        :param tasks: 
        :param parameters: 
        :return: 
        """
    def ImportAsUpdate(self, notification: ProgressNotification, task: ImportTask, original: ScoreInfo) -> Task[Live[ScoreInfo]]:
        """
        
        :param notification: 
        :param task: 
        :param original: 
        :return: 
        """
    def ImportModel(self, item: ScoreInfo, archive: ArchiveReader = ..., parameters: ImportParameters = ..., cancellationToken: CancellationToken = ...) -> Live[ScoreInfo]:
        """
        
        :param item: 
        :param archive: 
        :param parameters: 
        :param cancellationToken: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class ScoreInfo(RealmObject, IRealmObject, IRealmObjectBase, ISettableManagedAccessor, INotifyPropertyChanged, IReflectableType, IEquatable[ScoreInfo], IHasGuidPrimaryKey, IHasNamedFiles, IHasOnlineID[Int64], IHasRealmFiles, ISoftDelete, IScoreInfo):
    """"""
    def __init__(self, beatmap: BeatmapInfo = ..., ruleset: RulesetInfo = ..., realmUser: RealmUser = ...):
        """
        
        :param beatmap: 
        :param ruleset: 
        :param realmUser: 
        """
    @property
    def APIMods(self) -> Array[APIMod]:
        """
        
        :return: 
        """
    @APIMods.setter
    def APIMods(self, value: Array[APIMod]) -> None: ...
    @property
    def Accessor(self) -> IRealmAccessor:
        """"""
    @property
    def Accuracy(self) -> float:
        """
        
        :return: 
        """
    @Accuracy.setter
    def Accuracy(self, value: float) -> None: ...
    @property
    def BackgroundReprocessingFailed(self) -> bool:
        """
        
        :return: 
        """
    @BackgroundReprocessingFailed.setter
    def BackgroundReprocessingFailed(self, value: bool) -> None: ...
    @property
    def BacklinksCount(self) -> int:
        """"""
    @property
    def Beatmap(self) -> IBeatmapInfo:
        """
        
        :return: 
        """
    @property
    def BeatmapHash(self) -> str:
        """
        
        :return: 
        """
    @BeatmapHash.setter
    def BeatmapHash(self, value: str) -> None: ...
    @property
    def BeatmapInfo(self) -> BeatmapInfo:
        """
        
        :return: 
        """
    @BeatmapInfo.setter
    def BeatmapInfo(self, value: BeatmapInfo) -> None: ...
    @property
    def ClientVersion(self) -> str:
        """
        
        :return: 
        """
    @ClientVersion.setter
    def ClientVersion(self, value: str) -> None: ...
    @property
    def Combo(self) -> int:
        """
        
        :return: 
        """
    @Combo.setter
    def Combo(self, value: int) -> None: ...
    @property
    def Date(self) -> DateTimeOffset:
        """
        
        :return: 
        """
    @Date.setter
    def Date(self, value: DateTimeOffset) -> None: ...
    @property
    def DeletePending(self) -> bool:
        """
        
        :return: 
        """
    @DeletePending.setter
    def DeletePending(self, value: bool) -> None: ...
    @property
    def DisplayAccuracy(self) -> LocalisableString:
        """
        
        :return: 
        """
    @property
    def DynamicApi(self) -> DynamicObjectApi:
        """"""
    @property
    def Files(self) -> IList[RealmNamedFileUsage]:
        """
        
        :return: 
        """
    @property
    def HasOnlineReplay(self) -> bool:
        """
        
        :return: 
        """
    @HasOnlineReplay.setter
    def HasOnlineReplay(self, value: bool) -> None: ...
    @property
    def Hash(self) -> str:
        """
        
        :return: 
        """
    @Hash.setter
    def Hash(self, value: str) -> None: ...
    @property
    def HitEvents(self) -> List[HitEvent]:
        """
        
        :return: 
        """
    @HitEvents.setter
    def HitEvents(self, value: List[HitEvent]) -> None: ...
    @property
    def ID(self) -> Guid:
        """
        
        :return: 
        """
    @ID.setter
    def ID(self, value: Guid) -> None: ...
    @property
    def IsFrozen(self) -> bool:
        """"""
    @property
    def IsLegacyScore(self) -> bool:
        """
        
        :return: 
        """
    @IsLegacyScore.setter
    def IsLegacyScore(self, value: bool) -> None: ...
    @property
    def IsManaged(self) -> bool:
        """"""
    @property
    def IsValid(self) -> bool:
        """"""
    @property
    def LegacyOnlineID(self) -> int:
        """
        
        :return: 
        """
    @LegacyOnlineID.setter
    def LegacyOnlineID(self, value: int) -> None: ...
    @property
    def LegacyTotalScore(self) -> Optional[int]:
        """
        
        :return: 
        """
    @LegacyTotalScore.setter
    def LegacyTotalScore(self, value: Optional[int]) -> None: ...
    @property
    def MaxCombo(self) -> int:
        """
        
        :return: 
        """
    @MaxCombo.setter
    def MaxCombo(self, value: int) -> None: ...
    @property
    def MaximumStatistics(self) -> Dictionary[HitResult, int]:
        """
        
        :return: 
        """
    @MaximumStatistics.setter
    def MaximumStatistics(self, value: Dictionary[HitResult, int]) -> None: ...
    @property
    def MaximumStatisticsJson(self) -> str:
        """
        
        :return: 
        """
    @MaximumStatisticsJson.setter
    def MaximumStatisticsJson(self, value: str) -> None: ...
    @property
    def Mods(self) -> Array[Mod]:
        """
        
        :return: 
        """
    @Mods.setter
    def Mods(self, value: Array[Mod]) -> None: ...
    @property
    def ModsJson(self) -> str:
        """
        
        :return: 
        """
    @ModsJson.setter
    def ModsJson(self, value: str) -> None: ...
    @property
    def ObjectSchema(self) -> ObjectSchema:
        """"""
    @property
    def OnlineID(self) -> int:
        """
        
        :return: 
        """
    @OnlineID.setter
    def OnlineID(self, value: int) -> None: ...
    @property
    def PP(self) -> Optional[float]:
        """
        
        :return: 
        """
    @PP.setter
    def PP(self, value: Optional[float]) -> None: ...
    @property
    def Passed(self) -> bool:
        """
        
        :return: 
        """
    @Passed.setter
    def Passed(self, value: bool) -> None: ...
    @property
    def Pauses(self) -> IList[int]:
        """
        
        :return: 
        """
    @property
    def Position(self) -> Optional[int]:
        """
        
        :return: 
        """
    @Position.setter
    def Position(self, value: Optional[int]) -> None: ...
    @property
    def Rank(self) -> ScoreRank:
        """
        
        :return: 
        """
    @Rank.setter
    def Rank(self, value: ScoreRank) -> None: ...
    @property
    def RankInt(self) -> int:
        """
        
        :return: 
        """
    @RankInt.setter
    def RankInt(self, value: int) -> None: ...
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @Ranked.setter
    def Ranked(self, value: bool) -> None: ...
    @property
    def Realm(self) -> Realm:
        """"""
    @property
    def RealmUser(self) -> RealmUser:
        """
        
        :return: 
        """
    @RealmUser.setter
    def RealmUser(self, value: RealmUser) -> None: ...
    @property
    def Ruleset(self) -> RulesetInfo:
        """
        
        :return: 
        """
    @Ruleset.setter
    def Ruleset(self, value: RulesetInfo) -> None: ...
    @property
    def RulesetID(self) -> int:
        """
        
        :return: 
        """
    @property
    def Statistics(self) -> Dictionary[HitResult, int]:
        """
        
        :return: 
        """
    @Statistics.setter
    def Statistics(self, value: Dictionary[HitResult, int]) -> None: ...
    @property
    def StatisticsJson(self) -> str:
        """
        
        :return: 
        """
    @StatisticsJson.setter
    def StatisticsJson(self, value: str) -> None: ...
    @property
    def TotalScore(self) -> int:
        """
        
        :return: 
        """
    @TotalScore.setter
    def TotalScore(self, value: int) -> None: ...
    @property
    def TotalScoreVersion(self) -> int:
        """
        
        :return: 
        """
    @TotalScoreVersion.setter
    def TotalScoreVersion(self, value: int) -> None: ...
    @property
    def TotalScoreWithoutMods(self) -> int:
        """
        
        :return: 
        """
    @TotalScoreWithoutMods.setter
    def TotalScoreWithoutMods(self, value: int) -> None: ...
    @property
    def User(self) -> APIUser:
        """
        
        :return: 
        """
    @User.setter
    def User(self, value: APIUser) -> None: ...
    @property
    def UserID(self) -> int:
        """
        
        :return: 
        """
    def DeepClone(self) -> ScoreInfo:
        """
        
        :return: 
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: ScoreInfo) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetStatisticsForDisplay(self) -> IEnumerable[HitResultDisplayStatistic]:
        """
        
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self) -> TypeInfo:
        """"""
    def SetManagedAccessor(self, accessor: IRealmAccessor, helper: IRealmObjectHelper = ..., update: bool = ..., skipDefaults: bool = ...) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    PropertyChanged: EventType[PropertyChangedEventHandler] = ...
    """"""
class ScoreInfoExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetAllLocalScoresForUser(cls, realm: Realm, userId: Optional[int]) -> IQueryable[ScoreInfo]:
        """
        
        :param realm: 
        :param userId: 
        :return: 
        """
    @classmethod
    def GetDisplayTitle(cls, scoreInfo: IScoreInfo) -> str:
        """
        
        :param scoreInfo: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetMaximumAchievableCombo(cls, score: ScoreInfo) -> int:
        """
        
        :param score: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    @classmethod
    def OrderByCriteria(cls, scores: IEnumerable[ScoreInfo], leaderboardSortMode: LeaderboardSortMode) -> IEnumerable[ScoreInfo]:
        """
        
        :param scores: 
        :param leaderboardSortMode: 
        :return: 
        """
    @classmethod
    def OrderByTotalScore(cls, scores: IEnumerable[ScoreInfo]) -> IEnumerable[ScoreInfo]:
        """
        
        :param scores: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class ScoreManager(ModelManager[ScoreInfo], ICanAcceptFiles, IModelFileManager[ScoreInfo, RealmNamedFileUsage], IModelImporter[ScoreInfo], IModelManager[ScoreInfo], IPostNotifications):
    """"""
    def __init__(self, rulesets: RulesetStore, beatmaps: Func[BeatmapManager], storage: Storage, realm: RealmAccess, api: IAPIProvider, configManager: OsuConfigManager = ...):
        """
        
        :param rulesets: 
        :param beatmaps: 
        :param storage: 
        :param realm: 
        :param api: 
        :param configManager: 
        """
    @property
    def HandledExtensions(self) -> IEnumerable[str]:
        """
        
        :return: 
        """
    @property
    def HumanisedModelName(self) -> str:
        """
        
        :return: 
        """
    @property
    def PauseImports(self) -> bool:
        """
        
        :return: 
        """
    @PauseImports.setter
    def PauseImports(self, value: bool) -> None: ...
    @property
    def PostNotification(self) -> Action[Notification]:
        """
        
        :return: 
        """
    @PostNotification.setter
    def PostNotification(self, value: Action[Notification]) -> None: ...
    @property
    def PresentImport(self) -> Action[IEnumerable[Live[ScoreInfo]]]:
        """
        
        :return: 
        """
    @PresentImport.setter
    def PresentImport(self, value: Action[IEnumerable[Live[ScoreInfo]]]) -> None: ...
    @overload
    def AddFile(self, item: ScoreInfo, contents: Stream, filename: str) -> None:
        """
        
        :param model: 
        :param contents: 
        :param filename: 
        """
    @overload
    def AddFile(self, item: ScoreInfo, contents: Stream, filename: str, realm: Realm) -> None:
        """
        
        :param item: 
        :param contents: 
        :param filename: 
        :param realm: 
        """
    def BeginExternalEditing(self, model: ScoreInfo) -> Task[ExternalEditOperation[ScoreInfo]]:
        """
        
        :param model: 
        :return: 
        """
    @overload
    def Delete(self, item: ScoreInfo) -> bool:
        """
        
        :param item: 
        :return: 
        """
    @overload
    def Delete(self, items: List[ScoreInfo], silent: bool = ...) -> None:
        """
        
        :param item: 
        :return: 
        """
    @overload
    def Delete(self, filter: Expression[Func, bool] = ..., silent: bool = ...) -> None:
        """"""
    @overload
    def Delete(self, beatmap: BeatmapInfo, silent: bool = ...) -> None:
        """
        
        :param beatmap: 
        :param silent: 
        """
    @overload
    def DeleteFile(self, item: ScoreInfo, file: RealmNamedFileUsage) -> None:
        """
        
        :param model: 
        :param file: 
        """
    @overload
    def DeleteFile(self, item: ScoreInfo, file: RealmNamedFileUsage, realm: Realm) -> None:
        """
        
        :param item: 
        :param file: 
        :param realm: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def Export(self, scoreInfo: ScoreInfo) -> Task:
        """
        
        :param scoreInfo: 
        :return: 
        """
    def GetBindableTotalScore(self, score: ScoreInfo) -> Bindable[int]:
        """
        
        :param score: 
        :return: 
        """
    def GetBindableTotalScoreString(self, score: ScoreInfo) -> Bindable[str]:
        """
        
        :param score: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetScore(self, scoreInfo: IScoreInfo) -> Score:
        """
        
        :param scoreInfo: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    @overload
    def Import(self, paths: Array[str]) -> Task:
        """
        
        :param paths: 
        :return: 
        """
    @overload
    def Import(self, imports: Array[ImportTask], parameters: ImportParameters = ...) -> Task:
        """
        
        :param tasks: 
        :param parameters: 
        :return: 
        """
    @overload
    def Import(self, notification: ProgressNotification, tasks: Array[ImportTask], parameters: ImportParameters = ...) -> Task[IEnumerable[Live[ScoreInfo]]]:
        """
        
        :param notification: 
        :param tasks: 
        :param parameters: 
        :return: 
        """
    @overload
    def Import(self, item: ScoreInfo, archive: ArchiveReader = ..., parameters: ImportParameters = ..., cancellationToken: CancellationToken = ...) -> Live[ScoreInfo]:
        """
        
        :param item: 
        :param archive: 
        :param parameters: 
        :param cancellationToken: 
        :return: 
        """
    def ImportAsUpdate(self, notification: ProgressNotification, task: ImportTask, original: ScoreInfo) -> Task[Live[ScoreInfo]]:
        """
        
        :param notification: 
        :param task: 
        :param original: 
        :return: 
        """
    def IsAvailableLocally(self, model: ScoreInfo) -> bool:
        """
        
        :param model: 
        :return: 
        """
    def PopulateMaximumStatistics(self, score: ScoreInfo) -> None:
        """
        
        :param score: 
        """
    def Query(self, query: Expression[Func, bool]) -> ScoreInfo:
        """"""
    @overload
    def ReplaceFile(self, file: RealmNamedFileUsage, contents: Stream, realm: Realm) -> None:
        """
        
        :param file: 
        :param contents: 
        :param realm: 
        """
    @overload
    def ReplaceFile(self, item: ScoreInfo, file: RealmNamedFileUsage, contents: Stream) -> None:
        """
        
        :param model: 
        :param file: 
        :param contents: 
        """
    def ToString(self) -> str:
        """"""
    @overload
    def Undelete(self, item: ScoreInfo) -> None:
        """
        
        :param item: 
        """
    @overload
    def Undelete(self, items: List[ScoreInfo], silent: bool = ...) -> None:
        """
        
        :param item: 
        """
class ScoreModelDownloader(ModelDownloader[ScoreInfo, IScoreInfo], IModelDownloader[IScoreInfo], IPostNotifications):
    """"""
    def __init__(self, scoreManager: IModelImporter[ScoreInfo], api: IAPIProvider):
        """
        
        :param scoreManager: 
        :param api: 
        """
    @property
    def PostNotification(self) -> Action[Notification]:
        """
        
        :return: 
        """
    @PostNotification.setter
    def PostNotification(self, value: Action[Notification]) -> None: ...
    def Download(self, model: IScoreInfo, minimiseDownloadSize: bool = ...) -> bool:
        """
        
        :param item: 
        :param minimiseDownloadSize: 
        :return: 
        """
    def DownloadAsUpdate(self, originalModel: ScoreInfo, minimiseDownloadSize: bool) -> None:
        """
        
        :param originalModel: 
        :param minimiseDownloadSize: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetExistingDownload(self, model: IScoreInfo) -> ArchiveDownloadRequest[IScoreInfo]:
        """
        
        :param item: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    DownloadBegan: EventType[Action[ArchiveDownloadRequest[IScoreInfo]]] = ...
    """"""
    DownloadFailed: EventType[Action[ArchiveDownloadRequest[IScoreInfo]]] = ...
    """"""
class ScoreRank(Enum):
    """"""
    D: ScoreRank = ...
    """"""
    C: ScoreRank = ...
    """"""
    B: ScoreRank = ...
    """"""
    A: ScoreRank = ...
    """"""
    S: ScoreRank = ...
    """"""
    SH: ScoreRank = ...
    """"""
    X: ScoreRank = ...
    """"""
    XH: ScoreRank = ...
    """"""
    F: ScoreRank = ...
    """"""