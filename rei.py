import peca
import common

class Rei(peca.Peca):
    def __init__(self, cor):
        posicao_x = 0
        posicao_y = 4
        if cor is common.COR_BRANCA:
            posicao_x = 7
        super.__init__(posicao_x, posicao_y, cor)

    
    def possibleAvailablePositions(self):
        possible_available_positions = []
        for i in range(-1, 2) :
            for j in range(-1, 2) :
                if self.posicao_x + i > 0 and self.posicao_y + j > 0 and self.posicao_x + i < 7 and self.posicao_y - i < 7:
                    possible_available_positions.append([self.posicao_x + i , self.posicao_y + j])
        return possible_available_positions

