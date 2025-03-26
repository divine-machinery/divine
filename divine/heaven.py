import curses
from .realm import Realm


class Heaven(Realm):

    def start(self):
        self.realm = curses.initscr()
        return super().start()

    def run(self):
        self.start()
        self.main()
        self.stop()
    
    def spawn(self):
        self.realm = curses.newwin(self.maxy, self.maxx, self.begy, self.begx)