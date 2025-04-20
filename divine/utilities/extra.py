from typing import TypeGuard, TYPE_CHECKING
from . import types as Type

if TYPE_CHECKING:
    from ..domains import Realm

# So apparently TypeGuard is for type predicting functions
# It is a bool at runtime according to the docstrings

def isdomain(source: Type.Entities) -> TypeGuard['Realm']:
    return hasattr(source, 'realm')
