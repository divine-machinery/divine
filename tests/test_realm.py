from curses import endwin
from divine import Realm

try:

    realm = Realm()

    print() # ---

    print(realm)
    print(repr(realm))

    print() # ---

    print(f"Coordinate: {realm.coordinate}")
    print(f"Height: {realm.height}")
    print(f"Width: {realm.width}")

    print() # ---

    print(f"Beginning Coordinates: ({realm.begy}, {realm.begx})")
    print(f"Ending Coordinates: ({realm.endy}, {realm.endx})")

    print() # ---

except Exception as error:
    raise error
