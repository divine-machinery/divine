from typing import Optional, Tuple
from . import types as Type


class Layout(object):

    def __init__(self,

        source: Type.Domain,
        coordinate: Tuple[int, int],
        height: int, width: int,
        begy: Optional[int] = None, begx: Optional[int] = None,
        endy: Optional[int] = None, endx: Optional[int] = None,

    ) -> None:

        self.source: Type.Domain = source

        self.coordinate: Tuple = coordinate
        self.height: int = height
        self.width: int = width
        self.begy: int = begy
        self.begx: int = begx
        self.endy: int = endy
        self.endy: int = endx


    def __str__(self) -> str:
        return f"<{self.source}({self.height}x{self.width}) at {self.coordinate}>"
