from divine import Heaven

class MainMenu(Heaven):

    def styles(self):
        self.height = 3
        self.y = self.parent.height - self.height

    def main(self):
        self.realm.addstr(1, 1, "Hello, World!")
        self.realm.getch()

MainMenu(border=True).run()
