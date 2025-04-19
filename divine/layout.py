from typing import Optional, Tuple, Literal
from .utilities import types as Type


class Layout(object):

    def __init__(self,

        source: Type.Source,
        coordinate: Type.Coordinate,
        height: Optional[int],
        width: Optional[int],

    ) -> None:

        self.source = source

        self.__y, self.__x = coordinate
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
    def coordinate(self) -> Tuple[int, int]:

        return (self.y, self.x)

    # ---

    @property
    def height(self) -> int:

        if self.__height is None:
            return self.source.parent.height - self.y - self.source.parent.border.ACTIVATED * 2

        return self.__height

    @property
    def width(self) -> int:

        if self.__width is None:
            return self.source.parent.width - self.x - self.source.parent.border.ACTIVATED * 2

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

    def validate(self, mode=Literal['debug', 'validate']) -> None:

        # Validate if coordinate is not less than its parent's ending coordiante

        if self.x >= self.source.parent.endx:
            raise ValueError(
                f"x({self.x}) of {self.source.name} must be less than the ending x({self.source.parent.endx}) of its parent, {self.source.parent.name}."
            )


        if self.y >= self.source.parent.endy:
            raise ValueError(
                f"y({self.y}) of {self.source.name} must be less than the ending y({self.source.parent.endy}) of its parent, {self.source.parent.name}."
            )


        # Validate if coordinate is less than its parent's ending coordiante

        if self.x < self.source.parent.begx:
            raise ValueError(
                f"x({self.x}) of {self.source.name} cannot less than the beginning x({self.source.parent.endx}) of its parent, {self.source.parent.name}."
            )

        if self.y < self.source.parent.begy:
            raise ValueError(
                f"y({self.y}) of {self.source.name} cannot less than the beginning y({self.source.parent.endy}) of its parent, {self.source.parent.name}."
            )


        # NOTE that width and height doesn't rely on thier source's borders but vice versa.
        # border characters are drawned at the edge of width and height


        # NOTE: This is redundanted. Should be removed this completely after making sure it is stable

        # # Validate if width and height is exceeding its parent's width and height

        # if self.width > self.source.parent.width + (self.source.parent.border.ACTIVATED * 2):
        #     raise ValueError(f"width({self.width}) cannot exceed the parent's width({self.source.parent.width + (self.source.parent.border.ACTIVATED * 2)}).")

        # if self.height > self.source.parent.height + (self.source.parent.border.ACTIVATED * 2):
        #     raise ValueError(f"height({self.height}) cannot exceed the parent's height({self.source.parent.height + (self.source.parent.border.ACTIVATED * 2)}).")


        # Validate if width and height is less than its parent's beginning coordinate

        if self.width < self.source.parent.begy:
            raise ValueError(
                f"width({self.width}) of {self.source.name} cannot be less than the beginning x({self.source.parent.begx}) of its parent, {self.source.parent.name}."
            )

        if self.height < self.source.parent.begy:
            raise ValueError(
                f"width({self.height}) of {self.source.name} cannot be less than the beginning y({self.source.parent.begy}) of its parent, {self.source.parent.name}."
            )


        # Validate if width and height is exceeding its parent's available space

        if self.width > self.source.parent.width - self.x - (self.source.parent.border.ACTIVATED * 2):
            raise ValueError(
                f"width({self.width}) of {self.source.name} cannot exceed the available width({self.source.parent.width - self.x - (self.source.parent.border.ACTIVATED * 2)}) of its parent, {self.source.parent.name}."
            )

        if self.height > self.source.parent.height - self.y - (self.source.parent.border.ACTIVATED * 2):
            raise ValueError(
                f"height({self.height}) of {self.source.name} cannot exceed the available height({self.source.parent.height - self.y - (self.source.parent.border.ACTIVATED * 2)}) of its parent, {self.source.parent.name}."
            )
