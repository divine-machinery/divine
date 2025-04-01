import curses
from box import Box
from prodict import Prodict
from .cursor import Cursor


class Realm(object):

    realm: curses.window
    cursor: Cursor

    has_border = False

    def _styles(self):
        """ Custom internal-stylings can be applied here. Borders, Layouts
            are also included here.
        """

    def main(self):
        """ The main application logics can be written here 
        """

    def start(self):
        """ Construct a ready-made realm, the default Terminal is 
            no longer accessible until it is deconstructed
        """

        # Assign Default Configurations
        self.__Default_Configurations()

        # Define Internal Stylings(not immediately used)
        self._styles()

        # Create the Heaven or Paradise, ready to utilize
        self.__validate_Layout()
        self.spawn()

        # Echo mode enabled for ask method
        curses.echo()

    def stop(self):
        """ Deconstruct the realm, restoring the default Terminal
        """
        curses.endwin()

    def run(self):
        """ Run the inheritance
        """
        ...

    def spawn(self):
        """ Spawn a Realm according to Layouts
        """
        ...

    def refresh(self):
        """ Update the Realm outputs
        """
        self.realm.refresh()

    def purify(self):
        """ Clear the Realm outputs.
            Reset the cursors
        """
        self.realm.clear()
        self.cursor.reset('x')
        self.cursor.reset('y')
        self.refresh()

    def write(
        self, 
        text = '', 
        *coordinates, 
        pully = True, 
        pullx = True, 
        pullyx = False, 
        reverse = False, 
        top = 0,
        bottom = 0,
        left = 0,
        right = 0,
        tag = ''
    ):

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

        def inline_styled(property):
            match property:
                case 'top': return top != 0
                case 'bottom': return bottom != 0
                case 'left': return left != 0
                case 'right': return right != 0

        def update_cursor(axis):
            match axis:
                case 'y': self.cursor.y = y - self.has_border
                case 'x': self.cursor.x = x - self.has_border
                case _: raise Exception

        # -----------------------------------------------------------------

        # Update cursor
        if pully: update_cursor('y')
        if pullx: update_cursor('x')
        if not pullx: self.cursor.reset('x') # Reset to 0

        # -----------------------------------------------------------------

        tags = tag.split()

        # Apply internal-stylings for each tags
        for tag in tags:
            if tag in self.tag.keys():
                # NOTE <--------------------------------------- !!!
                # If the property is only changing axis but not
                # cursor, the cursor is specifically need to update 
                if self.__tag_has_property('top', tag) and not inline_styled('top'): 
                    y += self.tag[tag]['top']
                    update_cursor('y')

                if self.__tag_has_property('bottom', tag) and not inline_styled('bottom'): 
                    self.cursor.y += self.tag[tag]['bottom']

                if self.__tag_has_property('left', tag) and not inline_styled('left'): 
                    x += self.tag[tag]['left']
                    update_cursor('x')

                if self.__tag_has_property('right', tag) and not inline_styled('right'): 
                    text = text + " " * self.tag[tag]['right']

        # -----------------------------------------------------------------
        
        # Apply inline-stylings

        if pullyx:
            self.cursor.y = y - self.has_border - 1
            self.cursor.x = x + len(text) - self.has_border

        if reverse: x = self.maxx - len(text) - self.has_border

        if inline_styled('top'):
            y += top
            update_cursor('y')

        if inline_styled('bottom'):
            self.cursor.y += bottom
            update_cursor('x')

        if inline_styled('left'):
            x += left

        if inline_styled('trightop'):
            text = text + " " * right

        # AND FINALLY, Write the text :>
        self.realm.addstr(y, x, text)
        self.refresh()

    def ask(
        self, 
        question = '', 
        *coordinates, 
        pully = True, 
        pullx = True, 
        pullyx = False, 
        reverse = False, 
        top = 0,
        bottom = 0,
        left = 0,
        right = 0,
        desired = str, 
        informative = False,
        tag = ''
    ):

        self.write(question, *coordinates, pully=pully, pullx=pullx, pullyx=pullyx, reverse=reverse, top=top, bottom=bottom, left=left, right=right, tag=tag)
        answer = self.realm.getstr().decode('utf-8')

        try: answer = (desired(answer)); fullfilled = True
        except: fullfilled = False

        return answer if not informative else Box({'answer': answer, 'fullfilled': fullfilled})
    def barrier(self, activate=None, **kwargs):
        """ Draw a border, if called again, erase the drawn border.
        """

        # TODO: Make a own border function, the Curses one does not support all 
        # characters. (Raises OverflowError)

        self.border.all          = kwargs.get('all', self.border.all)
        self.border.left         = kwargs.get('left', self.border.left )
        self.border.right        = kwargs.get('right', self.border.right )
        self.border.top          = kwargs.get('top', self.border.top )
        self.border.bottom       = kwargs.get('bottom', self.border.bottom )
        self.border.top_left     = kwargs.get('top_left', self.border.top_left )
        self.border.top_right    = kwargs.get('top_right', self.border.top_right )
        self.border.bottom_left  = kwargs.get('bottom_left', self.border.bottom_left )
        self.border.bottom_right = kwargs.get('bottom_right', self.border.bottom_right )

        def draw():
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
            if activate == None: self.has_border = True

        def erase():
            self.realm.border(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
            if activate == None: self.has_border = False

        if self.border.all != None:
            for border_ch in self.border:
                self.border[border_ch] = self.border.all

        if activate == None: draw() if not self.has_border else erase()
        elif activate: draw()
        elif not activate: erase()


    def __Default_Configurations(self):

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

        self.tag = Box()

    def __validate_Layout(self):
        # TODO: Create a own exception or find a suitable
        for layout in (self.maxy, self.maxx, self.begy, self.begx):
            if layout < 0:
                raise Exception

    def __tag_has_property(self, property, tag) -> bool:
        match property:
            case 'top':         return 'top'        in self.tag[tag].keys()
            case 'bottom':      return 'bottom'     in self.tag[tag].keys()
            case 'left':        return 'left'       in self.tag[tag].keys()
            case 'right':       return 'right'      in self.tag[tag].keys()
