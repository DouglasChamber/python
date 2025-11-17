num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x{:2} = {}' .format(num, c, num*c))

'''
from time import sleep
from colorama import Fore, Style

n = int(input(Fore.YELLOW + 'Digite um número para ver sua tabuada: ' + Style.RESET_ALL))

print(Fore.CYAN + f"\n📊 Tabuada do {n}\n" + Style.RESET_ALL)

for i in range(1, 11):
    print(Fore.GREEN + f"{n} x {i:2} = {n*i}" + Style.RESET_ALL)
    sleep(0.5)

print(Fore.MAGENTA + "\n🎉 FIM 🎉" + Style.RESET_ALL)
'''