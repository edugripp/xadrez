class Tabuleiro():
    tabuleiro_completo = None
    def __init__(self):
        for i in range(8):
            for j in range(8):
                self.tabuleiro_completo[i][j] = ''


    def setPeca(self, p):
        x, y = p.getPosicao()
        self.tabuleiro_completo[x][y] = p

        old_x, old_y = p.getPosicaoAntiga()
        if x != old_x or y != old_y:
            self.tabuleiro_completo[old_x][old_y] = ''


    def temPeca(self, x, y):
        if self.tabuleiro_completo[x][y] is '':
            return False
        return self.tabuleiro_completo[x][y].getCorPeca()



