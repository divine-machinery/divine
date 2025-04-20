from divine import Heaven, Paradise

class MainMenu(Heaven):

    def main(self):
        paradise = Paradise(self, (2, 0), border=True)
        paradise.name = "MyParadise"
        paradise.realm.addstr(1, 1, f"{paradise.name}")
        self.realm.getch()

MainMenu(coordinate=(15, 20), width=50, height=15, border=True).run()
