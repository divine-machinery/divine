from curses import window
from typing import Optional
from ..utilities import types as Type
from .screen import Screen
from ..layout import Layout
from ..components import Border


class Realm(object):

    def __init__(self,

        parent: Type.Source = Screen(),
        coordinate: Type.Coordinate = (None, None), 
        height: Optional[int] = None,
        width: Optional[int] = None,
        border: bool = False,
        name: Optional[str] = None,

    ) -> None:

        self.name = f"{self.__class__.__name__}" if name is None else name

        self.parent = parent
        self.layout = Layout(self, coordinate, height, width)

        self.border = Border(self, border)

        self.realm: window

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

    # ---

    def __str__(self):
        return f"{self.__class__.__name__} {self.height}x{self.width} at {self.coordinate}"

    def __repr__(self):
        return f"<{self.__class__.__name__} (x:[{self.begy}..{self.endy}], y:[{self.begx}..{self.endx}]) ({self.height}x{self.width})>"
