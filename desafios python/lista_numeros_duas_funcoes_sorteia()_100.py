from random import randint
from time import sleep

def sorteio(lista):
    print('Sorteando 5 números: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.5)
    print('PRONTO')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}.')

números = list()
sorteio(números)
somaPar(números)

'''
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
'''
