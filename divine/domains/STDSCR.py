from curses import initscr, endwin

# initscr enter some kind of mode
terminal = initscr()

# endwin restore the default terminal
endwin()

# STDSCR is does a Domain but its layouts do not need to be 
# maintained by Layout objects. STDSCR is always constant.
class STDSCR(object):

    def __init__(self) -> None:

        self.freezed = False
        self.y, self.x = terminal.getbegyx()
        self.height, self.width = terminal.getmaxyx()
        self.freezed = True

    def __getattribute__(self, name):

        # self parenting >w<
        if name == 'parent':
            return self

        return super().__getattribute__(name)

    def __setattr__(self, name, value):            

        if name in ('y', 'x', 'height', 'width') and self.freezed:
            raise AttributeError(f"Freezed Domain, unable to set {name} to {value}.")

        return super().__setattr__(name, value)


def main() -> None:

    Terminal = STDSCR()

    print(Terminal.parent)
    print(f"Terminal<{Terminal.height}x{Terminal.width} at ({Terminal.y}, {Terminal.x})>")


if __name__ == '__main__':
    main()