from System import Action
from System import Array
from System.Collections.Generic import ICollection
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IReadOnlyCollection
from System.Collections.Generic import IReadOnlyList
from System.Collections.Generic import List
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections.ObjectModel import ObservableCollection
from System import DateTimeOffset
from System import Enum
from System import Exception
from System import Func
from System import IComparable
from System import IDisposable
from System import IEquatable
from System import Object
from System import Predicate
from System.Reflection import MethodBase
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System import String
from System.Text.RegularExpressions import Match
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Framework.Allocation import IDependencyActivatorRegistry
from osu.Framework.Allocation import IDependencyInjectionCandidate
from osu.Framework.Allocation import IReadOnlyDependencyContainer
from osu.Framework.Allocation import ISourceGeneratedDependencyActivator
from osu.Framework.Allocation import ISourceGeneratedLongRunningLoadCache
from osu.Framework.Bindables import Bindable
from osu.Framework.Bindables import BindableBool
from osu.Framework.Bindables import IBindableList
from osu.Framework.Graphics import Anchor
from osu.Framework.Graphics import Axes
from osu.Framework.Graphics import BlendingParameters
from osu.Framework.Graphics.Colour import ColourInfo
from osu.Framework.Graphics import Component
from osu.Framework.Graphics.Containers import CompositeComponent
from osu.Framework.Graphics.Containers import CompositeDrawable
from osu.Framework.Graphics.Containers import Container
from osu.Framework.Graphics.Containers.Container import Enumerator
from osu.Framework.Graphics.Containers import IContainer
from osu.Framework.Graphics.Containers import IContainerCollection
from osu.Framework.Graphics.Containers import IContainerEnumerable
from osu.Framework.Graphics.Containers import ITabbableContainer
from osu.Framework.Graphics.Containers import ITextPart
from osu.Framework.Graphics.Containers import Visibility
from osu.Framework.Graphics.Cursor import IHasTooltip
from osu.Framework.Graphics.Cursor import ITooltipContentProvider
from osu.Framework.Graphics import DrawColourInfo
from osu.Framework.Graphics import DrawInfo
from osu.Framework.Graphics import Drawable
from osu.Framework.Graphics import Easing
from osu.Framework.Graphics.Effects import EdgeEffectParameters
from osu.Framework.Graphics.Effects import IEffect
from osu.Framework.Graphics import FillMode
from osu.Framework.Graphics import IDrawable
from osu.Framework.Graphics import Invalidation
from osu.Framework.Graphics import LoadState
from osu.Framework.Graphics import MarginPadding
from osu.Framework.Graphics.Primitives import Quad
from osu.Framework.Graphics.Primitives import RectangleF
from osu.Framework.Graphics.Sprites import IconUsage
from osu.Framework.Graphics.Transforms import ITransformable
from osu.Framework.Graphics.Transforms import Transform
from osu.Framework.Graphics.UserInterface import IHasCurrentValue
from osu.Framework.Graphics.UserInterface.TextBox import OnCommitHandler
from osu.Framework.Input.Bindings import IKeyBindingHandler
from osu.Framework.Input.Events import KeyBindingPressEvent
from osu.Framework.Input.Events import KeyBindingReleaseEvent
from osu.Framework.Input.Events import UIEvent
from osu.Framework.Input import ICanSuppressKeyEventLogging
from osu.Framework.Input import ISourceGeneratedHandleInputCache
from osu.Framework.Input import PlatformAction
from osu.Framework.Input import TextInputProperties
from osu.Framework.Layout import InvalidationSource
from osu.Framework.Lists import SlimReadOnlyListWrapper
from osu.Framework.Lists import SortedList
from osu.Framework.Localisation import LocalisableString
from osu.Framework.Timing import FrameTimeInfo
from osu.Framework.Timing import IFrameBasedClock
from osu.Game.Graphics.Containers import OsuHoverContainer
from osu.Game.Graphics.UserInterface import HistoryTextBox
from osu.Game.Input.Bindings import GlobalAction
from osu.Game.Online.API import IAPIProvider
from osu.Game.Online.API.Requests.Responses import APIUser
from osu.Game.Online.Chat.MessageFormatter import MessageFormatterResult
from osu.Game.Overlays.Chat import ChatLine
from osu.Game.Overlays.Chat import DrawableChannel
from osu.Game.Overlays.Dialog import PopupDialog
from osu.Game.Overlays.Dialog import PopupDialogButton
from osu.Game.Overlays.Notifications import UserAvatarNotification
from osuTK.Graphics import Color4
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
class Channel(Object):
    """"""
    HighlightedMessage: Final[Bindable[Message]] = ...
    """
    
    :return: 
    """
    Id: Final[int] = ...
    """
    
    :return: 
    """
    Joined: Final[Bindable[bool]] = ...
    """
    
    :return: 
    """
    LastMessageId: Final[Optional[int]] = ...
    """
    
    :return: 
    """
    LastReadId: Final[Optional[int]] = ...
    """
    
    :return: 
    """
    MAX_HISTORY: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MessageLengthLimit: Final[Optional[int]] = ...
    """
    
    :return: 
    """
    Messages: Final[SortedList[Message]] = ...
    """
    
    :return: 
    """
    MessagesLoaded: Final[bool] = ...
    """
    
    :return: 
    """
    Name: Final[str] = ...
    """
    
    :return: 
    """
    TextBoxMessage: Final[Bindable[str]] = ...
    """
    
    :return: 
    """
    Topic: Final[str] = ...
    """
    
    :return: 
    """
    Type: Final[ChannelType] = ...
    """
    
    :return: 
    """
    Users: Final[ObservableCollection[APIUser]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, user: APIUser):
        """
        
        :param user: 
        """
    @property
    def ReadOnly(self) -> bool:
        """
        
        :return: 
        """
    @property
    def UnreadMessages(self) -> IEnumerable[Message]:
        """
        
        :return: 
        """
    def AddLocalEcho(self, message: LocalEchoMessage) -> None:
        """
        
        :param message: 
        """
    def AddNewMessages(self, messages: Array[Message]) -> None:
        """
        
        :param messages: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def RemoveMessagesFromUser(self, userId: int) -> None:
        """
        
        :param userId: 
        """
    def ReplaceMessage(self, echo: LocalEchoMessage, final: Message) -> None:
        """
        
        :param echo: 
        :param final: 
        """
    def ToString(self) -> str:
        """"""
    MessageRemoved: EventType[Action[Message]] = ...
    """"""
    NewMessagesArrived: EventType[Action[IEnumerable[Message]]] = ...
    """"""
    PendingMessageResolved: EventType[Action[LocalEchoMessage, Message]] = ...
    """"""
class ChannelManager(CompositeComponent, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache, IChannelPostTarget):
    """"""
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    def __init__(self, api: IAPIProvider):
        """
        
        :param api: 
        """
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
    def AutoSizeAxes(self) -> Axes:
        """"""
    @property
    def AutoSizeDuration(self) -> float:
        """"""
    @property
    def AutoSizeEasing(self) -> Easing:
        """"""
    @property
    def AvailableChannels(self) -> IBindableList[Channel]:
        """
        
        :return: 
        """
    @property
    def Blending(self) -> BlendingParameters:
        """"""
    @Blending.setter
    def Blending(self, value: BlendingParameters) -> None: ...
    @property
    def BorderColour(self) -> ColourInfo:
        """"""
    @property
    def BorderThickness(self) -> float:
        """"""
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
    def ChildMaskingBounds(self) -> RectangleF:
        """"""
    @property
    def ChildOffset(self) -> Vector2:
        """"""
    @property
    def ChildSize(self) -> Vector2:
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
    def CornerExponent(self) -> float:
        """"""
    @property
    def CornerRadius(self) -> float:
        """"""
    @property
    def CurrentChannel(self) -> Bindable[Channel]:
        """
        
        :return: 
        """
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
    def JoinedChannels(self) -> IBindableList[Channel]:
        """
        
        :return: 
        """
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
    @property
    def MaskingSmoothness(self) -> float:
        """"""
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
    @property
    def RelativeChildSize(self) -> Vector2:
        """"""
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
    def JoinChannel(self, channel: Channel) -> Channel:
        """
        
        :param channel: 
        :return: 
        """
    def JoinLastClosedChannel(self) -> None:
        """"""
    def LeaveChannel(self, channel: Channel) -> None:
        """
        
        :param channel: 
        """
    def MarkChannelAsRead(self, channel: Channel) -> None:
        """
        
        :param channel: 
        """
    def OpenChannel(self, name: str) -> None:
        """
        
        :param name: 
        """
    def OpenPrivateChannel(self, user: APIUser) -> None:
        """
        
        :param user: 
        """
    def PostCommand(self, text: str, target: Channel = ...) -> None:
        """
        
        :param text: 
        :param target: 
        """
    def PostMessage(self, text: str, isAction: bool = ..., target: Channel = ...) -> None:
        """
        
        :param text: 
        :param isAction: 
        :param target: 
        """
    def ReceivePositionalInputAt(self, screenSpacePos: Vector2) -> bool:
        """"""
    def RegisterForDependencyActivation(self, registry: IDependencyActivatorRegistry) -> None:
        """"""
    def RemoveTransform(self, toRemove: Transform) -> None:
        """"""
    def SendAck(self) -> None:
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
class ChannelNotFoundException(Exception, ISerializable):
    """"""
    def __init__(self, channelName: str):
        """
        
        :param channelName: 
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
class ChannelType(Enum):
    """"""
    Public: ChannelType = ...
    """"""
    Private: ChannelType = ...
    """"""
    Multiplayer: ChannelType = ...
    """"""
    Spectator: ChannelType = ...
    """"""
    Temporary: ChannelType = ...
    """"""
    PM: ChannelType = ...
    """"""
    Group: ChannelType = ...
    """"""
    System: ChannelType = ...
    """"""
    Announce: ChannelType = ...
    """"""
    Team: ChannelType = ...
    """"""
