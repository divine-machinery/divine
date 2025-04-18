from curses import window
from typing import Optional, Tuple
from .utilities import types as Type
from .screen import Screen
from .layout import Layout
from .components import Border


class Realm(object):

    def __init__(self,

        parent: Type.Source = Screen(),
        coordinate: Type.Coordinate = (None, None), 
        width: Optional[int] = None,
        height: Optional[int] = None,
        border: bool = False,

    ) -> None:

        self.parent = parent
        self.layout = Layout(self, coordinate, height, width)

        self.border = Border(self, border)

        self.realm: window

    # ---

    @property
    def coordinate(self) -> Tuple[int, int]:
        return self.layout.coordinate


    @property
    def height(self) -> int:
        return self.layout.height

    @property
    def width(self) -> int:
        return self.layout.width


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
