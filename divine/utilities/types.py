from typing import Tuple, Optional, Union, Literal, TYPE_CHECKING

if TYPE_CHECKING:

    from ..domains import STDSCR, Screen, Realm, Heaven, Paradise
    from ..components import Write
    from ..organs import Border, Cursor

Axis = Literal['y', 'x']
CoordinateMember = Optional[int]
Coordinate = Tuple[Optional[int], Optional[int]]
Domain = Union['Screen', 'Realm', 'Heaven', 'Paradise']
RootDomain = Union['STDSCR']
RealmBasedDomain = Union['Realm', 'Heaven', 'Paradise']
Component = Union['Write']
Organ = Union['Border', 'Cursor']
Entitie = Union[Domain, Component]