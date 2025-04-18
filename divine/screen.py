from curses import initscr, endwin
from .utilities import types as Type 

class Screen(object):

    def __init__(self) -> None:

        stdscr = initscr()

        self.coordinate: Type.Coordinate = stdscr.getbegyx()

        self.height: int = stdscr.getmaxyx()[0]
        self.width: int = stdscr.getmaxyx()[1]

        # This may seem like redundated but they 
        # are useful. They really are ;)
        self.begy: int = 0
        self.begx: int = 0
        self.endy: int = self.height - 1
        self.endx: int = self.width - 1

        # TODO: This should be removed once Realm 
        # object is implemented
        endwin()

    def __str__(self):
        return f"{self.__class__.__name__} {self.height}x{self.width} at {self.coordinate}"

    def __repr__(self):
        return f"<{self.__class__.__name__} (x:[{self.begy}..{self.endy}], y:[{self.begx}..{self.endx}]) ({self.height}x{self.width})>"