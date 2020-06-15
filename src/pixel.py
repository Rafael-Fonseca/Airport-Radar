'''
          PROJETO DESENVOLVIDO POR:

          FELIPE OLIVEIRA MAIA          RA: 21801679
          RAFAEL ABREU FONSECA          RA: 21700439
'''

class Pixel:
    '''
        Esta classe define um pixel.

        Ela mantém a posição no plano cartesiano de duas dimensões e a cor do pixel.
    '''

    def __init__(self, x, y, color):
        '''
            Constrói o objeto Pixel com os parâmetros fornecidos.

        :param x: Posição no eixo X.
        :param y: Posição no eixo Y.
        :param color: String que representa a cor.
        '''

        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        '''
            Função instanciada ao utilizar a função print, sua função é auxiliar o debug dos desenvolvedores.
        :return: String
        '''

        return 'Position: {}, {}\tColor: {}'.format(self.x, self.y, self.color)

    def __ne__(self, other):
        '''
        Essa função ensina ao python como comparar dois objetos do tipo Pixel.

        E neste caso, dois objetos do tipo Pixels são iguais apenas se todos os seus atributos forem iguais.

        :param other:
        :return: True se o pixel atual e o other são iguais.
        '''
        if self.x != other.x or self.y != other.y or self.color != other.color:
            return True
        else:
            return False

    def __eq__(self, other):
        '''
        O python não implementa automaticamente a negação da função __ne__()
        e uma vez que esta função __ne__ está definida o python solicita que a função __eq__ também seja definida.

        :param other:
        :return: True se o pixel atual e o other são diferentes.
        '''
        return not(self.__ne__(other))
