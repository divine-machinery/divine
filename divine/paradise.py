import curses
from .realm import Realm
from .cursor import Cursor


class Paradise(Realm):

    cursor = Cursor()

    def run(self):
        self.start()
        self.main()

    def spawn(self):
        self.realm = self.parent.realm.derwin(self.maxy, self.maxx, self.begy, self.begx)

