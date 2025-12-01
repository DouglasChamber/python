soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma do {cont} valores foi {soma}!')







'''
from time import sleep

# Cores ANSI
verde = '\033[32m'
vermelho = '\033[31m'
amarelo = '\033[33m'
azul = '\033[34m'
reset = '\033[m'

soma = numeros = cont = 0

print(azul + "=== SOMADOR INTERATIVO ===" + reset)
sleep(0.5)

while True:
    numeros = int(input(f"{amarelo}Digite um Número [999 para parar]: {reset}"))
    if numeros == 999:
        print(vermelho + "Encerrando..." + reset)
        sleep(0.5)
        break
    soma += numeros
    cont += 1
    print(verde + "Número adicionado!" + reset)
    sleep(0.3)

print(f"\n{azul}A soma dos números é {verde}{soma}{azul} e foram digitados {amarelo}{cont}{azul} números.{reset}")
'''