class ClosedChannel(Object):
    """"""
    Id: Final[int] = ...
    """
    
    :return: 
    """
    Type: Final[ChannelType] = ...
    """
    
    :return: 
    """
    def __init__(self, type: ChannelType, id: int):
        """
        
        :param type: 
        :param id: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Matches(self, channel: Channel) -> bool:
        """
        
        :param channel: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class DrawableLinkCompiler(OsuHoverContainer, ICollection[Drawable], IEnumerable[Drawable], IReadOnlyCollection[Drawable], IReadOnlyList[Drawable], IEnumerable, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, IContainer, IContainerCollection[Drawable], IContainerEnumerable[Drawable], IHasTooltip, ITooltipContentProvider, ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
    """"""
    Enabled: Final[BindableBool] = ...
    """"""
    Name: Final[str] = ...
    """"""
    Parts: Final[SlimReadOnlyListWrapper[Drawable]] = ...
    """
    
    :return: 
    """
    ProcessCustomClock: Final[bool] = ...
    """"""
    @overload
    def __init__(self, parts: IEnumerable[Drawable]):
        """
        
        :param parts: 
        """
    @overload
    def __init__(self, part: ITextPart):
        """
        
        :param part: 
        """
    @property
    def AcceptsFocus(self) -> bool:
        """"""
    @property
    def Action(self) -> Action:
        """"""
    @Action.setter
    def Action(self, value: Action) -> None: ...
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
    def HoverColour(self) -> Optional[Color4]:
        """
        
        :return: 
        """
    @HoverColour.setter
    def HoverColour(self, value: Optional[Color4]) -> None: ...
    @property
    def IdleColour(self) -> Optional[Color4]:
        """
        
        :return: 
        """
    @IdleColour.setter
    def IdleColour(self, value: Optional[Color4]) -> None: ...
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
    def TooltipText(self) -> LocalisableString:
        """"""
    @TooltipText.setter
    def TooltipText(self, value: LocalisableString) -> None: ...
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
    def TriggerClickWithSound(self) -> None:
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
class ErrorMessage(InfoMessage, IComparable[Message], IEquatable[Message]):
    """"""
    ChannelId: Final[int] = ...
    """
    
    :return: 
    """
    Content: Final[str] = ...
    """
    
    :return: 
    """
    Id: Final[Optional[int]] = ...
    """
    
    :return: 
    """
    IsAction: Final[bool] = ...
    """
    
    :return: 
    """
    Links: Final[List[Link]] = ...
    """
    
    :return: 
    """
    Sender: Final[APIUser] = ...
    """
    
    :return: 
    """
    Timestamp: Final[DateTimeOffset] = ...
    """
    
    :return: 
    """
    def __init__(self, message: str):
        """
        
        :param message: 
        """
    @property
    def DisplayContent(self) -> str:
        """
        
        :return: 
        """
    @DisplayContent.setter
    def DisplayContent(self, value: str) -> None: ...
    @property
    def SenderId(self) -> int:
        """
        
        :return: 
        """
    @SenderId.setter
    def SenderId(self, value: int) -> None: ...
    @property
    def Uuid(self) -> str:
        """
        
        :return: 
        """
    @Uuid.setter
    def Uuid(self, value: str) -> None: ...
    def CompareTo(self, other: Message) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: Message) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class ExternalLinkOpener(Component, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
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
    def OpenUrlExternally(self, url: str, warnMode: LinkWarnMode = ...) -> None:
        """
        
        :param url: 
        :param warnMode: 
        """
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
    class ExternalLinkDialog(PopupDialog, ICollection[Drawable], IEnumerable[Drawable], IReadOnlyCollection[Drawable], IReadOnlyList[Drawable], IEnumerable, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, IContainer, IContainerCollection[Drawable], IContainerEnumerable[Drawable], ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
        """"""
        Name: Final[str] = ...
        """"""
        ProcessCustomClock: Final[bool] = ...
        """"""
        State: Final[Bindable[Visibility]] = ...
        """"""
        def __init__(self, url: str, openExternalLinkAction: Action, copyExternalLinkAction: Action):
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
        def BodyText(self) -> LocalisableString:
            """
            
            :return: 
            """
        @BodyText.setter
        def BodyText(self, value: LocalisableString) -> None: ...
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
        def Buttons(self) -> IEnumerable[PopupDialogButton]:
            """
            
            :return: 
            """
        @Buttons.setter
        def Buttons(self, value: IEnumerable[PopupDialogButton]) -> None: ...
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
        def HeaderText(self) -> LocalisableString:
            """
            
            :return: 
            """
        @HeaderText.setter
        def HeaderText(self, value: LocalisableString) -> None: ...
        @property
        def Height(self) -> float:
            """"""
        @Height.setter
        def Height(self, value: float) -> None: ...
        @property
        def Icon(self) -> IconUsage:
            """
            
            :return: 
            """
        @Icon.setter
        def Icon(self, value: IconUsage) -> None: ...
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
        def MainContent(self) -> Container:
            """
            
            :return: 
            """
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
        def Flash(self) -> None:
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
        def PerformAction(self) -> None:
            """"""
        def PerformOkAction(self) -> None:
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
        def ToggleVisibility(self) -> None:
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
class IChannelPostTarget:
    """"""
    def PostMessage(self, text: str, isAction: bool = ..., target: Channel = ...) -> None:
        """
        
        :param text: 
        :param isAction: 
        :param target: 
        """
class IChatClient(IDisposable):
    """"""
    def Dispose(self) -> None:
        """"""
    def RequestPresence(self) -> None:
        """"""
    ChannelJoined: EventType[Action[Channel]] = ...
    """"""
    ChannelParted: EventType[Action[Channel]] = ...
    """"""
    NewMessages: EventType[Action[List[Message]]] = ...
    """"""
    PresenceReceived: EventType[Action] = ...
    """"""
class InfoMessage(LocalMessage, IComparable[Message], IEquatable[Message]):
    """"""
    ChannelId: Final[int] = ...
    """
    
    :return: 
    """
    Content: Final[str] = ...
    """
    
    :return: 
    """
    Id: Final[Optional[int]] = ...
    """
    
    :return: 
    """
    IsAction: Final[bool] = ...
    """
    
    :return: 
    """
    Links: Final[List[Link]] = ...
    """
    
    :return: 
    """
    Sender: Final[APIUser] = ...
    """
    
    :return: 
    """
    Timestamp: Final[DateTimeOffset] = ...
    """
    
    :return: 
    """
    def __init__(self, message: str):
        """
        
        :param message: 
        """
    @property
    def DisplayContent(self) -> str:
        """
        
        :return: 
        """
    @DisplayContent.setter
    def DisplayContent(self, value: str) -> None: ...
    @property
    def SenderId(self) -> int:
        """
        
        :return: 
        """
    @SenderId.setter
    def SenderId(self, value: int) -> None: ...
    @property
    def Uuid(self) -> str:
        """
        
        :return: 
        """
    @Uuid.setter
    def Uuid(self, value: str) -> None: ...
    def CompareTo(self, other: Message) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: Message) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class Link(Object, IComparable[Link]):
    """"""
    Action: Final[LinkAction] = ...
    """
    
    :return: 
    """
    Argument: Final[object] = ...
    """
    
    :return: 
    """
    Index: Final[int] = ...
    """
    
    :return: 
    """
    Length: Final[int] = ...
    """
    
    :return: 
    """
    Url: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self, url: str, startIndex: int, length: int, action: LinkAction, argument: object):
        """
        
        :param url: 
        :param startIndex: 
        :param length: 
        :param action: 
        :param argument: 
        """
    def CompareTo(self, otherLink: Link) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Overlaps(self, otherLink: Link) -> bool:
        """
        
        :param otherLink: 
        :return: 
        """
    @overload
    def Overlaps(self, otherIndex: int, otherLength: int) -> bool:
        """
        
        :param otherIndex: 
        :param otherLength: 
        :return: 
        """
    def ToString(self) -> str:
        """"""
