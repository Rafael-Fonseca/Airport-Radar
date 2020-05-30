from pixel import Pixel

'''
          PROJETO DESENVOLVIDO POR:

          FELIPE OLIVEIRA MAIA          RA: 21801679
          RAFAEL ABREU FONSECA          RA: 21700439
'''

class Screen(list):
    def __init__(self, screen):
        super().__init__()
        self.pixels = self.create_screen(int(screen.cget('width')), int(screen.cget('height')), screen.cget('bg'))

    def create_screen(self, width, height,color):
        screen = []

        for x in range(0, width + 1):
            line = []

            for y in range(0, height + 1):
                line.append(Pixel(x, y, color))

            screen.append(line)

        return screen
