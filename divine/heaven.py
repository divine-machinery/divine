import curses
from .realm import Realm
from .cursor import Cursor


class Heaven(Realm):

    cursor = Cursor()

    def start(self):
        self.realm = curses.initscr()
        return super().start()

    def run(self):
        self.start()
        self.main()
        self.stop()
    
    def spawn(self):
        self.realm = curses.newwin(self.maxy, self.maxx, self.begy, self.begx)

    def Default_Configurations(self):

      # def _Layouts(self):
            self.maxy, self.maxx = self.realm.getmaxyx()
            self.begy, self.begx = self.realm.getbegyx()
        
            return super().Default_Configurations()
