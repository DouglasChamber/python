
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')




'''
from time import sleep

# Cores ANSI
verde = '\033[32m'
vermelho = '\033[31m'
amarelo = '\033[33m'
azul = '\033[34m'
reset = '\033[m'

print(azul + 'Digite um número para ver sua tabuada (número negativo para encerrar): ' + reset)

while True:
    num = int(input(amarelo + 'Digite o número da Tabuada: ' + reset))

    if num < 0:
        print(vermelho + 'Número negativo digitado. Encerrando o programa...' + reset)
        sleep(0.6)
        break

    print(f'{azul}Tabuada do {verde}{num}{reset}:')
    sleep(0.3)

    for i in range(1, 11):
        resultado = num * i
        print(f'{verde}{num}{reset} x {amarelo}{i}{reset} = {azul}{resultado}{reset}')
        sleep(0.15)

    print(azul + '---' + reset)
    sleep(0.3)
'''