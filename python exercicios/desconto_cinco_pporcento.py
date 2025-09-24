n1 = int(input('Digite o valor da compra: '))
desconto = n1 * 0.05
valor_final = n1 - desconto
print('O valor com 5% de desconto é R${:.2f}'.format(valor_final))