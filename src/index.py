from graphics import *
from draw import Draw



class Main:
    def main(self):

        self.display = GraphWin("Radar", 500,500)
        self.display.setBackground('black')
        
        self.draw = Draw(self.display)

        self.draw.pixel(10,10,"white")
        
        self.display.getMouse()
        self.display.close()





teste = Main()
teste.main()

