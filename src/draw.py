from graphics import *

class Draw:
    def __init__(self, display):
        #Janela para abrir o Graphics,
        self.display = display
        
    def pixel(self, x, y, color, size):
        if size == 1:
            self.display.plotPixel(x, y, color)

        elif size == 2:
            self.display.plotPixel(x    , y    , color)
            self.display.plotPixel(x + 1, y    , color)
            self.display.plotPixel(x    , y + 1, color)
            self.display.plotPixel(x + 1, y + 1, color)

        elif size == 3:
            self.display.plotPixel(x    , y    , color)
            self.display.plotPixel(x + 1, y    , color)
            self.display.plotPixel(x - 1, y    , color)
            self.display.plotPixel(x    , y + 1, color)
            self.display.plotPixel(x    , y - 1, color)

        elif size == 4:
            self.display.plotPixel(x    , y    , color)
            self.display.plotPixel(x + 1, y    , color)

            self.display.plotPixel(x - 1, y + 1, color)
            self.display.plotPixel(x    , y + 1, color)
            self.display.plotPixel(x + 1, y + 1, color)
            self.display.plotPixel(x + 2, y + 1, color)

            self.display.plotPixel(x - 1, y + 2, color)
            self.display.plotPixel(x    , y + 2, color)
            self.display.plotPixel(x + 1, y + 2, color)
            self.display.plotPixel(x + 2, y + 2, color)

            self.display.plotPixel(x    , y + 4, color)
            self.display.plotPixel(x + 1, y + 4, color)

        #TODO: reduzir a quantidade de ifs
        
    def line(self, initial_x, initial_y, final_x, final_y, color, thickness, type_line):
        delta_x = final_x - initial_x
        delta_y = final_y - initial_y

        if delta_x < 0:
            initial_x, final_x = final_x, initial_x
            initial_y, final_y = final_y, initial_y

            delta_x = final_x - initial_x
            delta_y = final_y - initial_y

        incremental_error = 2 * delta_y - delta_x

        if abs(delta_x) >= abs(delta_y):
            y = initial_y
            y_increment = 1

            if delta_y < 0:
                y_increment = -1
                delta_y = -delta_y
            elif delta_y == 0:
                y_increment = 0

            if delta_x < 0:
                for x in range(initial_x, final_x-1, -1):
                    self.pixel(x, y, color, thickness)
                    if incremental_error > 0:
                        y = y + y_increment
                        incremental_error = incremental_error - 2 * delta_x

                    incremental_error = incremental_error + 2 * delta_y

            if delta_x > 0:
                for x in range(initial_x, final_x + 1):
                    self.pixel(x, y, color, thickness)
                    if incremental_error > 0:
                        y = y + y_increment
                        incremental_error = incremental_error - 2 * delta_x

                    incremental_error = incremental_error + 2 * delta_y

        else:
            x = initial_x
            x_increment = 1

            if delta_x < 0:
                x_increment = -1
                delta_x = -delta_x
            elif delta_x == 0:
                x_increment = 0

            if delta_y < 0:
                for y in range(initial_y, final_y-1, -1):
                    self.pixel(x, y, color, thickness)
                    if incremental_error > 0:
                        x = x + x_increment
                        incremental_error = incremental_error - 2 * delta_x

                    incremental_error = incremental_error + 2 * delta_y

            if delta_y > 0:
                for y in range(initial_y, final_y+1):
                    self.pixel(x, y, color, thickness)
                    if incremental_error > 0:
                        x = x + x_increment
                        incremental_error = incremental_error - 2 * delta_x

                    incremental_error = incremental_error + 2 * delta_y
    
    def circle_points(self, xc, yc, x, y, color):
        self.pixel(xc + x, yc + y, color, 1)
        self.pixel(xc - x, yc + y, color, 1)
        self.pixel(xc + x, yc - y, color, 1)
        self.pixel(xc - x, yc - y, color, 1)
        self.pixel(xc + y, yc + x, color, 1)
        self.pixel(xc - y, yc + x, color, 1)
        self.pixel(xc + y, yc - x, color, 1)
        self.pixel(xc - y, yc - x, color, 1)
    
    
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