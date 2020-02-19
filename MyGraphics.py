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

    def line(self, initial_x, final_x, initial_y, final_y, color, thickness, type_line):

        delta_x = final_x - initial_x
        delta_y = final_y - initial_y
        y_increment = 1

        if delta_y < 0:
            y_increment = -1
            delta_y = -delta_y

        incremental_error = 2 * delta_y - delta_x
        y = initial_y

        # TODO: Estrutura de decisão baseada no crescimento positivo ou negativo de X ou Y, conforme o caso, seleciona qual
        # TODO: linha do For deve ser selecionada.
        # for x in range(x0, x1-1, -1):
        for x in range(initial_x, final_x + 1):
            self.point(x, y, color, thickness)
            print('to no for')  #Esse print auxilia enquanto o TODO acima não for realizado.
            if incremental_error > 0:
                y = y + y_increment
                incremental_error = incremental_error - 2 * delta_x

            incremental_error = incremental_error + 2 * delta_y

        #TODO: A impressão por tipo de linha não foi implementada
        #TODO: Caso delta_x < 0 && delta_y > 0 devemos alterar o ponto inicial com o ponto final, caso contrario a linha
        #TODO: fica impressa de forma errada.

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
a.line(105, 127, 103, 104, 'white', 1,'null')
a.wait()