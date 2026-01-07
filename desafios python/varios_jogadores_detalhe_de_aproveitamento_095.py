time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')






'''
# 🎨 Códigos de cores ANSI
VERDE = '\033[92m'
VERMELHO = '\033[91m'
AZUL = '\033[94m'
AMARELO = '\033[93m'
RESET = '\033[0m'

jogadores = []

print(f"{AZUL}⚽ Cadastro de Jogadores{RESET}\n")

# Cadastro de vários jogadores
while True:
    jogador = {}
    nome = str(input(f"{AMARELO}👤 Nome: {RESET}")).strip()
    partidas = int(input(f"{AMARELO}🎮 Número de partidas jogadas por {nome}: {RESET}"))

    gols = []
    for p in range(partidas):
        gols_partida = int(input(f"{AZUL}   ➡️ Quantos gols na partida {p + 1}: {RESET}"))
        gols.append(gols_partida)

    jogador['nome'] = nome
    jogador['gols'] = gols
    jogador['total'] = sum(gols)

    jogadores.append(jogador)

    continuar = str(input(f"{AZUL}Deseja cadastrar outro jogador? [S/N]: {RESET}")).strip().upper()
    if continuar == 'N':
        break

# Resumo em tabela
print(f"\n{VERDE}{'-=' * 35}{RESET}")
print(f'{AZUL}{"📋 RESUMO DOS JOGADORES":^70}{RESET}')
print(f'{AMARELO}{"ID":<5}{"Nome":<20}{"Partidas":<10}{"Total de Gols":<15}{RESET}')
for idx, j in enumerate(jogadores):
    print(f'{VERDE}{idx:<5}{RESET}{j["nome"]:<20}{len(j["gols"]):<10}{j["total"]:<15}')
print(f"{VERDE}{'-=' * 35}{RESET}")

# Visualização de detalhes por jogador
while True:
    escolha = str(input(f"\n{AMARELO}🔎 Ver detalhes de qual jogador? (ID) [ou 'S' para sair]: {RESET}")).strip().upper()
    if escolha == 'S':
        print(f"\n{VERDE}✅ Encerrado. Obrigado!{RESET}")
        break

    if not escolha.isdigit():
        print(f"{VERMELHO}⚠️ Entrada inválida. Digite um ID numérico ou 'S'.{RESET}")
        continue

    idx = int(escolha)
    if idx < 0 or idx >= len(jogadores):
        print(f"{VERMELHO}⚠️ ID inexistente. Tente novamente.{RESET}")
        continue

    j = jogadores[idx]
    print(f"\n{VERDE}{'-=' * 35}{RESET}")
    print(f'{AZUL}{"📋 FICHA DO JOGADOR":^70}{RESET}')
    print(f'{AMARELO}👤 Nome:{RESET} {j["nome"]}')
    print(f'{AMARELO}🎮 Partidas:{RESET} {len(j["gols"])}')
    for i, v in enumerate(j["gols"]):
        emoji_gol = "⚽" if v > 0 else "❌"
        print(f'   {emoji_gol} Partida {i + 1}: {VERDE}{v}{RESET} gols')
    print(f'{AMARELO}📊 Total de gols:{RESET} {VERDE}{j["total"]}{RESET}')
    print(f"{VERDE}{'-=' * 35}{RESET}")
'''