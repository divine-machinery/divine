from divine import Layout, Heaven

class MyHeaven(Heaven):

    def __init__(self, y = 2, x = 2, height = 10, width = 30):
        super().__init__(y, x, height, width)

print(MyHeaven().layout)
# output: "<MyHeaven(10x30) at (2, 2)>"
