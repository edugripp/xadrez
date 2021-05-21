#tabuleiro
#00 01 02 03 04 05 06 07
#10 11 12 13 14 15 16 17
#20 21 22 23 24 25 26 27
#30 31 32 33 34 35 36 37
#40 41 42 43 44 45 46 47
#50 51 52 53 54 55 56 57
#60 61 62 63 64 65 66 67
#70 71 72 73 74 75 76 77

import  common

class Peca():
    cor_peca = common.COR_PRETA
    posicao_x = 0
    posicao_y = 0
    antiga_posicao_x = 0
    antiga_posicao_y = 0


    def __init__(self, posicao_x, posicao_y, cor):
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.antiga_posicao_x = posicao_x
        self.antiga_posicao_y = posicao_y
        self.cor_peca = cor


    def setPosicao(self, posicao_x, posicao_y):
        self.antiga_posicao_x = self.posicao_x
        self.antiga_posicao_y = self.posicao_y
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y


    def getPosicao(self):
        return self.posicao_x, self.posicao_y

    def getPosicaoAntiga(self):
        return self.antiga_posicao_x, self.antiga_posicao_y


    def getCorPeca(self):
        return self.cor_peca