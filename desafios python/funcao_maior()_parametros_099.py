from time import sleep
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

def maior(*numeros):
    print(f'\n{Fore.CYAN}{Style.BRIGHT}-= Analisando os valores passados =-{Style.RESET_ALL}')
    
    if len(numeros) == 0:
        print(f'{Fore.RED}Nenhum valor foi informado.{Style.RESET_ALL}')
        return
    
    # Mostra os números com pausa
    for n in numeros:
        print(Fore.YELLOW + str(n), end=' ', flush=True)
        sleep(0.5)  # pausa de meio segundo entre cada número
    
    print(f'\n{Fore.GREEN}Foram informados {len(numeros)} valores ao todo.{Style.RESET_ALL}')
    sleep(0.5)
    print(f'{Fore.MAGENTA}{Style.BRIGHT}O maior valor informado foi {max(numeros)}.{Style.RESET_ALL}')
    sleep(0.5)


# Programa Principal
print(f'{Fore.BLUE}{Style.BRIGHT}=== Demonstração da Função maior() ==={Style.RESET_ALL}')

# Testes fixos
maior(2, 9, 4, 5, 7, 1)
maior(8, 3, 10)
maior(1, 2)
maior()

