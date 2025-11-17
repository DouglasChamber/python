soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números PARES e a soma foi {}' .format(cont, soma))


'''
from colorama import Fore, Style
from time import sleep

soma = 0
contador = 0

print(Fore.YELLOW + "🔢 Digite seis números inteiros:\n" + Style.RESET_ALL)

for c in range(6):
    n = int(input(Fore.CYAN + f"➡️ Número {c+1}: " + Style.RESET_ALL))
    if n % 2 == 0:   # verifica se é par
        soma += n
        contador += 1
        print(Fore.GREEN + f"✅ {n} é par! Soma parcial: {soma}" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"❌ {n} é ímpar, desconsiderado." + Style.RESET_ALL)
    sleep(0.3)

print(Fore.MAGENTA + f"\n📊 Resultado final: A soma dos {contador} números pares é {soma}" + Style.RESET_ALL)
print(Fore.BLUE + "🎉 FIM 🎉" + Style.RESET_ALL)
'''