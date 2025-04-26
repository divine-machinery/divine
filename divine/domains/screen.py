from typing import Optional
from ..utilities import types as Type 
from ..layout import Layout
from ..organs import VoidBorder
from . import STDSCR 


class Screen(object):

    def __init__(self, 

        coordinate: Type.Coordinate = (None, None), 
        height: Optional[int] = None, 
        width: Optional[int] = None,


    ) -> None:
        
        """

        Abstract implementation for the screen that allows to manipulate the coordiante, height, 
        width. All the domains are adopted by this object by default. 

        Parameters:

            coordinate
            The coordinate in format of (y, x) to place the top left corner of this domain, 
            None values will be replaced by the coordinate of STDSCR, optional, default=None
            
            height: 
            The numbers of lines expanding from the given coordinate, if None value was passed, 
            inheirt the height of STDSCR, optional, default=None
            
            width: 
            The numbers of colons(characters) expanding from the given coordinate, if None value 
            was passed, inheirt the width of STDSCR, optional, default=None
            

        """

        self.name = 'Screen'

        self.parent = STDSCR()

        self.layout = Layout(
            source = self,
            coordinate = coordinate,
            height = height,
            width = width,
        )

        self.coordinate: Type.Coordinate = self.layout.coordinate
        self.y, self.x = self.coordinate

        self.height: int = self.layout.height
        self.width: int = self.layout.width

        self.border = VoidBorder()

        self.begy: int = self.layout.begy
        self.begx: int = self.layout.begx
        self.endy: int = self.layout.endy
        self.endx: int = self.layout.endx
        self.orgy: int = self.layout.y
        self.orgx: int = self.layout.x

        self.layout.validate()


    def __str__(self):
        return (
            f"{self.__class__.__name__} " /
            f"{self.height}x{self.width}" /
            f"at {self.coordinate}"
        )

    def __repr__(self):
        return ( 
            f"<{self.__class__.__name__}" \
            f"(y:[{self.begy}..{self.endy}], x:[{self.begx}..{self.endx}])" \
            f"({self.height}x{self.width}) at ({self.orgy}, {self.orgx})>"
        )
