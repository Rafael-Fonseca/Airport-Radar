from graphics import *
from draw import Draw

class Radar:
    def draw_radar(self):
        self.display = GraphWin("Radar", 500,500)
        self.display.setBackground('black')
        
        self.draw = Draw(self.display)
        print(self.draw)

        self.draw.circle(250, 250, 62, 'green')
        self.draw.circle(250, 250, 124, 'green')
        self.draw.circle(250, 250, 186, 'green')
        self.draw.circle(250, 250, 248, 'green')

        self.draw.line(0, 0, 500, 500, 'green', 1, 3)
        self.draw.line(0, 500, 500, 0, 'green', 1, 3)
        self.draw.line(0, 250, 500, 250, 'green', 1, 3)
        self.draw.line(250, 0, 250, 500, 'green', 1, 3)

        '''
        for line_of_pixel in self.draw.screen.pixels:
            for pixel in line_of_pixel:
               print(pixel)
        '''

        self.display.getMouse()
        self.display.close()



    