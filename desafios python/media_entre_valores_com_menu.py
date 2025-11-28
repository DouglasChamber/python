resp = 'S'
soma = quant = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um Número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a media foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))




'''
from time import sleep

# Códigos ANSI para cores
VERDE = '\033[92m'
VERMELHO = '\033[91m'
AMARELO = '\033[93m'
AZUL = '\033[94m'
RESET = '\033[0m'

print(AZUL + "=== Analisador de Números ===" + RESET)
print(AMARELO + "Digite vários números inteiros. O programa mostrará a média, o maior e o menor valor." + RESET)

soma = 0
cont = 0
maior = None
menor = None

while True:
    n = int(input(AZUL + "Digite um número: " + RESET))
    soma += n
    cont += 1

    # Atualiza maior e menor
    if maior is None or n > maior:
        maior = n
    if menor is None or n < menor:
        menor = n

    print(VERDE + f"✅ Número {n} adicionado! Soma parcial = {soma}" + RESET)
    sleep(0.5)

    resposta = input(AMARELO + "Você deseja continuar? [S/N]: " + RESET).strip().upper()
    if resposta == 'N':
        break

# Calcula média
media = soma / cont

print(VERMELHO + "\n⏹ Programa encerrado!" + RESET)
print(VERDE + f"📊 Você digitou {cont} números." + RESET)
print(VERDE + f"📊 A média dos valores é {media:.2f}." + RESET)
print(VERDE + f"📊 O maior valor foi {maior} e o menor foi {menor}." + RESET)
'''