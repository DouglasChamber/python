peso = float(input('Qual é seu peso? (Kg): '))
altura = float(input('Qual é sua altura? (m): '))
imc = peso / (altura ** 2)

print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30: 
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')


'''
from colorama import Fore, Style, init
import re

init(autoreset=True)

print("🏋️‍♂️ Calculadora de IMC 🧮")

def interpretar_peso(peso_str):
    peso_str = peso_str.lower().replace("kg", "").strip()
    return float(peso_str)

def interpretar_altura(altura_str):
    altura_str = altura_str.replace(",", ".").strip()
    altura_str = re.sub(r"[^\d.]", "", altura_str)  # remove letras e símbolos
    if "." in altura_str:
        return float(altura_str)
    elif len(altura_str) == 3:
        return float(altura_str) / 100  # ex: 175 → 1.75
    elif len(altura_str) == 2:
        return float(altura_str) / 10   # ex: 17 → 1.7
    else:
        return float(altura_str)

peso_input = input("Digite seu peso: ")
altura_input = input("Digite sua altura: ")

try:
    peso = interpretar_peso(peso_input)
    altura = interpretar_altura(altura_input)

    imc = peso / (altura ** 2)
    print(f"\n📊 Seu IMC é: {imc:.2f}")

    # Classificação com cor e emoji
    if imc < 18.5:
        print(Fore.YELLOW + "⚠️ Você está abaixo do peso.")
    elif 18.5 <= imc < 25:
        print(Fore.GREEN + "✅ Peso normal. Parabéns!")
    elif 25 <= imc < 30:
        print(Fore.MAGENTA + "📈 Sobrepeso. Atenção à saúde.")
    elif 30 <= imc < 35:
        print(Fore.RED + "🚨 Obesidade grau I.")
    elif 35 <= imc < 40:
        print(Fore.RED + "🚨 Obesidade grau II (severa).")
    else:
        print(Fore.RED + "🚨 Obesidade grau III (mórbida). Cuide-se!")

except ValueError:
    print(Fore.RED + "❌ Entrada inválida! Verifique se digitou números corretamente.")
'''