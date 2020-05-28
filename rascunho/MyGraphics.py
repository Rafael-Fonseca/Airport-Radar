from graphics import GraphWin, Text, Point
import stack2

class Pixel:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return 'Position: {}, {}\tColor: {}'.format(self.x, self.y, self.color)


class Screen:

    def __init__(self, screen):
        self.pixels = self.create_screen(int(screen.cget('width')), int(screen.cget('height')), screen.cget('bg'))

    def create_screen(self, width, height, color):
        screen = []
        for x in range(0, width + 1):
            line = []
            for y in range(0, height + 1):
                line.append(Pixel(x, y, color))
            screen.append(line)

        return screen

class MyGraphics:

    def __init__(self):
        self.win = GraphWin('Radar de aeroporto', 500, 500)
        self.win.setBackground('black')

        self.screen = Screen(self.win)

        self.label = Text(Point(100, 100), '')
        self.label.setTextColor('white')

    # A função que deve ser usada para desenhar pontos é a função point
    def pixel_point(self, x, y, color):
        self.win.plot(x, y, color)
        self.screen.pixels[x][y].color = color # Essa linha aqui

    # A função que deve ser usada para desenhar pontos é a função point
    def square_point(self, x, y, color):
        self.win.plot(x, y, color)
        self.win.plot(x + 1, y, color)
        self.win.plot(x, y + 1, color)
        self.win.plot(x + 1, y + 1, color)

        self.screen.pixels[x][y].color = color
        self.screen.pixels[x+1][y].color = color
        self.screen.pixels[x][y+1].color = color
        self.screen.pixels[x+1][y+1].color = color

    # A função que deve ser usada para desenhar pontos é a função point
    def cross_point(self, x, y, color):
        self.win.plot(x, y, color)
        self.win.plot(x + 1, y, color)
        self.win.plot(x - 1, y, color)
        self.win.plot(x, y + 1, color)
        self.win.plot(x, y - 1, color)

        self.screen.pixels[x][y].color = color
        self.screen.pixels[x+1][y].color = color
        self.screen.pixels[x-1][y].color = color
        self.screen.pixels[x][y+1].color = color
        self.screen.pixels[x][y-1].color = color

    # A função que deve ser usada para desenhar pontos é a função point
    def maximum_point(self, x, y, color):
        self.win.plot(x, y, color)
        self.win.plot(x + 1, y, color)

        self.screen.pixels[x][y].color = color
        self.screen.pixels[x+1][y].color = color

        self.win.plot(x - 1, y + 1, color)
        self.win.plot(x, y + 1, color)
        self.win.plot(x + 1, y + 1, color)
        self.win.plot(x + 2, y + 1, color)

        self.screen.pixels[x-1][y+1].color = color
        self.screen.pixels[x][y+1].color = color
        self.screen.pixels[x+1][y+1].color = color
        self.screen.pixels[x+2][y+1].color = color

        self.win.plot(x - 1, y + 2, color)
        self.win.plot(x, y + 2, color)
        self.win.plot(x + 1, y + 2, color)
        self.win.plot(x + 2, y + 2, color)

        self.screen.pixels[x-1][y+2].color = color
        self.screen.pixels[x][y+2].color = color
        self.screen.pixels[x+1][y+2].color = color
        self.screen.pixels[x+2][y+2].color = color

        self.win.plot(x, y + 3, color)
        self.win.plot(x + 1, y + 3, color)

        self.screen.pixels[x][y+3].color = color
        self.screen.pixels[x+1][y+3].color = color

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

    def my_text(self, x, y, text, color):
        self.label = Text(Point(x, y), text)
        self.label.setTextColor(color)
        self.label.draw(self.win)

    def __fill_recursivo(self, x, y, color, bg_color='black'):
        '''
        NÃO USAR!!!! ESTA CRASHANDO POR MAXIMO DE RECURSAO!!!!!

        :param x: Posição no eixo X de um ponto dentro da área a ser preenchida
        :param y: Posição no eixo Y de um ponto dentro da área a ser preenchida
        :param color: A cor com a qual você deseja preencher
        :param bg_color: A cor do background
        :return: Preenche a área com a cor selecionada, em caso de colocar um ponto fora da área, index error.
        '''
        if self.screen.pixels[x][y].color == bg_color:
            self.point(x, y, color, 1)
            self.fill(x + 1, y, color)
            self.fill(x - 1, y, color)
            self.fill(x, y + 1, color)
            self.fill(x, y - 1, color)

    def fill(self, x, y, color, bg_color='black'):
        area = stack2.Stack()
        area.push(self.screen.pixels[x][y])

        while not area.isEmpty():
            pixel = area.pop()
            # print('\nEntrei no while:', pixel.x, pixel.y, '\t', pixel.color)

            if pixel.color == bg_color:
                self.point(pixel.x, pixel.y, color, 1)
                # print('\tentrei no IF:\n\t\tTroquei a cor deste pixel para:', pixel.color, '\n')

            # if self.screen.pixels[pixel.x + 1][pixel.y].color != color:
                area.push(self.screen.pixels[pixel.x + 1][pixel.y])
                # print('\t\tDei push no pixel', area.peek().x, area.peek().y, area.peek().color)

            # if self.screen.pixels[pixel.x - 1][pixel.y].color != color:
                area.push(self.screen.pixels[pixel.x - 1][pixel.y])
                # print('\t\tDei push no pixel', area.peek().x, area.peek().y, area.peek().color)

            # if self.screen.pixels[pixel.x][pixel.y + 1].color != color:
                area.push(self.screen.pixels[pixel.x][pixel.y + 1])
                # print('\t\tDei push no pixel', area.peek().x, area.peek().y, area.peek().color)

            # if self.screen.pixels[pixel.x][pixel.y - 1].color != color:
                area.push(self.screen.pixels[pixel.x][pixel.y - 1])
                # print('\t\tDei push no pixel', area.peek().x, area.peek().y, area.peek().color)

            # else:
                # print('\t\tDesta vez entrei no ELSE: ',pixel.x, pixel.y, pixel.color)

    def wait(self):
        self.win.getMouse()
        self.win.close()


a = MyGraphics()
#a.point(100, 100, 'white', 20)  #                              ok
a.line(200, 200, 100, 200, 'white', 1, 1)  # dX < 0 dY < 0        ok
a.line(200, 200, 200, 100, 'white', 1, 1)
a.line(100, 200, 100, 100, 'white', 1, 1)
a.line(200, 100, 100, 100, 'white', 1, 1)

a.fill(199, 150, 'white')

a.line(0, 250, 500, 250, 'green', 1, 1)  # dX > 0 dY < 0        ok
#a.line(200, 200, 100, 300, 'red', 1)  # dX < 0 dY > 0          ok
#a.line(200, 200, 300, 300, 'orange', 1)  # dX > 0 dY > 0       ok
#a.line(200, 100, 200, 300, 'blue', 1)  # dX = 0 dY <ou> 0      ok
#a.line(100, 200, 300, 200, 'yellow', 1)  # dX <ou> 0 dY = 0    ok
#a.my_text(100, 100, 'Texto Teste', 'red')  #  ok

#print(type(a.win.config))
#print(a.win.keys())
#print(a.win.cget('height'))
'''
for line_of_pixels in a.screen.pixels:
    for pixel in line_of_pixels:
        print(pixel)
'''
'''
for x in range (100, 206):
    print(a.screen.pixels[x][200])
'''

a.wait()
