from ..utilities import types as Type
from . import STDSCR
from ..layout import Layout
from typing import Tuple


class Realm(object):

    def __init__(self,
    
        parent: Type.Domain = STDSCR(),
        y: Type.LValue = None, x: Type.LValue = None,
        width: Type.LValue = None, height: Type.LValue = None

    ):

        self.parent = parent

        self.layout = Layout(self,
            coordinate = (y, x),
            width = width, height = height
        )


    # ===== lazy getters and setters or whatever it is =====
    
    # -- coordinates

    @property
    def y(self) -> int:
        return self.layout.y

    @y.setter
    def y(self, value: Type.LValue) -> None:
        self.layout.y = value


    @property
    def x(self) -> int:
        return self.layout.x

    @x.setter
    def x(self, value: Type.LValue) -> None:
        self.layout.x = value
    
    # -- height

    @property
    def height(self) -> int:
        return self.layout.height

    @height.setter
    def height(self, value: Type.LValue) -> None:
        self.layout.height = value
    
    # -- width

    @property
    def width(self) -> int:
        return self.layout.width

    @width.setter
    def width(self, value: Type.LValue) -> None:
        self.layout.width = value

    # -- extras

    @property
    def coordinate(self) -> Tuple[int, int]:
        return self.layout.coordinate

    @coordinate.setter
    def coordinate(self, coordinate: Type.Coordinate) -> None:
        self.layout.coordinate = coordinate
