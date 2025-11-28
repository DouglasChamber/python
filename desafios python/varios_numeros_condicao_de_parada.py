núm = cont = soma = 0 
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))





'''
from time import sleep

# Códigos ANSI para cores
VERDE = '\033[92m'
VERMELHO = '\033[91m'
AMARELO = '\033[93m'
AZUL = '\033[94m'
RESET = '\033[0m'

print(AZUL + "=== Somador de Números ===" + RESET)
print(AMARELO + "Digite vários números inteiros. Para encerrar, digite 999." + RESET)

soma = 0
cont = 0

n = int(input(AZUL + "Digite um número (999 para parar): " + RESET))

while n != 999:
    soma += n
    cont += 1
    print(VERDE + f"✅ Número {n} adicionado! Soma parcial = {soma}" + RESET)
    sleep(0.5)
    n = int(input(AZUL + "Digite outro número (999 para parar): " + RESET))

print(VERMELHO + "\n⏹ Programa encerrado!" + RESET)
print(VERDE + f"📊 Você digitou {cont} números e a soma entre eles foi {soma}." + RESET)
'''