print('=' * 30)
print('{:^30}'.format('BANCO CHAMBERS'))
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0

while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1   # aqui garantimos que o programa use notas de R$1
        totcéd = 0
        if total == 0:
            break

print('=' * 30)
print('Volte Sempre ao BANCO CHAMBERS. Tenha um bom dia!')








'''
from time import sleep

# Cores ANSI
verde = '\033[32m'
vermelho = '\033[31m'
amarelo = '\033[33m'
azul = '\033[34m'
ciano = '\033[36m'
reset = '\033[m'

print(ciano + "╔══════════════════════════════════╗")
print("║      SIMULADOR DE SAQUE CBR      ║")
print("╚══════════════════════════════════╝" + reset)
sleep(0.7)

# Validação do valor
while True:
    valor_str = input(ciano + "Digite o valor que deseja sacar: R$ " + reset).strip()
    if valor_str.isdigit():
        valor = int(valor_str)
        if valor > 0:
            break
    print(vermelho + "Valor inválido! Digite um número inteiro positivo." + reset)

sleep(0.5)
print(amarelo + "\nProcessando saque..." + reset)
sleep(1)

# Inicializando variáveis
cedulas50 = cedulas20 = cedulas10 = 0
valor_original = valor  # guardar valor para exibir depois

# Cálculos
cedulas50 = valor // 50
valor = valor % 50

cedulas20 = valor // 20
valor = valor % 20

cedulas10 = valor // 10
valor = valor % 10

cedulas1 = valor // 1
valor = valor % 1

# Resultado
print(azul + f"\n=== Notas para sacar R$ {valor_original} ===" + reset)

if cedulas50 > 0:
    print(verde + f"{cedulas50} nota(s) de R$50" + reset)

if cedulas20 > 0:
    print(verde + f"{cedulas20} nota(s) de R$20" + reset)

if cedulas10 > 0:
    print(verde + f"{cedulas10} nota(s) de R$10" + reset)

else:
    print(verde + f"{cedulas1} nota(s) de R$1" + reset)

# Caso não seja possível sacar exatamente
if valor != 0:
    print(vermelho + "\nNão é possível sacar esse valor com as cédulas disponíveis." + reset)

print(ciano + "\nObrigado por usar o Caixa Eletrônico!" + reset)
sleep(0.5)
print(ciano + "Tenha um ótimo dia!" + reset)
'''