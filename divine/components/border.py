from ..utilities import types as Type


class Border(object):

    def __init__(self,

        parent: Type.Source,
        activate: bool,

    ) -> None:

        self.parent = parent
        self.ACTIVATED = activate

    def apply(self) -> None:

        """ Draw a border if ACTIVATED is True. Otherwise, do nothing.
        """

        if self.ACTIVATED:
            self.parent.realm.border()
