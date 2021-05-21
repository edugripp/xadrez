import peca
import common

class Rei(peca.Peca):
    def __init__(self, cor):
        posicao_x = 0
        posicao_y = 4
        if cor is common.COR_BRANCA:
            posicao_x = 7
        super.__init__(posicao_x, posicao_y)
