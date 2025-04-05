import curses
from math import ceil
from box import Box
from .cursor import Cursor
from .exceptions import *


class Realm(object):

    realm: curses.window
    cursor: Cursor

    has_border = False

    def styles(self):
        """ Custom internal-stylings can be applied here. Borders, 
            Realm Layouts are also included here.
        """

    def main(self):
        """ The main application logics can be written here 
        """

    def start(self):
        """ Construct a ready-made realm, the default Terminal is 
            no longer accessible until it is deconstructed.
        """

        # Apply Default Configurations
        self.__Default_Configurations()

        # Apply Internal Stylings, overide the Default Configurations
        self.styles()

        # Validate the layouts. Raise InvalidLayout 
        # if custom layouts are below zero 
        self.__validate_Layout()

        # Spawn a realm to display output
        self.summon()

        # Enable Echo mode, specifically for ask()
        curses.echo()

    def stop(self):
        """ Deconstruct the realm, restoring the default Terminal
        """
        curses.endwin()

    def run(self):
        """ Run the main() of the Realm
        """
        ...

    def summon(self):
        """ Spawn a Realm according to Layouts
        """
        ...

    def refresh(self):
        """ Update the Realm outputs
        """
        self.realm.refresh()

    def clear(self):
        """ Clear the Realm outputs.
            Reset the cursors
        """
        self.realm.clear()
        self.cursor.reset('x')
        self.cursor.reset('y')
        self.refresh()


