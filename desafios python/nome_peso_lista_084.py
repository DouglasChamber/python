temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp in ['N', 'NAO', 'NÃO']:
        break

print('-='*30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai} kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men} kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()


'''
# Códigos ANSI para cores
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AZUL = "\033[94m"
AMARELO = "\033[93m"
RESET = "\033[0m"

dados = []
while True:
    nome = str(input(f"{AZUL}📝 Nome Completo: {RESET}"))
    peso = float(input(f"{AZUL}⚖️ Peso (kg): {RESET}"))
    dados.append([nome, peso])
    resposta = str(input(f"{AMARELO}👉 Quer Continuar? [S/N] {RESET}")).strip().upper()
    if resposta in ['N', 'NAO', 'NÃO']:
        break

# Inicializa maior e menor com o primeiro peso
maiorpeso = menorpeso = dados[0][1]

# Descobre maior e menor peso
for p in dados:
    if p[1] > maiorpeso:
        maiorpeso = p[1]
    if p[1] < menorpeso:
        menorpeso = p[1]

print(f"\n{VERDE}📊 Ao todo, foram cadastradas {len(dados)} pessoas.{RESET}")

print(f"{VERMELHO}💪 O maior peso foi de {maiorpeso} kg. Peso de:{RESET} ", end='')
for p in dados:
    if p[1] == maiorpeso:
        print(f"[{p[0]} 🏋️] ", end='')
print()  # quebra de linha

print(f"{AZUL}🪶 O menor peso foi de {menorpeso} kg. Peso de:{RESET} ", end='')
for p in dados:
    if p[1] == menorpeso:
        print(f"[{p[0]} 🌸] ", end='')
print()  # quebra de linha
'''