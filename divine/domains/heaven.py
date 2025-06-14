# domain

from .. import types as Type
from typing import Optional
from .. import Layout


class Heaven(object):

    def __init__(self, 

        y: Optional[int] = None, x: Optional[int] = None,
        height: Optional[int] = None, width: Optional[int] = None,

    ) -> None:

        self.layout = Layout(self, 
            coordinate=(y, x), 
            height=height, 
            width=width        
        )

