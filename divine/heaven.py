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
    
    def summon(self):
        self.realm = curses.newwin(self.maxy, self.maxx, self.begy, self.begx)

    def _Realm__Default_Configurations(self):

        # NOTE <-------------------------------------------- !!!
        # * If not specified the Realm Layouts inside styles(),
        # * Heave will take over the screen's layouts

        self.maxy, self.maxx = self.realm.getmaxyx()
        self.begy, self.begx = self.realm.getbegyx()
    
        return super()._Realm__Default_Configurations()
