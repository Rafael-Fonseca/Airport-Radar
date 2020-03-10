from graphics import *
from draw import Draw

class Main:
    def main(self):

        self.display = GraphWin("Radar", 500,500)
        self.display.setBackground('black')
        
        self.draw = Draw(self.display)

        self.draw.pixel(10, 10, "green", 1)
        self.draw.line(200, 200, 100, 200, 'green', 1, 'null')
        self.draw.line(200, 200, 200, 100, 'green', 1, 'null')
        self.draw.line(100, 100, 100, 200, 'green', 1, 'null')
        self.draw.line(100, 100, 200, 100, 'green', 1, 'null')

        self.draw.circle(30, 30, 10, "green")
        
        self.display.getMouse()
        self.display.close()


teste = Main()
teste.main()

