import curses
from .realm import Realm
from .cursor import Cursor


class Paradise(Realm):

    cursor = Cursor()

    def start(self):
        self.parent()
        return super().start()

    def run(self):
        self.start()
        self.main()

    def spawn(self):
        self.realm = self.parent.realm.derwin(self.maxy, self.maxx, self.begy, self.begx)

    def _Realm__Default_Configurations(self):
    # If not specified _Layout(), the Pardise will take over its parent, Heaven

      # def _Layouts(self):
            self.maxy, self.maxx = self.parent.realm.getmaxyx()
            self.begy, self.begx = self.parent.realm.getbegyx()
        
            return super()._Realm__Default_Configurations()

    def parent(self):
         ...