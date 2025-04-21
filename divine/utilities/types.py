from typing import Tuple, Optional, Union, Literal, TYPE_CHECKING

if TYPE_CHECKING:

    from ..domains import Screen
    from ..domains import Realm

    from ..components import Write

Axis = Literal['y', 'x']
CoordinateMember = Optional[int]
Coordinate = Tuple[Optional[int], Optional[int]]
Domain = Union['Screen', 'Realm']
Component = Union['Write']
Entities = Domain | Component
