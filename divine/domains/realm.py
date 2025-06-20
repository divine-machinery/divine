from ..utilities import types as Type
from . import STDSCR
from ..layout import Layout
from typing import Tuple
from curses import window, newwin, endwin


class Realm(object):

    def __init__(self,
    
        parent: Type.Domain = STDSCR(),
        y: Type.LValue = None, x: Type.LValue = None,
        width: Type.LValue = None, height: Type.LValue = None

    ):

        self.parent = parent

        self.layout = Layout(self,
            coordinate = (y, x),
            width = width, height = height
        )

        self.realm: window
        self.has_border: bool = False


    # ===== cranking methods =====

    def summon(self) -> None:
        """ Create a window object and store it in this instance's ".realm".

        This method will call styles() first, then create the desired object.

        Any Python curses' window object methods are eligible to use as if 
        they were the same(They are). 
        
        curses' initscr() might be required to call first, at least for this 
        model. curses' endwin() is required to call as a clean up process after.

        """

        # user defined layouts will be applied first
        self.styles()

        # create a curses window object
        self.realm = newwin(self.height, self.width, self.y, self.x)


    def styles(self) -> None:
        """ This is where you pre-define the layouts you want.
        """


    def main(self) -> None:
        """ This is where your application logics go.
        """


    def terminate(self) -> None:
        """ Same as doing curses.endwin() """

        endwin()


    def run(self) -> None:
        """ Call this when you intend to run your application logics written 
            in main(). By default, this method will call summon(), main(), 
            and terminate() in sequence.
        """
        
        self.summon()
        self.main()
        self.terminate()


    # ===== operational methods =====

    def fence(self, enable: bool = True) -> None:
        """ Draw a border around the window object.

        This method is an Operational Method
        ====================================
        Running this without calling summon() first will 
        result in curses' error and put your terminal in 
        a certain mode which is not usable at all. Reseting 
        or restarting your terminal might help.
        """

        # TODO: Instead of relying on curses' original border() 
        # method, manually draw the border for flexibility
        if enable and not self.has_border:
            self.realm.border()
            self.has_border = True

        elif not enable and self.has_border:
            self.realm.border(" ", " ", " ", " ", " ", " ", " ", " ")
            self.has_border = False


    # ===== lazy getters and setters or whatever it is =====
    
    # -- coordinates

    @property
    def y(self) -> int:
        return self.layout.y

    @y.setter
    def y(self, value: Type.LValue) -> None:
        self.layout.y = value


    @property
    def x(self) -> int:
        return self.layout.x

    @x.setter
    def x(self, value: Type.LValue) -> None:
        self.layout.x = value
    
    # -- height

    @property
    def height(self) -> int:
        return self.layout.height

    @height.setter
    def height(self, value: Type.LValue) -> None:
        self.layout.height = value
    
    # -- width

    @property
    def width(self) -> int:
        return self.layout.width

    @width.setter
    def width(self, value: Type.LValue) -> None:
        self.layout.width = value

    # -- extras

    @property
    def coordinate(self) -> Tuple[int, int]:
        return self.layout.coordinate

    @coordinate.setter
    def coordinate(self, coordinate: Type.Coordinate) -> None:
        self.layout.coordinate = coordinate
