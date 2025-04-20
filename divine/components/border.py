from ..utilities import types as Type
from ..utilities import isdomain


class Border(object):

    def __init__(self,

        parent: Type.Entities,
        activate: bool,

    ) -> None:

        self.parent = parent
        self.ACTIVATED = activate

    def apply(self) -> None:

        """ Draw a border if ACTIVATED is True. Otherwise, do nothing.
        """

        if self.ACTIVATED and isdomain(self.parent):
            self.parent.realm.border()
