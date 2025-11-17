from colorama import Fore, Style
from time import sleep

# Entrada de dados
primeiro = int(input(Fore.YELLOW + "Digite o primeiro termo da PA: " + Style.RESET_ALL))
razao = int(input(Fore.CYAN + "Digite a razão da PA: " + Style.RESET_ALL))

print(Fore.MAGENTA + f"\n📊 Os 10 primeiros termos da PA (primeiro={primeiro}, razão={razao}):\n" + Style.RESET_ALL)

# Laço para mostrar os 10 termos
for i in range(10):
    termo = primeiro + i * razao
    print(Fore.GREEN + f"✨ Termo {i+1}: {termo}" + Style.RESET_ALL)
    sleep(0.3)  # efeito de animação

print(Fore.BLUE + "\n🎉 FIM da Progressão Aritmética!" + Style.RESET_ALL)
