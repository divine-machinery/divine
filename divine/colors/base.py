
class ChannelError(Exception):
    """Exception raised for errors related to color model channels."""


class ColorModel(object):

    def __init__(self, *args):
        
        if len(args) not in (1, 3):
            raise ValueError(f"Expected 1 or 3 arguments, got {len(args)}.")

        elif len(args) == 1:
            self.convert(args[0])

        elif len(args) == 3:

            for channel in args:

                if not isinstance(channel, int) or not (0 <= channel <= self.channel_capacity-1): 
                    raise ChannelError(
                        f"Invalid {self.__class__.__name__} Channel. Expected 'int' between 0 and {self.channel_capacity-1}, got {channel} as '{type(channel).__name__}' type."
                    )

            self.r, self.g, self.b = args

    def __repr__(self):
        return f"{self.__class__.__name__}({self.r}, {self.g}, {self.b})"
