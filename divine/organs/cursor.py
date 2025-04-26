from ..utilities import types as Type

class Cursor(object):

    def __init__(self, source: Type.Domain):

        self.source = source
        self.__y = 0 + self.source.border.ACTIVATED
        self.__x = 0 + self.source.border.ACTIVATED

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

        self.__x = value

    # -----

    def render(self):

        self.source.realm.move(
            self.y,
            self.x
        )

    def validate(self, value, axis: Type.Axis):

        # validate type
        if not isinstance(value, int):
            raise TypeError(f"Cannot assign {value} to {self.__class__.__name__}.{axis}. Expected 'int' type. Got '{type(value).__name__}' type.")

        # validate cursor placement
        # TODO

    def reset(self, axis: Type.Axis):

        match axis:
            case 'y':
                self.__y = 0 + self.source.border.ACTIVATED
            case 'x':
                self.__x = 0 + self.source.border.ACTIVATED