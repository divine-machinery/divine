from .realm import Realm


class Paradise(Realm):

    def __init__(self, parent, coordinate = (None, None), height = None, width = None, border = False, name = None):
        super().__init__(parent, coordinate, height, width, border, name)
        self.layout.validate()
        self.realm = self.parent.realm.subpad(
            self.height, 
            self.width, 
            self.coordinate[0] + self.parent.coordinate[0] + self.parent.border.ACTIVATED, 
            self.coordinate[1] + self.parent.coordinate[1] + self.parent.border.ACTIVATED
        )
        self.border.apply()