class LinkAction(Enum):
    """"""
    External: LinkAction = ...
    """"""
    OpenBeatmap: LinkAction = ...
    """"""
    OpenBeatmapSet: LinkAction = ...
    """"""
    OpenChannel: LinkAction = ...
    """"""
    OpenEditorTimestamp: LinkAction = ...
    """"""
    JoinRoom: LinkAction = ...
    """"""
    Spectate: LinkAction = ...
    """"""
    OpenUserProfile: LinkAction = ...
    """"""
    SearchBeatmapSet: LinkAction = ...
    """"""
    OpenWiki: LinkAction = ...
    """"""
    Custom: LinkAction = ...
    """"""
    OpenChangelog: LinkAction = ...
    """"""
    FilterBeatmapSetGenre: LinkAction = ...
    """"""
    FilterBeatmapSetLanguage: LinkAction = ...
    """"""
class LinkDetails(Object):
    """"""
    Action: Final[LinkAction] = ...
    """
    
    :return: 
    """
    Argument: Final[object] = ...
    """
    
    :return: 
    """
    def __init__(self, action: LinkAction, argument: object):
        """
        
        :param action: 
        :param argument: 
        """
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class LinkWarnMode(Enum):
    """"""
    Default: LinkWarnMode = ...
    """"""
    AlwaysWarn: LinkWarnMode = ...
    """"""
    NeverWarn: LinkWarnMode = ...
    """"""
