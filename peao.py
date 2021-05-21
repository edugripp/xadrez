import peca
import common

class Peao(peca.Peca):
    def __init__(self, cor, ordem):
        posicao_x = 1
        if cor is common.COR_BRANCA:
            posicao_x = 6
        posicao_y = ordem
        super().__init__(posicao_x, posicao_y, cor)

    def possibleAvailablePositions(self):
        direction_x = -1 if self.cor_peca == common.COR_BRANCA else 1
        possible_available_positions = [[self.posicao_x + direction_x, self.posicao_y]]
        if self.posicao_y > 0:
            possible_available_positions.append([self.posicao_x + direction_x, self.posicao_y - 1])
        if self.posicao_y < 7:
            possible_available_positions.append([self.posicao_x + direction_x, self.posicao_y + 1])
        if (self.posicao_x == 1 or self.posicao_x == 6) and 0 <= self.posicao_x + 2 * direction_x <= 7:
            possible_available_positions.append([self.posicao_x + 2 * direction_x, self.posicao_y])
        return possible_available_positions
