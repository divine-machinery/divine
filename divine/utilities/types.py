from typing import Tuple, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from ..screen import Screen
    from ..realm import Realm

Coordinate = Tuple[Optional[int], Optional[int]]
Source = Union['Screen', 'Realm']
