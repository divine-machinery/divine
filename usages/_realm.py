from divine import Realm

def main() -> None:

    class Window(Realm):

        def styles(self) -> None:
            self.y = 10
            self.height = 10

        def main(self) -> None:
            self.realm.box()
            self.realm.addstr(1, 2, "Hello, World!")
            self.realm.getch()

    Window().run()

if __name__ == '__main__':
    main()
