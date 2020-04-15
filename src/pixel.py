'''
          PROJETO DESENVOLVIDO POR:

          FELIPE OLIVEIRA MAIA          RA: 21801679
          RAFAEL ABREU FONSECA          RA: 21700439
'''

class Pixel:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return 'Position: {}, {}\tColor: {}'.format(self.x, self.y, self.color) 
