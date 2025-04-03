from .base import ColorModel, ChannelError

class hexatone(ColorModel):

    channel_capacity = 6

    def convert(self, colormodel):
        from .rgb import rgb, rgb_to_hexatone

        if isinstance(colormodel, rgb):
            self.r = rgb_to_hexatone(colormodel.r)
            self.g = rgb_to_hexatone(colormodel.g)
            self.b = rgb_to_hexatone(colormodel.b)

def hexatone_to_rgb(hextone_channel):
    if not isinstance(hextone_channel, int) or not (0 <= hextone_channel <= 5): 
        raise ChannelError(
            f"Invalid HexaTone Channel. Expected 'int' type between 0 and 255, got {hextone_channel} as '{type(hextone_channel).__name__}' type."
        )

    elif hextone_channel == 0: return 0
    elif hextone_channel == 1: return 51
    elif hextone_channel == 2: return 102
    elif hextone_channel == 3: return 153
    elif hextone_channel == 4: return 204
    elif hextone_channel == 5: return 255
