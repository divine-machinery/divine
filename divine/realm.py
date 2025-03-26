import curses
from box import Box


class Realm(object):

    def _Layout(self):
        """ Custom layout configurations can be written here. If
            not specified, the default configurations will take over
        """

    def _Border(self):
        """ Custom border configurations can be written here. If
            not specified, the default configurations will take over
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

        # Define Default Configurations
        self.__Default_Configurations()

        # Overwrite the Default Configurations if specified
        self._Layout()
        self.__validate_Layout()

        self._Border()

        # Recreate the screen, ready to utilize
        self.screen = curses.newwin(self.maxy, self.maxx, self.begy, self.begx)

        # Apply Configurations
        if self.border.all != None:
            for border_ch in self.border:
                self.border[border_ch] = self.border.all
        self.__draw_border() if self.has_border else self.__erase_border()

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

    def __validate_Layout(self):
        # TODO: Create a own exception or find a suitable
        for layout in (self.maxy, self.maxx, self.begy, self.begx):
            if layout < 0:
                raise Exception 

    def __Default_Configurations(self):
      # def _Layouts(self):
            self.maxy, self.maxx = self.screen.getmaxyx()
            self.begy, self.begx = self.screen.getbegyx()

      # def _Border(self):
            self.has_border = False
            self.border = Box()
            self.border.all          = None
            self.border.left         = curses.ACS_VLINE
            self.border.right        = curses.ACS_VLINE
            self.border.top          = curses.ACS_HLINE
            self.border.bottom       = curses.ACS_HLINE
            self.border.top_left     = curses.ACS_ULCORNER
            self.border.top_right    = curses.ACS_URCORNER
            self.border.bottom_left  = curses.ACS_LLCORNER
            self.border.bottom_right = curses.ACS_LRCORNER

    def __draw_border(self):
        # TODO: Make a own border function, the Curses one does not support all characters. (Raises OverflowError)
        self.screen.border(
            self.border.left,
            self.border.right,
            self.border.top,
            self.border.bottom,
            self.border.top_left,
            self.border.top_right,
            self.border.bottom_left,
            self.border.bottom_right,
        )

    def __erase_border(self):
        self.screen.border(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
