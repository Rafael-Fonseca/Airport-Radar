from line import Line


class Polygon:

    def __init__(self, *tuple_points):

        if len(tuple_points) < 3:
            raise AttributeError('A classe polygon deve ser iniciada com no mínimo 3 pontos.')

        self.lines = []

        for point in range(0, len(tuple_points)-1):
            self.lines.append(Line(tuple_points[point][0], tuple_points[point][1],
                                   tuple_points[point+1][0], tuple_points[point+1][1]))

        self.lines.append(Line(tuple_points[-1][0], tuple_points[-1][1], tuple_points[0][0], tuple_points[0][1]))
