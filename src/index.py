from radar import Radar

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
        self.radar.reset()

        self.radar.display.getMouse()
        self.radar.display.close()



        
teste = Main()
teste.main()

