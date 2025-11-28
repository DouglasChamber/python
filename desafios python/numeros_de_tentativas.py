from random import randint

computador = randint(0, 10)
print('=== Jogo da Adivinhação ===')
print('Tente adivinhar o número que estou pensando entre 0 e 10.')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente.')
        elif jogador > computador:
            print('Menos... Tente novamente.')
print('Parabéns! Você acertou o número {} em {} tentativas.'.format(computador, palpites))

'''
import random

# Códigos ANSI para cores
VERDE = '\033[92m'
VERMELHO = '\033[91m'
AMARELO = '\033[93m'
AZUL = '\033[94m'
RESET = '\033[0m'

tentativas = 0
numero_secreto = random.randint(1, 10)
acertou = False

print(AMARELO + "=== Jogo da Adivinhação ===" + RESET)

while not acertou:
    palpite = int(input(AZUL + 'Digite seu palpite (1 a 10): ' + RESET))
    tentativas += 1
    if palpite == numero_secreto:
        acertou = True
        print(VERDE + '🎉 Parabéns! Você acertou o número {} em {} tentativas.'.format(numero_secreto, tentativas) + RESET)
    else:
        print(VERMELHO + '❌ Errado! Tente novamente.' + RESET)
'''