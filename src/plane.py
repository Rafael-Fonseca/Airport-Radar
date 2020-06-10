'''
          PROJETO DESENVOLVIDO POR:

          FELIPE OLIVEIRA MAIA          RA: 21801679
          RAFAEL ABREU FONSECA          RA: 21700439
'''


import math
from polygon import Polygon


class Plane():
    def __init__(self, x, y, z):
        self.plane_points = []
        self.points_projection = self.get_points_projection(x, y, z)
        self.get_plane_points(self.points_projection[0], self.points_projection[1])
        #self.get_plane_points(x,y)
        self.points_to_draw = self.rotate_points()
        #print(self.points_to_draw)
        self.lines_to_draw = Polygon(self.points_to_draw)
        #for x in self.rotate_points():
            #print(type(x))

    def get_points_projection(self, x, y, z, f=3500, F=15000):
        x1 = x * f / (F - z)
        y1 = y * f / (F - z)

        return x1, y1

    def get_plane_points(self, x, y):
        self.plane_points = [(x, y), (x-3, y+2), (x-3, y+12),
                             (x-16, y+27), (x-3, y+21), (x-3, y+26),
                             (x-10, y+31), (x-4, y+31), (x, y+28),
                             (x+4, y+31), (x+10, y+31), (x+3, y+26),
                             (x+3, y+21), (x+16, y+27), (x+3, y+12),
                             (x+3, y+2)]

    def get_direction(self, x, y):
        return math.atan(y/x)

    def x_rotation(self, x, y):
        direction = self.get_direction(x, y)
        return int(x * math.cos(direction) - y * math.sin(direction))

    def y_rotation(self, x, y):
        direction = self.get_direction(x, y)
        return int(y * math.cos(direction) + x * math.sin(direction))

    def rotate_points(self):
        rotated_points = []
        for point in self.plane_points:
            rotated_points.append((self.x_rotation(point[0], point[1]), self.y_rotation(point[0], point[1])))
        return rotated_points

    def midle_point(self):
        #  Deverá retornar um ponto dentro do aviao para possibilitar o uso da função fill
        pass

