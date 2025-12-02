from time import sleep

times = (
    'Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Botafogo',
    'Fluminense', 'Bahia', 'São Paulo', 'Corinthians', 'Grêmio',
    'Vasco da Gama', 'Red Bull Bragantino', 'Atlético-MG', 'Ceará',
    'Internacional', 'Fortaleza', 'Santos', 'Vitória', 'Juventude',
    'Sport')

print('-=' * 35)
print('TABELA BRASILEIRÃO 2025')
print('-=' * 35)
sleep(1)
print(f'🏆 Os primeiros 5 colocados são: {times[0:5]}')
sleep(4)
print(f'⚠️ Os últimos 4 colocados são: {times[-4:]}')
sleep(4)
print(f'📋 Times em ordem alfabética: {sorted(times)}')
sleep(4)
print(f'🔎 O Corinthians está na {times.index("Corinthians") + 1}ª posição.')


'''
from colorama import Fore, Style, init
from time import sleep

# Inicializa o Colorama para usar cores no terminal
init(autoreset=True)

print(Fore.YELLOW + '-=' * 35)
print(Fore.GREEN + Style.BRIGHT + 'TABELA BRASILEIRÃO 2025')
print(Fore.YELLOW + '-=' * 35)

sleep(1)

brasileirao = (
    'Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Botafogo',
    'Fluminense', 'Bahia', 'São Paulo', 'Corinthians', 'Grêmio',
    'Vasco da Gama', 'Red Bull Bragantino', 'Atlético-MG', 'Ceará',
    'Internacional', 'Fortaleza', 'Santos', 'Vitória', 'Juventude',
    'Sport'
)

sleep(1)
# Mostra os primeiros 5 colocados
print(Fore.CYAN + '🏆 Os primeiros 5 colocados são:')
for pos, time in enumerate(brasileirao[:5], start=1):
    print(Fore.WHITE + f'{pos}º - {time}')

print(Fore.YELLOW + '-=' * 35)

sleep(4)

# Mostra os últimos 4 colocados
print(Fore.RED + '⚠️ Os últimos 4 colocados são:')
for pos, time in enumerate(brasileirao[-4:], start=len(brasileirao)-3):
    print(Fore.WHITE + f'{pos}º - {time}')

print(Fore.YELLOW + '-=' * 35)

sleep(4)

# Times em ordem alfabética
print(Fore.MAGENTA + '📋 Times em ordem alfabética:')
for time in sorted(brasileirao):
    print(Fore.WHITE + f'- {time}')

print(Fore.YELLOW + '-=' * 35)

sleep(4)

# Posição específica
time_busca = 'Corinthians'
posicao = brasileirao.index(time_busca) + 1
print(Fore.BLUE + f'🔎 O {time_busca} está na {posicao}ª posição.')
'''
