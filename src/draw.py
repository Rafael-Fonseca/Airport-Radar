from screen import Screen
from stack import Stack
from graphics import *


'''
          PROJETO DESENVOLVIDO POR:
          
          FELIPE OLIVEIRA MAIA          RA: 21801679
          RAFAEL ABREU FONSECA          RA: 21700439
'''

class Draw:
    def __init__(self, display):
        #Janela para abrir o Graphics,
        self.display = display
        self.screen = Screen(self.display)

    # A função que deve ser usada para desenhar pontos é a função point    
    def pixel_point(self,x, y, color):
        self.display.plot(x, y, color)
        self.screen.pixels[x][y].color = color

    # A função que deve ser usada para desenhar pontos é a função point
    def square_point(self,x, y, color):
        self.display.plot(x, y, color)
        self.display.plot(x + 1, y, color)
        self.display.plot(x, y + 1, color)
        self.display.plot(x + 1, y + 1, color)

    # A função que deve ser usada para desenhar pontos é a função point
    def cross_point(self, x, y, color):
        self.display.plot(x, y , color)
        self.display.plot(x + 1, y, color)
        self.display.plot(x - 1, y, color)
        self.display.plot(x, y + 1, color)
        self.display.plot(x, y - 1, color)

    # A função que deve ser usada para desenhar pontos é a função point
    def maximum_point(self, x, y , color):
        self.display.plot(x, y, color)
        self.display.plot(x + 1, y, color)

        self.display.plot(x - 1, y + 1, color)
        self.display.plot(x, y + 1, color)
        self.display.plot(x + 1, y + 1, color)
        self.display.plot(x + 2, y + 1, color)

        self.display.plot(x - 1, y + 2, color)
        self.display.plot(x, y + 2, color)
        self.display.plot(x + 1, y + 2, color)
        self.display.plot(x + 2, y + 2, color)

        self.display.plot(x, y + 4, color)
        self.display.plot( x + 1, y + 4, color)

    #Função que gera o pontos
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

        elif type == 3:  # Type is tracejada
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
    
    def circle_points(self, xc, yc, x, y, color):
        self.point(xc + x, yc + y, color, 1)
        self.point(xc - x, yc + y, color, 1)
        self.point(xc + x, yc - y, color, 1)
        self.point(xc - x, yc - y, color, 1)
        self.point(xc + y, yc + x, color, 1)
        self.point(xc - y, yc + x, color, 1)
        self.point(xc + y, yc - x, color, 1)
        self.point(xc - y, yc - x, color, 1)
    
    
    def circle(self, xc, yc, r, color):
        x = 0
        y = r
        d = 3 - 2 * r
        self.circle_points(xc, yc, x, y, color)

        while (y >= x):
            x += 1
            
            if (d > 0):
                y -= 1
                d = d + 4 * (x - y) + 10

            else:
                d = d + 4 * x + 6

            self.circle_points(xc, yc, x, y, color)

    def text(self, x, y, word, cor, size, style):
        t = Text(Point(x,y), word)
        t.setOutline(cor)
        t.setSize(size)
        t.setStyle(style)
        t.draw(self.display)


    def fill(self, x, y, color, bg_color='black'):
        area = stack.Stack()
        area.push(self.screen.pixels[x][y])

        while not area.isEmpty():
            pixel = area.pop()

            if pixel.color == bg_color:
                self.point(pixel.x, pixel.y, color, 1)

                area.push(self.screen.pixels[pixel.x + 1][pixel.y])

                area.push(self.screen.pixels[pixel.x - 1][pixel.y])

                area.push(self.screen.pixels[pixel.x][pixel.y + 1])

                area.push(self.screen.pixels[pixel.x][pixel.y - 1])

    def project_plane(self, x, y, z,f, F, x1, y1):
        x1 = int(x * f/(F-z))
        y1 = int(y * f/(F-z))

        self.point(x1,y1, "green",1)
 
