from ..utilities import types as Type
from ..layout import Layout
from .border import Border


class Write(object):

    def __init__(self,

        parent: Type.Domain,
        coordinate: Type.Coordinate,
        text: str = '',
        name: str = '',
        border: bool = False,

    ) -> None:

        self.parent = parent
        self.layout = Layout(self, coordinate, None, None)

        self.string = text
        self.chlist = list(text)

        self.name = name
        self.border = Border(self, border)

    def render(self) -> None:

        # This will stores/remember the orginally defined x
        # This is done because we will be changing the values of self.layout.x
        orgx = self.layout.x

        for ch in self.string:

            # Will only prints the character if it is not a
            # ' '(space) while also on original x(starting x)

            if not (ch == ' ' and self.layout.x == orgx):

                self.parent.realm.addch(

                    # Borders thickness(1) is added if border is activated(True)
                    self.layout.y + self.parent.border.ACTIVATED,
                    self.layout.x + self.parent.border.ACTIVATED,
                    ch

                )

                # moves x to left by 1
                self.layout.x += 1

                # line-break if it reaches the ending x of parent
                # this will be determined just before it reaches the border
                if self.layout.x > self.parent.endx:

                    # moves y to bottom by 1
                    self.layout.y += 1

                    # reset the x to orginally defined x 
                    self.layout.x = orgx
