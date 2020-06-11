'''
          PROJETO DESENVOLVIDO POR:

          FELIPE OLIVEIRA MAIA          RA: 21801679
          RAFAEL ABREU FONSECA          RA: 21700439
'''

#Classe para pegar as cores do pixel
class Pixel:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return 'Position: {}, {}\tColor: {}'.format(self.x, self.y, self.color)

    def __ne__(self, other):
        if self.x != other.x or self.y != other.y or self.color != other.color:
            return True
        else:
            return False

    def __eq__(self, other):
        return not(self.__ne__(other))
