from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), 
           randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')


'''
import random
import time
from colorama import Fore, Style, init

# Inicializa o Colorama
init(autoreset=True)

print(Fore.YELLOW + Style.BRIGHT + '-=' * 20)
print(Fore.GREEN + Style.BRIGHT + '🎲 SORTEIO DE NÚMEROS ALEATÓRIOS 🎲')
print(Fore.YELLOW + Style.BRIGHT + '-=' * 20)

# Gera 5 números aleatórios entre 1 e 100
numeros = tuple(random.randint(1, 100) for _ in range(5))

# Exibe os números sorteados um por um com pausa
print(Fore.CYAN + 'Os números sorteados foram:')
for n in numeros:
    print(Fore.WHITE + f'→ {n}')
    time.sleep(1)  # pausa de 1 segundo entre cada número

time.sleep(2)  # pausa maior antes das estatísticas
print(Fore.YELLOW + '-=' * 20)

# Estatísticas
menor = min(numeros)
maior = max(numeros)
media = sum(numeros) / len(numeros)

print(Fore.RED + f'📉 O menor número sorteado foi: {menor}')
time.sleep(1)
print(Fore.BLUE + f'📈 O maior número sorteado foi: {maior}')
time.sleep(1)
print(Fore.MAGENTA + f'📊 A média dos números sorteados é: {media:.2f}')

time.sleep(2)
print(Fore.YELLOW + '-=' * 20)

# Números em ordem crescente
print(Fore.GREEN + '📋 Números em ordem crescente:')
print(sorted(numeros))
'''