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

    def summon(self):
        self.realm = self.parent.realm.derwin(self.maxy, self.maxx, self.begy, self.begx)

    def _Realm__Default_Configurations(self):

        # NOTE <-------------------------------------------- !!!
        # If not assigned the Layouts inside styles(), Pardise
        # will take over the, parent, Heaven's layouts

        self.maxy, self.maxx = self.parent.realm.getmaxyx()
        self.begy, self.begx = self.parent.realm.getbegyx()
    
        return super()._Realm__Default_Configurations()

    def parent(self):
         ...