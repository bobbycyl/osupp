from Newtonsoft.Json.Linq import JObject
from System import Array
from System.Collections.Generic import Dictionary
from System.Collections.Generic import ICollection
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import List
from System import DateTime
from System import DateTimeOffset
from System import Enum
from System import IComparable
from System import IEquatable
from System import Int32
from System import Int64
from System import Object
from System import Type
from System import ValueTuple
from System import ValueType
from __future__ import annotations
from osu.Framework.Graphics.Colour import ColourInfo
from osu.Game.Beatmaps import APIBeatmapTag
from osu.Game.Beatmaps import APIFailTimes
from osu.Game.Beatmaps import BeatmapInfo
from osu.Game.Beatmaps import BeatmapOnlineStatus
from osu.Game.Beatmaps import BeatmapSetHypeStatus
from osu.Game.Beatmaps import BeatmapSetNominationStatus
from osu.Game.Beatmaps import BeatmapSetOnlineAvailability
from osu.Game.Beatmaps import BeatmapSetOnlineCovers
from osu.Game.Beatmaps import BeatmapSetOnlineGenre
from osu.Game.Beatmaps import BeatmapSetOnlineLanguage
from osu.Game.Beatmaps import BeatmapSetOnlineNomination
from osu.Game.Beatmaps import IBeatmapDifficultyInfo
from osu.Game.Beatmaps import IBeatmapInfo
from osu.Game.Beatmaps import IBeatmapMetadataInfo
from osu.Game.Beatmaps import IBeatmapOnlineInfo
from osu.Game.Beatmaps import IBeatmapSetInfo
from osu.Game.Beatmaps import IBeatmapSetOnlineInfo
from osu.Game.Database import IHasNamedFiles
from osu.Game.Database import IHasOnlineID
from osu.Game.Database import INamedFileUsage
from osu.Game.Online.API import APIMod
from osu.Game.Online.API.Requests import BeatmapApproval
from osu.Game.Online.API.Requests import RecentActivityType
from osu.Game.Online.API.Requests.Responses.APIChangelogBuild import VersionNavigation
from osu.Game.Online.API.Requests.Responses.APIKudosuHistory import KudosuGiver
from osu.Game.Online.API.Requests.Responses.APIKudosuHistory import ModdingPost
from osu.Game.Online.API.Requests.Responses.APIRecentActivity import RecentActivityAchievement
from osu.Game.Online.API.Requests.Responses.APIRecentActivity import RecentActivityBeatmap
from osu.Game.Online.API.Requests.Responses.APIRecentActivity import RecentActivityUser
from osu.Game.Online.API.Requests.Responses.APIUser import GlobalRank
from osu.Game.Online.API.Requests.Responses.APIUser import KudosuCount
from osu.Game.Online.API.Requests.Responses.APIUser import UserCover
from osu.Game.Online.API.Requests.Responses.APIUser import UserRankHighest
from osu.Game.Online.API.Requests.Responses.CommentableMeta import CommentableCurrentUserAttributes
from osu.Game.Online.Chat import Channel
from osu.Game.Online.Chat import Message
from osu.Game.Rulesets import IRulesetInfo
from osu.Game.Rulesets.Mods import Mod
from osu.Game.Rulesets import Ruleset
from osu.Game.Rulesets import RulesetStore
from osu.Game.Rulesets.Scoring import HitResult
from osu.Game.Scoring import IScoreInfo
from osu.Game.Scoring import ScoreInfo
from osu.Game.Scoring import ScoreRank
from osu.Game.Users import Badge
from osu.Game.Users import CountryCode
from osu.Game.Users import IUser
from osu.Game.Users import TournamentBanner
from osu.Game.Users import UserStatistics
from typing import ClassVar
from typing import Final
from typing import Optional
from typing import overload
class APIBeatmap(Object, IEquatable[IBeatmapInfo], IBeatmapInfo, IBeatmapOnlineInfo, IHasOnlineID[Int32]):
    """"""
    MINIMUM_USER_TAG_VOTES_FOR_DISPLAY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
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
    def AuthorID(self) -> int:
        """
        
        :return: 
        """
    @AuthorID.setter
    def AuthorID(self, value: int) -> None: ...
    @property
    def BPM(self) -> float:
        """
        
        :return: 
        """
    @BPM.setter
    def BPM(self, value: float) -> None: ...
    @property
    def BeatmapOwners(self) -> Array[BeatmapOwner]:
        """
        
        :return: 
        """
    @BeatmapOwners.setter
    def BeatmapOwners(self, value: Array[BeatmapOwner]) -> None: ...
    @property
    def BeatmapSet(self) -> APIBeatmapSet:
        """
        
        :return: 
        """
    @BeatmapSet.setter
    def BeatmapSet(self, value: APIBeatmapSet) -> None: ...
    @property
    def Checksum(self) -> str:
        """
        
        :return: 
        """
    @Checksum.setter
    def Checksum(self, value: str) -> None: ...
    @property
    def CircleCount(self) -> int:
        """
        
        :return: 
        """
    @CircleCount.setter
    def CircleCount(self, value: int) -> None: ...
    @property
    def CircleSize(self) -> float:
        """
        
        :return: 
        """
    @CircleSize.setter
    def CircleSize(self, value: float) -> None: ...
    @property
    def Convert(self) -> bool:
        """
        
        :return: 
        """
    @Convert.setter
    def Convert(self, value: bool) -> None: ...
    @property
    def Difficulty(self) -> IBeatmapDifficultyInfo:
        """
        
        :return: 
        """
    @property
    def DifficultyName(self) -> str:
        """
        
        :return: 
        """
    @DifficultyName.setter
    def DifficultyName(self, value: str) -> None: ...
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
    @property
    def FailTimes(self) -> APIFailTimes:
        """
        
        :return: 
        """
    @FailTimes.setter
    def FailTimes(self, value: APIFailTimes) -> None: ...
    @property
    def Hash(self) -> str:
        """
        
        :return: 
        """
    @property
    def HitLength(self) -> float:
        """
        
        :return: 
        """
    @HitLength.setter
    def HitLength(self, value: float) -> None: ...
    @property
    def LastUpdated(self) -> DateTimeOffset:
        """
        
        :return: 
        """
    @LastUpdated.setter
    def LastUpdated(self, value: DateTimeOffset) -> None: ...
    @property
    def Length(self) -> float:
        """
        
        :return: 
        """
    @Length.setter
    def Length(self, value: float) -> None: ...
    @property
    def MD5Hash(self) -> str:
        """
        
        :return: 
        """
    @property
    def MaxCombo(self) -> Optional[int]:
        """
        
        :return: 
        """
    @MaxCombo.setter
    def MaxCombo(self, value: Optional[int]) -> None: ...
    @property
    def Metadata(self) -> IBeatmapMetadataInfo:
        """
        
        :return: 
        """
    @property
    def OnlineBeatmapSetID(self) -> int:
        """
        
        :return: 
        """
    @OnlineBeatmapSetID.setter
    def OnlineBeatmapSetID(self, value: int) -> None: ...
    @property
    def OnlineID(self) -> int:
        """
        
        :return: 
        """
    @OnlineID.setter
    def OnlineID(self, value: int) -> None: ...
    @property
    def OverallDifficulty(self) -> float:
        """
        
        :return: 
        """
    @OverallDifficulty.setter
    def OverallDifficulty(self, value: float) -> None: ...
    @property
    def OwnTagIds(self) -> Array[int]:
        """
        
        :return: 
        """
    @OwnTagIds.setter
    def OwnTagIds(self, value: Array[int]) -> None: ...
    @property
    def PassCount(self) -> int:
        """
        
        :return: 
        """
    @PassCount.setter
    def PassCount(self, value: int) -> None: ...
    @property
    def PlayCount(self) -> int:
        """
        
        :return: 
        """
    @PlayCount.setter
    def PlayCount(self, value: int) -> None: ...
    @property
    def Ruleset(self) -> IRulesetInfo:
        """
        
        :return: 
        """
    @property
    def RulesetID(self) -> int:
        """
        
        :return: 
        """
    @RulesetID.setter
    def RulesetID(self, value: int) -> None: ...
    @property
    def SliderCount(self) -> int:
        """
        
        :return: 
        """
    @SliderCount.setter
    def SliderCount(self, value: int) -> None: ...
    @property
    def SpinnerCount(self) -> int:
        """
        
        :return: 
        """
    @SpinnerCount.setter
    def SpinnerCount(self, value: int) -> None: ...
    @property
    def StarRating(self) -> float:
        """
        
        :return: 
        """
    @StarRating.setter
    def StarRating(self, value: float) -> None: ...
    @property
    def Status(self) -> BeatmapOnlineStatus:
        """
        
        :return: 
        """
    @Status.setter
    def Status(self, value: BeatmapOnlineStatus) -> None: ...
    @property
    def TopTags(self) -> Array[APIBeatmapTag]:
        """
        
        :return: 
        """
    @TopTags.setter
    def TopTags(self, value: Array[APIBeatmapTag]) -> None: ...
    @property
    def TotalObjectCount(self) -> int:
        """
        
        :return: 
        """
    @property
    def UserPlayCount(self) -> int:
        """
        
        :return: 
        """
    @UserPlayCount.setter
    def UserPlayCount(self, value: int) -> None: ...
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IBeatmapInfo) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTopUserTags(self, confirmedOnly: bool = ...) -> Array[ValueTuple, int]:
        """
        
        :param confirmedOnly: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    class APIRuleset(Object, IComparable[IRulesetInfo], IEquatable[IRulesetInfo], IHasOnlineID[Int32], IRulesetInfo):
        """"""
        def __init__(self):
            """"""
        @property
        def InstantiationInfo(self) -> str:
            """
            
            :return: 
            """
        @property
        def Name(self) -> str:
            """
            
            :return: 
            """
        @property
        def OnlineID(self) -> int:
            """
            
            :return: 
            """
        @OnlineID.setter
        def OnlineID(self, value: int) -> None: ...
        @property
        def ShortName(self) -> str:
            """
            
            :return: 
            """
        def CompareTo(self, other: IRulesetInfo) -> int:
            """"""
        def CreateInstance(self) -> Ruleset:
            """
            
            :return: 
            """
        @overload
        def Equals(self, obj: object) -> bool:
            """"""
        @overload
        def Equals(self, other: IRulesetInfo) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
    class BeatmapOwner(Object):
        """"""
        def __init__(self):
            """"""
        @property
        def Id(self) -> int:
            """"""
        @Id.setter
        def Id(self, value: int) -> None: ...
        @property
        def Username(self) -> str:
            """"""
        @Username.setter
        def Username(self, value: str) -> None: ...
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
class APIBeatmapSet(Object, IEquatable[IBeatmapSetInfo], IBeatmapSetInfo, IBeatmapSetOnlineInfo, IHasNamedFiles, IHasOnlineID[Int32]):
    """"""
    Author: Final[APIUser] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def Artist(self) -> str:
        """
        
        :return: 
        """
    @Artist.setter
    def Artist(self, value: str) -> None: ...
    @property
    def ArtistUnicode(self) -> str:
        """
        
        :return: 
        """
    @ArtistUnicode.setter
    def ArtistUnicode(self, value: str) -> None: ...
    @property
    def AuthorID(self) -> int:
        """
        
        :return: 
        """
    @AuthorID.setter
    def AuthorID(self, value: int) -> None: ...
    @property
    def AuthorString(self) -> str:
        """
        
        :return: 
        """
    @AuthorString.setter
    def AuthorString(self, value: str) -> None: ...
    @property
    def Availability(self) -> BeatmapSetOnlineAvailability:
        """
        
        :return: 
        """
    @Availability.setter
    def Availability(self, value: BeatmapSetOnlineAvailability) -> None: ...
    @property
    def BPM(self) -> float:
        """
        
        :return: 
        """
    @BPM.setter
    def BPM(self, value: float) -> None: ...
    @property
    def Beatmaps(self) -> Array[APIBeatmap]:
        """
        
        :return: 
        """
    @Beatmaps.setter
    def Beatmaps(self, value: Array[APIBeatmap]) -> None: ...
    @property
    def Converts(self) -> Array[APIBeatmap]:
        """
        
        :return: 
        """
    @Converts.setter
    def Converts(self, value: Array[APIBeatmap]) -> None: ...
    @property
    def Covers(self) -> BeatmapSetOnlineCovers:
        """
        
        :return: 
        """
    @Covers.setter
    def Covers(self, value: BeatmapSetOnlineCovers) -> None: ...
    @property
    def CurrentNominations(self) -> Array[BeatmapSetOnlineNomination]:
        """
        
        :return: 
        """
    @CurrentNominations.setter
    def CurrentNominations(self, value: Array[BeatmapSetOnlineNomination]) -> None: ...
    @property
    def DateAdded(self) -> DateTimeOffset:
        """
        
        :return: 
        """
    @property
    def FavouriteCount(self) -> int:
        """
        
        :return: 
        """
    @FavouriteCount.setter
    def FavouriteCount(self, value: int) -> None: ...
    @property
    def FeaturedInSpotlight(self) -> bool:
        """
        
        :return: 
        """
    @FeaturedInSpotlight.setter
    def FeaturedInSpotlight(self, value: bool) -> None: ...
    @property
    def Files(self) -> IEnumerable[INamedFileUsage]:
        """
        
        :return: 
        """
    @property
    def Genre(self) -> BeatmapSetOnlineGenre:
        """
        
        :return: 
        """
    @Genre.setter
    def Genre(self, value: BeatmapSetOnlineGenre) -> None: ...
    @property
    def HasExplicitContent(self) -> bool:
        """
        
        :return: 
        """
    @HasExplicitContent.setter
    def HasExplicitContent(self, value: bool) -> None: ...
    @property
    def HasFavourited(self) -> bool:
        """
        
        :return: 
        """
    @HasFavourited.setter
    def HasFavourited(self, value: bool) -> None: ...
    @property
    def HasStoryboard(self) -> bool:
        """
        
        :return: 
        """
    @HasStoryboard.setter
    def HasStoryboard(self, value: bool) -> None: ...
    @property
    def HasVideo(self) -> bool:
        """
        
        :return: 
        """
    @HasVideo.setter
    def HasVideo(self, value: bool) -> None: ...
    @property
    def HypeStatus(self) -> BeatmapSetHypeStatus:
        """
        
        :return: 
        """
    @HypeStatus.setter
    def HypeStatus(self, value: BeatmapSetHypeStatus) -> None: ...
    @property
    def Language(self) -> BeatmapSetOnlineLanguage:
        """
        
        :return: 
        """
    @Language.setter
    def Language(self, value: BeatmapSetOnlineLanguage) -> None: ...
    @property
    def LastUpdated(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @LastUpdated.setter
    def LastUpdated(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def MaxBPM(self) -> float:
        """
        
        :return: 
        """
    @property
    def MaxLength(self) -> float:
        """
        
        :return: 
        """
    @property
    def MaxStarDifficulty(self) -> float:
        """
        
        :return: 
        """
    @property
    def Metadata(self) -> IBeatmapMetadataInfo:
        """
        
        :return: 
        """
    @property
    def NominationStatus(self) -> BeatmapSetNominationStatus:
        """
        
        :return: 
        """
    @NominationStatus.setter
    def NominationStatus(self, value: BeatmapSetNominationStatus) -> None: ...
    @property
    def OnlineID(self) -> int:
        """
        
        :return: 
        """
    @OnlineID.setter
    def OnlineID(self, value: int) -> None: ...
    @property
    def PlayCount(self) -> int:
        """
        
        :return: 
        """
    @PlayCount.setter
    def PlayCount(self, value: int) -> None: ...
    @property
    def Preview(self) -> str:
        """
        
        :return: 
        """
    @Preview.setter
    def Preview(self, value: str) -> None: ...
    @property
    def Ranked(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @Ranked.setter
    def Ranked(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def Ratings(self) -> Array[int]:
        """
        
        :return: 
        """
    @Ratings.setter
    def Ratings(self, value: Array[int]) -> None: ...
    @property
    def RelatedTags(self) -> Array[APITag]:
        """
        
        :return: 
        """
    @RelatedTags.setter
    def RelatedTags(self, value: Array[APITag]) -> None: ...
    @property
    def RelatedUsers(self) -> Array[APIUser]:
        """
        
        :return: 
        """
    @RelatedUsers.setter
    def RelatedUsers(self, value: Array[APIUser]) -> None: ...
    @property
    def Source(self) -> str:
        """
        
        :return: 
        """
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def Status(self) -> BeatmapOnlineStatus:
        """
        
        :return: 
        """
    @Status.setter
    def Status(self, value: BeatmapOnlineStatus) -> None: ...
    @property
    def Submitted(self) -> DateTimeOffset:
        """
        
        :return: 
        """
    @Submitted.setter
    def Submitted(self, value: DateTimeOffset) -> None: ...
    @property
    def Tags(self) -> str:
        """
        
        :return: 
        """
    @Tags.setter
    def Tags(self, value: str) -> None: ...
    @property
    def Title(self) -> str:
        """
        
        :return: 
        """
    @Title.setter
    def Title(self, value: str) -> None: ...
    @property
    def TitleUnicode(self) -> str:
        """
        
        :return: 
        """
    @TitleUnicode.setter
    def TitleUnicode(self, value: str) -> None: ...
    @property
    def TrackId(self) -> Optional[int]:
        """
        
        :return: 
        """
    @TrackId.setter
    def TrackId(self, value: Optional[int]) -> None: ...
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: IBeatmapSetInfo) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APIChangelogBuild(Object, IEquatable[APIChangelogBuild]):
    """"""
    def __init__(self):
        """"""
    @property
    def ChangelogEntries(self) -> List[APIChangelogEntry]:
        """
        
        :return: 
        """
    @ChangelogEntries.setter
    def ChangelogEntries(self, value: List[APIChangelogEntry]) -> None: ...
    @property
    def CreatedAt(self) -> DateTimeOffset:
        """
        
        :return: 
        """
    @CreatedAt.setter
    def CreatedAt(self, value: DateTimeOffset) -> None: ...
    @property
    def DisplayVersion(self) -> str:
        """
        
        :return: 
        """
    @DisplayVersion.setter
    def DisplayVersion(self, value: str) -> None: ...
    @property
    def Id(self) -> int:
        """
        
        :return: 
        """
    @Id.setter
    def Id(self, value: int) -> None: ...
    @property
    def UpdateStream(self) -> APIUpdateStream:
        """
        
        :return: 
        """
    @UpdateStream.setter
    def UpdateStream(self, value: APIUpdateStream) -> None: ...
    @property
    def Url(self) -> str:
        """
        
        :return: 
        """
    @property
    def Users(self) -> int:
        """
        
        :return: 
        """
    @Users.setter
    def Users(self, value: int) -> None: ...
    @property
    def Version(self) -> str:
        """
        
        :return: 
        """
    @Version.setter
    def Version(self, value: str) -> None: ...
    @property
    def Versions(self) -> APIChangelogBuild.VersionNavigation:
        """
        
        :return: 
        """
    @Versions.setter
    def Versions(self, value: APIChangelogBuild.VersionNavigation) -> None: ...
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: APIChangelogBuild) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    class VersionNavigation(Object):
        """"""
        def __init__(self):
            """"""
        @property
        def Next(self) -> APIChangelogBuild:
            """"""
        @Next.setter
        def Next(self, value: APIChangelogBuild) -> None: ...
        @property
        def Previous(self) -> APIChangelogBuild:
            """"""
        @Previous.setter
        def Previous(self, value: APIChangelogBuild) -> None: ...
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
class APIChangelogEntry(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Category(self) -> str:
        """
        
        :return: 
        """
    @Category.setter
    def Category(self, value: str) -> None: ...
    @property
    def CreatedAt(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @CreatedAt.setter
    def CreatedAt(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def GithubPullRequestId(self) -> Optional[int]:
        """
        
        :return: 
        """
    @GithubPullRequestId.setter
    def GithubPullRequestId(self, value: Optional[int]) -> None: ...
    @property
    def GithubUrl(self) -> str:
        """
        
        :return: 
        """
    @GithubUrl.setter
    def GithubUrl(self, value: str) -> None: ...
    @property
    def GithubUser(self) -> APIChangelogUser:
        """
        
        :return: 
        """
    @GithubUser.setter
    def GithubUser(self, value: APIChangelogUser) -> None: ...
    @property
    def Id(self) -> Optional[int]:
        """
        
        :return: 
        """
    @Id.setter
    def Id(self, value: Optional[int]) -> None: ...
    @property
    def Major(self) -> bool:
        """
        
        :return: 
        """
    @Major.setter
    def Major(self, value: bool) -> None: ...
    @property
    def Message(self) -> str:
        """
        
        :return: 
        """
    @Message.setter
    def Message(self, value: str) -> None: ...
    @property
    def MessageHtml(self) -> str:
        """
        
        :return: 
        """
    @MessageHtml.setter
    def MessageHtml(self, value: str) -> None: ...
    @property
    def Repository(self) -> str:
        """
        
        :return: 
        """
    @Repository.setter
    def Repository(self, value: str) -> None: ...
    @property
    def Title(self) -> str:
        """
        
        :return: 
        """
    @Title.setter
    def Title(self, value: str) -> None: ...
    @property
    def Type(self) -> ChangelogEntryType:
        """
        
        :return: 
        """
    @Type.setter
    def Type(self, value: ChangelogEntryType) -> None: ...
    @property
    def Url(self) -> str:
        """
        
        :return: 
        """
    @Url.setter
    def Url(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APIChangelogIndex(Object):
    """"""
    Builds: Final[List[APIChangelogBuild]] = ...
    """
    
    :return: 
    """
    Streams: Final[List[APIUpdateStream]] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APIChangelogUser(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def DisplayName(self) -> str:
        """
        
        :return: 
        """
    @DisplayName.setter
    def DisplayName(self, value: str) -> None: ...
    @property
    def GithubUrl(self) -> str:
        """
        
        :return: 
        """
    @GithubUrl.setter
    def GithubUrl(self, value: str) -> None: ...
    @property
    def Id(self) -> Optional[int]:
        """
        
        :return: 
        """
    @Id.setter
    def Id(self, value: Optional[int]) -> None: ...
    @property
    def OsuUsername(self) -> str:
        """
        
        :return: 
        """
    @OsuUsername.setter
    def OsuUsername(self, value: str) -> None: ...
    @property
    def UserId(self) -> Optional[int]:
        """
        
        :return: 
        """
    @UserId.setter
    def UserId(self, value: Optional[int]) -> None: ...
    @property
    def UserUrl(self) -> str:
        """
        
        :return: 
        """
    @UserUrl.setter
    def UserUrl(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APIChatChannel(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def ChannelID(self) -> Optional[int]:
        """
        
        :return: 
        """
    @ChannelID.setter
    def ChannelID(self, value: Optional[int]) -> None: ...
    @property
    def RecentMessages(self) -> List[Message]:
        """
        
        :return: 
        """
    @RecentMessages.setter
    def RecentMessages(self, value: List[Message]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APIKudosuHistory(Object):
    """"""
    Action: Final[KudosuAction] = ...
    """
    
    :return: 
    """
    Amount: Final[int] = ...
    """
    
    :return: 
    """
    CreatedAt: Final[DateTimeOffset] = ...
    """
    
    :return: 
    """
    Giver: Final[APIKudosuHistory.KudosuGiver] = ...
    """
    
    :return: 
    """
    Post: Final[APIKudosuHistory.ModdingPost] = ...
    """
    
    :return: 
    """
    Source: Final[KudosuSource] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    class KudosuGiver(Object):
        """"""
        Url: Final[str] = ...
        """"""
        Username: Final[str] = ...
        """"""
        def __init__(self):
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
    class ModdingPost(Object):
        """"""
        Title: Final[str] = ...
        """"""
        Url: Final[str] = ...
        """"""
        def __init__(self):
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
class APIMatchmakingPool(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Active(self) -> bool:
        """
        
        :return: 
        """
    @Active.setter
    def Active(self, value: bool) -> None: ...
    @property
    def Id(self) -> int:
        """
        
        :return: 
        """
    @Id.setter
    def Id(self, value: int) -> None: ...
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def RulesetId(self) -> int:
        """
        
        :return: 
        """
    @RulesetId.setter
    def RulesetId(self, value: int) -> None: ...
    @property
    def VariantId(self) -> int:
        """
        
        :return: 
        """
    @VariantId.setter
    def VariantId(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APIMe(APIUser, IEquatable[APIUser], IEquatable[IUser], IHasOnlineID[Int32], IUser):
    """"""
    Achievements: Final[Array[APIUserAchievement]] = ...
    """
    
    :return: 
    """
    Active: Final[bool] = ...
    """
    
    :return: 
    """
    AvatarUrl: Final[str] = ...
    """
    
    :return: 
    """
    Badges: Final[Array[Badge]] = ...
    """
    
    :return: 
    """
    BeatmapPlayCountsCount: Final[int] = ...
    """
    
    :return: 
    """
    Colour: Final[str] = ...
    """
    
    :return: 
    """
    CommentsCount: Final[int] = ...
    """
    
    :return: 
    """
    Cover: Final[APIUser.UserCover] = ...
    """
    
    :return: 
    """
    DailyChallengeStatistics: Final[APIUserDailyChallengeStatistics] = ...
    """
    
    :return: 
    """
    Discord: Final[str] = ...
    """
    
    :return: 
    """
    FavouriteBeatmapsetCount: Final[int] = ...
    """
    
    :return: 
    """
    FollowerCount: Final[int] = ...
    """
    
    :return: 
    """
    GraveyardBeatmapsetCount: Final[int] = ...
    """
    
    :return: 
    """
    Groups: Final[Array[APIUserGroup]] = ...
    """
    
    :return: 
    """
    GuestBeatmapsetCount: Final[int] = ...
    """
    
    :return: 
    """
    Interests: Final[str] = ...
    """
    
    :return: 
    """
    IsAdmin: Final[bool] = ...
    """
    
    :return: 
    """
    IsBNG: Final[bool] = ...
    """
    
    :return: 
    """
    IsGMT: Final[bool] = ...
    """
    
    :return: 
    """
    IsQAT: Final[bool] = ...
    """
    
    :return: 
    """
    IsSupporter: Final[bool] = ...
    """
    
    :return: 
    """
    JoinDate: Final[DateTimeOffset] = ...
    """
    
    :return: 
    """
    Kudosu: Final[APIUser.KudosuCount] = ...
    """
    
    :return: 
    """
    LastVisit: Final[Optional[DateTimeOffset]] = ...
    """
    
    :return: 
    """
    Location: Final[str] = ...
    """
    
    :return: 
    """
    LovedBeatmapsetCount: Final[int] = ...
    """
    
    :return: 
    """
    MappingFollowerCount: Final[int] = ...
    """
    
    :return: 
    """
    MatchmakingStatistics: Final[Array[APIUserMatchmakingStatistics]] = ...
    """
    
    :return: 
    """
    MonthlyPlayCounts: Final[Array[APIUserHistoryCount]] = ...
    """
    
    :return: 
    """
    NominatedBeatmapsetCount: Final[int] = ...
    """
    
    :return: 
    """
    Occupation: Final[str] = ...
    """
    
    :return: 
    """
    PMFriendsOnly: Final[bool] = ...
    """
    
    :return: 
    """
    PendingBeatmapsetCount: Final[int] = ...
    """
    
    :return: 
    """
    PlayMode: Final[str] = ...
    """
    
    :return: 
    """
    PlayStyles: Final[Array[APIPlayStyle]] = ...
    """
    
    :return: 
    """
    PostCount: Final[int] = ...
    """
    
    :return: 
    """
    PreviousUsernames: Final[Array[str]] = ...
    """
    
    :return: 
    """
    ProfileHue: Final[Optional[int]] = ...
    """
    
    :return: 
    """
    ProfileOrder: Final[Array[str]] = ...
    """
    
    :return: 
    """
    RankHighest: Final[APIUser.UserRankHighest] = ...
    """
    
    :return: 
    """
    RankedBeatmapsetCount: Final[int] = ...
    """
    
    :return: 
    """
    ReplaysWatchedCounts: Final[Array[APIUserHistoryCount]] = ...
    """
    
    :return: 
    """
    ScoresBestCount: Final[int] = ...
    """
    
    :return: 
    """
    ScoresFirstCount: Final[int] = ...
    """
    
    :return: 
    """
    ScoresPinnedCount: Final[int] = ...
    """
    
    :return: 
    """
    ScoresRecentCount: Final[int] = ...
    """
    
    :return: 
    """
    SupportLevel: Final[int] = ...
    """
    
    :return: 
    """
    Title: Final[str] = ...
    """
    
    :return: 
    """
    TournamentBanners: Final[Array[TournamentBanner]] = ...
    """
    
    :return: 
    """
    Twitter: Final[str] = ...
    """
    
    :return: 
    """
    WasRecentlyOnline: Final[bool] = ...
    """
    
    :return: 
    """
    Website: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def CountryCode(self) -> CountryCode:
        """
        
        :return: 
        """
    @CountryCode.setter
    def CountryCode(self, value: CountryCode) -> None: ...
    @property
    def CoverUrl(self) -> str:
        """
        
        :return: 
        """
    @CoverUrl.setter
    def CoverUrl(self, value: str) -> None: ...
    @property
    def Id(self) -> int:
        """
        
        :return: 
        """
    @Id.setter
    def Id(self, value: int) -> None: ...
    @property
    def IsBot(self) -> bool:
        """
        
        :return: 
        """
    @IsBot.setter
    def IsBot(self, value: bool) -> None: ...
    @property
    def OnlineID(self) -> int:
        """
        
        :return: 
        """
    @property
    def Rank(self) -> APIUser.GlobalRank:
        """
        
        :return: 
        """
    @Rank.setter
    def Rank(self, value: APIUser.GlobalRank) -> None: ...
    @property
    def RulesetsStatistics(self) -> Dictionary[str, UserStatistics]:
        """
        
        :return: 
        """
    @RulesetsStatistics.setter
    def RulesetsStatistics(self, value: Dictionary[str, UserStatistics]) -> None: ...
    @property
    def SessionVerificationMethod(self) -> Optional[SessionVerificationMethod]:
        """
        
        :return: 
        """
    @SessionVerificationMethod.setter
    def SessionVerificationMethod(self, value: Optional[SessionVerificationMethod]) -> None: ...
    @property
    def Statistics(self) -> UserStatistics:
        """
        
        :return: 
        """
    @Statistics.setter
    def Statistics(self, value: UserStatistics) -> None: ...
    @property
    def Team(self) -> APITeam:
        """
        
        :return: 
        """
    @Team.setter
    def Team(self, value: APITeam) -> None: ...
    @property
    def Username(self) -> str:
        """
        
        :return: 
        """
    @Username.setter
    def Username(self, value: str) -> None: ...
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: APIUser) -> bool:
        """"""
    @overload
    def Equals(self, other: IUser) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APIMenuContent(Object, IEquatable[APIMenuContent]):
    """"""
    def __init__(self):
        """"""
    @property
    def Images(self) -> Array[APIMenuImage]:
        """
        
        :return: 
        """
    @Images.setter
    def Images(self, value: Array[APIMenuImage]) -> None: ...
    @overload
    def Equals(self, other: object) -> bool:
        """"""
    @overload
    def Equals(self, other: APIMenuContent) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APIMenuImage(Object, IEquatable[APIMenuImage]):
    """"""
    def __init__(self):
        """"""
    @property
    def Begins(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @Begins.setter
    def Begins(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def Expires(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @Expires.setter
    def Expires(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def Image(self) -> str:
        """
        
        :return: 
        """
    @Image.setter
    def Image(self, value: str) -> None: ...
    @property
    def IsCurrent(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Url(self) -> str:
        """
        
        :return: 
        """
    @Url.setter
    def Url(self, value: str) -> None: ...
    @overload
    def Equals(self, other: object) -> bool:
        """"""
    @overload
    def Equals(self, other: APIMenuImage) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APINewsPost(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Author(self) -> str:
        """
        
        :return: 
        """
    @Author.setter
    def Author(self, value: str) -> None: ...
    @property
    def EditUrl(self) -> str:
        """
        
        :return: 
        """
    @EditUrl.setter
    def EditUrl(self, value: str) -> None: ...
    @property
    def FirstImage(self) -> str:
        """
        
        :return: 
        """
    @FirstImage.setter
    def FirstImage(self, value: str) -> None: ...
    @property
    def Id(self) -> int:
        """
        
        :return: 
        """
    @Id.setter
    def Id(self, value: int) -> None: ...
    @property
    def Preview(self) -> str:
        """
        
        :return: 
        """
    @Preview.setter
    def Preview(self, value: str) -> None: ...
    @property
    def PublishedAt(self) -> DateTimeOffset:
        """
        
        :return: 
        """
    @PublishedAt.setter
    def PublishedAt(self, value: DateTimeOffset) -> None: ...
    @property
    def Slug(self) -> str:
        """
        
        :return: 
        """
    @Slug.setter
    def Slug(self, value: str) -> None: ...
    @property
    def Title(self) -> str:
        """
        
        :return: 
        """
    @Title.setter
    def Title(self, value: str) -> None: ...
    @property
    def UpdatedAt(self) -> DateTimeOffset:
        """
        
        :return: 
        """
    @UpdatedAt.setter
    def UpdatedAt(self, value: DateTimeOffset) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APINewsSidebar(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def CurrentYear(self) -> int:
        """
        
        :return: 
        """
    @CurrentYear.setter
    def CurrentYear(self, value: int) -> None: ...
    @property
    def NewsPosts(self) -> IEnumerable[APINewsPost]:
        """
        
        :return: 
        """
    @NewsPosts.setter
    def NewsPosts(self, value: IEnumerable[APINewsPost]) -> None: ...
    @property
    def Years(self) -> Array[int]:
        """
        
        :return: 
        """
    @Years.setter
    def Years(self, value: Array[int]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APINotification(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def CreatedAt(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @CreatedAt.setter
    def CreatedAt(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def Details(self) -> JObject:
        """
        
        :return: 
        """
    @Details.setter
    def Details(self, value: JObject) -> None: ...
    @property
    def Id(self) -> int:
        """
        
        :return: 
        """
    @Id.setter
    def Id(self, value: int) -> None: ...
    @property
    def IsRead(self) -> bool:
        """
        
        :return: 
        """
    @IsRead.setter
    def IsRead(self, value: bool) -> None: ...
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def ObjectId(self) -> str:
        """
        
        :return: 
        """
    @ObjectId.setter
    def ObjectId(self, value: str) -> None: ...
    @property
    def ObjectType(self) -> str:
        """
        
        :return: 
        """
    @ObjectType.setter
    def ObjectType(self, value: str) -> None: ...
    @property
    def SourceUserId(self) -> Optional[int]:
        """
        
        :return: 
        """
    @SourceUserId.setter
    def SourceUserId(self, value: Optional[int]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APINotificationsBundle(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Endpoint(self) -> str:
        """
        
        :return: 
        """
    @Endpoint.setter
    def Endpoint(self, value: str) -> None: ...
    @property
    def HasMore(self) -> bool:
        """
        
        :return: 
        """
    @HasMore.setter
    def HasMore(self, value: bool) -> None: ...
    @property
    def Notifications(self) -> Array[APINotification]:
        """
        
        :return: 
        """
    @Notifications.setter
    def Notifications(self, value: Array[APINotification]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APIPlayStyle(Enum):
    """"""
    Keyboard: APIPlayStyle = ...
    """"""
    Mouse: APIPlayStyle = ...
    """"""
    Tablet: APIPlayStyle = ...
    """"""
    Touch: APIPlayStyle = ...
    """"""
class APIRankHistory(Object):
    """"""
    Data: Final[Array[int]] = ...
    """
    
    :return: 
    """
    Mode: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APIRecentActivity(Object):
    """"""
    Achievement: Final[APIRecentActivity.RecentActivityAchievement] = ...
    """
    
    :return: 
    """
    Approval: Final[BeatmapApproval] = ...
    """
    
    :return: 
    """
    Beatmap: Final[APIRecentActivity.RecentActivityBeatmap] = ...
    """
    
    :return: 
    """
    Beatmapset: Final[APIRecentActivity.RecentActivityBeatmap] = ...
    """
    
    :return: 
    """
    Count: Final[int] = ...
    """
    
    :return: 
    """
    CreatedAt: Final[DateTimeOffset] = ...
    """
    
    :return: 
    """
    ID: Final[int] = ...
    """
    
    :return: 
    """
    Mode: Final[str] = ...
    """
    
    :return: 
    """
    Rank: Final[int] = ...
    """
    
    :return: 
    """
    ScoreRank: Final[ScoreRank] = ...
    """
    
    :return: 
    """
    Type: Final[RecentActivityType] = ...
    """
    
    :return: 
    """
    User: Final[APIRecentActivity.RecentActivityUser] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    class RecentActivityAchievement(Object):
        """"""
        Name: Final[str] = ...
        """"""
        Slug: Final[str] = ...
        """"""
        def __init__(self):
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
    class RecentActivityBeatmap(Object):
        """"""
        Title: Final[str] = ...
        """"""
        Url: Final[str] = ...
        """"""
        def __init__(self):
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
    class RecentActivityUser(Object):
        """"""
        PreviousUsername: Final[str] = ...
        """"""
        Url: Final[str] = ...
        """"""
        Username: Final[str] = ...
        """"""
        def __init__(self):
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
class APIRelation(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Mutual(self) -> bool:
        """
        
        :return: 
        """
    @Mutual.setter
    def Mutual(self, value: bool) -> None: ...
    @property
    def RelationType(self) -> RelationType:
        """
        
        :return: 
        """
    @RelationType.setter
    def RelationType(self, value: RelationType) -> None: ...
    @property
    def TargetID(self) -> int:
        """
        
        :return: 
        """
    @TargetID.setter
    def TargetID(self, value: int) -> None: ...
    @property
    def TargetUser(self) -> APIUser:
        """
        
        :return: 
        """
    @TargetUser.setter
    def TargetUser(self, value: APIUser) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APIScoreWithPosition(Object):
    """"""
    Position: Final[Optional[int]] = ...
    """
    
    :return: 
    """
    Score: Final[SoloScoreInfo] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    def CreateScoreInfo(self, rulesets: RulesetStore, beatmap: BeatmapInfo = ...) -> ScoreInfo:
        """
        
        :param rulesets: 
        :param beatmap: 
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
class APIScoresCollection(Object):
    """"""
    Scores: Final[List[SoloScoreInfo]] = ...
    """
    
    :return: 
    """
    ScoresCount: Final[int] = ...
    """
    
    :return: 
    """
    UserScore: Final[APIScoreWithPosition] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APISeasonalBackground(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Url(self) -> str:
        """
        
        :return: 
        """
    @Url.setter
    def Url(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APISeasonalBackgrounds(Object):
    """"""
    EndDate: Final[DateTimeOffset] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def Backgrounds(self) -> List[APISeasonalBackground]:
        """
        
        :return: 
        """
    @Backgrounds.setter
    def Backgrounds(self, value: List[APISeasonalBackground]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APISpotlight(Object):
    """"""
    EndDate: Final[DateTimeOffset] = ...
    """
    
    :return: 
    """
    Id: Final[int] = ...
    """
    
    :return: 
    """
    ModeSpecific: Final[bool] = ...
    """
    
    :return: 
    """
    Name: Final[str] = ...
    """
    
    :return: 
    """
    Participants: Final[Optional[int]] = ...
    """
    
    :return: 
    """
    StartDate: Final[DateTimeOffset] = ...
    """
    
    :return: 
    """
    Type: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APITag(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Description(self) -> str:
        """
        
        :return: 
        """
    @Description.setter
    def Description(self, value: str) -> None: ...
    @property
    def Id(self) -> int:
        """
        
        :return: 
        """
    @Id.setter
    def Id(self, value: int) -> None: ...
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def RulesetId(self) -> Optional[int]:
        """
        
        :return: 
        """
    @RulesetId.setter
    def RulesetId(self, value: Optional[int]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APITagCollection(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Tags(self) -> Array[APITag]:
        """
        
        :return: 
        """
    @Tags.setter
    def Tags(self, value: Array[APITag]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APITeam(Object):
    """"""
    FlagUrl: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def Id(self) -> int:
        """
        
        :return: 
        """
    @Id.setter
    def Id(self, value: int) -> None: ...
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def ShortName(self) -> str:
        """
        
        :return: 
        """
    @ShortName.setter
    def ShortName(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APIUpdateStream(Object, IEquatable[APIUpdateStream]):
    """"""
    def __init__(self):
        """"""
    @property
    def Colour(self) -> ColourInfo:
        """
        
        :return: 
        """
    @property
    def DisplayName(self) -> str:
        """
        
        :return: 
        """
    @DisplayName.setter
    def DisplayName(self, value: str) -> None: ...
    @property
    def Id(self) -> int:
        """
        
        :return: 
        """
    @Id.setter
    def Id(self, value: int) -> None: ...
    @property
    def IsFeatured(self) -> bool:
        """
        
        :return: 
        """
    @IsFeatured.setter
    def IsFeatured(self, value: bool) -> None: ...
    @property
    def LatestBuild(self) -> APIChangelogBuild:
        """
        
        :return: 
        """
    @LatestBuild.setter
    def LatestBuild(self, value: APIChangelogBuild) -> None: ...
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def UserCount(self) -> int:
        """
        
        :return: 
        """
    @UserCount.setter
    def UserCount(self, value: int) -> None: ...
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: APIUpdateStream) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APIUser(Object, IEquatable[APIUser], IEquatable[IUser], IHasOnlineID[Int32], IUser):
    """"""
    Achievements: Final[Array[APIUserAchievement]] = ...
    """
    
    :return: 
    """
    Active: Final[bool] = ...
    """
    
    :return: 
    """
    AvatarUrl: Final[str] = ...
    """
    
    :return: 
    """
    Badges: Final[Array[Badge]] = ...
    """
    
    :return: 
    """
    BeatmapPlayCountsCount: Final[int] = ...
    """
    
    :return: 
    """
    Colour: Final[str] = ...
    """
    
    :return: 
    """
    CommentsCount: Final[int] = ...
    """
    
    :return: 
    """
    Cover: Final[APIUser.UserCover] = ...
    """
    
    :return: 
    """
    DailyChallengeStatistics: Final[APIUserDailyChallengeStatistics] = ...
    """
    
    :return: 
    """
    Discord: Final[str] = ...
    """
    
    :return: 
    """
    FavouriteBeatmapsetCount: Final[int] = ...
    """
    
    :return: 
    """
    FollowerCount: Final[int] = ...
    """
    
    :return: 
    """
    GraveyardBeatmapsetCount: Final[int] = ...
    """
    
    :return: 
    """
    Groups: Final[Array[APIUserGroup]] = ...
    """
    
    :return: 
    """
    GuestBeatmapsetCount: Final[int] = ...
    """
    
    :return: 
    """
    Interests: Final[str] = ...
    """
    
    :return: 
    """
    IsAdmin: Final[bool] = ...
    """
    
    :return: 
    """
    IsBNG: Final[bool] = ...
    """
    
    :return: 
    """
    IsGMT: Final[bool] = ...
    """
    
    :return: 
    """
    IsQAT: Final[bool] = ...
    """
    
    :return: 
    """
    IsSupporter: Final[bool] = ...
    """
    
    :return: 
    """
    JoinDate: Final[DateTimeOffset] = ...
    """
    
    :return: 
    """
    Kudosu: Final[APIUser.KudosuCount] = ...
    """
    
    :return: 
    """
    LastVisit: Final[Optional[DateTimeOffset]] = ...
    """
    
    :return: 
    """
    Location: Final[str] = ...
    """
    
    :return: 
    """
    LovedBeatmapsetCount: Final[int] = ...
    """
    
    :return: 
    """
    MappingFollowerCount: Final[int] = ...
    """
    
    :return: 
    """
    MatchmakingStatistics: Final[Array[APIUserMatchmakingStatistics]] = ...
    """
    
    :return: 
    """
    MonthlyPlayCounts: Final[Array[APIUserHistoryCount]] = ...
    """
    
    :return: 
    """
    NominatedBeatmapsetCount: Final[int] = ...
    """
    
    :return: 
    """
    Occupation: Final[str] = ...
    """
    
    :return: 
    """
    PMFriendsOnly: Final[bool] = ...
    """
    
    :return: 
    """
    PendingBeatmapsetCount: Final[int] = ...
    """
    
    :return: 
    """
    PlayMode: Final[str] = ...
    """
    
    :return: 
    """
    PlayStyles: Final[Array[APIPlayStyle]] = ...
    """
    
    :return: 
    """
    PostCount: Final[int] = ...
    """
    
    :return: 
    """
    PreviousUsernames: Final[Array[str]] = ...
    """
    
    :return: 
    """
    ProfileHue: Final[Optional[int]] = ...
    """
    
    :return: 
    """
    ProfileOrder: Final[Array[str]] = ...
    """
    
    :return: 
    """
    RankHighest: Final[APIUser.UserRankHighest] = ...
    """
    
    :return: 
    """
    RankedBeatmapsetCount: Final[int] = ...
    """
    
    :return: 
    """
    ReplaysWatchedCounts: Final[Array[APIUserHistoryCount]] = ...
    """
    
    :return: 
    """
    SYSTEM_USER: Final[ClassVar[APIUser]] = ...
    """
    
    :return: 
    """
    SYSTEM_USER_ID: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ScoresBestCount: Final[int] = ...
    """
    
    :return: 
    """
    ScoresFirstCount: Final[int] = ...
    """
    
    :return: 
    """
    ScoresPinnedCount: Final[int] = ...
    """
    
    :return: 
    """
    ScoresRecentCount: Final[int] = ...
    """
    
    :return: 
    """
    SupportLevel: Final[int] = ...
    """
    
    :return: 
    """
    Title: Final[str] = ...
    """
    
    :return: 
    """
    TournamentBanners: Final[Array[TournamentBanner]] = ...
    """
    
    :return: 
    """
    Twitter: Final[str] = ...
    """
    
    :return: 
    """
    WasRecentlyOnline: Final[bool] = ...
    """
    
    :return: 
    """
    Website: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def CountryCode(self) -> CountryCode:
        """
        
        :return: 
        """
    @CountryCode.setter
    def CountryCode(self, value: CountryCode) -> None: ...
    @property
    def CoverUrl(self) -> str:
        """
        
        :return: 
        """
    @CoverUrl.setter
    def CoverUrl(self, value: str) -> None: ...
    @property
    def Id(self) -> int:
        """
        
        :return: 
        """
    @Id.setter
    def Id(self, value: int) -> None: ...
    @property
    def IsBot(self) -> bool:
        """
        
        :return: 
        """
    @IsBot.setter
    def IsBot(self, value: bool) -> None: ...
    @property
    def OnlineID(self) -> int:
        """
        
        :return: 
        """
    @property
    def Rank(self) -> APIUser.GlobalRank:
        """
        
        :return: 
        """
    @Rank.setter
    def Rank(self, value: APIUser.GlobalRank) -> None: ...
    @property
    def RulesetsStatistics(self) -> Dictionary[str, UserStatistics]:
        """
        
        :return: 
        """
    @RulesetsStatistics.setter
    def RulesetsStatistics(self, value: Dictionary[str, UserStatistics]) -> None: ...
    @property
    def Statistics(self) -> UserStatistics:
        """
        
        :return: 
        """
    @Statistics.setter
    def Statistics(self, value: UserStatistics) -> None: ...
    @property
    def Team(self) -> APITeam:
        """
        
        :return: 
        """
    @Team.setter
    def Team(self, value: APITeam) -> None: ...
    @property
    def Username(self) -> str:
        """
        
        :return: 
        """
    @Username.setter
    def Username(self, value: str) -> None: ...
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: APIUser) -> bool:
        """"""
    @overload
    def Equals(self, other: IUser) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def UnknownUser(cls, userId: int) -> APIUser:
        """
        
        :param userId: 
        :return: 
        """
    class GlobalRank(Object):
        """"""
        Rank: Final[Optional[int]] = ...
        """"""
        RulesetId: Final[int] = ...
        """"""
        def __init__(self):
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
    class KudosuCount(Object):
        """"""
        Available: Final[int] = ...
        """"""
        Total: Final[int] = ...
        """"""
        def __init__(self):
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
    class UserCover(Object):
        """"""
        CustomUrl: Final[str] = ...
        """"""
        Id: Final[Optional[int]] = ...
        """"""
        Url: Final[str] = ...
        """"""
        def __init__(self):
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
    class UserRankHighest(Object):
        """"""
        Rank: Final[int] = ...
        """"""
        UpdatedAt: Final[DateTimeOffset] = ...
        """"""
        def __init__(self):
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
class APIUserAchievement(Object):
    """"""
    AchievedAt: Final[DateTimeOffset] = ...
    """
    
    :return: 
    """
    ID: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APIUserContainer(Object):
    """"""
    User: Final[APIUser] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APIUserDailyChallengeStatistics(Object):
    """"""
    DailyStreakBest: Final[int] = ...
    """
    
    :return: 
    """
    DailyStreakCurrent: Final[int] = ...
    """
    
    :return: 
    """
    LastUpdate: Final[Optional[DateTimeOffset]] = ...
    """
    
    :return: 
    """
    LastWeeklyStreak: Final[Optional[DateTimeOffset]] = ...
    """
    
    :return: 
    """
    PlayCount: Final[int] = ...
    """
    
    :return: 
    """
    Top10PercentPlacements: Final[int] = ...
    """
    
    :return: 
    """
    Top50PercentPlacements: Final[int] = ...
    """
    
    :return: 
    """
    UserID: Final[int] = ...
    """
    
    :return: 
    """
    WeeklyStreakBest: Final[int] = ...
    """
    
    :return: 
    """
    WeeklyStreakCurrent: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APIUserGroup(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Colour(self) -> str:
        """
        
        :return: 
        """
    @Colour.setter
    def Colour(self, value: str) -> None: ...
    @property
    def HasListings(self) -> bool:
        """
        
        :return: 
        """
    @HasListings.setter
    def HasListings(self, value: bool) -> None: ...
    @property
    def HasPlaymodes(self) -> bool:
        """
        
        :return: 
        """
    @HasPlaymodes.setter
    def HasPlaymodes(self, value: bool) -> None: ...
    @property
    def Id(self) -> int:
        """
        
        :return: 
        """
    @Id.setter
    def Id(self, value: int) -> None: ...
    @property
    def Identifier(self) -> str:
        """
        
        :return: 
        """
    @Identifier.setter
    def Identifier(self, value: str) -> None: ...
    @property
    def IsProbationary(self) -> bool:
        """
        
        :return: 
        """
    @IsProbationary.setter
    def IsProbationary(self, value: bool) -> None: ...
    @property
    def Name(self) -> str:
        """
        
        :return: 
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Playmodes(self) -> Array[str]:
        """
        
        :return: 
        """
    @Playmodes.setter
    def Playmodes(self, value: Array[str]) -> None: ...
    @property
    def ShortName(self) -> str:
        """
        
        :return: 
        """
    @ShortName.setter
    def ShortName(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APIUserHistoryCount(Object):
    """"""
    Count: Final[int] = ...
    """
    
    :return: 
    """
    Date: Final[DateTime] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APIUserMatchmakingStatistics(Object):
    """"""
    UserId: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def FirstPlacements(self) -> int:
        """
        
        :return: 
        """
    @FirstPlacements.setter
    def FirstPlacements(self, value: int) -> None: ...
    @property
    def IsRatingProvisional(self) -> bool:
        """
        
        :return: 
        """
    @IsRatingProvisional.setter
    def IsRatingProvisional(self, value: bool) -> None: ...
    @property
    def Plays(self) -> int:
        """
        
        :return: 
        """
    @Plays.setter
    def Plays(self, value: int) -> None: ...
    @property
    def Pool(self) -> APIMatchmakingPool:
        """
        
        :return: 
        """
    @Pool.setter
    def Pool(self, value: APIMatchmakingPool) -> None: ...
    @property
    def PoolId(self) -> int:
        """
        
        :return: 
        """
    @PoolId.setter
    def PoolId(self, value: int) -> None: ...
    @property
    def Rank(self) -> Optional[int]:
        """
        
        :return: 
        """
    @Rank.setter
    def Rank(self, value: Optional[int]) -> None: ...
    @property
    def Rating(self) -> int:
        """
        
        :return: 
        """
    @Rating.setter
    def Rating(self, value: int) -> None: ...
    @property
    def TotalPoints(self) -> int:
        """
        
        :return: 
        """
    @TotalPoints.setter
    def TotalPoints(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APIUserMostPlayedBeatmap(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def BeatmapID(self) -> int:
        """
        
        :return: 
        """
    @BeatmapID.setter
    def BeatmapID(self, value: int) -> None: ...
    @property
    def BeatmapInfo(self) -> APIBeatmap:
        """
        
        :return: 
        """
    @property
    def BeatmapSet(self) -> APIBeatmapSet:
        """
        
        :return: 
        """
    @BeatmapSet.setter
    def BeatmapSet(self, value: APIBeatmapSet) -> None: ...
    @property
    def PlayCount(self) -> int:
        """
        
        :return: 
        """
    @PlayCount.setter
    def PlayCount(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class APIUserScoreAggregate(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Accuracy(self) -> float:
        """
        
        :return: 
        """
    @Accuracy.setter
    def Accuracy(self, value: float) -> None: ...
    @property
    def CompletedBeatmaps(self) -> int:
        """
        
        :return: 
        """
    @CompletedBeatmaps.setter
    def CompletedBeatmaps(self, value: int) -> None: ...
    @property
    def PP(self) -> Optional[float]:
        """
        
        :return: 
        """
    @PP.setter
    def PP(self, value: Optional[float]) -> None: ...
    @property
    def Position(self) -> Optional[int]:
        """
        
        :return: 
        """
    @Position.setter
    def Position(self, value: Optional[int]) -> None: ...
    @property
    def RoomID(self) -> int:
        """
        
        :return: 
        """
    @RoomID.setter
    def RoomID(self, value: int) -> None: ...
    @property
    def TotalAttempts(self) -> int:
        """
        
        :return: 
        """
    @TotalAttempts.setter
    def TotalAttempts(self, value: int) -> None: ...
    @property
    def TotalScore(self) -> int:
        """
        
        :return: 
        """
    @TotalScore.setter
    def TotalScore(self, value: int) -> None: ...
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
    @UserID.setter
    def UserID(self, value: int) -> None: ...
    def CreateScoreInfo(self) -> ScoreInfo:
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
class APIWikiPage(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Layout(self) -> str:
        """
        
        :return: 
        """
    @Layout.setter
    def Layout(self, value: str) -> None: ...
    @property
    def Locale(self) -> str:
        """
        
        :return: 
        """
    @Locale.setter
    def Locale(self, value: str) -> None: ...
    @property
    def Markdown(self) -> str:
        """
        
        :return: 
        """
    @Markdown.setter
    def Markdown(self, value: str) -> None: ...
    @property
    def Path(self) -> str:
        """
        
        :return: 
        """
    @Path.setter
    def Path(self, value: str) -> None: ...
    @property
    def Subtitle(self) -> str:
        """
        
        :return: 
        """
    @Subtitle.setter
    def Subtitle(self, value: str) -> None: ...
    @property
    def Tags(self) -> List[str]:
        """
        
        :return: 
        """
    @Tags.setter
    def Tags(self, value: List[str]) -> None: ...
    @property
    def Title(self) -> str:
        """
        
        :return: 
        """
    @Title.setter
    def Title(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class BeatmapSetFile(ValueType):
    """"""
    @property
    def Filename(self) -> str:
        """
        
        :return: 
        """
    @Filename.setter
    def Filename(self, value: str) -> None: ...
    @property
    def SHA2Hash(self) -> str:
        """
        
        :return: 
        """
    @SHA2Hash.setter
    def SHA2Hash(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class ChangelogEntryType(Enum):
    """"""
    Add: ChangelogEntryType = ...
    """"""
    Fix: ChangelogEntryType = ...
    """"""
    Misc: ChangelogEntryType = ...
    """"""
class ChatAckResponse(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Silences(self) -> Array[ChatSilence]:
        """
        
        :return: 
        """
    @Silences.setter
    def Silences(self, value: Array[ChatSilence]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class ChatSilence(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Id(self) -> int:
        """
        
        :return: 
        """
    @Id.setter
    def Id(self, value: int) -> None: ...
    @property
    def UserId(self) -> int:
        """
        
        :return: 
        """
    @UserId.setter
    def UserId(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class Comment(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def CommentableId(self) -> int:
        """
        
        :return: 
        """
    @CommentableId.setter
    def CommentableId(self, value: int) -> None: ...
    @property
    def CommentableType(self) -> str:
        """
        
        :return: 
        """
    @CommentableType.setter
    def CommentableType(self, value: str) -> None: ...
    @property
    def CreatedAt(self) -> DateTimeOffset:
        """
        
        :return: 
        """
    @CreatedAt.setter
    def CreatedAt(self, value: DateTimeOffset) -> None: ...
    @property
    def DeletedAt(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @DeletedAt.setter
    def DeletedAt(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def EditedAt(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @EditedAt.setter
    def EditedAt(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def EditedById(self) -> Optional[int]:
        """
        
        :return: 
        """
    @EditedById.setter
    def EditedById(self, value: Optional[int]) -> None: ...
    @property
    def EditedUser(self) -> APIUser:
        """
        
        :return: 
        """
    @EditedUser.setter
    def EditedUser(self, value: APIUser) -> None: ...
    @property
    def HasMessage(self) -> bool:
        """
        
        :return: 
        """
    @property
    def Id(self) -> int:
        """
        
        :return: 
        """
    @Id.setter
    def Id(self, value: int) -> None: ...
    @property
    def IsDeleted(self) -> bool:
        """
        
        :return: 
        """
    @property
    def IsTopLevel(self) -> bool:
        """
        
        :return: 
        """
    @property
    def IsVoted(self) -> bool:
        """
        
        :return: 
        """
    @IsVoted.setter
    def IsVoted(self, value: bool) -> None: ...
    @property
    def LegacyName(self) -> str:
        """
        
        :return: 
        """
    @LegacyName.setter
    def LegacyName(self, value: str) -> None: ...
    @property
    def Message(self) -> str:
        """
        
        :return: 
        """
    @Message.setter
    def Message(self, value: str) -> None: ...
    @property
    def MessageHtml(self) -> str:
        """
        
        :return: 
        """
    @MessageHtml.setter
    def MessageHtml(self, value: str) -> None: ...
    @property
    def ParentComment(self) -> Comment:
        """
        
        :return: 
        """
    @ParentComment.setter
    def ParentComment(self, value: Comment) -> None: ...
    @property
    def ParentId(self) -> Optional[int]:
        """
        
        :return: 
        """
    @ParentId.setter
    def ParentId(self, value: Optional[int]) -> None: ...
    @property
    def Pinned(self) -> bool:
        """
        
        :return: 
        """
    @Pinned.setter
    def Pinned(self, value: bool) -> None: ...
    @property
    def RepliesCount(self) -> int:
        """
        
        :return: 
        """
    @RepliesCount.setter
    def RepliesCount(self, value: int) -> None: ...
    @property
    def UpdatedAt(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @UpdatedAt.setter
    def UpdatedAt(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def User(self) -> APIUser:
        """
        
        :return: 
        """
    @User.setter
    def User(self, value: APIUser) -> None: ...
    @property
    def UserId(self) -> Optional[int]:
        """
        
        :return: 
        """
    @UserId.setter
    def UserId(self, value: Optional[int]) -> None: ...
    @property
    def VotesCount(self) -> int:
        """
        
        :return: 
        """
    @VotesCount.setter
    def VotesCount(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class CommentBundle(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def CommentableMeta(self) -> List[CommentableMeta]:
        """
        
        :return: 
        """
    @CommentableMeta.setter
    def CommentableMeta(self, value: List[CommentableMeta]) -> None: ...
    @property
    def Comments(self) -> List[Comment]:
        """
        
        :return: 
        """
    @Comments.setter
    def Comments(self, value: List[Comment]) -> None: ...
    @property
    def HasMore(self) -> bool:
        """
        
        :return: 
        """
    @HasMore.setter
    def HasMore(self, value: bool) -> None: ...
    @property
    def HasMoreId(self) -> Optional[int]:
        """
        
        :return: 
        """
    @HasMoreId.setter
    def HasMoreId(self, value: Optional[int]) -> None: ...
    @property
    def IncludedComments(self) -> List[Comment]:
        """
        
        :return: 
        """
    @IncludedComments.setter
    def IncludedComments(self, value: List[Comment]) -> None: ...
    @property
    def PinnedComments(self) -> List[Comment]:
        """
        
        :return: 
        """
    @PinnedComments.setter
    def PinnedComments(self, value: List[Comment]) -> None: ...
    @property
    def TopLevelCount(self) -> int:
        """
        
        :return: 
        """
    @TopLevelCount.setter
    def TopLevelCount(self, value: int) -> None: ...
    @property
    def Total(self) -> int:
        """
        
        :return: 
        """
    @Total.setter
    def Total(self, value: int) -> None: ...
    @property
    def UserFollow(self) -> bool:
        """
        
        :return: 
        """
    @UserFollow.setter
    def UserFollow(self, value: bool) -> None: ...
    @property
    def UserVotes(self) -> List[int]:
        """
        
        :return: 
        """
    @UserVotes.setter
    def UserVotes(self, value: List[int]) -> None: ...
    @property
    def Users(self) -> List[APIUser]:
        """
        
        :return: 
        """
    @Users.setter
    def Users(self, value: List[APIUser]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class CommentableMeta(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def CurrentUserAttributes(self) -> Optional[CommentableMeta.CommentableCurrentUserAttributes]:
        """
        
        :return: 
        """
    @CurrentUserAttributes.setter
    def CurrentUserAttributes(self, value: Optional[CommentableMeta.CommentableCurrentUserAttributes]) -> None: ...
    @property
    def Id(self) -> int:
        """
        
        :return: 
        """
    @Id.setter
    def Id(self, value: int) -> None: ...
    @property
    def OwnerId(self) -> Optional[int]:
        """
        
        :return: 
        """
    @OwnerId.setter
    def OwnerId(self, value: Optional[int]) -> None: ...
    @property
    def OwnerTitle(self) -> str:
        """
        
        :return: 
        """
    @OwnerTitle.setter
    def OwnerTitle(self, value: str) -> None: ...
    @property
    def Title(self) -> str:
        """
        
        :return: 
        """
    @Title.setter
    def Title(self, value: str) -> None: ...
    @property
    def Type(self) -> str:
        """
        
        :return: 
        """
    @Type.setter
    def Type(self, value: str) -> None: ...
    @property
    def Url(self) -> str:
        """
        
        :return: 
        """
    @Url.setter
    def Url(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    class CommentableCurrentUserAttributes(ValueType):
        """"""
        @property
        def CanNewCommentReason(self) -> str:
            """"""
        @CanNewCommentReason.setter
        def CanNewCommentReason(self, value: str) -> None: ...
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
class GetChannelResponse(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def Channel(self) -> Channel:
        """
        
        :return: 
        """
    @Channel.setter
    def Channel(self, value: Channel) -> None: ...
    @property
    def Users(self) -> List[APIUser]:
        """
        
        :return: 
        """
    @Users.setter
    def Users(self, value: List[APIUser]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class GetMyFavouriteBeatmapSetsResponse(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def BeatmapSetIds(self) -> Array[int]:
        """
        
        :return: 
        """
    @BeatmapSetIds.setter
    def BeatmapSetIds(self, value: Array[int]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class KudosuAction(Enum):
    """"""
    Give: KudosuAction = ...
    """"""
    Reset: KudosuAction = ...
    """"""
    Revoke: KudosuAction = ...
    """"""
class KudosuSource(Enum):
    """"""
    Unknown: KudosuSource = ...
    """"""
    AllowKudosu: KudosuSource = ...
    """"""
    Delete: KudosuSource = ...
    """"""
    DenyKudosu: KudosuSource = ...
    """"""
    Forum: KudosuSource = ...
    """"""
    Recalculate: KudosuSource = ...
    """"""
    Restore: KudosuSource = ...
    """"""
    Vote: KudosuSource = ...
    """"""
class PutBeatmapSetResponse(Object):
    """"""
    def __init__(self):
        """"""
    @property
    def BeatmapIds(self) -> ICollection[int]:
        """
        
        :return: 
        """
    @BeatmapIds.setter
    def BeatmapIds(self, value: ICollection[int]) -> None: ...
    @property
    def BeatmapSetId(self) -> int:
        """
        
        :return: 
        """
    @BeatmapSetId.setter
    def BeatmapSetId(self, value: int) -> None: ...
    @property
    def Files(self) -> ICollection[BeatmapSetFile]:
        """
        
        :return: 
        """
    @Files.setter
    def Files(self, value: ICollection[BeatmapSetFile]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class RelationType(Enum):
    """"""
    Friend: RelationType = ...
    """"""
    Block: RelationType = ...
    """"""
class SessionVerificationMethod(Enum):
    """"""
    TimedOneTimePassword: SessionVerificationMethod = ...
    """"""
    EmailMessage: SessionVerificationMethod = ...
    """"""
class SoloScoreInfo(Object, IHasOnlineID[Int64], IScoreInfo):
    """"""
    def __init__(self):
        """"""
    @property
    def Accuracy(self) -> float:
        """
        
        :return: 
        """
    @Accuracy.setter
    def Accuracy(self, value: float) -> None: ...
    @property
    def Beatmap(self) -> APIBeatmap:
        """
        
        :return: 
        """
    @Beatmap.setter
    def Beatmap(self, value: APIBeatmap) -> None: ...
    @property
    def BeatmapID(self) -> int:
        """
        
        :return: 
        """
    @BeatmapID.setter
    def BeatmapID(self, value: int) -> None: ...
    @property
    def BeatmapSet(self) -> APIBeatmapSet:
        """
        
        :return: 
        """
    @BeatmapSet.setter
    def BeatmapSet(self, value: APIBeatmapSet) -> None: ...
    @property
    def BuildID(self) -> Optional[int]:
        """
        
        :return: 
        """
    @BuildID.setter
    def BuildID(self, value: Optional[int]) -> None: ...
    @property
    def CreatedAt(self) -> DateTimeOffset:
        """
        
        :return: 
        """
    @CreatedAt.setter
    def CreatedAt(self, value: DateTimeOffset) -> None: ...
    @property
    def Date(self) -> DateTimeOffset:
        """
        
        :return: 
        """
    @property
    def DeletedAt(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @DeletedAt.setter
    def DeletedAt(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def EndedAt(self) -> DateTimeOffset:
        """
        
        :return: 
        """
    @EndedAt.setter
    def EndedAt(self, value: DateTimeOffset) -> None: ...
    @property
    def HasReplay(self) -> bool:
        """
        
        :return: 
        """
    @HasReplay.setter
    def HasReplay(self, value: bool) -> None: ...
    @property
    def ID(self) -> Optional[int]:
        """
        
        :return: 
        """
    @ID.setter
    def ID(self, value: Optional[int]) -> None: ...
    @property
    def IsLegacyScore(self) -> bool:
        """
        
        :return: 
        """
    @property
    def LegacyOnlineID(self) -> int:
        """
        
        :return: 
        """
    @property
    def LegacyScoreId(self) -> Optional[int]:
        """
        
        :return: 
        """
    @LegacyScoreId.setter
    def LegacyScoreId(self, value: Optional[int]) -> None: ...
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
    def Mods(self) -> Array[APIMod]:
        """
        
        :return: 
        """
    @Mods.setter
    def Mods(self, value: Array[APIMod]) -> None: ...
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
    def Pauses(self) -> Array[int]:
        """
        
        :return: 
        """
    @Pauses.setter
    def Pauses(self, value: Array[int]) -> None: ...
    @property
    def Preserve(self) -> bool:
        """
        
        :return: 
        """
    @Preserve.setter
    def Preserve(self, value: bool) -> None: ...
    @property
    def Processed(self) -> bool:
        """
        
        :return: 
        """
    @Processed.setter
    def Processed(self, value: bool) -> None: ...
    @property
    def Rank(self) -> ScoreRank:
        """
        
        :return: 
        """
    @Rank.setter
    def Rank(self, value: ScoreRank) -> None: ...
    @property
    def Ranked(self) -> bool:
        """
        
        :return: 
        """
    @Ranked.setter
    def Ranked(self, value: bool) -> None: ...
    @property
    def Ruleset(self) -> IRulesetInfo:
        """
        
        :return: 
        """
    @property
    def RulesetID(self) -> int:
        """
        
        :return: 
        """
    @RulesetID.setter
    def RulesetID(self, value: int) -> None: ...
    @property
    def StartedAt(self) -> Optional[DateTimeOffset]:
        """
        
        :return: 
        """
    @StartedAt.setter
    def StartedAt(self, value: Optional[DateTimeOffset]) -> None: ...
    @property
    def Statistics(self) -> Dictionary[HitResult, int]:
        """
        
        :return: 
        """
    @Statistics.setter
    def Statistics(self, value: Dictionary[HitResult, int]) -> None: ...
    @property
    def TotalScore(self) -> int:
        """
        
        :return: 
        """
    @TotalScore.setter
    def TotalScore(self, value: int) -> None: ...
    @property
    def TotalScoreWithoutMods(self) -> int:
        """
        
        :return: 
        """
    @TotalScoreWithoutMods.setter
    def TotalScoreWithoutMods(self, value: int) -> None: ...
    @property
    def UpdatedAt(self) -> DateTimeOffset:
        """
        
        :return: 
        """
    @UpdatedAt.setter
    def UpdatedAt(self, value: DateTimeOffset) -> None: ...
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
    @UserID.setter
    def UserID(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def ForSubmission(cls, score: ScoreInfo) -> SoloScoreInfo:
        """
        
        :param score: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ShouldSerializeBeatmap(self) -> bool:
        """
        
        :return: 
        """
    def ShouldSerializeBeatmapID(self) -> bool:
        """
        
        :return: 
        """
    def ShouldSerializeBeatmapSet(self) -> bool:
        """
        
        :return: 
        """
    def ShouldSerializeBuildID(self) -> bool:
        """
        
        :return: 
        """
    def ShouldSerializeEndedAt(self) -> bool:
        """
        
        :return: 
        """
    def ShouldSerializeHasReplay(self) -> bool:
        """
        
        :return: 
        """
    def ShouldSerializeID(self) -> bool:
        """
        
        :return: 
        """
    def ShouldSerializeLegacyScoreId(self) -> bool:
        """
        
        :return: 
        """
    def ShouldSerializeLegacyTotalScore(self) -> bool:
        """
        
        :return: 
        """
    def ShouldSerializeMods(self) -> bool:
        """
        
        :return: 
        """
    def ShouldSerializeOnlineID(self) -> bool:
        """
        
        :return: 
        """
    def ShouldSerializePP(self) -> bool:
        """
        
        :return: 
        """
    def ShouldSerializePreserve(self) -> bool:
        """
        
        :return: 
        """
    def ShouldSerializeProcessed(self) -> bool:
        """
        
        :return: 
        """
    def ShouldSerializeStartedAt(self) -> bool:
        """
        
        :return: 
        """
    def ShouldSerializeUser(self) -> bool:
        """
        
        :return: 
        """
    def ShouldSerializeUserID(self) -> bool:
        """
        
        :return: 
        """
    @overload
    def ToScoreInfo(self, mods: Array[Mod], beatmap: IBeatmapInfo = ...) -> ScoreInfo:
        """
        
        :param mods: 
        :param beatmap: 
        :return: 
        """
    @overload
    def ToScoreInfo(self, rulesets: RulesetStore, beatmap: BeatmapInfo = ...) -> ScoreInfo:
        """
        
        :param rulesets: 
        :param beatmap: 
        :return: 
        """
    def ToString(self) -> str:
        """"""