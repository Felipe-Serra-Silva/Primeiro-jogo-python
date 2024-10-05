
from funcoes import *

# Largura e altura do tabuleiro
largura = 8
altura = 8

# Sorteia posição do monstro
x_monstro, y_monstro = sorteia_posicao_do_monstro(largura, altura)

# Sorteia posição do Jogador
x_jogador, y_jogador = sorteia_posicao_do_jogador(largura, altura, x_monstro, y_monstro)

# Sorteia posição da Porta
x_porta, y_porta = sorteia_posicao_da_porta(largura, altura, x_monstro, y_monstro, x_jogador, y_jogador)

# ---------------------------------------------------------- #

jogando = True
debug = True # Com o debug igual a True a posição do monstro e da porta são visíveis
while jogando:

    tabuleiro = imprime_tabuleiro(x_monstro, y_monstro, x_jogador, y_jogador, x_porta, y_porta, largura, altura, debug)
    print(tabuleiro)

    # TODO 1 Coloque aqui o seu código do exercício: Valida entrada do Jogador
    
    direcao = input('Qual direção? ')

    while direcao != 'w' and direcao != 'a' and direcao != 's' and direcao != 'd':
        print ('Entrada do jogador inválida!\nVocê deve digitar a/s/d/w!')
        direcao = input('Qual direção? ')

    print('Entrada válida')

    # TODO 2 Adicione abaixo o código referente ao exercício: Atualiza posição do jogador abaixo

    if direcao == 'w':
        y_jogador = y_jogador - 1
    if  direcao == 's':
        y_jogador = y_jogador + 1
    if direcao == 'd':
        x_jogador = x_jogador + 1
    if direcao == 'a':
        x_jogador = x_jogador - 1
    print(f"({x_jogador}, {y_jogador})")


    # TODO 3 Adicione abaixo o código referente ao exercício: Verifica se o Jogador encontrou a porta

    while x_jogador != x_porta or y_jogador != y_porta:
        tabuleiro = imprime_tabuleiro(x_monstro, y_monstro, x_jogador, y_jogador, x_porta, y_porta, largura, altura, debug)
        print(tabuleiro)

        direcao = input('Qual direção? ')

        while direcao != 'w' and direcao != 'a' and direcao != 's' and direcao != 'd':
            print ('Entrada do jogador inválida!\nVocê deve digitar a/s/d/w!')
            direcao = input('Qual direção? ')

        print('Entrada válida')

        if direcao == 'w':
            y_jogador = y_jogador - 1
        if  direcao == 's':
            y_jogador = y_jogador + 1
        if direcao == 'd':
            x_jogador = x_jogador + 1
        if direcao == 'a':
            x_jogador = x_jogador - 1
        print(f"({x_jogador}, {y_jogador})")
    print("Achou a porta!")


    # TODO 5 Adicione abaixo o código referente ao exercício: Movimenta Monstro

    jogando = False
