listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}:')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
print('=-' * 30)





'''
# Programa para ler 5 valores e mostrar maior e menor com suas posições

num = []

# Entrada de dados com mensagens mais claras
for i in range(5):
    valor = int(input(f'Digite o {i+1}º valor: '))
    num.append(valor)

print('-=' * 30)
print(f'Você digitou os valores: {num}')

# Maior valor
maior = max(num)
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}... ', end='')

# Menor valor
menor = min(num)
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}... ', end='')

print('\n' + '-=' * 30)
'''