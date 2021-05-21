import peca
import common
import tabuleiro

class Torre(peca.Peca):
    def __init__(self, cor, ordem):
        posicao_x = 0
        if cor is common.COR_BRANCA:
            posicao_x = 7
        posicao_y = 7
        if ordem == 0:
                posicao_y = 0
        super().__init__(posicao_x, posicao_y, cor)
    
    def possibleAvailablePositions(self):
        possible_available_positions = []
        for direction_x in [-1, 1]:
            posicao_x = self.posicao_x + direction_x
            while (not TABULEIRO.temPeca(posicao_x, self.posicao_y)) and 0 <= posicao_x <= 7:
                possible_available_positions.append([posicao_x + direction_x, self.posicao_y])
                posicao_x += direction_x
            if 0 <= posicao_x <= 7 and TABULEIRO.temPeca(posicao_x, self.posicao_y) == self.cor_peca:
                possible_available_positions.pop()
        for direction_y in [-1, 1]:
            posicao_y = self.posicao_y + direction_y
            while (not TABULEIRO.temPeca(self.posicao_x, posicao_y)) and 0 <= posicao_y <= 7:
                possible_available_positions.append([self.posicao_x, posicao_y + direction_y])
                posicao_y += direction_y
            if 0 <= posicao_y <= 7 and TABULEIRO.temPeca(self.posicao_x, posicao_y) == self.cor_peca:
                possible_available_positions.pop()
        return possible_available_positions
