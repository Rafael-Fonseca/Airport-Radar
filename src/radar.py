from graphics import *
from draw import Draw

class Radar:
    def draw_radar(self):
        self.display = GraphWin("Radar", 500,500)
        self.display.setBackground('black')
        
        self.draw = Draw(self.display)


        self.draw.circle(250, 250, 50, 'green')
        self.draw.circle(250, 250, 125, 'green')
        self.draw.circle(250, 250, 200, 'green')
        self.draw.circle(250, 250, 275, 'green')

        self.draw.line(250,250, 500, 0, 'green', 1, 3)
        self.draw.line(250,250, 0, 500, 'green', 1, 3)
        self.draw.line(250,250, 500, 500, 'green', 1, 3)
        self.draw.line(250,250, 0, 0, 'green', 1, 3)

        self.draw.line(250, 250, 250, 0, 'green', 1, 3)
        self.draw.line(250, 250, 250,500, 'green', 1, 3)

        for line_of_pixel in self.draw.screen.pixels:
            print(line_of_pixel)
            #for pixel in line_of_pixel:
             #   print(pixel)


        self.display.getMouse()
        self.display.close()

