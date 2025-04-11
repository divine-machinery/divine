from divine import Realm


class _MainMenu(Realm):

    def styles(self):
        self.begy = 5
        self.begx = 10

    def main(self):
        self.realm.border()
        self.write(1, 1, "Itsumi Mario!")
        self.realm.getch()

MainMenu = _MainMenu()

MainMenu.run()
