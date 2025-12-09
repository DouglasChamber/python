a = [2, 3, 4, 7]
b = a[:]  # Cria uma cópia da lista a em b
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')



'''
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
'''



'''
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
'''


'''
num = [2, 3, 5, 1, 4]
num[2] = 3
num.append(3)
num.sort()
num.insert(2, 2)
if 5 in num:
    num.remove(3)
else:
    print('Não achei o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos.')
'''