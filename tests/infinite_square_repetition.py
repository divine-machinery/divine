# [22x11]: may requires a terminal size of 22 characters and 11 lines to run

from divine import Heaven, Paradise

class MainMenu(Heaven):
        
    def main(self):

        paradises = [Paradise(self, (None, None), border=True)]

        for _ in range(4, self.endy, 4):

            paradises.append(Paradise(paradises[-1], (None, None), border=True))

        text = "Hello World"
        midy = (paradises[-1].height // 2) 
        midx = (paradises[-1].width // 2) - (len(text) // 2) 

        paradises[-1].realm.addstr(midy, midx, text)

        self.realm.getch()

MainMenu(border=True).run()

#  To whoever reading this(prolly my old me)
#  
#  This is juts an bad example, the real usage shouldn't be this complicated
# 
#  I'm sorry if I scared you with these formula
#
#  15 | text = "Hello World"
#  16 | midy = (paradises[-1].width // 2)
#  17 | midx = (paradises[-1].height // 2) - (len(text) // 2) 
#
#  But if you are willing to put some effort on this simple 
#  formula, I assure your life will be easier than before.
#
#  The name of the variable is self-explantory to be honest.
#  midy calculates the middle point of a y axis
#  Like wise, midx calcualtes the middle point of an x axis
#
#  You may have already know that if you divide a number with
#  with two, you will get the half of that number if you either
#  ceil or floor it.
#
#  For example: 10  //  2  ==  5
#               24  //  2  ==  12
#                5  //  2  ==  2
#               15  //  2  ==  7
#
#  If your text that you want to display only consist of one 
#  character and 1 line, well no issue here.
#
#  But if your text has more than one characters or lines, you
#  will need to divide that numbers of characters and lines by
#  two.
#
#  This is what my example basically does
#  17 | midx = (paradises[-1].height // 2) - (len(text) // 2)
#
#  Well we don't need to do the same thing for midy since my
#  text only got one line :/
