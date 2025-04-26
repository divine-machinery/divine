from ..utilities import types as Type
from ..layout import Layout
from ..organs import Border


class Write(object):

    def __init__(self,

        parent: Type.RealmBasedDomain,
        text: str = '',
        y: Type.CoordinateMember = None,
        x: Type.CoordinateMember = None,
        name: str = '',
        border: bool = False,

    ) -> None:

        """

        Prints a text on realm of parent on a certain coordinates. Line-break will be occured 
        once a character from the text hits the endx of parent. Move the cursor of the parent to 
        the end of the text afterward.

        Parameters

            parent:
            The Domain that is desired to be used as a host to print the text, required. 

            text:
            The text that is desired to be printed, optional, default=''

            y, x:
            The coordinate that will be used as the placement coordinate for the first character in 
            the text. If passed None(s), use the cursor coordiante of this(self) Domain. optional, 
            default=None, None

            name:
            The string representation of this Component, if None was passed, use an empty string, 
            optional, default=''

            border:
            TBA

        Raises:
            TBA

        """

        self.parent = parent

        self.string = text

        y = self.parent.cursor.y if y is None else y
        x = self.parent.cursor.x if x is None else x

        self.layout: Layout = Layout(self, (y, x), None, None)

        self.name: str = name
        self.border: Border = Border(self, border)

    def render(self) -> None:

        """

        Renders the stored text in the parent realm, starting at the stored coordinates (y, x). 
        This method will processes the stored text character by character, line breaks will be 
        occured when a character from a text reaches the edge of the realm(determined by endx
        of parent) while also considerate about the parent border thickness.

        """

        self.parent.cursor.y = self.layout.y
        self.parent.cursor.x = self.layout.x

        for character in self.string:

            # Will only prints the character if it is not a
            # ' '(space) while also on original x(starting x)

            if not (character == ' ' and self.parent.cursor.x == self.layout.x):

                self.parent.realm.addch(

                    # Borders thickness(1) is added if border is activated(True)
                    self.parent.cursor.y,
                    self.parent.cursor.x,
                    character,

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

        # Render the cursor after the processing
        self.parent.cursor.render()

        # Update the cursor coordinates
        self.parent.cursor.y += 1
        self.parent.cursor.reset('x')
