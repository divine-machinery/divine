from divine import Heaven

class MainMenu(Heaven):

    def main(self):
        self.realm.addstr(1, 1, f"{repr(self)}")
        self.realm.getch()

MainMenu(border=True).run()
