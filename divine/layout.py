from .utilities import types as Type


# the intention of this object is to maintain the layouts of 
# all Domains. One usecase could be layout validations.
class Layout(object):

    def __init__(self, 
    
        source: Type.Domain,
        coordinate: Type.Coordinate = (None, None),
        height: Type.LValue = None,
        width: Type.LValue = None
    
    ) -> None:

        self.source = source
        self.__y, self.__x = coordinate
        self.__height = height
        self.__width = width
