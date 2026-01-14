def área(larg, comp):
    a = larg * comp
    print(f'A àrea de um terreno {larg}x{comp} é de {a}m²')

print('=== Calculadora de Terrenos ===')
print('-' * 32)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)

'''
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

def area(largura, comprimento):
    resultado = largura * comprimento
    perimetro = 2 * (largura + comprimento)
    print(f'\n{Fore.CYAN}📐 Dimensões do terreno: {Fore.YELLOW}{largura}m x {comprimento}m')
    print(f'{Fore.GREEN}➡️  Área total: {resultado} m²')
    print(f'{Fore.MAGENTA}➡️  Perímetro: {perimetro} m')

# Programa Principal
print(f'{Fore.BLUE}{Style.BRIGHT}=== Calculadora de Terrenos ==={Style.RESET_ALL}')
while True:
    largura = float(input(f'\n{Fore.YELLOW}Digite a largura (m): {Style.RESET_ALL}'))
    comprimento = float(input(f'{Fore.YELLOW}Digite o comprimento (m): {Style.RESET_ALL}'))
    area(largura, comprimento)

    continuar = input(f'\n{Fore.CYAN}Deseja calcular outro terreno? (s/n): {Style.RESET_ALL}').lower()
    if continuar != 's':
        print(f'\n{Fore.RED}{Style.BRIGHT}Encerrando programa. Obrigado por usar a calculadora!{Style.RESET_ALL}')
        break
'''
