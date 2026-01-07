from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1,6)}
ranking = list()
print('Valores Sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado. ')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 15)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f' {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)



'''
from random import randint
from time import sleep

# 🎨 Códigos de cores ANSI
VERDE = '\033[92m'
VERMELHO = '\033[91m'
AZUL = '\033[94m'
AMARELO = '\033[93m'
RESET = '\033[0m'

# 🎲 Agora com 4 jogadores
jogadores = {'Jogador 1': 0, 'Jogador 2': 0, 'Jogador 3': 0, 'Jogador 4': 0}

print(f'{AZUL}🎲 Lançando os dados...{RESET}\n')
sleep(1)

# Sorteio dos dados
for j in jogadores.keys():
    jogadores[j] = randint(1, 6)
    print(f'{AMARELO}{j}{RESET} tirou 🎲 {VERDE}{jogadores[j]}{RESET} no dado.')
    sleep(0.5)

print(f'\n{AZUL}{"-=" * 15}{RESET}\n')

# Ranking em ordem decrescente
ranking = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)

print(f'{VERDE}🏆 RANKING DOS JOGADORES 🏆{RESET}\n')
for i, v in enumerate(ranking):
    # Verifica se há empate com o anterior
    if i > 0 and v[1] == ranking[i-1][1]:
        status = f'{VERMELHO}🤝 Empatado com {ranking[i-1][0]}{RESET}'
    else:
        status = ''
    
    medalha = "🥇" if i == 0 else "🥈" if i == 1 else "🥉" if i == 2 else "🎖️"
    print(f'  {medalha} {i + 1}º lugar: {AZUL}{v[0]}{RESET} com 🎲 {VERDE}{v[1]}{RESET} {status}')
    sleep(0.5)
'''