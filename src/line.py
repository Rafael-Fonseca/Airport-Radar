from pixel import Pixel

'''
          PROJETO DESENVOLVIDO POR:

          FELIPE OLIVEIRA MAIA          RA: 21801679
          RAFAEL ABREU FONSECA          RA: 21700439
'''

class Line:
    '''
        A classe Line define uma reta.

        Ela mantém os pontos inicial e final.
        E mantém todos os objetos Pixel que compõe a reta no dicionário self.pixels
    '''

    def __init__(self, x_initial, y_initial, x_final, y_final):
        '''

        :param x_initial: Posição no eixo X em que a reta se inicia.
        :param y_initial: Posição no eixo y em que a reta se inicia.
        :param x_final:   Posição no eixo X em que a reta termina.
        :param y_final:   Posição no eixo Y em que a reta termina.
        '''

        self.x_initial = x_initial
        self.y_initial = y_initial
        self.x_final = x_final
        self.y_final = y_final
        self.pixels = {}

    def __str__(self):
        '''
        :return: Essa função é instânciada quando o usuário executa a função print e serviu para que os
        desenvolvedores debugassem o código com maior facilidade.
        '''

        return 'Linha com ponto inicial em ({},{}) e final em ({},{})'.format(self.x_initial, self.y_initial,
                                                                              self.x_final, self.y_final)

    '''
        As funções abaixo são idênticas, exceto por uma linha, às funções que calculam à reta da classe Draw
        por questão de escolha elas terão seus comentários realizados na classe Draw. Este código esta repetido 
    '''
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
