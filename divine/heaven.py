import curses


class Heaven(object):

    def _Layout(self):
        """ Custom layout configurations can be written here. If
            not specified, the default layouts will take over
        """

    def main(self):
        """ The main application logics can be written here 
        """

    def start(self):
        """ Construct a ready-made screen, the default Terminal is 
            no longer accessible until it is deconstructed
        """

        # Initialize the screen
        self.screen = curses.initscr()

        # Apply Default Configurations
        self.__Default_Configurations()

        # Overwrite the Default Configurations if specified
        self._Layout()

        # Recreate the screen, ready to utilize
        self.screen = curses.newwin(self.maxy, self.maxx, self.begy, self.begx)

    def stop(self):
        """ Deconstruct the screen, restoring the default Terminal
        """
        curses.endwin()

    def run(self):
        """ Run the inheritance
        """
        self.start()
        self.main()
        self.stop()

    def __Default_Configurations(self):
        self.maxy, self.maxx = self.screen.getmaxyx()
        self.begy, self.begx = self.screen.getbegyx()
