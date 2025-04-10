from curses import endwin
from divine import Screen

# NOTE: Still don't know how to write unit tests (yet), prolly due to the laziness or 'desire' to progress

stdscr = Screen()
endwin()  # Passed

print(stdscr.maxy) # Passed

print(stdscr.maxx) # Passed

print(stdscr.begx) # Passed

print(stdscr.begy) # Passed
