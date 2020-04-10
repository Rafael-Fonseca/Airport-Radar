from graphics import GraphWin, Text, Point

class MyGraphics:

    def __init__(self):
        self.win = GraphWin('Radar de aeroporto', 500, 500)
        self.win.setBackground('black')
        self.label = Text(Point(100, 100), '')
        self.label.setTextColor('white')

    # A função que deve ser usada para desenhar pontos é a função point
    def pixel_point(self, x, y, color):
        self.win.plot(x, y, color)

    # A função que deve ser usada para desenhar pontos é a função point
    def square_point(self, x, y, color):
        self.win.plot(x, y, color)
        self.win.plot(x + 1, y, color)
        self.win.plot(x, y + 1, color)
        self.win.plot(x + 1, y + 1, color)

    # A função que deve ser usada para desenhar pontos é a função point
    def cross_point(self, x, y, color):
        self.win.plot(x, y, color)
        self.win.plot(x + 1, y, color)
        self.win.plot(x - 1, y, color)
        self.win.plot(x, y + 1, color)
        self.win.plot(x, y - 1, color)

    # A função que deve ser usada para desenhar pontos é a função point
    def maximum_point(self, x, y, color):
        self.win.plot(x, y, color)
        self.win.plot(x + 1, y, color)

        self.win.plot(x - 1, y + 1, color)
        self.win.plot(x, y + 1, color)
        self.win.plot(x + 1, y + 1, color)
        self.win.plot(x + 2, y + 1, color)

        self.win.plot(x - 1, y + 2, color)
        self.win.plot(x, y + 2, color)
        self.win.plot(x + 1, y + 2, color)
        self.win.plot(x + 2, y + 2, color)

        self.win.plot(x, y + 4, color)
        self.win.plot(x + 1, y + 4, color)

    def point(self, x, y, color, size):
        point_dict = {1: self.pixel_point,
                      2: self.square_point,
                      3: self.cross_point,
                      4: self.maximum_point}
        try:
            point_dict[size](x, y, color)
        except KeyError:
            # Em casos que o usuário escolher um tamanho não disponível, o tamanho é alterado para o maximo,
            # na intenção de que o usuário perceba que algo está errado.
            point_dict[4](x, y, color)

    # A função que deve ser usada para desenhar retas é a função line
    def line_low(self, initial_x, initial_y, final_x, final_y, color, size, type):
        delta_x = final_x - initial_x
        delta_y = final_y - initial_y
        yi = 1

        if delta_y < 0:
            yi = -1
            delta_y = -delta_y

        incremental_error = 2 * delta_y - delta_x
        y = initial_y

        if type == 1:  # Type is normal
            for x in range(initial_x, final_x + 1):
                self.point(x, y, color, size)
                if incremental_error > 0:
                    y = y + yi
                    incremental_error = incremental_error - 2 * delta_x

                incremental_error = incremental_error + 2 * delta_y

        elif type == 2:  # Type is pontilhada
            counter = 0
            for x in range(initial_x, final_x + 1):
                if counter != 2:
                    self.point(x, y, color, size)
                if counter == 2:
                    counter = 0

                if incremental_error > 0:
                    y = y + yi
                    incremental_error = incremental_error - 2 * delta_x

                incremental_error = incremental_error + 2 * delta_y
                counter += 1

        elif type == 3:  # Type is tracejada
            counter = 6
            for x in range(initial_x, final_x + 1):
                if counter % 6 in [0, 1, 2]:
                    self.point(x, y, color, size)

                if incremental_error > 0:
                    y = y + yi
                    incremental_error = incremental_error - 2 * delta_x

                incremental_error = incremental_error + 2 * delta_y
                counter += 1

    # A função que deve ser usada para desenhar retas é a função line
    def line_high(self, initial_x, initial_y, final_x, final_y, color, size, type):
        delta_x = final_x - initial_x
        delta_y = final_y - initial_y
        xi = 1

        if delta_x < 0:
            xi = -1
            delta_x = -delta_x

        incremental_error = 2 * delta_x - delta_y
        x = initial_x

        if type == 1:  # Type is normal
            for y in range(initial_y, final_y + 1):
                self.point(x, y, color, size)
                if incremental_error > 0:
                    x = x + xi
                    incremental_error = incremental_error - 2 * delta_y

                incremental_error = incremental_error + 2 * delta_x

        elif type == 2:  # Type is pontilhada
            counter = 0
            for y in range(initial_y, final_y + 1):
                if counter != 2:
                    self.point(x, y, color, size)
                elif counter == 2:
                    counter = 0

                if incremental_error > 0:
                    x = x + xi
                    incremental_error = incremental_error - 2 * delta_y

                incremental_error = incremental_error + 2 * delta_x
                counter += 1

        elif type == 3:    # Type is tracejada
            counter = 6
            for y in range(initial_y, final_y + 1):
                if counter % 6 in [0, 1, 2]:
                    self.point(x, y, color, size)

                if incremental_error > 0:
                    x = x + xi
                    incremental_error = incremental_error - 2 * delta_y

                incremental_error = incremental_error + 2 * delta_x
                counter += 1

    def line(self, initial_x, initial_y, final_x, final_y, color, size, type):
        if type not in [1, 2, 3]:
            print('Tipo de linha inválido')
            return 'Type line invalid'

        if abs(final_y - initial_y) < abs(final_x - initial_x):
            if initial_x > final_x:
                self.line_low(final_x, final_y, initial_x, initial_y, color, size, type)
            else:
                self.line_low(initial_x, initial_y, final_x, final_y, color, size, type)

        else:
            if initial_y > final_y:
                self.line_high(final_x, final_y, initial_x, initial_y, color, size, type)
            else:
                self.line_high(initial_x, initial_y, final_x, final_y, color, size, type)

    def circle_points(self, center_x, center_y, x, y, color):
        self.point(center_x + x, center_y + y, color, 1)
        self.point(center_x - x, center_y + y, color, 1)
        self.point(center_x + x, center_y - y, color, 1)
        self.point(center_x - x, center_y - y, color, 1)
        self.point(center_x + y, center_y + x, color, 1)
        self.point(center_x - y, center_y + x, color, 1)
        self.point(center_x + y, center_y - x, color, 1)
        self.point(center_x - y, center_y - x, color, 1)

    def circle(self, center_x, center_y, radius, color):
        x = 0
        y = radius
        d = 3 - 2 * radius
        self.circle_points(center_x, center_y, x, y, color)

        while y >= x:
            x += 1

            if d > 0:
                y -= 1
                d = d + 4 * (x - y) + 10

            else:
                d = d + 4 * x + 6

            self.circle_points(center_x, center_y, x, y, color)

    def airplane(self, x, y, color, ident, direction):
        pass

    def my_text(self, x, y, text, collor):
        self.label = Text(Point(x, y), text)
        self.label.setTextColor(collor)
        self.label.draw(self.win)

    def fill(self, x, y, color):
        pass

    def wait(self):
        self.win.getMouse()
        self.win.close()


a = MyGraphics()
#a.point(100, 100, 'white', 20)  #                              ok
#a.line(200, 200, 100, 100, 'white', 1, 3)  # dX < 0 dY < 0        ok
#a.line(200, 200, 300, 100, 'green', 1)  # dX > 0 dY < 0        ok
#a.line(200, 200, 100, 300, 'red', 1)  # dX < 0 dY > 0          ok
#a.line(200, 200, 300, 300, 'orange', 1)  # dX > 0 dY > 0       ok
#a.line(200, 100, 200, 300, 'blue', 1)  # dX = 0 dY <ou> 0      ok
#a.line(100, 200, 300, 200, 'yellow', 1)  # dX <ou> 0 dY = 0    ok
#a.my_text(100, 100, 'Texto Teste', 'red')  #  ok

a.wait()
