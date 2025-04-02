import time
from divine import Heaven

class _MainMenu(Heaven):

    menu = (
        "I love you.",
        "Perhaps, I like you.",
        "I do not like you.",
        "I hate you.",
    )

    def main(self):
        
        def draw_menu(menu):
            for index, item in enumerate(menu):
                self.write(f"{index}.{item}")

        while True:
            self.barrier(activate=True)
            self.write("> examples/main_menu.py", tag='awesome', top=2)
            self.write("Hello, World! Welcome Human!", bottom=1)
            draw_menu(self.menu)

            guess = self.ask("> Enter your guess(0/1/2/3): ", desired=int, informative=True, top=1)

            if guess.fullfilled and guess.answer in (0, 1, 2, 3):
                self.write("│ Oh okay...", top=1)
                self.write("│ Just remember. I always loved you<3")
                self.write("│ Exiting..")
                time.sleep(3)
                break
        
            self.purify()

    def _styles(self):
        self.tag.awesome = {
            'left': 4,
        }
        self.border.all = 'X'

MainMenu = _MainMenu()

MainMenu.run()
