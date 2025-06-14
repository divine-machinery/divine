from typing import Optional, Tuple
from . import types as Type


class Layout(object):

    def __init__(self,

        # pardon my "unholinesses"

        source: Type.Domain,
        coordinate: Tuple[Optional[int], Optional[int]] = (None, None),
        height: Optional[int] = None, width: Optional[int] = None,
        begy: Optional[int] = None, begx: Optional[int] = None,
        endy: Optional[int] = None, endx: Optional[int] = None,

    ) -> None:

        self.source: Type.Domain = source

        self.coordinate: Tuple[Optional[int], Optional[int]] = coordinate
        self.height: Optional[int] = height
        self.width: Optional[int] = width
        self.begy: Optional[int] = begy
        self.begx: Optional[int] = begx
        self.endy: Optional[int] = endy
        self.endx: Optional[int] = endx


    def __str__(self) -> str:
        return f"<{self.source.__class__.__name__}({self.height}x{self.width}) at {self.coordinate}>"
