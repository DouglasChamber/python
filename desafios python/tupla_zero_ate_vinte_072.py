cont = ('zero', 'um', 'dois', 'tres', 'quatro', 
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez' ,'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito', 
        'dezenove', 'vinte')
while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        print(f'Você digitou o número {cont[núm]}')
    else:
        print('Número inválido. Tente novamente!')
        continue

    resp = input('Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break
    





'''
from colorama import Fore, Style, init

# Inicializa o Colorama
init(autoreset=True)

# Tupla com os números por extenso
contagem = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
    'dezoito', 'dezenove', 'vinte'
)

while True:
    try:
        numero = int(input(Fore.CYAN + 'Digite um número entre 0 e 20: '))
        if 0 <= numero <= 20:
            break
        print(Fore.RED + 'Número inválido. Tente novamente!')
    except ValueError:
        print(Fore.RED + 'Entrada inválida! Digite apenas números.')

print(Fore.GREEN + f'Você digitou o número {Style.BRIGHT}{contagem[numero]}')
'''