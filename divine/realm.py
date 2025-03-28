import curses
from box import Box
from prodict import Prodict
from .cursor import Cursor


class Realm(object):

    realm: curses.window
    cursor: Cursor

    def _Layout(self):
        """ Custom layout configurations can be written here. If
            not specified, the default configurations will take over
        """

    def _Border(self):
        """ Custom border configurations can be written here. If
            not specified, the default configurations will take over
        """

    def _styles(self):
        ...

    def main(self):
        """ The main application logics can be written here 
        """

    def start(self):
        """ Construct a ready-made realm, the default Terminal is 
            no longer accessible until it is deconstructed
        """

        # Define Default Configurations
        self.Default_Configurations()

        # Overwrite the Default Configurations if specified
        self._Layout()
        self.__validate_Layout()

        self._Border()

        self._Layout()
        self.__validate_Layout()

        self._styles()

        # Create the Heaven or Paradise, ready to utilize
        self.spawn()

        # Echo mode enabled for ask method
        curses.echo()

        # Apply Configurations
        if self.border.all != None:
            for border_ch in self.border:
                self.border[border_ch] = self.border.all
        self.__draw_border() if self.has_border else self.__erase_border()

    def stop(self):
        """ Deconstruct the realm, restoring the default Terminal
        """
        curses.endwin()

    def run(self):
        """ Run the inheritance
        """
        ...

    def spawn(self):
        ...

    def write(self, text, *coordinates, pully=True, pullx=True, pullyx=False, reverse=False, id=''):

        if len(coordinates) not in (0, 2):
            raise Exception

        elif len(coordinates) == 0:

            self.cursor.y += 1
            y = self.cursor.y + self.has_border
            x = self.cursor.x + self.has_border

        elif len(coordinates) == 2:

            if not isinstance(coordinates[0], int) or not isinstance(coordinates[1], int):
                raise Exception

            y = coordinates[0] + self.has_border
            x = coordinates[1] + self.has_border

        # -----------------------------------------------------------------

        def update_cursor(axis):
            match axis:
                case 'y': self.cursor.y = y - self.has_border
                case 'x': self.cursor.x = x - self.has_border
                case _: raise Exception

        def id_has_property(property) -> bool:
            match property:
                case 'padding':     return 'padding'    in self.id[id].keys()

        def padding_has_property(property) -> bool:
            match property:
                case 'top':         return 'top'        in self.id[id].padding.keys()
                case 'bottom':      return 'bottom'     in self.id[id].padding.keys()
                case 'left':        return 'left'       in self.id[id].padding.keys()
                case 'right':       return 'right'      in self.id[id].padding.keys()

        # -----------------------------------------------------------------

        if pully: update_cursor('y')
        if pullx: update_cursor('x')
        if not pullx: self.cursor.reset('x') # Reset to 0

        # Apply internal-stylings
        if id in self.id.keys():
            if id_has_property('padding'):
                # NOTE <--------------------------------------- !!!
                # If the property is only changing axis but not
                # cursor, the cursor is specifically need to update 

                if padding_has_property('top'):                          # Padding Top
                    y += self.id[id].padding.top
                    update_cursor('y')

                if padding_has_property('bottom'):                       # Padding Bottom
                    self.cursor.y += self.id[id].padding.bottom

                if padding_has_property('left'):                         # Padding Left
                    text = " " * self.id[id].padding.left + text

                if padding_has_property('right'):                        # Padding Right
                    text = text + " " * self.id[id].padding.right

        # Apply inline-stylings
        if pullyx:
            self.cursor.y = y - self.has_border - 1
            self.cursor.x = x + len(text) - self.has_border

        if reverse: x = self.maxx - len(text) - self.has_border

        # AND FINALLY, Write the text :>
        self.realm.addstr(y, x, text)

    def __validate_Layout(self):
        # TODO: Create a own exception or find a suitable
        for layout in (self.maxy, self.maxx, self.begy, self.begx):
            if layout < 0:
                raise Exception

    def Default_Configurations(self):

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

            # ID will use Box for now. It wasn't usable until commit baf873d83edc7936d288941e24557b71058b9da2
            self.id = Box()

    def __draw_border(self):
        # TODO: Make a own border function, the Curses one does not support all characters. (Raises OverflowError)
        self.realm.border(
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
        self.realm.border(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
