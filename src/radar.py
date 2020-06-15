from graphics import *
from draw import Draw
from plane import Plane
from utils import Utils
import copy
import time as tm


'''
          PROJETO DESENVOLVIDO POR:

          FELIPE OLIVEIRA MAIA          RA: 21801679
          RAFAEL ABREU FONSECA          RA: 21700439
'''
#Classe do radar.
class Radar:
    '''
    Classe que chama todos os procedimentos necessários ao implante da tela
    '''

    def __init__(self):
        self.base = []
        self.utils = Utils()
        self.table = "./planes/planilha de radar.csv"
        self.display = GraphWin("Radar", 500, 500)
        self.display.setBackground('black')

    def get_plane(self):
        '''
        Função utiliza função para ler arquivo CSV e realiza loop que
        utiliza os dados obtidos no CSV, para desenhar os aviões na tela.

        :return: Os aviões desenhados na tela.
        '''

        #TODO: MUDAR A FORMA DE OBTENÇÃO DOS AVIÕES
        self.id_flight = ['LA 2203', 'GZ 0331', 'AZ 0032', 'AZ 0157', 'GZ 0667']

        self.airplane_routes = self.utils.transform_data_file(self.utils.read_csv(self.table))

        for time in range(0, 151, 10):

            for flight in self.id_flight:
                self.data_flight = self.airplane_routes.get((str(time), flight))

                if int(self.data_flight[5]) != 0:
                    self.airplane = Plane(int(self.data_flight[5]) + 250, int(float(self.data_flight[6])) + 250, int(self.data_flight[7]))
                if int(self.data_flight[5]) == 0:
                    self.airplane = Plane(int(self.data_flight[5]), int(float(self.data_flight[6])), int(self.data_flight[7]))

                self.airplane.draw_plane(self.draw, self.data_flight)
            
            tm.sleep(1)
            self.reset()

    def draw_radar(self):
        '''
            Além do seu retorno essa função cria a variável self.base
            esta variável matém as informações das cores na tela após
            o desenho do radar.
        :return: Desenha as linhas do radar na tela.
        '''

        self.draw = Draw(self.display)

        # Circulos concentricos
        self.draw.circle(250, 250, 62, 'green')
        self.draw.circle(250, 250, 124, 'green')
        self.draw.circle(250, 250, 186, 'green')
        self.draw.circle(250, 250, 248, 'green')

        # Linha do segundo ao quarto quadrante
        self.draw.line(0, 0, 500, 500, 'green', 1, 3)

        # Linha do terceiro ao primeiro quadrante
        self.draw.line(0, 500, 250, 250, 'green', 1, 3)
        self.draw.line(250, 250, 500, 0, 'green', 1, 3)

        # Linha horizontal
        self.draw.line(1, 250, 249, 249, 'green', 1, 3)
        self.draw.line(250, 250, 500, 250, 'green', 1, 3)

        # Linha vertical
        self.draw.line(250, 0, 250, 500, 'green', 1, 3)

        # Necessário o uso do deepcopy, uma vez que as listas do python se comportam como ponteiros.
        self.base = copy.deepcopy(self.draw.screen.pixels)

        self.get_plane()

    #Função para limpar a tela
    def reset(self):
        '''
            Esta função realiza um loop por toda a variavel self.base.
                self.base é uma matriz(lista de listas) na organização
                self.base[coluna][linha] = "cor"

                self.base matém valores necessários para desenhar o radar.

            Neste loop, a função compara:
            Os valores da variável que guarda a cor de cada pixel, atualmente na tela.
            com
            Os valores da variável self.base
        :return:
        '''

        for column_pixel in self.base:
            for pixel in column_pixel:
                if pixel != self.draw.screen.pixels[pixel.x][pixel.y]:
                    self.draw.point(pixel.x, pixel.y, pixel.color, 1)
