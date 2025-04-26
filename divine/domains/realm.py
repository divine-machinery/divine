from curses import window
from typing import Optional
from ..utilities import types as Type
from .screen import Screen
from ..layout import Layout
from ..components import Write
from ..organs import Border, Cursor


class Realm(object):

    def __init__(self,

        parent: Type.Domain = Screen(),
        coordinate: Type.Coordinate = (None, None), 
        height: Optional[int] = None,
        width: Optional[int] = None,
        border: bool = False,
        name: Optional[str] = None,

    ) -> None:

        """

        This object can be used by either inheriting it or any other such forms, mainly to 
        create Template Domains. Pre-implemented Layouts and components such as Write, Border.

        Parameters:

            parent: 
            Root Domain oject, or parent for this domain to use as reference, default=Screen()
            
            coordinate: 
            The coordinate in format of (y, x) to place the top left corner of this domain, 
            None values will be replaced by the coordinate of Root Domain, parent, optional, 
            default=None
            
            height: 
            The numbers of lines expanding from the given coordinate, if None value was passed, 
            inheirt the height of parent, Root Domain, optional, default=None
            
            width: 
            The numbers of colons(characters) expanding from the given coordinate, if None value 
            was passed, inheirt the width of parent, Root Domain, optional, default=None

            border:
            If passed True, insert the border characters around the coordinates begy, begx, endy, 
            endx, otherwise do nothing, option, default=False

            name:
            The string representation of this Realm, if None was passed, use the class name, 
            optional, default=None

        """

        self.name = f"{self.__class__.__name__}" if name is None else name

        self.parent = parent
        self.layout = Layout(self, coordinate, height, width)

        self.border = Border(self, border)

        self.realm: window

        self.cursor = Cursor(self)

    # ---

    def write(self,

        text: str = '',
        y: Type.CoordinateMember = None,
        x: Type.CoordinateMember = None,

    ) -> None:

        """

        Prints a text on this(self) Domain on a certain coordinates. Line-break will be occured
        once a character from the text hits the endx of this(self) Domain. Move the cursor to
        the end of the text afterward. 

        Parameters

        text:
        The text that is desired to be printed, optional, default=''

        y, x:
        The coordinate that will be used as the placement coordinate for the first character in 
        the text. If passed None(s), use the cursor coordiante of this(self) Domain. optional, 
        default=None, None

        """

        WriteObject = Write(self, str(text), y, x)
        WriteObject.render()

    # ---

    @property
    def coordinate(self) -> Type.Coordinate:
        return self.layout.coordinate

    @coordinate.setter
    def coordinate(self, value: Type.Coordinate):
        self.layout.coordinate = value


    @property
    def y(self) -> int:
        return self.layout.y

    @y.setter
    def y(self, value: int):
        self.layout.y = value

    @property
    def x(self) -> int:
        return self.layout.x

    @x.setter
    def x(self, value: int):
        self.layout.x = value

    # ---

    @property
    def height(self) -> int:
        return self.layout.height

    @height.setter
    def height(self, value: int):
        self.layout.height = value


    @property
    def width(self) -> int:
        return self.layout.width

    @width.setter
    def width(self, value: int):
        self.layout.width = value

    # ---

    @property
    def begy(self) -> int:
        return self.layout.begy

    @property
    def begx(self) -> int:
        return self.layout.begx

    @property
    def endy(self) -> int:
        return self.layout.endy

    @property
    def endx(self) -> int:
        return self.layout.endx

    @property
    def orgy(self) -> int:
        return self.layout.orgy

    @property
    def orgx(self) -> int:
        return self.layout.orgx

    # ---

    def __str__(self):
        return (
            f"{self.__class__.__name__} " \
            f"{self.height}x{self.width}" \
            f"at {self.coordinate}"
        )

    def __repr__(self):
        return ( 
            f"<{self.__class__.__name__}" \
            f"(y:[{self.begy}..{self.endy}], x:[{self.begx}..{self.endx}])" \
            f"({self.height}x{self.width}) at ({self.orgy}, {self.orgx})>"
        )
