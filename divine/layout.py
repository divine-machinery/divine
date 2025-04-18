from typing import Optional
from .utilities import types as Type


class Layout(object):

    def __init__(self,

        source: Type.Source,
        coordinate: Type.Coordinate,
        height: Optional[int],
        width: Optional[int],

    ) -> None:

        self.source = source

        self.__x, self.__y = coordinate
        self.__height = height
        self.__width = width

    # ---

    @property
    def y(self) -> int:

        if self.__y is None:
            return self.source.parent.begy

    @property
    def x(self) -> int:

        if self.__x is None:
            return self.source.parent.begx

    @property
    def coordinate(self) -> Type.Coordinate:

        return (self.y, self.x)

    # ---

    @property
    def height(self) -> int:

        if self.__height is None:
            return self.source.parent.height

        return self.__height

    @property
    def width(self) -> int:

        if self.__width is None:
            return self.source.parent.width

        return self.__width

    # ---

    @property
    def begy(self) -> int:

        # Always return zero
        return 0

    @property
    def begx(self) -> int:

        # Always return zero
        return 0

    @property
    def endy(self) -> int:

        return self.height - 1

    @property
    def endx(self) -> int:

        return self.width - 1

    # ---
