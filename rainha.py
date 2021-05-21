import peca
import common
import main

class Rainha(peca.Peca):
    def __init__(self, cor):
        posicao_x = 0
        posicao_y = 3
        if cor is common.COR_BRANCA:
            posicao_x = 7
        super().__init__(posicao_x, posicao_y, cor)

    def possibleAvailablePositions(self):
        possible_available_positions = []
        directions = [[-1, -1], [-1, 1], [1, -1], [1,1], [-1, 0], [1, 0], [0, 1], [0, -1]]
        for [direction_x, direction_y] in directions:
            posicao_x = self.posicao_x + direction_x
            posicao_y = self.posicao_y + direction_y
            while (not main.tabuleiro_do_jogo.temPeca(posicao_x, posicao_y)) and 0 <= posicao_x <= 7 and 0 <= posicao_y <= 7:
                possible_available_positions.append([posicao_x, posicao_y])
                posicao_x += direction_x
                posicao_y += direction_y
            if 0 <= posicao_x <= 7 and 0 <= posicao_y <= 7 and main.tabuleiro_do_jogo.temPeca(posicao_x, posicao_y) == self.cor_peca:
                possible_available_positions.pop()
        return possible_available_positions