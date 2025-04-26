from divine import Heaven, Paradise


class Paper(Heaven):

    def styles(self):
        self.width = 50
        self.coordinate = (2, 2)
        self.height = self.height - self.y
        self.inside = Paradise(self)
        self.inside.y = 1
        self.inside.x = 2
        self.inside.height = self.inside.height - self.inside.y
        self.inside.width = self.inside.width - self.inside.x

    def main(self):
        self.inside.write("Now that we know who you are, I know who I am. I'm not a mistake! It all makes sense! In a comic, you know how you can tell who the arch-villain's going to be? He's the exact opposite of the hero. And most times they're friends, like you and me! I should've known way back when... You know why, David? Because of the kids. They called me Mr Glass.")
        self.inside.write()
        self.inside.write("Now that there is the Tec-9, a crappy spray gun from South Miami. This gun is advertised as the most popular gun in American crime. Do you believe that shit? It actually says that in the little book that comes with it: the most popular gun in American crime. Like they're actually proud of that shit.")
        self.inside.write()
        self.inside.write("The path of the righteous man is beset on all sides by the iniquities of the selfish and the tyranny of evil men. Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of darkness, for he is truly his brother's keeper and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who would attempt to poison and destroy My brothers. And you will know My name is the Lord when I lay My vengeance upon thee.")
        self.inside.write()
        self.inside.write("Generated from: https://slipsum.com/")
        self.realm.getch()

Paper(border=True).run()