from graphics import *

class Draw:
    def __init__(self, display):
        self.display = display
        

    def pixel(self, x, y, color):
        return self.display.plotPixel(x,y,color)

