num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] Converter para Binário
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua Opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num) [2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num) [2:]))
elif opção == 3:
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)))
else:
    print('Opção Inválida. Tente Novamente!')


'''
from colorama import Fore, Style

print(Fore.CYAN + "🔢 Conversor de Bases Numéricas" + Style.RESET_ALL)

numero = int(input("🧠 Digite um Número Inteiro: "))

print("\n 📌 Escolha a Base de Conversão: ")
print("1️⃣ - Binário")
print("2️⃣ - Octal")
print("3️⃣ - Hexadecimal")
opção = int(input("👉 Sua opção: "))

if opção == 1:
    print(Fore.GREEN + f"📦 Binário: {bin(numero)[2:]}" + Style.RESET_ALL)
    
elif opção == 2:
    print(Fore.YELLOW + f"📦 Octal: {oct(numero)[2:]}" + Style.RESET_ALL)

elif opção == 3:
    print(Fore.MAGENTA + f"📦 Binário: {hex(numero)[2:]. upper()}" + Style.RESET_ALL)

else:
    print(Fore.RED + "❌ OPÇÃO INVÁLIDA. Escolha 1, 2 ou 3." + Style.RESET_ALL)
'''