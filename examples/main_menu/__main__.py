# NOTE <------------------------------------------------------------------- !!!
# This is still in experiment stage, preferably a prototype, even though this 
# was pushed into main brach due to my lack of experiences with git, this needs
# a lot of refinements.

import time
from divine import Heaven

class _MainMenu(Heaven):

    def _Layout(self):
        self.maxy =19
        self.maxx = 50

    def _Border(self):
        self.has_border = True

    menu = (
        "I love you.",
        "Perhaps, I like you.",
        "I do not like you.",
        "I hate you.",
    )

    def main(self):
        
        def draw_menu(menu):
            self.write()
            for index, item in enumerate(menu):
                self.write(f"{index}.{item}", tag='menu_item')

        while True:
            self.write("> examples/main_menu.py", tag='filepath norm_text')
            self.write("Hello, World! Welcome Human!", tag='welcoming_message')
            draw_menu(self.menu)

            guess = self.ask("> Enter your guess(0/1/2/3): ", desired=int, informative=True, tag='question', pullx=False)

            if guess.fullfilled and guess.answer in (0, 1, 2, 3):
                self.write("│ Oh okay...", tag='farewell norm_text')
                self.write("│ Just remember. I always loved you<3")
                self.write("│ Exiting..", tag='log')
                time.sleep(3)
                break
        
            self.reset()

    def _styles(self):
        self.tag.norm_text = {
            'left': 2,
        }

        self.tag.filepath = {
            'top': 1,
        }

        self.tag.question = {
            'top': 2,
        }

        self.tag.farewell = {
            'top': 1,
        }

        self.tag.log = {
            'top': 1,
        }

MainMenu = _MainMenu()

MainMenu.run()
