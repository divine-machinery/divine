from divine import Realm


class _MainMenu(Realm):

    def main(self):
        # self.realm.border()
        self.write("Itsumi!")
        self.write("Mario!")
        self.write(6, 12, "Hello, World!")
        self.realm.getch()

MainMenu = _MainMenu()

MainMenu.run()
