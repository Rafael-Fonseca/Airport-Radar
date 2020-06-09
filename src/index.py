from radar import Radar
import time

'''
          PROJETO DESENVOLVIDO POR:

          FELIPE OLIVEIRA MAIA          RA: 21801679
          RAFAEL ABREU FONSECA          RA: 21700439
          
          Para imprimir a tela rodar este arquivo.
'''

class Main:
    def main(self):
        self.radar = Radar()
        self.radar.draw_radar()
        
        '''
        self.radar.draw.text(250, 250, 'Teste', 'red', 12, 'bold')
        
        self.radar.draw.line(238, 244, 262, 244, 'blue', 1, 1)
        self.radar.draw.line(238, 244, 238, 256, 'blue', 1, 1)
        self.radar.draw.line(262, 256, 262, 244, 'blue', 1, 1)
        self.radar.draw.line(262, 256, 238, 256, 'blue', 1, 1)

        self.radar.draw.point(301, 250, 'white', 2)
        self.radar.draw.point(302, 250, 'white', 3)
        self.radar.draw.point(303, 250, 'white', 4)
        self.radar.draw.point(305, 250, 'white', 2)

        time.sleep(2)
        self.radar.reset()
        '''
        self.radar.draw.airplane(335, 225, 'white')
        self.radar.draw.fill(335, 225, 'white')

        self.radar.display.getMouse()
        self.radar.display.close()



        
teste = Main()
teste.main()

