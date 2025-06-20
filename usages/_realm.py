# raw usage

from divine import Realm

def main() -> None:

    class Window(Realm):

        def main(self) -> None:
            self.realm.box()
            self.realm.addstr(1, 2, "Hello, World!")
            self.realm.getch()

    Window().run()

if __name__ == '__main__':
    main()
