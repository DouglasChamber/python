maior = 0.0
menor = 0.0

for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso lido foi {:.2f} kg'.format(maior))
print('O menor peso lido foi {:.2f} kg'.format(menor))



    


'''
from colorama import Fore, Style
from time import sleep

maior = 0
menor = 0

print(Fore.YELLOW + "⚖️ Verificação de pesos\n" + Style.RESET_ALL)

for i in range(1, 6):
    peso = float(input(Fore.CYAN + f"➡️ Digite o peso da {i}ª pessoa (kg): " + Style.RESET_ALL))
    sleep(0.3)  # efeito de pausa para dar mais interatividade
    
    if i == 1:  # inicializa maior e menor com o primeiro peso
        maior = peso
        menor = peso
        print(Fore.GREEN + f"✅ Primeiro peso registrado: {peso} kg" + Style.RESET_ALL)
    else:
        if peso > maior:
            maior = peso
            print(Fore.GREEN + f"⬆️ Novo maior peso encontrado: {peso} kg" + Style.RESET_ALL)
        elif peso < menor:
            menor = peso
            print(Fore.RED + f"⬇️ Novo menor peso encontrado: {peso} kg" + Style.RESET_ALL)
        else:
            print(Fore.MAGENTA + f"ℹ️ Peso registrado: {peso} kg" + Style.RESET_ALL)

print(Fore.BLUE + "\n📊 Resultado final:" + Style.RESET_ALL)
print(Fore.GREEN + f"👉 O maior peso lido foi {maior} kg" + Style.RESET_ALL)
print(Fore.RED + f"👉 O menor peso lido foi {menor} kg" + Style.RESET_ALL)
print(Fore.MAGENTA + "\n🎉 FIM da verificação!" + Style.RESET_ALL)
'''