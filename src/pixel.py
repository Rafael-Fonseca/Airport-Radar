from graphics import *

class Pixel:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return('Position: {}, {}\tColor: {}'.format(self.x, self.y, self.color) )



    