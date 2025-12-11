matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))   
print('-=-' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()




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
'''