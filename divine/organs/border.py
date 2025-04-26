from ..utilities import types as Type
from ..utilities import isdomain


class Border(object):

    def __init__(self,

        parent: Type.Entitie,
        activate: bool = True,

    ) -> None:
        
        """

        Draw a border around the the edge of parent realm.

        Parameters

            parent:
            The Domain that is desired to use it as a host for the border to be drawn, required

            activate:
            Determine if this object is border drawable or not, optional, default=True

        """

        self.parent = parent
        self.ACTIVATED = activate

    def apply(self) -> None:

        """ 

        If ACTIVATED is True, draw a border around the coordinates of parent width and height. 
        Otherwise, do nothing. 

        """

        # for domains
        if self.ACTIVATED and isdomain(self.parent):
            self.parent.realm.border()

            # TODO: draw the border without relying on curses's winow.border()

        # for components
        # TODO


class VoidBorder(object):
    """ For root domains such as screens and sorts
    """
    ACTIVATED = False
