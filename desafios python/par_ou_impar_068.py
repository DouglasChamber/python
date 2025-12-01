from random import randint

v = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI': 
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('VAMOS JOGAR NOVAMENTE...')
print(f'GAME OVER! Você venceu {v} vezes.')






'''
import random
from time import sleep

# Cores ANSI
verde = '\033[32m'
vermelho = '\033[31m'
amarelo = '\033[33m'
azul = '\033[34m'
ciano = '\033[36m'
reset = '\033[m'

win = lose = cont = 0

print(ciano + '=== Jogo do Par ou Ímpar ===' + reset)
sleep(0.5)

while True:
    escolha = str(input(amarelo + 'Escolha Par ou Ímpar [P/I]: ' + reset)).strip().upper()[0]
    jogador = int(input(azul + 'Digite um número de 0 a 100: ' + reset))
    computador = random.randint(0, 100)
    total = jogador + computador

    print(f'\n{verde}Você jogou {jogador}{reset} e o computador jogou {vermelho}{computador}{reset}.')
    sleep(0.5)
    print(f'Total de {azul}{total}{reset}.', end=' ')
    sleep(0.5)

    if total % 2 == 0:
        print(verde + 'Deu Par!' + reset)
        if escolha == 'P':
            print(ciano + 'Você Venceu!' + reset)
            win += 1
        else:
            print(vermelho + 'Você Perdeu!' + reset)
            lose += 1
            break
    else:
        print(vermelho + 'Deu Ímpar!' + reset)
        if escolha == 'I':
            print(ciano + 'Você Venceu!' + reset)
            win += 1
        else:
            print(vermelho + 'Você Perdeu!' + reset)
            lose += 1
            break

    cont += 1
    print(amarelo + 'Vamos jogar novamente...\n' + reset)
    sleep(0.6)

# Ao sair
print(f'\n{azul}Vitórias: {verde}{win}{azul} | Derrotas: {vermelho}{lose}{reset}')
'''