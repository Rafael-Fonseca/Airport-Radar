from line import Line

'''
          PROJETO DESENVOLVIDO POR:

          FELIPE OLIVEIRA MAIA          RA: 21801679
          RAFAEL ABREU FONSECA          RA: 21700439
'''


class Polygon:
    '''
    Todo: verificação se len tuple_points é maior que 3
    '''

    def __init__(self, list_tuple_points):
        self.lines = []
        for point in range(0, len(list_tuple_points)-1):
            self.lines.append(Line(list_tuple_points[point][0], list_tuple_points[point][1],
                                   list_tuple_points[point+1][0], list_tuple_points[point+1][1]))

        '''
        A linha abaixo garante que não aja index error e realiza a ultima iteração.
        '''
        self.lines.append(Line(list_tuple_points[-1][0], list_tuple_points[-1][1],
                               list_tuple_points[0][0], list_tuple_points[0][1]))
