from divine import Heaven

class MainMenu(Heaven):

    def main(self):
        self.realm.border()
        self.realm.addstr(1, 1, "Hello, World!")
        self.realm.getch()

MainMenu().run()
