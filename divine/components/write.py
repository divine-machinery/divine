from ..utilities import types as Type
from ..layout import Layout
from .border import Border


class Write(object):

    def __init__(self,

        parent: Type.Domain,
        text: str = '',
        y: Type.CoordinateMember = None,
        x: Type.CoordinateMember = None,
        name: str = '',
        border: bool = False,

    ) -> None:

        self.parent = parent

        self.string = text
        self.chlist = list(text)

        y = self.parent.cursor.y if y is None else y
        x = 0 if x is None else x

        self.layout: Layout = Layout(self, (y, x), None, None)

        self.name: str = name
        self.border: Border = Border(self, border)

    def render(self) -> None:

        self.parent.cursor.y = self.layout.y
        self.parent.cursor.x = self.layout.x

        for ch in self.string:

            # Will only prints the character if it is not a
            # ' '(space) while also on original x(starting x)

            if not (ch == ' ' and self.parent.cursor.x == self.layout.x):

                self.parent.realm.addch(

                    # Borders thickness(1) is added if border is activated(True)
                    self.parent.cursor.y + self.parent.border.ACTIVATED,
                    self.parent.cursor.x + self.parent.border.ACTIVATED,
                    ch,

                )

                # moves x to left by 1
                self.parent.cursor.x += 1

                # line-break if it reaches the ending x of parent
                # this will be determined just before it reaches the border
                if self.parent.cursor.x > self.parent.endx:

                    # moves y to bottom by 1
                    self.parent.cursor.y += 1

                    # reset the x to orginally defined x 
                    self.parent.cursor.x = self.layout.x


        self.parent.cursor.y += 1

        # Render the cursor after the prcoessing
        self.parent.cursor.render()
