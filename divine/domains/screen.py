from curses import initscr
from ..utilities import types as Type 
from ..layout import Layout
from ..components import Border

class Screen(object):

    def __init__(self, source = initscr()) -> None:

        self.name = 'Screen'

        self.realm = source

        # self parenting on steroids > <
        self.parent = self

        self.layout = Layout(
            source = self,
            coordinate = self.realm.getbegyx(),
            height = self.realm.getmaxyx()[0],
            width = self.realm.getmaxyx()[1],
        )

        self.coordinate: Type.Coordinate = self.layout.coordinate

        self.height: int = self.layout.height
        self.width: int = self.layout.width

        self.border = Border(self, False)

        # This may seem like redundated but they 
        # are useful. They really are ;)
        self.begy: int = self.layout.begy
        self.begx: int = self.layout.begx
        self.endy: int = self.layout.endy
        self.endx: int = self.layout.endx
        self.orgy: int = 0
        self.orgx: int = 0

    def __str__(self):
        return f"{self.__class__.__name__} {self.height}x{self.width} at {self.coordinate}"

    def __repr__(self):
        return f"<{self.__class__.__name__} (x:[{self.begy}..{self.endy}], y:[{self.begx}..{self.endx}]) ({self.height}x{self.width})>"