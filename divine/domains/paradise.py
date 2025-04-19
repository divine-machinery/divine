from .realm import Realm


class Paradise(Realm):

    def __init__(self, parent, coordinate = (None, None), height = None, width = None, border = False, name = None):
        super().__init__(parent, coordinate, height, width, border, name)
        self.layout.validate()
        self.realm = self.parent.realm.subpad(
            self.height, 
            self.width, 
            self.y + self.parent.border.ACTIVATED + self.parent.orgy, # I had to pull this shit 
            self.x + self.parent.border.ACTIVATED + self.parent.orgx,
        )
        self.border.apply()