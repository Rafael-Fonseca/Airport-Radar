from graphics import *
from draw import Draw
from plane import Plane
import copy

'''
          PROJETO DESENVOLVIDO POR:

          FELIPE OLIVEIRA MAIA          RA: 21801679
          RAFAEL ABREU FONSECA          RA: 21700439
'''

class Radar:

    def __init__(self):
        self.base = []

    def draw_radar(self):
        self.display = GraphWin("Radar", 500,500)
        self.display.setBackground('black')
        
        self.draw = Draw(self.display)
        

        self.draw.circle(250, 250, 62, 'green')
        self.draw.circle(250, 250, 124, 'green')
        self.draw.circle(250, 250, 186, 'green')
        self.draw.circle(250, 250, 248, 'green')

        # Linha do segundo ao quarto quadrante
        self.draw.line(0, 0, 500, 500, 'green', 1, 3)

        # Linha do terceiro ao primeiro quadrante
        self.draw.line(0, 500, 250, 250, 'green', 1, 3)
        self.draw.line(250, 250, 500, 0, 'green', 1, 3)

        # Linha horizontal
        self.draw.line(1, 250, 249, 249, 'green', 1, 3)
        self.draw.line(250, 250, 500, 250, 'green', 1, 3)

        # Linha vertical
        self.draw.line(250, 0, 250, 500, 'green', 1, 3)

        self.base = copy.deepcopy(self.draw.screen.pixels)


    def reset(self):

        for column_pixel in self.base:
            for pixel in column_pixel:
                if pixel != self.draw.screen.pixels[pixel.x][pixel.y]:
                    self.draw.point(pixel.x, pixel.y, pixel.color, 1)


#radar = Radar()
#radar.draw_radar()
