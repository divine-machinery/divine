from curses import initscr, window


stdscr = initscr()


class Screen(object):

    def __init__(self, screen=None):

        """ Initiate a custom or the whole screen.

            Note that this object specfically requires to manually shutdown, 
            otherwise will stays in curses' program mode until a certain point
        """

        if screen is not None and not isinstance(screen, window):
            raise TypeError(
                f"Invalid 'window' object. Expected 'curses.window'. Got '{type(screen).__name__}'"
            )

        elif isinstance(screen, window):
            self.__screen = screen

        elif screen is None:
            self.__screen = stdscr

    # NOTE: Currently practicing the habit of writing dostrings. Apologize if my getters hurt your eyes :3
    # NOTE: But I am guessing that I will need to implement them anyway at some points for (setters)validations

    @property
    def maxy(self):

        """ Returns the maximum coordinate y or the height of a screen
        """

        return self.__screen.getmaxyx()[0]

    @property
    def maxx(self):

        """ Returns the maximum coordinate x or the width of a screen
        """

        return self.__screen.getmaxyx()[1]

    @property
    def begy(self):

        """ Returns the lowest level of coordinate y of a screen
        """

        return self.__screen.getbegyx()[0]

    @property
    def begx(self):

        """ Returns the lowest level of coordinate x of a screen
        """

        return self.__screen.getbegyx()[1]
