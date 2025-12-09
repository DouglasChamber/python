números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Não será adicionado.')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r == 'N':
        break
print('=-=' * 20)
números.sort()
print(f'Você digitou os valores {números}')

'''
num = []

while True:
    valor = int(input('Digite um valor: '))
    if valor not in num:
        num.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não será adicionado.')

    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

print('=-=' * 20)
print(f'Você digitou os valores únicos: {sorted(num)}')
print('=-=' * 20)
'''