# -----------------------------------------------------------------


    def write(
        self, 

        text: str = '', 
        *coordinates, 
        pully: bool = True, 
        pullx: bool = False, 
        pullyx: bool = False, 
        # reverse: bool = False, 
        top: int = None,
        bottom: int = None,
        left: int = None,
        right: int = None,
        leading: int = 1,
        tag: str = ''

    ) -> None:

        # Validate the coordinates
        if len(coordinates) not in (0, 2):
            raise InvalidCoordinate(
                f"Expected zero to two coordinates. Got {coordinates}"
            )

        # If received no coordinates, automatically 
        # assign coordinates by tracking the cursors
        elif len(coordinates) == 0:

            # Assign the coordinates to write on
            y = self.cursor.y + self.has_border
            x = self.cursor.x + self.has_border


        # If received two coordinates, simply assign those
        # coordinates.(What else you expect anyway.. XD)
        elif len(coordinates) == 2:

            # But wait, validate the type of received coordinates first.
            # Gotta raise TypeError if they aren't 'int' types :< 
            if not isinstance(coordinates[0], int) or not isinstance(coordinates[1], int):
                raise TypeError(
                    f"Expected coordinates as intgers. Got {type(coordinates[0]).__name__}, {type(coordinates[1]).__name__}."
                )

            # Assign the coordinates to write on
            y = coordinates[0] + self.has_border
            x = coordinates[1] + self.has_border


        # -----------------------------------------------------------------

        # INTERNAL FUNCTIONS <--------------------------------------- > w <

        # Can safely create internal functions, assuming
        # no Error can be produced at this point :>

        def inline_styled(property):
            # Checked if a property has inline-styled; Determine
            # by if the property has passed in write()'s arguments 

            # TODO: This funciton can be refined using locals()

            # I just love switch cases sooo MUCH :3
            match property:
                case 'top': return top is not None
                case 'bottom': return bottom is not None
                case 'left': return left is not None
                case 'right': return right is not None

        # -----------------------------------------------------------------

        # This dictionary is a list that track all the stylings defined
        style = dict()

        # Assin default styles:
        style['top'] = 0
        style['bottom'] = 0
        style['left'] = 0
        style['right'] = 0

        # -----------------------------------------------------------------

        # INTERNAL STYLINGS <--------------------------------------- > w <

        # NOTE: <------------------------------------------- !!!
        # All the internatl stylings will be applied only if no 
        # inline-styles were applied, otherwise will overide.

        # Separate the tags
        tags = tag.split()

        # Add internal-stylings for each tags
        for tag in tags:

            # Check if received tag is styled
            if tag in self.tag.keys():

                # top
                if self.__tag_has_property(tag, has='top') and not inline_styled('top'):
                    style['top'] = self.tag[tag]['top']

                # bottom
                if self.__tag_has_property(tag, has='bottom') and not inline_styled('bottom'): 
                    style['bottom'] = self.tag[tag]['bottom']

                # left
                if self.__tag_has_property(tag, has='left') and not inline_styled('left'): 
                    style['left'] = self.tag[tag]['left']

                # right
                if self.__tag_has_property(tag, has='right') and not inline_styled('right'): 
                    style['right'] = self.tag[tag]['right']


        # -----------------------------------------------------------------

        # INLINE STYLINGS <--------------------------------------- > w <

        # Apply inline-stylings

        if inline_styled('top'):
            style['top'] = top

        if inline_styled('bottom'):
            style['bottom'] = bottom

        if inline_styled('left'):
            style['left'] = left

        if inline_styled('right'):
            style['right'] = right

        # -----------------------------------------------------------------

        # NOTE <-------------------------------------------------------- !!!
        # The cursor also should be updated once any changes on coordinates
        # has been made. 

        y += style['top']
        x += style['left']

        if pully: self.cursor.y = y - self.has_border + style['bottom'] + leading
        if pullx: self.cursor.x = x - self.has_border + style['right']
        if not pullx: self.cursor.reset('x') #! Reset to 0

        #  NOTE ---------------------------------------------------------------------
        # 
        #  pully:
        #     True(default): convince the later write() to follow its y coordinate
        #     False: The later write() will step on this write()'s y coordinate  
        # 
        #  pullx:
        #    True(default): convince the later wrtie() to follow its x coordinate
        #    False: The later write() will always start at 0 x coordinate
        #
        #  --------------------------------------------------------------------------

        # This is the another concept to style left and right
        # text = (' ' * style['left']) + str(text) + (' ' * style['right'])

        if pullyx:
            self.cursor.y = y - self.has_border
            self.cursor.x = x + len(text) - self.has_border

        # TODO: Need to refactor, until then will be commented out
        # if reverse: x = self.maxx - len(text) - self.has_border

        # AND FINALLY, Write the text :>
        self.realm.addstr(y, x, str(text))
        self.refresh()

    def ask(
        self, 

        question: str = '', 
        *coordinates, 
        pully: bool = True, 
        pullx: bool = False, 
        pullyx: bool = False, 
        # reverse: bool = False, 
        top: int = None,
        bottom: int = None,
        left: int = None,
        right: int = None,
        desired: type = str, 
        informative: bool = False,
        tag: str = ''

    ) -> Box | None:

        self.write(question, *coordinates, pully=pully, pullx=pullx, pullyx=pullyx, top=top, bottom=bottom, left=left, right=right, tag=tag)
        answer = self.realm.getstr().decode('utf-8')

        try: answer = (desired(answer)); fullfilled = True
        except: fullfilled = False

        return answer if not informative else Box({'answer': answer, 'fullfilled': fullfilled})

    def listen(self, *coordinates, length=None):
        """ A very customizable input method.
        """

        # TODO ------------------------------------------------------- > w <
        # Add arrow keys functionality

        # This list will track all the characters that user pressed between ascii values 32 to 126
        string = []

        # Temporarily Disable the text echoing, specifically for curses.window.getch() 
        curses.noecho()

        if len(coordinates) not in (0, 2):
            raise InvalidCoordinate(
                f"Expected zero to two coordinates. Got {coordinates}"
            )

        elif len(coordinates) == 0:
            y = 0 + (self.cursor.y + 1)
            x = 0 + self.cursor.x

        elif len(coordinates) == 2:
            y = coordinates[0]
            x = coordinates[1]

        cursor_y = y + self.has_border
        cursor_x = x + self.has_border

        # Determine the maximum amount of inputtable characters
        border_length = (self.has_border + self.has_border)
        max_ch = (self.maxy - border_length - self.cursor.x) * (self.maxx - border_length - self.cursor.y)

        if length is not None:
            if max_ch < length: raise ValueError(
                f"Expected the parameter 'length' to be less than {max_ch}. Got {length}."
            )
        else:
            length = max_ch

        # Enter a loop and stay inside until Enter Key(ascii value 10) is pressed 
        while True:

            # Move the cursor 
            self.realm.move(cursor_y, cursor_x)

            # This guy is the one who has been listening almost all the keyboard events 
            ch = self.realm.getch()

            # If the received character is a backspace 
            if ch == 127 and len(string) != 0:

                # Remove the latest character from the list
                string.pop()

                # Update the cursors
                if cursor_x == self.has_border:
                    cursor_y -= 1
                    cursor_x = self.maxx - self.has_border
                cursor_x -= 1

                # Update the screen
                self.realm.addch(cursor_y, cursor_x, " ")


            # If the received character is a typable letter(ascii value 32 to 126)
            elif 32 <= ch <= 126 and len(string) < length:

                # Append the received character to the list
                string.append(chr(ch))

                # Update the screen
                self.realm.addch(cursor_y, cursor_x, chr(ch))

                # Update the cursors
                if cursor_x == self.maxx - 1 - self.has_border:
                    cursor_x = self.has_border
                    cursor_y += 1

                else: cursor_x += 1

            # If the received character is an Enter
            elif ch == 10:

                # Leave the loop
                break

        # Re-enable the enchoing for other curses.window.get* methods
        curses.echo()

        # Update self.cursors (not better_getstr's cursors)
        self.cursor.y = cursor_y - 1

        # Finally return the list of received characters 
        return "".join(string)
    
    def barrier(
            self, 
            
            activate: bool = None, 
            **kwargs

        ) -> None:

        """ Draw a border, if called again, erase the drawn border.
        """

        # TODO ------------------------------------------------------ > w <
        # Make a own border function, the Curses one does not support all 
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
            self.has_border = True

        def erase():
            self.realm.border(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
            self.has_border = False

        if self.border.all != None:
            for border_ch in self.border:
                self.border[border_ch] = self.border.all

        if activate == None: draw() if not self.has_border else erase()
        elif activate: draw()
        elif not activate: erase()


# -----------------------------------------------------------------


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
        for layout in (self.maxy, self.maxx, self.begy, self.begx):
            if layout < 0:
                raise InvalidLayout(f"Expected a layout larger than 0. Got {layout}.")

    def __tag_has_property(self, tag, has) -> bool:
        match has:
            case 'top':         return 'top'        in self.tag[tag].keys()
            case 'bottom':      return 'bottom'     in self.tag[tag].keys()
            case 'left':        return 'left'       in self.tag[tag].keys()
            case 'right':       return 'right'      in self.tag[tag].keys()
