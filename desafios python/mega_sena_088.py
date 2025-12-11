from random import randint
from time import sleep
lista = list()
jogos = list()
print('-=' * 20)
print('      JOGA NA MEGA SENA      ')
print('-=' * 20)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1.5)
print('-=' * 3, '< BOA SORTE! >', '-=' * 3)

'''
from random import randint
import time

# Códigos ANSI para cores
VERDE = "\033[92m"
AZUL = "\033[94m"
AMARELO = "\033[93m"
RESET = "\033[0m"

palpites = []

print(f"{AZUL}🎲 GERADOR DE PALPITES MEGA SENA 🎲{RESET}")
jogos = int(input(f"{AMARELO}Quantos jogos você quer que eu sorteie? {RESET}"))

for jogo in range(jogos):
    palpites.append([])
    while len(palpites[jogo]) < 6:
        numero = randint(1, 60)
        if numero not in palpites[jogo]:
            palpites[jogo].append(numero)
    palpites[jogo].sort()
    print(f"{VERDE}Jogo {jogo + 1}:{RESET} {palpites[jogo]}")
    time.sleep(0.5)  # pausa para dar suspense

print(f"\n{AZUL}🍀 Boa sorte! 🍀{RESET}")
'''