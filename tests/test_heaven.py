from divine import Heaven

class MainMenu(Heaven):

    def main(self):
        # self.realm.addstr(1, 1, f"{repr(self.parent)}")
        self.realm.getch()

MainMenu(coordinate=(10, 20), width=20, height=10, border=True).run()
