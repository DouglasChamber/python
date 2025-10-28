r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os seguimentos acima NÃO PODEM formar um triângulo')



'''
from colorama import Fore, Style, init

init(autoreset=True)

print("🔺 Verificador de Triângulos 🔺")

lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        print(Fore.GREEN + "✅ Triângulo é EQUILÁTERO (todos os lados iguais) 🟩")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print(Fore.YELLOW + "⚠️ Triângulo é ISÓSCELES (dois lados iguais)🟨")
    else:
        print(Fore.CYAN + "🔷 Triângulo é ESCALENO (todos os lados diferentes) 🟦")
else:
    print(Fore.RED + "❌ Os lados informados não formam um triângulo 🚫")
'''