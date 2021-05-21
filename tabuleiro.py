class Tabuleiro():
    tabuleiro_completo = []
    def __init__(self):
        for i in range(8):
            lista_auxiliar = []
            for j in range(8):
                lista_auxiliar.append('')
            self.tabuleiro_completo.append(lista_auxiliar)

    def setPeca(self, p):
        x, y = p.getPosicao()
        self.tabuleiro_completo[x][y] = p

        old_x, old_y = p.getPosicaoAntiga()
        if x != old_x or y != old_y:
            self.tabuleiro_completo[old_x][old_y] = ''


    def temPeca(self, x, y):
        if self.tabuleiro_completo[x][y] == '':
            return False
        return self.tabuleiro_completo[x][y].getCorPeca()



