from radar import Radar
from utils import Utils
from plane import Plane
import time

'''
          PROJETO DESENVOLVIDO POR:

          FELIPE OLIVEIRA MAIA          RA: 21801679
          RAFAEL ABREU FONSECA          RA: 21700439
          
          Para imprimir a tela rodar este arquivo.
'''


class Main:

    radar = Radar()
    utils = Utils()
    # A linha abaixo é uma gambiarra, pode ser lida do csv, mas to com sono agora.
    id_flight = ['LA 2203', 'GZ 0331', 'AZ 0032', 'AZ 0157', 'GZ 0667']

    def main(self):

        self.radar.draw_radar()
        airplane_routes = self.utils.transform_data_file(self.utils.read_csv('./planes/planilha de radar.csv'))

        for time in range(0, 151, 10):

            for flight in self.id_flight:
                data_flight = airplane_routes.get((str(time), flight))
                airplane = Plane(int(data_flight[5]), int(float(data_flight[6])), int(data_flight[7]))
                airplane.draw_plane(self.radar.display)

            self.radar.reset()

        print('acabei o loop')

        self.radar.display.getMouse()
        self.radar.display.close()
        



        
teste = Main()
teste.main()

