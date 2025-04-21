from ..utilities import types as Type

class Cursor(object):

    def __init__(self, source: Type.Domain):

        self.source = source
        self.__y = 0
        self.__x = 0

    # -----

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, value: int):

        self.validate(value, 'y')

        self.__y = value


    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, value: int):

        self.validate(value, 'x')

        if value > self.source.endx:
            self.__x = 0
            self.__y += 1

        else:
            self.__x = value

    # -----

    def render(self):

        self.source.realm.move(
            self.__y,
            self.x + 1
        )

    def validate(self, value, axis: Type.Axis):

        # validate type
        if not isinstance(value, int):
            raise TypeError(f"Cannot assign {value} to {self.__class__.__name__}.{axis}. Expected 'int' type. Got '{type(value).__name__}' type.")

        # validate cursor placement
        # TODO
