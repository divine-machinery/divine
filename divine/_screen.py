from curses import initscr, endwin

stdscr = initscr()
endwin()

class __Screen(object):
    maxy, maxx = stdscr.getmaxyx()
    begy, begx = stdscr.getbegyx()

screen = __Screen()