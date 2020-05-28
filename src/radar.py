from graphics import *
from draw import Draw
from plane import Plane

class Radar:
    def draw_radar(self):
        self.display = GraphWin("Radar", 500,500)
        self.display.setBackground('black')
        
        self.draw = Draw(self.display)
        
        '''
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


        self.draw.text(250, 250, "Teste", "red", 10, "bold")
        '''

        self.draw.project_plane(250,250,5, 100, 500, 250,250 )

        self.display.getMouse()
        self.display.close()



    