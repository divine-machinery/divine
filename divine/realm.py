import curses
from ._screen import screen 


class Realm(object):

    def styles(self):
        """ Realm styles can and must be defined here, including Layouts.
        """
        ...

    def start(self):
        """ Construct a Realm either using default or user-defined values.
        """

        # Use user-defined configurations if exists
        self.styles()

        # Use default configurations in case user didn't defined, otherwise overide
        # NOTE: This will overid ONLY the values that hasn't defined
        self.__default_configurations()

        # Finally construct a Realm
        # TODO: Currently, only Windows are implemented, Pads will be required as well
        self.realm = curses.newwin(self.maxy, self.maxx, self.begy, self.begx)

    def stop(self):
        """ Deconstruct the Realm, restores the Default Shell
        """
        curses.endwin()

    def main(self):
        """ The main Realm(App) logics can and must be written here
        """
        ...

    def run(self):
        """ Run all the written Realm(App) logics
        """
        self.start()
        self.main()
        self.stop()

    def __default_configurations(self):
        if not hasattr(self, 'begy'):
            self.begy = screen.begy
        if not hasattr(self, 'begx'):
            self.begx = screen.begx
        if not hasattr(self, 'maxy'):
            self.maxy = screen.maxy - self.begy
        if not hasattr(self, 'maxx'):
            self.maxx = screen.maxx - self.begx
