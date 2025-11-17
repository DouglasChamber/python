num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')


'''
from colorama import Fore, Style
from time import sleep

c = int(input(Fore.YELLOW + "🔢 Digite um número inteiro: " + Style.RESET_ALL))

print(Fore.CYAN + f"\n🔎 Verificando se {c} é primo..." + Style.RESET_ALL)
sleep(1)

if c < 2:
    print(Fore.RED + f"❌ O número {c} não é primo." + Style.RESET_ALL)
else:
    for i in range(2, int(c**0.5) + 1):
        if c % i == 0:
            print(Fore.RED + f"❌ O número {c} não é primo, pois é divisível por {i}." + Style.RESET_ALL)
            break
    else:
        print(Fore.GREEN + f"✅ O número {c} é primo!" + Style.RESET_ALL)

print(Fore.MAGENTA + "\n🎉 FIM da verificação!" + Style.RESET_ALL)
'''