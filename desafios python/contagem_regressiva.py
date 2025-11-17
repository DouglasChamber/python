from time import sleep

for count in range(10, -1, -1):
    print(count)
    sleep(0.5)
print('POW! POW! BOOM!')

'''
from time import sleep
from colorama import Fore, Style

for c in range(10, 0, -1):
    # Alterna cores conforme o número
    if c % 2 == 0:
        print(Fore.YELLOW + f"⏳ {c}" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + f"🎇 {c}" + Style.RESET_ALL)
    sleep(1)

print(Fore.CYAN + "🥳 FELIZ ANO NOVO!!! 🎆🎉" + Style.RESET_ALL)
'''