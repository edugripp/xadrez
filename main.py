import common, tabuleiro, rei, rainha, torre, cavalo, peao, bispo

#pecas pretas
rei_p = None
rainha_p = None
torres_p = []
cavalos_p = []
bispos_p = []
peoes_p = []

#pecas brancas
rei_b = None
rainha_b = None
torres_b = []
cavalos_b = []
bispos_b = []
peoes_b = []

#tabuleiro
tabuleiro_do_jogo = None


def iniciar_pecas_pretas():
    global rei_p, rainha_p, torres_p, cavalos_p, bispos_p, peoes_p, tabuleiro_do_jogo
    cor = common.COR_PRETA
    rei_p = rei.Rei(cor)
    tabuleiro_do_jogo.setPeca(rei_p)
    rainha_p = rainha.Rainha(cor)
    tabuleiro_do_jogo.setPeca(rainha_p)
    for i in range(8):
        if i < 2:
            torres_p.append(torre.Torre(cor, i))
            tabuleiro_do_jogo.setPeca(torres_p[i])
            cavalos_p.append(cavalo.Cavalo(cor, i))
            tabuleiro_do_jogo.setPeca(cavalos_p[i])
            bispos_p.append(bispo.Bispo(cor, i))
            tabuleiro_do_jogo.setPeca(bispos_p[i])
        peoes_p.append(peao.Peao(cor, i))
        tabuleiro_do_jogo.setPeca(peoes_p[i])


def iniciar_pecas_brancas():
    global rei_b, rainha_b, torres_b, cavalos_b, bispos_b, peoes_b, tabuleiro_do_jogo
    cor = common.COR_BRANCA
    rei_b = rei.Rei(cor)
    tabuleiro_do_jogo.setPeca(rei_b)
    rainha_b = rainha.Rainha(cor)
    tabuleiro_do_jogo.setPeca(rainha_b)
    for i in range(8):
        if i < 2:
            torres_b.append(torre.Torre(cor, i))
            tabuleiro_do_jogo.setPeca(torres_b[i])
            cavalos_b.append(cavalo.Cavalo(cor, i))
            tabuleiro_do_jogo.setPeca(cavalos_b[i])
            bispos_b.append(bispo.Bispo(cor, i))
            tabuleiro_do_jogo.setPeca(bispos_b[i])
        peoes_b.append(peao.Peao(cor, i))
        tabuleiro_do_jogo.setPeca(peoes_b[i])


def iniciar_tabuleiro():
    global tabuleiro_do_jogo
    tabuleiro_do_jogo = tabuleiro.Tabuleiro()


def printPecas():
    global rei_p, rainha_p, torres_p, cavalos_p, bispos_p, peoes_p
    global rei_b, rainha_b, torres_b, cavalos_b, bispos_b, peoes_b
    print(rei_p, rainha_p, torres_p, cavalos_p, bispos_p, peoes_p)
    print(rei_b, rainha_b, torres_b, cavalos_b, bispos_b, peoes_b)


def main():
    iniciar_tabuleiro()
    iniciar_pecas_pretas()
    iniciar_pecas_brancas()
    global tabuleiro_do_jogo
    print(tabuleiro_do_jogo.tabuleiro_completo)


if __name__ == "__main__":
    main()