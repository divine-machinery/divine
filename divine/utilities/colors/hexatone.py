# TODO: Manaully make the dataclass frozen(mutable)
from dataclasses import dataclass
from .rgb import rgb


@dataclass(order=True)
class hexatone:

    r: int
    g: int
    b: int

    def __init__(self, r, g, b):
        self.r, self.g, self.b = hexatone.colormodel((r, g, b), returnable=True)

    def __repr__(self):
        return f"hexatone({self.r}, {self.g}, {self.b})"

    @classmethod
    def channel(cls, channel: int, returnable=False) -> bool | int:
        """ Validate a HexaTone channel

        Arg:

            channel(int): The value of a HexaTone channel

            returnable(bool, optional): 
                Determine the return type. If True, return the received channel as an integer if valid, otherwise 
                raise Exception. If False(default), return True if the received channel is valid, otherwise False 

        """

        if not isinstance(channel, int) or not (0 <= channel <= 5): 
            if not returnable: return False
            elif returnable: raise Exception(f"{channel} is NOT a valid HexaTone channel.")

        else: return channel if returnable else True

    @classmethod
    def colormodel(cls, colormodel: tuple, returnable=False) -> None | tuple:
        """ Validate a HexaTone color model

        Args:

            channels(tuple[int, int, int]): 
                A tuple of channels, each representing a channel in a HexaTone color model.

            returnable(bool, optional): 
                Determine the return type. If True, return the received HexaTone color model as a tuple if valid, otherwise 
                raise Exception. If False(default), return True if the received color model is valid, otherwise False 
        
        """
        if not isinstance(colormodel, tuple):

            if not returnable: return False
            elif returnable: raise Exception(f"Channels must be implemented in a tuple.")

        elif len(colormodel) != 3:

            if not returnable: return False

            elif returnable: raise Exception(
                f"Received color model: {colormodel} is not in valid HexaTone color model format: (r, g, b)."
            )

        try:
            for channel in colormodel: cls.channel(channel, returnable=True)
            if not returnable: return True
            elif returnable: return tuple(colormodel)

        except Exception as error:
            if not returnable: return False
            elif returnable: raise error
