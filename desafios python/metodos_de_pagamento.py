print('{:=^40}'.format(' LOJAS CHAMBERS '))
preço = float(input('Preço das Compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))

if opção == 1:
    total = preço - (preço * 10 / 100)
    print('Sua compra era R${:.2f} e vai custar R${:.2f} com 10% de desconto.'.format(preço, total))
elif opção == 2:
    total = preço - (preço * 5 / 100)
    print('Sua compra era R${:.2f} e vai custar R${:.2f} com 5% de desconto.'.format(preço, total))
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(parcela))
    print('Valor total: R${:.2f}'.format(total))
elif opção == 4:
    totparc = int(input('Quantas parcelas? '))
    total = preço + (preço * 20 / 100)
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(totparc, parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente.')




'''
from colorama import Fore, Style, init

init(autoreset=True)

def calcular_valor_final(preco, forma_pagamento, parcelas):
     
    if forma_pagamento == "1":
        valor_final = preco * 0.90 
    elif forma_pagamento == "2":
        valor_final = preco * 0.95 
    elif forma_pagamento == "3":
        if parcelas <= 2:
            valor_final = preco 
        else:
            valor_final = preco * 1.20 
    else:
        valor_final = preco 

    return valor_final


print(Fore.CYAN + "🛒 Calculadora de Pagamento de Produto")

preco = float(input(Style.RESET_ALL + "Digite o preço do produto: R$ "))

print("\nEscolha a forma de pagamento:")
print("1 - À vista (dinheiro ou pix)")
print("2 - À vista no cartão (débito ou crédito)")
print("3 - Parcelado no cartão de crédito")

forma_pagamento = input("Digite o número da opção escolhida: ")

parcelas = 1
if forma_pagamento == "3":
    parcelas = int(input("Digite o número de parcelas: "))

valor_final = calcular_valor_final(preco, forma_pagamento, parcelas)

print(Fore.GREEN + f"\n💰 Valor final a ser pago: R$ {valor_final:.2f}")
'''