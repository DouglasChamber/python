from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

try:
    jogador = int(input('Qual é a sua jogada? '))
    if jogador not in [0, 1, 2]:
        print('JOGADA INVÁLIDA!')
    else:
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!')
        sleep(1)

        print('-=' * 11)
        print(f'O computador jogou {itens[computador]}')
        print(f'Jogador jogou {itens[jogador]}')
        print('-=' * 11)

        if computador == jogador:
            print('EMPATE')
        elif (computador == 0 and jogador == 1) or \
             (computador == 1 and jogador == 2) or \
             (computador == 2 and jogador == 0):
            print('JOGADOR VENCE')
        else:
            print('COMPUTADOR VENCE')
except ValueError:
    print('Entrada inválida! Digite 0, 1 ou 2.')





'''
import random
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.CYAN + "🕹️ Bem Vindo ao Jokenpô (pedra, papel ou tesoura) 🕹️ ")

opcoes = ["pedra", "papel", "tesoura"]

jogador = input(Style.RESET_ALL + "Escolha sua jogada (🧱 Pedra, 📄 Papel, ✂️  Tesoura): ").lower()

computador = random.choice(opcoes)

print(f"\n🤖 O Computador Jogou: {computador}")
print(f"🧑 Você Jogou: {jogador}")

if jogador == computador:
    print(Fore.YELLOW + "😐 EMPATE! ")
elif (jogador == "pedra" and computador == "tesoura") or (jogador == "papel" and computador == "pedra") or (jogador == "tesoura" and computador == "papel"):
    print(Fore.GREEN + "🎉Você Venceu!🎉 ")
elif jogador in opcoes:
    print(Fore.RED + "💥Você Perdeu!💥")
else:
    print(Fore.RED + "❌ Jogada Inválida. Tente Novamente com Pedra, Papel ou Tesoura ")
'''