class LocalEchoMessage(LocalMessage, IComparable[Message], IEquatable[Message]):
    """"""
    ChannelId: Final[int] = ...
    """
    
    :return: 
    """
    Content: Final[str] = ...
    """
    
    :return: 
    """
    Id: Final[Optional[int]] = ...
    """
    
    :return: 
    """
    IsAction: Final[bool] = ...
    """
    
    :return: 
    """
    Links: Final[List[Link]] = ...
    """
    
    :return: 
    """
    Sender: Final[APIUser] = ...
    """
    
    :return: 
    """
    Timestamp: Final[DateTimeOffset] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def DisplayContent(self) -> str:
        """
        
        :return: 
        """
    @DisplayContent.setter
    def DisplayContent(self, value: str) -> None: ...
    @property
    def SenderId(self) -> int:
        """
        
        :return: 
        """
    @SenderId.setter
    def SenderId(self, value: int) -> None: ...
    @property
    def Uuid(self) -> str:
        """
        
        :return: 
        """
    @Uuid.setter
    def Uuid(self, value: str) -> None: ...
    def CompareTo(self, other: Message) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: Message) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class LocalMessage(Message, IComparable[Message], IEquatable[Message]):
    """"""
    ChannelId: Final[int] = ...
    """
    
    :return: 
    """
    Content: Final[str] = ...
    """
    
    :return: 
    """
    Id: Final[Optional[int]] = ...
    """
    
    :return: 
    """
    IsAction: Final[bool] = ...
    """
    
    :return: 
    """
    Links: Final[List[Link]] = ...
    """
    
    :return: 
    """
    Sender: Final[APIUser] = ...
    """
    
    :return: 
    """
    Timestamp: Final[DateTimeOffset] = ...
    """
    
    :return: 
    """
    @property
    def DisplayContent(self) -> str:
        """
        
        :return: 
        """
    @DisplayContent.setter
    def DisplayContent(self, value: str) -> None: ...
    @property
    def SenderId(self) -> int:
        """
        
        :return: 
        """
    @SenderId.setter
    def SenderId(self, value: int) -> None: ...
    @property
    def Uuid(self) -> str:
        """
        
        :return: 
        """
    @Uuid.setter
    def Uuid(self, value: str) -> None: ...
    def CompareTo(self, other: Message) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: Message) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class Message(Object, IComparable[Message], IEquatable[Message]):
    """"""
    ChannelId: Final[int] = ...
    """
    
    :return: 
    """
    Content: Final[str] = ...
    """
    
    :return: 
    """
    Id: Final[Optional[int]] = ...
    """
    
    :return: 
    """
    IsAction: Final[bool] = ...
    """
    
    :return: 
    """
    Links: Final[List[Link]] = ...
    """
    
    :return: 
    """
    Sender: Final[APIUser] = ...
    """
    
    :return: 
    """
    Timestamp: Final[DateTimeOffset] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, id: Optional[int]):
        """
        
        :param id: 
        """
    @property
    def DisplayContent(self) -> str:
        """
        
        :return: 
        """
    @DisplayContent.setter
    def DisplayContent(self, value: str) -> None: ...
    @property
    def SenderId(self) -> int:
        """
        
        :return: 
        """
    @SenderId.setter
    def SenderId(self, value: int) -> None: ...
    @property
    def Uuid(self) -> str:
        """
        
        :return: 
        """
    @Uuid.setter
    def Uuid(self, value: str) -> None: ...
    def CompareTo(self, other: Message) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: Message) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
