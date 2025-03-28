

class Cursor(object):
    def __init__(self):
        self.y = -1
        self.x = 0

    def reset(self, axis):
        match axis:
            case 'y': self.y = -1
            case 'x': self.x = 0