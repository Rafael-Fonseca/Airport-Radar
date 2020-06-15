import math
from line import Line

'''
          PROJETO DESENVOLVIDO POR:

          FELIPE OLIVEIRA MAIA          RA: 21801679
          RAFAEL ABREU FONSECA          RA: 21700439
'''

class Plane:
    '''
        A classe Plane define o que é um objeto do tipo plane.

        Esse tipo de objeto terá todas as informações necessárias
    bem como os métodos necessários para que o mesmo possa ser desenhado na tela.
    '''
    def __init__(self, x, y, z):
        '''

        :param x: Posição no eixo X.
        :param y: Posição no eixo Y.
        :param z: Posição no eixo Z.

            Se as três variaveis acima são iguais a 0 o construtor cria um avião no aeroporto.

            Caso contrário o construtor chamas os métodos da classe para no fim obter a variável
            self.lines_to_draw igual a uma lista que contém 3 objetos do tipo Line.

            Para desenhar o avião na tela, basta desenhar estes 3 objetos Line.
        '''

        if x != 0:
            self.plane_points = []
            self.points_projection = self.get_points_projection(x, y, z)
            self.get_plane_points(self.points_projection[0], self.points_projection[1])
            self.points_to_draw = self.rotate_points()
            self.lines_to_draw = [Line(self.points_to_draw[0][0], self.points_to_draw[0][1],
                                       self.points_to_draw[1][0], self.points_to_draw[1][1]),

                                  Line(self.points_to_draw[2][0], self.points_to_draw[2][1],
                                       self.points_to_draw[3][0], self.points_to_draw[3][1]),

                                  Line(self.points_to_draw[4][0], self.points_to_draw[4][1],
                                       self.points_to_draw[5][0], self.points_to_draw[5][1]),
                                  ]
        if x == 0 and y == 0 and z == 0:
            self.lines_to_draw = [Line(255, 250, 245, 250),
                                  Line(253, 246, 253, 254),
                                  Line(247, 248, 247, 252)]

    def right(self, x, y, draw):
        '''

        :param x: Posição no eixo X.
        :param y: Posição no eixo Y.
        :param draw: Objeto do tipo Draw.

        :return:    True  se a posição (x +20, y) não contém Texto
                    False se a posição (x +20, y) contém Texto
        '''

        return self.can_draw_text(x+20, y, draw), (x+20, y)

    def up(self, x, y, draw):
        '''

        :param x: Posição no eixo X.
        :param y: Posição no eixo Y.
        :param draw: Objeto do tipo Draw.

        :return:    True  se a posição (x , y - 20) não contém Texto
                    False se a posição (x , y - 20) contém Texto
        '''

        return self.can_draw_text(x, y-20, draw), (x, y-20)

    def left(self, x, y, draw):
        '''

        :param x: Posição no eixo X.
        :param y: Posição no eixo Y.
        :param draw: Objeto do tipo Draw.

        :return:    True  se a posição (x - 30, y) não contém Texto
                    False se a posição (x - 30, y) contém Texto
        '''

        return self.can_draw_text(x-30, y, draw), (x-30, y)

    def down(self, x, y, draw):
        '''

        :param x: Posição no eixo X.
        :param y: Posição no eixo Y.
        :param draw: Objeto do tipo Draw.

        :return:    True  se a posição (x, y + 20) não contém Texto
                    False se a posição (x, y + 20) contém Texto
        '''

        return self.can_draw_text(x, y+20, draw), (x, y+20)

    def draw_plane(self, draw, data_list):
        '''
            A função draw_plane checa o estado do avião, e usa esta informação para decidir a cor do mesmo.

            Além disto realiza um 'for each' na variável self.lines_to_draw e a cada iteração
            utiliza o objeto do tipo draw para desenhar a respectiva linha.

            Antes de desenhar o nome do voo do avião, esta função utiliza um dicionário de funções para
            a cada iteração de um novo 'for each' checar se algum outro texto está escrito naquele local
            se o local estiver ocupado escreve na direção seguinte. Caso esteja disponível escreve e
            cancela as demais iterações com um return.

        :param draw: Objeto do tipo draw
        :param data_list: Lista com os dados do avião a ser desenhado.

        :return: Desenha avião e texto com o nome do voo do avião na tela.
        '''

        color = 'white'
        if data_list[1] == 'P':
            color = 'yellow'
        if data_list[1] == 'D':
            color = 'red'

        for line in self.lines_to_draw:
            draw.line(line.x_initial, line.y_initial, line.x_final, line.y_final, color, 1, 1)

        direction_dict = {
            'right' : self.right,
            'up'    : self.up,
            'left'  : self.left,
            'down'  : self.down
        }

        for direction in ['right', 'up', 'left', 'down']:
            can_text_in_coordinates = direction_dict[direction](self.lines_to_draw[0].x_initial,
                                                                self.lines_to_draw[0].y_initial, draw)
            if can_text_in_coordinates[0]:
                return draw.text(can_text_in_coordinates[1][0],
                                 can_text_in_coordinates[1][1], data_list[2], color, 6, 'bold')

    def can_draw_text(self, x, y, draw):
        '''

            Esta função compara:
            O atributo color do objeto Pixel
            O objeto Pixel esta armazenado na matriz pixels no indice: [x][y]
            A matriz pixels é um atributo do objeto do tipo screen.
            O objeto do tipo screen é um atributo do objeto draw.

            com a string 'text'

        :param x: Posição no eixo X.
        :param y: Posição no eixo Y.
        :param draw: Objeto do tipo Draw.

        :return:    True  se a posição (x, y) não contém Texto
                    False se a posição (x, y) contém Texto
        '''

        try:
            if draw.screen.pixels[x][y].color == 'text':
                return False
            return True
        except IndexError:
            return False

    def get_points_projection(self, x, y, z, f=1000, F=15000):
        '''

        :param x: Posição do avião no eixo X.
        :param y: Posição do avião no eixo Y.
        :param z: Posição do avião no eixo Z.
        :param f: Distância entre o plano projetivo e o observador
        :param F: Altura do observador

        :return: Novos valores para o ponto (x, y) que são a representação de um ponto 3D em um plano 2D
        '''

        x1 = x * f / (F - z)
        y1 = y * f / (F - z)

        return x1, y1

    def get_plane_points(self, x, y):
        '''

        :param x: Posição no eixo X do nariz do avião.
        :param y: Posição no eixo Y do nariz do avião.

        :return:  Lista com os pontos iniciais e finais de cada uma das três retas, respectivamente,
                necessárias para a representação 2D dos aviões.
        '''

        self.plane_points = [(x, y), (x-10, y), (x-8, y-2), (x-8, y+2), (x-3, y-4), (x-3, y+4)]

    def get_direction(self, x, y):
        '''

        :param x: Posição no eixo X do nariz do avião.
        :param y: Posição no eixo Y do nariz do avião.

        :return: Radiano que representa a inclinação da reta.
        '''

        return math.atan(y / x)

    def x_rotation(self, x, y):
        '''

        :param x: Posição no eixo X do nariz do avião.
        :param y: Posição no eixo Y do nariz do avião.

        :return: Posição no eixo X rotacionada.
        '''

        direction = self.get_direction(x, y)
        return int(x * math.cos(direction) - y * math.sin(direction))

    def y_rotation(self, x, y):
        '''

        :param x: Posição no eixo X do nariz do avião.
        :param y: Posição no eixo Y do nariz do avião.

        :return: Posição no eixo Y rotacionada.
        '''

        direction = self.get_direction(x, y)
        return int(y * math.cos(direction) + x * math.sin(direction))

    def rotate_points(self):
        '''
            Esta função rotaciona cada um dos pontos necessários para o desenho do avião

        :return: Lista com todos os pontos rotacionados nos eixos X e Y.
        '''

        rotated_points = []
        for point in self.plane_points:
            rotated_points.append((int(point[0] + self.x_rotation(point[0], point[1])),
                                   int(point[1] + self.y_rotation(point[0], point[1]))))
        return rotated_points