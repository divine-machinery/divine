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

        return self.__y

    @property
    def x(self) -> int:

        if self.__x is None:
            return self.source.parent.begx

        return self.__x

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

        # border takes 2 lines, thus minus 2 if activated
        # coordinate members always start at 0, thus minus 1
        return self.height - (self.source.border.ACTIVATED * 2) - 1

    @property
    def endx(self) -> int:

        # border takes 2 characters, thus minus 2 if activated
        # coordinate members always start at 0, thus minus 1
        return self.width - (self.source.border.ACTIVATED * 2) - 1

    # ---
