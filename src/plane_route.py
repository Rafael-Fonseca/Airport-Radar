import pandas as pd

class Plane_route():
    def __init__(self,table):
        self.table = table
        self.T = table["T"],
        self.Status = table["Status"],
        self.Voo = table["Voo"],
        self.Dist = table["Dist"],
        self.VEL = table["VEL"],
        self.X = table["X"],
        self.Y = table["Y"],
        self.Z = table["Z"]
        

    #ler a tabela e fazer a organizacao dos dados
    def get_plane(self):
        print(self.table)
        




