import time
import curses
from divine import Heaven


class _Colors(Heaven):

    def main(self):
        
        curses.curs_set(0)
        for color_num in range(256+256):
            self.realm.addstr(f'{color_num} ', curses.color_pair(color_num))
        self.realm.addstr(f" curses.COLOR_PAIRS: {curses.COLOR_PAIRS}")
        self.realm.addstr(f"  curses.COLORS: {curses.COLORS}")
        self.ask()

Colors = _Colors()

Colors.run()
