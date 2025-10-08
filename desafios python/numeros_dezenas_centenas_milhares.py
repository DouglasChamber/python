#numero = int(input("Digite um número de 1 a 9999: "))
#print("Analisando o número {}...".format(numero))
#unidade = numero // 1 % 10
#dezena = numero // 10 % 10
#centena = numero // 100 % 10
#milhar = numero // 1000 % 10
#print('Unidade: {}'.format(unidade))
#print('Dezena: {}'.format(dezena))
#print('Centena: {}'.format(centena))
#print('Milhar: {}'.format(milhar))


num = int(input('Informe um número de 1 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))