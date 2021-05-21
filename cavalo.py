import peca
import common
import main

class Cavalo(peca.Peca):
    def __init__(self, cor, ordem):
        posicao_x = 0
        if cor is common.COR_BRANCA:
            posicao_x = 7
        posicao_y = 6
        if ordem == 0:
                posicao_y = 1
        super().__init__(posicao_x, posicao_y, cor)

    def possibleAvailablePositions(self):
        possible_available_positions = []
        jumps = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
        for [jump_x, jump_y] in jumps:
            if 0 <= self.posicao_x + jump_x <= 7 and 0 <= self.posicao_y + jump_y <= 7 and ((not main.tabuleiro_do_jogo.temPeca(self.posicao_x + jump_x, self.posicao_y + jump_y) or main.tabuleiro_do_jogo.temPeca(self.posicao_x + jump_x, self.posicao_y + jump_y) != self.cor_peca)) :
                possible_available_positions.append([self.posicao_x + jump_x, self.posicao_y + jump_y])
        return possible_available_positions