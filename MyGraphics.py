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

            #TODO: Refatorar, substituir os if(s) por um dicionário de funções.

    def line(self, initial_x, initial_y, final_x, final_y, color, thickness, type_line):

        delta_x = final_x - initial_x
        delta_y = final_y - initial_y

        #if delta_x < 0 and delta_y > 0:
        if delta_x < 0:
            initial_x, final_x = final_x, initial_x
            initial_y, final_y = final_y, initial_y

            delta_x = final_x - initial_x
            delta_y = final_y - initial_y

        incremental_error = 2 * delta_y - delta_x


        if abs(delta_x) >= abs(delta_y):
            y = initial_y
            y_increment = 1

            if delta_y < 0:
                y_increment = -1
                delta_y = -delta_y
            elif delta_y == 0:
                y_increment = 0

            if delta_x < 0:
                for x in range(initial_x, final_x-1, -1):
                    self.point(x, y, color, thickness)
                    print('for 1', x, y)
                    # print('to no for')
                    if incremental_error > 0:
                        y = y + y_increment
                        incremental_error = incremental_error - 2 * delta_x

                    incremental_error = incremental_error + 2 * delta_y

            if delta_x > 0:
                for x in range(initial_x, final_x + 1):
                    self.point(x, y, color, thickness)
                    print('for 2', x, y)
                    # print('to no for')
                    if incremental_error > 0:
                        y = y + y_increment
                        incremental_error = incremental_error - 2 * delta_x

                    incremental_error = incremental_error + 2 * delta_y

        else:
            x = initial_x
            x_increment = 1

            if delta_x < 0:
                x_increment = -1
                delta_x = -delta_x
            elif delta_x == 0:
                x_increment = 0

            if delta_y < 0:
                for y in range(initial_y, final_y-1, -1):
                    self.point(x, y, color, thickness)
                    print('for 3', x, y)
                    if incremental_error > 0:
                        x = x + x_increment
                        incremental_error = incremental_error - 2 * delta_x

                    incremental_error = incremental_error + 2 * delta_y

            if delta_y > 0:
                for y in range(initial_y, final_y+1):
                    self.point(x, y, color, thickness)
                    print('for 4', x, y)
                    if incremental_error > 0:
                        x = x + x_increment
                        incremental_error = incremental_error - 2 * delta_x

                    incremental_error = incremental_error + 2 * delta_y


        #TODO: A impressão por tipo de linha não foi implementada
        #TODO: Ainda se faz necessário imprimir linhas onde deltaY > deltaX o que inclui linhas verticais

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
#a.point(100, 100, 'white', 1)
#a.line(200, 200, 100, 110, 'white', 1, 'null')  # dX < 0 dY < 0
#a.line(200, 200, 300, 110, 'white', 1, 'null')  # dX > 0 dY < 0 errou por pouco
#a.line(200, 200, 100, 300, 'white', 1, 'null')  # dX < 0 dY > 0 errou por pouco
#a.line(200, 200, 250, 310, 'white', 1, 'null')  # dX > 0 dY > 0 ERROU POR MUITO!!!
a.line(200, 200, 200, 300, 'blue', 1, 'null')  # dX = 0 dY <ou> 0
a.line(200, 200, 100, 200, 'white', 1, 'null')  # dX <ou> 0 dY = 0

a.wait()