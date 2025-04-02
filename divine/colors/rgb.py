from math import ceil
from .base import ColorModel, ChannelError

class rgb(ColorModel):

    channel_capacity = 256

    def convert(self, colormodel):
        from .hexatone import hexatone, hexatone_to_rgb

        if isinstance(colormodel, hexatone):
            self.r = hexatone_to_rgb(colormodel.r)
            self.g = hexatone_to_rgb(colormodel.g)
            self.b = hexatone_to_rgb(colormodel.b)

def rgb_to_hexatone(rgb_channel):
    if not isinstance(rgb_channel, int) or not (0 <= rgb_channel <= 255): 
        raise ChannelError(
            f"Invalid RGB Channel. Expected 'int' type between 0 and 255, got {rgb_channel} as '{type(rgb_channel).__name__}' type."
        )

    elif rgb_channel == 0: return 0
    elif (0 < rgb_channel <= 51): return 1
    elif (51 < rgb_channel <= 102): return 2
    elif (102 < rgb_channel <= 153): return 3
    elif (153 < rgb_channel <= 204): return 4
    elif (204 < rgb_channel <= 255): return 5

def rgb_to_termcolor(rgb_channel):
    if not isinstance(rgb_channel, int) or not (0 <= rgb_channel <= 255): 
        raise ChannelError(
            f"Invalid RGB Channel. Expected 'int' type between 0 and 255, got {rgb_channel} as '{type(rgb_channel).__name__}' type."
        )

    return ceil(rgb_channel/255 * 1000)
