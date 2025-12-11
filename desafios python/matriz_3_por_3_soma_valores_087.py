matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[1][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda coluna é {mai}')

'''
# Códigos ANSI para cores
VERDE = "\033[92m"
AZUL = "\033[94m"
AMARELO = "\033[93m"
RESET = "\033[0m"

# Criando a matriz 3x3
matriz = [[], [], []]

for i in range(3):  # linhas
    for j in range(3):  # colunas
        valor = int(input(f"{AZUL}🔢 Digite o valor para a posição [{i}, {j}]: {RESET}"))
        matriz[i].append(valor)

print(f"\n{VERDE}✅ Matriz 3x3 preenchida:{RESET}\n")

# Impressão formatada
for linha in matriz:
    for elemento in linha:
        print(f"{AMARELO}[ {elemento:^3} ]{RESET}", end=" ")
    print()  # quebra de linha
print()  # linha em branco após a matriz

# A) Soma de todos os valores pares
soma_pares = 0
for linha in matriz:
    for elemento in linha:
        if elemento % 2 == 0:
            soma_pares += elemento
print(f"{VERDE}➕ A soma de todos os valores pares é: {soma_pares}{RESET}")

# B) Soma dos valores da terceira coluna
soma_3col = sum(matriz[i][2] for i in range(3))
print(f"{VERDE}📊 A soma dos valores da 3ª coluna é: {soma_3col}{RESET}")

# C) Maior valor da segunda coluna
maior_2col = max(matriz[i][1] for i in range(3))
print(f"{VERDE}🏆 O maior valor da 2ª coluna é: {maior_2col}{RESET}")
'''