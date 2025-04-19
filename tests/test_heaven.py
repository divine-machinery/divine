from divine import Heaven

class MainMenu(Heaven):

    def styles(self):
        self.coordinate = (self.parent.height - 3, None)
        self.height = 3

    def main(self):
        self.realm.addstr(1, 1, "Hello, World!")
        self.realm.getch()

MainMenu(border=True).run()
