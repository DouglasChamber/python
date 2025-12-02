listagem = (
    'Lápis', 1.75,
    'Borracha', 2.00,
    'Caderno', 15.90,
    'Estojo', 25.00,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.90)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')
print('-' * 40)





'''
from colorama import Fore, Style, init
import time

# Inicializa o Colorama
init(autoreset=True)

listagem = (
    'Lápis', 1.75,
    'Borracha', 2.00,
    'Caderno', 15.90,
    'Estojo', 25.00,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.90
)

# Cabeçalho
print(Fore.YELLOW + Style.BRIGHT + '-' * 40)
print(Fore.GREEN + Style.BRIGHT + f'{"🛒 LISTAGEM DE PREÇOS 🛒":^40}')
print(Fore.YELLOW + Style.BRIGHT + '-' * 40)

# Corpo da tabela
for pos in range(0, len(listagem), 2):
    nome = listagem[pos]
    preco = listagem[pos + 1]
    time.sleep(0.5)  # pausa para dar efeito de leitura
    print(Fore.CYAN + f'{nome:.<30}' + Fore.WHITE + f'R$ {preco:>7.2f}')

# Rodapé
print(Fore.YELLOW + '-' * 40)
print(Fore.MAGENTA + Style.BRIGHT + '📋 Fim da listagem 📋')
print(Fore.YELLOW + '-' * 40)
'''