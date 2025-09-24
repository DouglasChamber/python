n1 = int(input('Digite um número inteiro: '))

tabuada = ''
for i in range(1, 11):
    tabuada += f'{n1} x {i} = {n1 * i}\n'

print(f'A tabuada de {n1} é:\n{tabuada}')
