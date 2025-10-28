n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')






'''
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.BLUE + "Digite dois números:")

numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))


if numero1 < numero2:
    print(Fore.GREEN + f"Seu primeiro número ({numero1}) é menor que o segundo número ({numero2}).")

elif numero2 < numero1:
    print(Fore.RED + f"Seu segundo número ({numero2}) é menor que o primeiro número ({numero1}).")

else:
    print(Fore.YELLOW + f"Seus números são IGUAIS.\nPrimeiro Número: {numero1}\nSegundo Número: {numero2}")
'''