class MessageFormatter(ABC, Object):
    """"""
    WebsiteRootUrl: ClassVar[str] = ...
    """
    
    :return: 
    """
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FormatMessage(cls, inputMessage: Message) -> Message:
        """
        
        :param inputMessage: 
        :return: 
        """
    @classmethod
    def FormatText(cls, text: str) -> MessageFormatter.MessageFormatterResult:
        """
        
        :param text: 
        :return: 
        """
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetLinkDetails(cls, url: str) -> LinkDetails:
        """
        
        :param url: 
        :return: 
        """
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    class MessageFormatterResult(Object):
        """"""
        Links: Final[List[Link]] = ...
        """"""
        OriginalText: Final[str] = ...
        """"""
        Text: Final[str] = ...
        """"""
        def __init__(self, text: str):
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
class MessageNotifier(Component, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
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
    @classmethod
    def MatchUsername(cls, message: str, username: str) -> Match:
        """
        
        :param message: 
        :param username: 
        :return: 
        """
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
    class MentionNotification(UserAvatarNotification, ICollection[Drawable], IEnumerable[Drawable], IReadOnlyCollection[Drawable], IReadOnlyList[Drawable], IEnumerable, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, IContainer, IContainerCollection[Drawable], IContainerEnumerable[Drawable], ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
        """"""
        Activated: Final[Func[bool]] = ...
        """
        
        :return: 
        """
        MainContent: Final[Container] = ...
        """
        
        :return: 
        """
        Name: Final[str] = ...
        """"""
        ProcessCustomClock: Final[bool] = ...
        """"""
        def __init__(self, message: Message, channel: Channel, match: Match):
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
        def DisplayOnTop(self) -> bool:
            """
            
            :return: 
            """
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
        def ForwardToOverlay(self) -> Action:
            """
            
            :return: 
            """
        @ForwardToOverlay.setter
        def ForwardToOverlay(self, value: Action) -> None: ...
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
        def Icon(self) -> IconUsage:
            """
            
            :return: 
            """
        @Icon.setter
        def Icon(self, value: IconUsage) -> None: ...
        @property
        def IconColour(self) -> ColourInfo:
            """
            
            :return: 
            """
        @IconColour.setter
        def IconColour(self, value: ColourInfo) -> None: ...
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
        def IsCritical(self) -> bool:
            """
            
            :return: 
            """
        @IsCritical.setter
        def IsCritical(self, value: bool) -> None: ...
        @property
        def IsDragged(self) -> bool:
            """"""
        @property
        def IsHovered(self) -> bool:
            """"""
        @property
        def IsImportant(self) -> bool:
            """
            
            :return: 
            """
        @IsImportant.setter
        def IsImportant(self, value: bool) -> None: ...
        @property
        def IsInToastTray(self) -> bool:
            """
            
            :return: 
            """
        @IsInToastTray.setter
        def IsInToastTray(self, value: bool) -> None: ...
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
        def PopInSampleName(self) -> str:
            """
            
            :return: 
            """
        @property
        def PopOutSampleName(self) -> str:
            """
            
            :return: 
            """
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
        def Read(self) -> bool:
            """
            
            :return: 
            """
        @Read.setter
        def Read(self, value: bool) -> None: ...
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
        def Text(self) -> LocalisableString:
            """
            
            :return: 
            """
        @Text.setter
        def Text(self, value: LocalisableString) -> None: ...
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
        def Transient(self) -> bool:
            """
            
            :return: 
            """
        @Transient.setter
        def Transient(self, value: bool) -> None: ...
        @property
        def WasClosed(self) -> bool:
            """
            
            :return: 
            """
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
        def Close(self, runFlingAnimation: bool) -> None:
            """
            
            :param runFlingAnimation: 
            """
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
        Closed: EventType[Action] = ...
        """"""
        OnLoadComplete: EventType[Action[Drawable]] = ...
        """"""
        OnUpdate: EventType[Action[Drawable]] = ...
        """"""
    class PrivateMessageNotification(UserAvatarNotification, ICollection[Drawable], IEnumerable[Drawable], IReadOnlyCollection[Drawable], IReadOnlyList[Drawable], IEnumerable, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, IContainer, IContainerCollection[Drawable], IContainerEnumerable[Drawable], ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
        """"""
        Activated: Final[Func[bool]] = ...
        """
        
        :return: 
        """
        MainContent: Final[Container] = ...
        """
        
        :return: 
        """
        Name: Final[str] = ...
        """"""
        ProcessCustomClock: Final[bool] = ...
        """"""
        def __init__(self, message: Message, channel: Channel):
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
        def DisplayOnTop(self) -> bool:
            """
            
            :return: 
            """
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
        def ForwardToOverlay(self) -> Action:
            """
            
            :return: 
            """
        @ForwardToOverlay.setter
        def ForwardToOverlay(self, value: Action) -> None: ...
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
        def Icon(self) -> IconUsage:
            """
            
            :return: 
            """
        @Icon.setter
        def Icon(self, value: IconUsage) -> None: ...
        @property
        def IconColour(self) -> ColourInfo:
            """
            
            :return: 
            """
        @IconColour.setter
        def IconColour(self, value: ColourInfo) -> None: ...
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
        def IsCritical(self) -> bool:
            """
            
            :return: 
            """
        @IsCritical.setter
        def IsCritical(self, value: bool) -> None: ...
        @property
        def IsDragged(self) -> bool:
            """"""
        @property
        def IsHovered(self) -> bool:
            """"""
        @property
        def IsImportant(self) -> bool:
            """
            
            :return: 
            """
        @IsImportant.setter
        def IsImportant(self, value: bool) -> None: ...
        @property
        def IsInToastTray(self) -> bool:
            """
            
            :return: 
            """
        @IsInToastTray.setter
        def IsInToastTray(self, value: bool) -> None: ...
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
        def PopInSampleName(self) -> str:
            """
            
            :return: 
            """
        @property
        def PopOutSampleName(self) -> str:
            """
            
            :return: 
            """
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
        def Read(self) -> bool:
            """
            
            :return: 
            """
        @Read.setter
        def Read(self, value: bool) -> None: ...
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
        def Text(self) -> LocalisableString:
            """
            
            :return: 
            """
        @Text.setter
        def Text(self, value: LocalisableString) -> None: ...
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
        def Transient(self) -> bool:
            """
            
            :return: 
            """
        @Transient.setter
        def Transient(self, value: bool) -> None: ...
        @property
        def WasClosed(self) -> bool:
            """
            
            :return: 
            """
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
        def Close(self, runFlingAnimation: bool) -> None:
            """
            
            :param runFlingAnimation: 
            """
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
        Closed: EventType[Action] = ...
        """"""
        OnLoadComplete: EventType[Action[Drawable]] = ...
        """"""
        OnUpdate: EventType[Action[Drawable]] = ...
        """"""
class NowPlayingCommand(Component, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
    """"""
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    def __init__(self, target: Channel):
        """
        
        :param target: 
        """
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
class StandAloneChatDisplay(CompositeDrawable, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
    """"""
    Channel: Final[Bindable[Channel]] = ...
    """
    
    :return: 
    """
    Name: Final[str] = ...
    """"""
    ProcessCustomClock: Final[bool] = ...
    """"""
    def __init__(self, postingTextBox: bool = ...):
        """
        
        :param postingTextBox: 
        """
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
    def AutoSizeAxes(self) -> Axes:
        """"""
    @property
    def AutoSizeDuration(self) -> float:
        """"""
    @property
    def AutoSizeEasing(self) -> Easing:
        """"""
    @property
    def Blending(self) -> BlendingParameters:
        """"""
    @Blending.setter
    def Blending(self, value: BlendingParameters) -> None: ...
    @property
    def BorderColour(self) -> ColourInfo:
        """"""
    @property
    def BorderThickness(self) -> float:
        """"""
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
    def ChildMaskingBounds(self) -> RectangleF:
        """"""
    @property
    def ChildOffset(self) -> Vector2:
        """"""
    @property
    def ChildSize(self) -> Vector2:
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
    def CornerExponent(self) -> float:
        """"""
    @property
    def CornerRadius(self) -> float:
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
    @property
    def MaskingSmoothness(self) -> float:
        """"""
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
    @property
    def RelativeChildSize(self) -> Vector2:
        """"""
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
    class ChatTextBox(HistoryTextBox, ICollection[Drawable], IEnumerable[Drawable], IReadOnlyCollection[Drawable], IReadOnlyList[Drawable], IEnumerable, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, IContainer, IContainerCollection[Drawable], IContainerEnumerable[Drawable], ITabbableContainer, ITransformable, IHasCurrentValue[String], IDrawable, IKeyBindingHandler, IKeyBindingHandler[PlatformAction], IKeyBindingHandler[GlobalAction], ICanSuppressKeyEventLogging, ISourceGeneratedHandleInputCache):
        """"""
        Focus: Final[Action] = ...
        """"""
        FocusLost: Final[Action] = ...
        """"""
        LengthLimit: Final[Optional[int]] = ...
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
        def CanBeTabbedTo(self) -> bool:
            """"""
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
        def CommitOnFocusLost(self) -> bool:
            """"""
        @CommitOnFocusLost.setter
        def CommitOnFocusLost(self, value: bool) -> None: ...
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
        def Current(self) -> Bindable[str]:
            """"""
        @Current.setter
        def Current(self, value: Bindable[str]) -> None: ...
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
        def FontSize(self) -> float:
            """"""
        @FontSize.setter
        def FontSize(self, value: float) -> None: ...
        @property
        def ForceLocalVertexBatch(self) -> bool:
            """"""
        @ForceLocalVertexBatch.setter
        def ForceLocalVertexBatch(self, value: bool) -> None: ...
        @property
        def HandleLeftRightArrows(self) -> bool:
            """"""
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
        def HistoryCount(self) -> int:
            """
            
            :return: 
            """
        @property
        def HoldFocus(self) -> bool:
            """
            
            :return: 
            """
        @HoldFocus.setter
        def HoldFocus(self, value: bool) -> None: ...
        @property
        def InputProperties(self) -> TextInputProperties:
            """"""
        @InputProperties.setter
        def InputProperties(self, value: TextInputProperties) -> None: ...
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
        def PlaceholderText(self) -> LocalisableString:
            """"""
        @PlaceholderText.setter
        def PlaceholderText(self, value: LocalisableString) -> None: ...
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
        def ReadOnly(self) -> bool:
            """"""
        @ReadOnly.setter
        def ReadOnly(self, value: bool) -> None: ...
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
        def ReleaseFocusOnCommit(self) -> bool:
            """"""
        @ReleaseFocusOnCommit.setter
        def ReleaseFocusOnCommit(self, value: bool) -> None: ...
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
        def SelectAllOnFocus(self) -> bool:
            """
            
            :return: 
            """
        @SelectAllOnFocus.setter
        def SelectAllOnFocus(self, value: bool) -> None: ...
        @property
        def SelectedText(self) -> str:
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
        def SuppressKeyEventLogging(self) -> bool:
            """"""
        @property
        def TabbableContentContainer(self) -> CompositeDrawable:
            """"""
        @TabbableContentContainer.setter
        def TabbableContentContainer(self, value: CompositeDrawable) -> None: ...
        @property
        def Text(self) -> str:
            """"""
        @Text.setter
        def Text(self, value: str) -> None: ...
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
        def KillFocus(self) -> None:
            """"""
        @overload
        def OnPressed(self, e: KeyBindingPressEvent[PlatformAction]) -> bool:
            """"""
        @overload
        def OnPressed(self, e: KeyBindingPressEvent[GlobalAction]) -> bool:
            """"""
        @overload
        def OnReleased(self, e: KeyBindingReleaseEvent[PlatformAction]) -> None:
            """"""
        @overload
        def OnReleased(self, e: KeyBindingReleaseEvent[GlobalAction]) -> None:
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
        def SelectAll(self) -> bool:
            """"""
        def Show(self) -> None:
            """"""
        def TakeFocus(self) -> None:
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
        OnCommit: EventType[TextBox.OnCommitHandler] = ...
        """"""
        OnLoadComplete: EventType[Action[Drawable]] = ...
        """"""
        OnUpdate: EventType[Action[Drawable]] = ...
        """"""
    class StandAloneDrawableChannel(DrawableChannel, ICollection[Drawable], IEnumerable[Drawable], IReadOnlyCollection[Drawable], IReadOnlyList[Drawable], IEnumerable, IDisposable, IDependencyInjectionCandidate, ISourceGeneratedDependencyActivator, ISourceGeneratedLongRunningLoadCache, IContainer, IContainerCollection[Drawable], IContainerEnumerable[Drawable], ITransformable, IDrawable, ISourceGeneratedHandleInputCache):
        """"""
        Channel: Final[Channel] = ...
        """
        
        :return: 
        """
        CreateChatLineAction: Final[Func[Message, ChatLine]] = ...
        """"""
        Name: Final[str] = ...
        """"""
        ProcessCustomClock: Final[bool] = ...
        """"""
        def __init__(self, channel: Channel):
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
        def ScrollbarVisible(self) -> bool:
            """
            
            :return: 
            """
        @ScrollbarVisible.setter
        def ScrollbarVisible(self, value: bool) -> None: ...
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
class WebSocketChatClient(Object, IDisposable, IChatClient):
    """"""
    def __init__(self, api: IAPIProvider):
        """
        
        :param api: 
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def RequestPresence(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    ChannelJoined: EventType[Action[Channel]] = ...
    """"""
    ChannelParted: EventType[Action[Channel]] = ...
    """"""
    NewMessages: EventType[Action[List[Message]]] = ...
    """"""
    PresenceReceived: EventType[Action] = ...
    """"""