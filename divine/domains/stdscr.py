from dataclasses import dataclass
from curses import initscr
from ..organs import VoidBorder

stdscr = initscr()


@dataclass(frozen=True, repr=False)
class STDSCR:
    name = 'Standard Screen(stdscr)'
    coordinate = stdscr.getbegyx()
    y, x = coordinate
    height, width = stdscr.getmaxyx()
    begy, begx = 0, 0
    endy, endx = width, height
    orgy, orgx = begy, begx

    border = VoidBorder()

    def __str__(self):
        return (
            f"{self.__class__.name} " \
            f"{self.height}x{self.width} " \
            f"at {self.coordinate}"
        )

    def __repr__(self):
        return ( 
            f"<{self.__class__.__name__}" \
            f"(" \
            f"x:[{self.begy}..{self.endy}], " \
            f"y:[{self.begx}..{self.endx}]" \
            f")" \
            f"({self.height}x{self.width}) "\
            f"at ({self.orgy}, {self.orgx})>"
        )
