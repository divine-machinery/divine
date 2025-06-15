from curses import initscr, endwin

# initscr enter some kind of mode
terminal = initscr()

# endwin restore the default terminal
endwin()


class STDSCR(object):

    y, x = terminal.getbegyx()
    height, width = terminal.getmaxyx()


if __name__ == '__main__':
    print(f"Terminal<{STDSCR.height}x{STDSCR.width} at ({STDSCR.y}, {STDSCR.x})>")
