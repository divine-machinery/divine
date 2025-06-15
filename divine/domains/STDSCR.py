from curses import initscr, endwin

# initscr enter some kind of mode
terminal = initscr()

# endwin restore the default terminal
endwin()

# STDSCR is does a Domain but its layouts do not need to be 
# maintained by Layout objects. STDSCR is always constant.
class STDSCR(object):

    y, x = terminal.getbegyx()
    height, width = terminal.getmaxyx()


if __name__ == '__main__':

    print(f"Terminal<{STDSCR.height}x{STDSCR.width} at ({STDSCR.y}, {STDSCR.x})>")

    # to be fixed later
    # this behaviour shouldn't be allowed
    STDSCR.height = 1000000
