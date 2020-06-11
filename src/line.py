'''
          PROJETO DESENVOLVIDO POR:

          FELIPE OLIVEIRA MAIA          RA: 21801679
          RAFAEL ABREU FONSECA          RA: 21700439
'''

from pixel import Pixel

#A classe tem a mesma funcionalidade da função Line dentro da classe Draw.
#Line usada para fazer o avião, essa classe tem apenas essa funcionalidade, devido a projeção 3D e rotação do avião
class Line:
    def __init__(self, x_initial, y_initial, x_final, y_final):
        self.x_initial = x_initial
        self.y_initial = y_initial
        self.x_final = x_final
        self.y_final = y_final
        self.pixels = {}

    def __str__(self):
        return 'Linha com ponto inicial em ({},{}) e final em ({},{})'.format(self.x_initial, self.y_initial,
                                                                              self.x_final, self.y_final)

    def line_low(self, initial_x, initial_y, final_x, final_y, color):
        delta_x = final_x - initial_x
        delta_y = final_y - initial_y
        yi = 1

        if delta_y < 0:
            yi = -1
            delta_y = -delta_y

        incremental_error = 2 * delta_y - delta_x
        y = initial_y

        for x in range(initial_x, final_x + 1):
            self.pixels.update({(x, y): Pixel(x, y, color)})
            if incremental_error > 0:
                y = y + yi
                incremental_error = incremental_error - 2 * delta_x

            incremental_error = incremental_error + 2 * delta_y

    def line_high(self, initial_x, initial_y, final_x, final_y, color):
        delta_x = final_x - initial_x
        delta_y = final_y - initial_y
        xi = 1

        if delta_x < 0:
            xi = -1
            delta_x = -delta_x

        incremental_error = 2 * delta_x - delta_y
        x = initial_x

        for y in range(initial_y, final_y + 1):
            self.pixels.update({(x, y): Pixel(x, y, color)})
            if incremental_error > 0:
                x = x + xi
                incremental_error = incremental_error - 2 * delta_y

            incremental_error = incremental_error + 2 * delta_x

    def trace_line(self, initial_x, initial_y, final_x, final_y, color):

        if abs(final_y - initial_y) < abs(final_x - initial_x):
            if initial_x > final_x:
                self.line_low(final_x, final_y, initial_x, initial_y, color)
            else:
                self.line_low(initial_x, initial_y, final_x, final_y, color)

        else:
            if initial_y > final_y:
                self.line_high(final_x, final_y, initial_x, initial_y, color)
            else:
                self.line_high(initial_x, initial_y, final_x, final_y, color)
