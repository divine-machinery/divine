from time import sleep
from divine import Heaven, Paradise

class MainMenu(Heaven):

    def main(self):

        paradise = Paradise(self, (2, 4), border=True)
        # paradise.write("Now that we know who you are, I know who I am. I'm not a mistake! It all makes sense! In a comic, you know how you can tell who the arch-villain's going to be? He's the exact opposite of the hero. And most times they're friends, like you and me! I should've known way back when... You know why, David? Because of the kids. They called me Mr Glass.")

        paradise.realm.refresh()

        self.write("Hello, World!", 0, 40)
        self.write("Hello, World!", 0, 40)
        self.realm.refresh()
        sleep(20)

MainMenu(width=50, border=True).run()
