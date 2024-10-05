import random
import math

def sorteia_posicao_do_monstro(largura, altura):
    return random.randint(0, largura-1), random.randint(0, altura-1)

def sorteia_posicao_do_jogador(largura, altura, x_monstro, y_monstro):
    sorteia_pos = True
    while sorteia_pos:
        x_jogador = random.randint(0, largura-1)
        y_jogador = random.randint(0, altura-1)
        if x_jogador != x_monstro or y_jogador != y_monstro:
            sorteia_pos = False
    return x_jogador, y_jogador

def sorteia_posicao_da_porta(largura, altura, x_monstro, y_monstro, x_jogador, y_jogador):
    sorteia_pos = True
    while sorteia_pos:
        x_porta = random.randint(0, largura-1)
        y_porta = random.randint(0, altura-1)
        if (x_porta != x_monstro or y_porta != y_monstro) and  (x_porta != x_jogador or y_porta != y_jogador):
            sorteia_pos = False
    return x_porta, y_porta

def dica(x_monstro, y_monstro, x_jogador, y_jogador):
    distancia = math.sqrt((x_jogador - x_monstro)**2 + (y_jogador-y_monstro)**2)
    if distancia <= 2:
        return 'quente'
    elif distancia <= 3:
        return 'morno'
    elif distancia <= 4:
        return 'fresco'
    else:
        return 'frio'

def imprime_tabuleiro(x_monstro, y_monstro, x_jogador, y_jogador,x_porta, y_porta, largura, altura, debug):
    tabuleiro = ''
    linha1 = f"   {'  '.join([f'{i}' for i in range(largura)])}"
    tabuleiro += f'{linha1}\n'
    tabuleiro += f'{"_"*len(linha1)}\n'

    for y in range(altura):
        linha = f'{y}| '
        for x in range(largura):
            if x == x_jogador and y == y_jogador:
                linha += f'J  '
            elif x == x_monstro and y == y_monstro and debug:
                linha += f'M  '
            elif x == x_porta and y == y_porta and debug:
                linha += f'P  '
            else:
                linha += f'_  '

        tabuleiro += f"{linha}\n"
    return tabuleiro
    
# TODO 4 Adicione abaixo a função referente ao exercício: Bússola

def bussola(x_monstro, y_monstro, x_jogador, y_jogador):
    if x_monstro == x_jogador and y_monstro == y_jogador:
        return 'achou'

    resultado_x = abs(x_jogador - x_monstro) 
    resultado_y = abs(y_jogador - y_monstro)
    if resultado_x == resultado_y:
        if y_monstro > y_jogador:
            y_monstro = y_monstro - 1
            return 'norte' 
        else:
            y_monstro = y_monstro + 1
            return 'sul' 
    if resultado_x > resultado_y and y_monstro != y_jogador:
        if y_monstro > y_jogador:
            y_monstro = y_monstro - 1
            return 'norte' 
        else:
            y_monstro = y_monstro + 1
            return 'sul' 
    if resultado_x < resultado_y and x_monstro != x_jogador:
        if x_monstro > x_jogador:
            x_monstro =  x_monstro - 1
            return 'oeste'
        else:
            x_monstro = x_monstro + 1
            return 'leste'
    if x_monstro == x_jogador and y_monstro != y_jogador:
        if y_monstro > y_jogador:
            y_monstro = y_monstro - 1
            return 'norte' 
        else:
            y_monstro = y_monstro + 1
            return 'sul'
    if y_monstro == y_jogador and x_monstro != x_jogador:
        if x_monstro > x_jogador:
            x_monstro =  x_monstro - 1
            return 'oeste'
        else:
            x_monstro = x_monstro + 1
            return 'leste'