from ..utilities import types as Type
from . import STDSCR
from ..layout import Layout


class Heaven(object):

    def __init__(self,
    
        parent: Type.Domain = STDSCR(),
        y: Type.LValue = None, x: Type.LValue = None,
        width: Type.LValue = None, height: Type.LValue = None

    ):

        self.layout = Layout(self,
            coordinate = (y, x),
            width = width, height = height
        )
