import peca
import common

class Cavalo(peca.Peca):
    def __init__(self, cor, ordem):
        posicao_x = 0
        if cor is common.COR_BRANCA:
            posicao_x = 7
        posicao_y = 6
        if ordem == 0:
                posicao_y = 1
        super.__init__(posicao_x, posicao_y)