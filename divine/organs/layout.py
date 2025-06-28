from ..utilities import types as Type
from typing import Tuple


# the intention of this object is to maintain the layouts of 
# all Domains. One usecase could be layout validations.
class Layout(object):

    def __init__(self, 
    
        source: Type.Domain,
        coordinate: Type.Coordinate = (None, None),
        height: Type.LValue = None,
        width: Type.LValue = None
    
    ) -> None:

        self.source = source
        self.__y, self.__x = coordinate
        self.__height = height
        self.__width = width


    # ===== lazy getters and setters or whatever it is =====
    
    # -- coordinates

    @property
    def y(self) -> int:
        return self.__y if self.__y is not None else self.source.parent.y

    @y.setter
    def y(self, value: Type.LValue) -> None:
        self.__y = value


    @property
    def x(self) -> int:
        return self.__x if self.__x is not None else self.source.parent.x

    @x.setter
    def x(self, value: Type.LValue) -> None:
        self.__x = value
    
    # -- height

    @property
    def height(self) -> int:
        return self.__height if self.__height is not None else self.source.parent.height

    @height.setter
    def height(self, value: Type.LValue) -> None:
        self.__height = value

    # -- width

    @property
    def width(self) -> int:
        return self.__width if self.__width is not None else self.source.parent.width

    @width.setter
    def width(self, value: Type.LValue) -> None:
        self.__width = value

    # -- extras

    @property
    def coordinate(self) -> Tuple[int, int]:
        return (self.y, self.x)

    @coordinate.setter
    def coordinate(self, coordinate: Type.Coordinate) -> None:
        self.y, self.x = coordinate
