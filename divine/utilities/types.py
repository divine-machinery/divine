from typing import TYPE_CHECKING, Union, Optional, Tuple

if TYPE_CHECKING:
    from ..domains import STDSCR, Realm


# to be added more
Domain = Union['STDSCR', 'Realm']

LValue = Optional[int]
Coordinate = Tuple[LValue, LValue]
