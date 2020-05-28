from graphics import *
from tkinter import *
import math

class Engine:
    def __init__(self, points, triangles, height=400, width=600, distance=5, scale=100):
        self.window = Tk()
        self.window.title('3D Graphics')

        self.image = tk.Canvas(self.window, width=width, height=height)
        self.image.pack()
        self.height = height
        self.width = width
        self.points = points
        self.triangles = triangles
        self.shapes = []
        self.distance = distance
        self.scale = scale
    
    def flattenPoint(self, point):
        (x, y, z) = (point[0], point[1], point[2])
        projectedY = int(self.height / 2 + ((y * self.distance) / (z + self.distance)) * self.scale)
        projectedX = int(self.width / 2 + ((x * self.distance) / (z + self.distance)) * self.scale)
        return (projectedX, projectedY)

    def createTriangle(self, points):
        a, b, c = points[0], points[1], points[2]
        coords = [a[0], a[1], b[0], b[1], c[0], c[1]]
        self.shapes.append(self.image.create_polygon(coords, fill="", outline="black"))

    def render(self):
        coords = []
        
        for point in self.points:
            coords.append(self.flattenPoint(point))
            
        for triangle in self.triangles:
            self.createTriangle((coords[triangle[0]],coords[triangle[1]], coords[triangle[2]]))



points = [(-1,-1,-1),(-1,-1,1),(-1,1,1),(-1,1,-1),(1,-1,-1),(1,-1,1),(1,1,1),(1,1,-1)]
triangles = [(0,1,2),(0,2,3), (2,3,7),(2,7,6), (1,2,5),(2,5,6), (0,1,4),(1,4,5), (4,5,6),(4,6,7), (3,7,4),(4,3,0)]
test = Engine(points, triangles)
test.render()
test.window.mainloop()