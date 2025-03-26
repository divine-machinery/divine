import curses
from .realm import Realm


class Paradise(Realm):

    def run(self):
        self.start()
        self.main()

    def spawn(self):
        self.realm = self.parent.realm.derwin(self.maxy, self.maxx, self.begy, self.begx)

