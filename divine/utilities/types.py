from typing import TYPE_CHECKING, Union, Optional, Tuple


if TYPE_CHECKING:
    from ..domains import STDSCR


# to be added more
Domain = Union['STDSCR']

LValue = Optional[int]
Coordinate = Tuple[LValue, LValue]
