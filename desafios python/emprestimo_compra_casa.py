casa = float(input('Valor da Casa: R$'))
salario = float(input('Salário do Comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 /100
print('Para pagar uma casa de R${:.2f} em {} anos.'.format(casa, anos), end='')
print(' A prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO! ')
else:
    print('Empréstimo NEGADO! ')


'''
from colorama import Fore, Style

print(Fore.CYAN + '🏠 Simulador de Empréstimo Bancário para Compra de Imóveis' + Style.RESET_ALL)

valor_casa = float(input('💰 Valor do Imóvel: R$ '))
salario = float(input('📄 Salário do Comprador: R$ '))
anos = int(input('📆 Em Quantos Anos Pretende Pagar: '))

if anos <= 0:
    print(Fore.RED + '❌ Número de anos inválido. Deve ser maior que ZERO.' + Style.RESET_ALL)
else:
    meses = anos * 12
    prestacao = valor_casa / meses
    limite = salario * 0.30

    print(f'\n📊 Prestação Mensal: R$ {prestacao:.2f}')
    print(f'📉 Limite Permitido (30% do Salário): R$ {limite:.2f}')

    if prestacao <= limite:
        print(Fore.GREEN + '✅ Empréstimo Aprovado! Parabéns pela nova conquista! 🏡' + Style.RESET_ALL)
    elif prestacao > limite:
        print(Fore.RED + '❌ Empréstimo Negado. A prestação excede os 30% do salário. 😞' + Style.RESET_ALL)
'''