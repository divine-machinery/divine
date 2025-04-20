from typing import Tuple, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:

    from ..domains import Screen
    from ..domains import Realm

    from ..components import Write

Coordinate = Tuple[Optional[int], Optional[int]]
Domain = Union['Screen', 'Realm']
Component = Union['Write']
Entities = Domain | Component
