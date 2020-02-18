from graphics import GraphWin
'''
win = GraphWin('Radar de aeroporto', 500, 500)
win.setBackground('black')
win.plot(50,50, 'white')

win.getMouse() # pause for click in window
win.close()
'''

class MyGraphics:

    def __init__(self):
        self.win = GraphWin('Radar de aeroporto', 500, 500)
        self.win.setBackground('black')

    def point(self, x, y, color, size):
        if size == 1:
            self.win.plot(x, y, color)

        if size == 2:
            self.win.plot(x    , y    , color)
            self.win.plot(x + 1, y    , color)
            self.win.plot(x    , y + 1, color)
            self.win.plot(x + 1, y + 1, color)

        if size == 3:
            self.win.plot(x    , y    , color)
            self.win.plot(x + 1, y    , color)
            self.win.plot(x - 1, y    , color)
            self.win.plot(x    , y + 1, color)
            self.win.plot(x    , y - 1, color)

        if size == 4:
            self.win.plot(x    , y    , color)
            self.win.plot(x + 1, y    , color)

            self.win.plot(x - 1, y + 1, color)
            self.win.plot(x    , y + 1, color)
            self.win.plot(x + 1, y + 1, color)
            self.win.plot(x + 2, y + 1, color)

            self.win.plot(x - 1, y + 2, color)
            self.win.plot(x    , y + 2, color)
            self.win.plot(x + 1, y + 2, color)
            self.win.plot(x + 2, y + 2, color)

            self.win.plot(x    , y + 4, color)
            self.win.plot(x + 1, y + 4, color)

    def line(self, x1, x2, y1, y2, color, thickness, type_line):
        if thickness == 1:
            pass

        if thickness == 2:
            pass

        if thickness == 3:
            pass

        if thickness == 4:
            pass

    def circle(self, xc, yc, radius, color):
        pass

    def airplane(self, x, y, color, ident, direction):
        pass

    def my_text(self, x, y, text):
        pass

    def fill(self, x, y, color):
        pass

    def wait(self):
        self.win.getMouse()
        self.win.close()

a = MyGraphics()
a.point(100,100,'white',4)
a.wait()