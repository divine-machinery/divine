from typing import Optional
from ..utilities import types as Type
from .realm import Realm


class Paradise(Realm):

    def __init__(self, 

        parent: Type.Domain, 
        coordinate: Type.Coordinate = (None, None), 
        height: Optional[int] = None, 
        width: Optional[int] = None, 
        border: bool = False, 
        name: Optional[None] = None

    ) -> None:

        super().__init__(parent, coordinate, height, width, border, name)
        self.adam.children.append(self)

    def summon(self):
        """ Summon a realm, store it as an attribute 'realm'.
        """
        self.realm = self.adam.realm.subpad(
            self.height, 
            self.width, 
            self.y + self.parent.border.ACTIVATED + self.parent.orgy,
            self.x + self.parent.border.ACTIVATED + self.parent.orgx,
        )

    def run(self):
        self.layout.validate()
        self.summon()
        self.border.apply()


    # Return the very first domain hierarchy, Heaven
    @property
    def adam(self):
        from .heaven import Heaven
        return self.parent if isinstance(self.parent, Heaven) else self.parent.adam
