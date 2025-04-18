from curses import endwin
from divine import Realm

try:

    realm = Realm()

    print() # ---

    print(realm)
    print(repr(realm))

    print() # ---

    print(f"Coordinate: {realm.layout.coordinate}")
    print(f"Height: {realm.layout.height}")
    print(f"Width: {realm.layout.width}")

    print() # ---

    print(f"Beginning Coordinates: ({realm.layout.begy}, {realm.layout.begx})")
    print(f"Ending Coordinates: ({realm.layout.endy}, {realm.layout.endx})")

    print() # ---

except Exception as error:
    raise error
