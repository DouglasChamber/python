lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('-=-' * 20)
print(f'Os valores digitados em ordem foram: {lista}')


'''
# 🎨 Programa com cores e emojis
# ANSI: \033[cor m ... \033[m

num = []

for i in range(5):
    valor = int(input(f'\033[36m🔢 Digite o {i+1}º valor: \033[m'))
    # Inserir o valor na posição correta para manter a lista ordenada
    if i == 0 or valor > num[-1]:
        num.append(valor)
        print(f'\033[32m✅ Adicionado ao final da lista.\033[m')
    else:
        for j in range(len(num)):
            if valor <= num[j]:
                num.insert(j, valor)
                print(f'\033[33m📍 Adicionado na posição {j} da lista.\033[m')
                break

print('\033[35m' + '=-=' * 20 + '\033[m')
print(f'\033[34m📊 Os valores digitados em ordem foram: {num}\033[m')
print('\033[35m' + '=-=' * 20 + '\033[m')
'''