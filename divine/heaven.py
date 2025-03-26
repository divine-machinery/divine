import curses


class Heaven(object):

    def configuration(self):
        ...

    def main(self):
        ...

    def start(self):
        self.screen = curses.initscr()

    def stop(self):
        curses.endwin()

    def run(self):
        self.start()
        self.configuration()
        self.main()
        self.stop()
