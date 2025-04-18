from curses import endwin
from divine import Screen

try:

    screen = Screen()

    print() # ---

    print(screen)
    print(repr(screen))

    print() # ---

    print(f"Coordinate: {screen.coordinate}")
    print(f"Height: {screen.height}")
    print(f"Width: {screen.width}")

    print() # ---

    print(f"Beginning Coordinates: ({screen.begy}, {screen.begx})")
    print(f"Ending Coordinates: ({screen.endy}, {screen.endx})")

    print() # ---

except Exception as error:
    endwin()
    raise error
