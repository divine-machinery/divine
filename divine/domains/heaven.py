from typing import List, Optional
from ..utilities import types as Type
from curses import window, newwin, endwin
from .realm import Realm
from .paradise import Paradise
from .screen import Screen


class Heaven(Realm):

    def __init__(self,

        parent: Type.Domain = Screen(),
        coordinate: Type.Coordinate = (None, None), 
        height: Optional[int] = None,
        width: Optional[int] = None,
        border: bool = False,
        name: Optional[str] = None,

    ) -> None:

        super().__init__(parent, coordinate, height, width, border, name)
        self.children: List[Paradise] = list()

    def styles(self) -> None:
        """ Layouts, Borders and such can be pre-implement here 
        """

        ...

    def summon(self) -> None:
        """ Enter Terminal raw mode. Summon a realm object and store it as attribute 'realm'.
        """

        self.realm: window = newwin(
            self.height, 
            self.width, 
            self.y + self.parent.orgy, 
            self.x + self.parent.orgx
        )


    def start(self) -> None:
        """ Pre-implemented styles will be imported first and validate them, upon sucess, summon
            a realm and immediately draw the border if defined.
        
        """

        self.styles()
        self.layout.validate()
        self.summon()
        self.border.apply()

        for child in self.children:
            child.run()


    def main(self) -> None:
        """ Main application logics such as loops, writes and such can be written here. """

        ...


    def stop(self) -> None:
        """ Exit Terminal raw mode. Enter the default cook mode. """

        endwin()


    def run(self) -> None:
        """ Call start(), main(), stop(). Any excpetion raised will be forced to call stop() and
            display the exception message afterewards.
        """

        try:
            self.start()
            self.main()

        except Exception as error:
            self.stop()
            raise error

        else:
            self.stop()

