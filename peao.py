import peca
import common

class Bispo(peca.Peca):
    def __init__(self, cor, ordem):
        posicao_x = 1
        if cor is common.COR_BRANCA:
            posicao_x = 6
        posicao_y = ordem
        super.__init__(posicao_x, posicao_y)