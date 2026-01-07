jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'  => Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')



'''
from datetime import datetime

# 🎨 Códigos de cores ANSI
VERDE = '\033[92m'
VERMELHO = '\033[91m'
AZUL = '\033[94m'
AMARELO = '\033[93m'
RESET = '\033[0m'

# Entrada de dados
print(f"{AZUL}⚽ Cadastro do Jogador{RESET}\n")
nome = str(input(f"{AMARELO}👤 Nome: {RESET}"))
partidas = int(input(f"{AMARELO}🎮 Número de partidas jogadas por {nome}: {RESET}"))

# Coleta dos gols
gols = []
for p in range(partidas):
    gols_partida = int(input(f"{AZUL}   ➡️ Quantos gols na partida {p + 1}: {RESET}"))
    gols.append(gols_partida)

# Total de gols
total_gols = sum(gols)

# Dicionário do jogador
jogador = {
    'nome': nome,
    'gols': gols,
    'total': total_gols
}

# Exibição da ficha
print(f"\n{VERDE}{'-=' * 30}{RESET}")
print(f'{AZUL}{"📋 FICHA DO JOGADOR":^60}{RESET}')
print(f'{AMARELO}👤 Nome do jogador:{RESET} {jogador["nome"]}')

for i, v in enumerate(jogador['gols']):
    emoji_gol = "⚽" if v > 0 else "❌"
    print(f'   {emoji_gol} Partida {i + 1}: {VERDE}{v}{RESET} gols')

print(f'{AMARELO}📊 Total de gols:{RESET} {VERDE}{jogador["total"]}{RESET}')
print(f"{VERDE}{'-=' * 30}{RESET}")
'''