import math
from line import Line
from draw import Draw

'''
          PROJETO DESENVOLVIDO POR:

          FELIPE OLIVEIRA MAIA          RA: 21801679
          RAFAEL ABREU FONSECA          RA: 21700439
'''
#Classe usada para desenhar o avião
class Plane():
    #Separando os valores da classe
    def __init__(self, x, y, z):

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
        if x == 0:
            self.lines_to_draw = [Line(255, 250, 245, 250),
                                  Line(253, 246, 253, 254),
                                  Line(247, 248, 247, 252)]
    #Colocando o avião virado para direita
    def right(self, x, y, draw):
        return self.can_draw_text(x+20, y, draw), (x+20, y)
    #Colocando o avião virado para cima
    def up(self, x, y, draw):
        return self.can_draw_text(x, y-20, draw), (x, y-20)
    #Colocando o avião virado para esquerda
    def left(self, x, y, draw):
        return self.can_draw_text(x-30, y, draw), (x-30, y)
    #Colocando o avião virado para baixo
    def down(self, x, y, draw):
        return self.can_draw_text(x, y+20, draw), (x, y+20)

    #função mudar as cores do avião e colocando eles no radar
    def draw_plane(self, draw, data_list):
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

    #Função para escrever os detalhes do voo
    def can_draw_text(self, x, y, draw):
        try:
            if draw.screen.pixels[x][y].color == 'text':
                return False
            return True
        except IndexError:
            return False

    #função para projetar o avião no plano
    def get_points_projection(self, x, y, z, f=3500, F=15000):
        x1 = x * f / (F - z)
        y1 = y * f / (F - z)

        return x1, y1
    #Colocando os valores do avião
    def get_plane_points(self, x, y):
        self.plane_points = [(x, y), (x-10, y), (x-8, y-2), (x-8, y+2), (x-3, y-4), (x-3, y+4)]
    #Colocando a direção do avião
    def get_direction(self, x, y):
        return math.atan(y / x)
    #Rotacinando do eixo X
    def x_rotation(self, x, y):
        direction = self.get_direction(x, y)
        return int(x * math.cos(direction) - y * math.sin(direction))
    #Rotacinando do eixo y
    def y_rotation(self, x, y):
        direction = self.get_direction(x, y)
        return int(y * math.cos(direction) + x * math.sin(direction))
    #Virando os pontos do avião
    def rotate_points(self):
        rotated_points = []
        for point in self.plane_points:
            rotated_points.append((int(point[0] + self.x_rotation(point[0], point[1])),
                                   int(point[1] + self.y_rotation(point[0], point[1]))))
        return rotated_points