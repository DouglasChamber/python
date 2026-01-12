from time import sleep
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1

    # Corrige o passo se for incoerente com a direção
    if inicio < fim and passo < 0:
        passo = -passo
    elif inicio > fim and passo > 0:
        passo = -passo

    print(f'{Fore.CYAN}{Style.BRIGHT}Contando de {inicio} até {fim} de {abs(passo)} em {abs(passo)}:{Style.RESET_ALL}')

    for i in range(inicio, fim + (1 if passo > 0 else -1), passo):
        print(Fore.YELLOW + str(i), end=' ', flush=True)
        sleep(0.3)  # pausa para dar efeito de contagem
    print(f'\n{Fore.MAGENTA}{Style.BRIGHT}Fim da contagem!\n{Style.RESET_ALL}')


# Programa Principal
print(f'{Fore.GREEN}{Style.BRIGHT}=== Demonstração da Função contador() ==={Style.RESET_ALL}\n')

print(f'{Fore.BLUE}A) Contagem de 1 até 10, de 1 em 1:{Style.RESET_ALL}')
contador(1, 10, 1)

print(f'{Fore.BLUE}B) Contagem de 10 até 0, de 2 em 2:{Style.RESET_ALL}')
contador(10, 0, -2)

print(f'{Fore.BLUE}C) Contagem personalizada:{Style.RESET_ALL}')
inicio = int(input(Fore.YELLOW + 'Início: ' + Style.RESET_ALL))
fim = int(input(Fore.YELLOW + 'Fim: ' + Style.RESET_ALL))
passo = int(input(Fore.YELLOW + 'Passo: ' + Style.RESET_ALL))
contador(inicio, fim, passo)
