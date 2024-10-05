direcao = input('Qual direção? ')

while direcao != 'w' and direcao != 'a' and direcao != 's' and direcao != 'd':
    print ('Entrada do jogador inválida!\nVocê deve digitar a/s/d/w!')
    direcao = input('Qual direção? ')

print('Entrada válida')