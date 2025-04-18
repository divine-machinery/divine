from typing import Optional
from .utilities import types as Type
from .screen import Screen
from .layout import Layout


class Realm(object):

    def __init__(self,

        parent: Type.Source = Screen(),
        coordinate: Type.Coordinate = (None, None), 
        width: Optional[int] = None,
        height: Optional[int] = None,

    ) -> None:

        self.parent = parent
        self.layout = Layout(self, coordinate, width, height)

