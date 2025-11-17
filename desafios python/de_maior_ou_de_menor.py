from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade =  atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E também tivemos {} pessoas menores de idade.'.format(totmenor))

'''
from datetime import date
from colorama import Fore, Style
from time import sleep

atual = date.today().year
maiores = 0
menores = 0

print(Fore.YELLOW + "🔢 Verificação de maioridade\n" + Style.RESET_ALL)

for i in range(1, 8):
    nasc = int(input(Fore.CYAN + f"➡️ Digite o ano de nascimento da {i}ª pessoa: " + Style.RESET_ALL))
    idade = atual - nasc
    sleep(0.3)  # efeito de pausa para dar mais interatividade
    
    if idade >= 18:
        maiores += 1
        print(Fore.GREEN + f"✅ Essa pessoa tem {idade} anos → MAIOR de idade!" + Style.RESET_ALL)
    else:
        menores += 1
        print(Fore.RED + f"❌ Essa pessoa tem {idade} anos → MENOR de idade." + Style.RESET_ALL)

print(Fore.MAGENTA + "\n📊 Resultado final:" + Style.RESET_ALL)
print(Fore.GREEN + f"👉 {maiores} pessoas são MAIORES de idade." + Style.RESET_ALL)
print(Fore.RED + f"👉 {menores} pessoas são MENORES de idade." + Style.RESET_ALL)
print(Fore.BLUE + "\n🎉 FIM da verificação!" + Style.RESET_ALL)
'''