frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')



'''
from colorama import Fore, Style
from time import sleep

# Entrada de dados
frase = input(Fore.YELLOW + "✍️ Digite uma frase: " + Style.RESET_ALL)

print(Fore.CYAN + "\n🔎 Analisando a frase..." + Style.RESET_ALL)
sleep(1)

# Remove espaços e coloca em minúsculo
frase_limpa = frase.replace(" ", "").lower()

# Verificação
if frase_limpa == frase_limpa[::-1]:
    print(Fore.GREEN + f"✅ A frase '{frase}' é um Palíndromo!" + Style.RESET_ALL)
else:
    print(Fore.RED + f"❌ A frase '{frase}' não é um Palíndromo." + Style.RESET_ALL)

print(Fore.MAGENTA + "\n🎉 FIM da verificação!" + Style.RESET_ALL)
'''