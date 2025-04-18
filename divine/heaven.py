from curses import window, newwin, endwin
from .realm import Realm


class Heaven(Realm):

    def summon(self) -> None:

        self.realm: window = newwin(self.height, self.width, self.coordinate[0], self.coordinate[1])


    def start(self) -> None:
        self.layout.validate()
        self.summon()
        self.border.apply()


    def main(self) -> None:
        ...


    def stop(self) -> None:
        endwin()


    def run(self) -> None:

        try:
            self.start()
            self.main()

        except Exception as error:
            self.stop()
            raise error

        else:
            self.stop()