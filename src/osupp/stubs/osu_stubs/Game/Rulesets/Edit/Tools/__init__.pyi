from System import Object
from System import Type
from __future__ import annotations
from abc import ABC
from osu.Framework.Graphics import Drawable
from osu.Framework.Localisation import LocalisableString
from osu.Game.Rulesets.Edit import PlacementBlueprint
from typing import Final
class CompositionTool(ABC, Object):
    """"""
    Name: Final[str] = ...
    """
    
    :return: 
    """
    @property
    def TooltipText(self) -> LocalisableString:
        """
        
        :return: 
        """
    @TooltipText.setter
    def TooltipText(self, value: LocalisableString) -> None: ...
    def CreateIcon(self) -> Drawable:
        """
        
        :return: 
        """
    def CreatePlacementBlueprint(self) -> PlacementBlueprint:
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
class SelectTool(CompositionTool):
    """"""
    Name: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    @property
    def TooltipText(self) -> LocalisableString:
        """
        
        :return: 
        """
    @TooltipText.setter
    def TooltipText(self, value: LocalisableString) -> None: ...
    def CreateIcon(self) -> Drawable:
        """
        
        :return: 
        """
    def CreatePlacementBlueprint(self) -> PlacementBlueprint:
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