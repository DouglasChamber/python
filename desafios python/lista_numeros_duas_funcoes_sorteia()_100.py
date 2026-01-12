from random import randint
from time import sleep

numeros = []

def sorteio():
    print('Sorteando 5 números: ', end='')
    for i in range(5):  
        n = randint(1, 100)
        numeros.append(n)  
        print(n, end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')

def somaPar():
    s = 0
    for n in numeros:
        if n % 2 == 0:
            s += n
    print(f'\nSomando os valores pares de {numeros}, temos {s}.')

# Programa Principal
sorteio()
somaPar()
