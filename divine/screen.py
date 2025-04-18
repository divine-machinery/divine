from curses import initscr
from .utilities import types as Type 
from .layout import Layout
from .components import Border

class Screen(object):

    def __init__(self) -> None:

        self.realm = stdscr = initscr()

        # self parenting on steroids > <
        self.parent = self

        self.layout = Layout(
            source = self,
            coordinate = stdscr.getbegyx(),
            height = stdscr.getmaxyx()[0],
            width = stdscr.getmaxyx()[1],
        )

        self.coordinate: Type.Coordinate = self.layout.coordinate

        self.height: int = self.layout.height
        self.width: int = self.layout.width

        self.border = Border(self, False)

        # This may seem like redundated but they 
        # are useful. They really are ;)
        self.begy: int = self.layout.begy
        self.begx: int = self.layout.begy
        self.endy: int = self.layout.endy
        self.endx: int = self.layout.endx

    def __str__(self):
        return f"{self.__class__.__name__} {self.height}x{self.width} at {self.coordinate}"

    def __repr__(self):
        return f"<{self.__class__.__name__} (x:[{self.begy}..{self.endy}], y:[{self.begx}..{self.endx}]) ({self.height}x{self.width})>"