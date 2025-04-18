from divine import Heaven, Paradise

class MainMenu(Heaven):

    def main(self):
        paradise = Paradise(self, (2, 4), border=True)
        paradise.realm.addstr(1, 1, f"{repr(paradise)}")
        self.realm.getch()

MainMenu(coordinate=(15, 20), width=50, height=15, border=True).run()
