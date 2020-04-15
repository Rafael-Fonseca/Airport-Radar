from graphics import *
from pixel import Pixel
from screen import Screen

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

        #Linha continua
        if type == 1:
            for x in range(initial_x, final_x + 1):
                self.point(x, y, color, size)
                if incremental_error > 0:
                    y = y + y1
                    incremental_error = incremental_error - 2 * delta_x

                incremental_error = incremental_error + 2 * delta_x
        
        #linha pontilhada
        elif type == 2:
            counter = 0
            for x in range(initial_x, final_x + 1):
                if counter != 2:
                    self.point(x, y , color, size)

                if counter == 2:
                    counter = 0

                if incremental_error > 0:
                    y = y + yi
                    incremental_error = incremental_error - 2 * delta_x

                incremental_error = incremental_error - 2 * delta_y
                counter += 1
       
        #linha tracejada
        elif type == 3:
            counter = 6
            for y in range(initial_y, final_y + 1):
                if counter % 6 in [0, 1, 2]:
                    self.point(x, y, color, size)

                if incremental_error > 0:
                    x = x + xi
                    incremental_error = incremental_error - 2 * delta_y

                incremental_error = incremental_error + 2 * delta_x
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

        #Linha continua
        if type == 1: 
            for y in range(initial_y, final_y + 1):
                self.point(x, y, color, size)
                if incremental_error > 0:
                    x = x + xi
                    incremental_error = incremental_error - 2 * delta_y

                incremental_error = incremental_error + 2 * delta_x

        #linha pontilhada
        elif type == 2:  
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

        #linha tracejada
        elif type == 3: 
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
        if type not in[1, 2, 3]:
            return print('Type invalid')

        if abs(final_x - initial_y) < abs(final_x - initial_x):
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

    def text(self):
        pass

    def fill(self):
        pass