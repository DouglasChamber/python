soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
        
print('A soma de todos os {} números ímpares múltiplos de 3 entre 1 e 500 é {}'.format(soma, cont))

'''
from colorama import Fore, Style
from time import sleep

print(Fore.YELLOW + "🔢 Vamos calcular a soma dos números ímpares múltiplos de 3 entre 1 e 500!" + Style.RESET_ALL)
sleep(1)

soma = 0
contador = 0

for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        soma += c
        contador += 1
        # Mostra uma pequena barra de progresso
        print(Fore.GREEN + f"✨ Somando {c}... Soma parcial: {soma}" + Style.RESET_ALL)
        sleep(0.05)

print(Fore.CYAN + f"\n✅ Soma final: {soma}" + Style.RESET_ALL)
print(Fore.MAGENTA + f"📊 Total de números somados: {contador}" + Style.RESET_ALL)
print(Fore.BLUE + "🎉 FIM" + Style.RESET_ALL)
'''