núm = [[], []]
valor = 0 
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-=' * 30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')




'''
# Códigos ANSI para cores
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AZUL = "\033[94m"
AMARELO = "\033[93m"
RESET = "\033[0m"

valores = [[], []]  # índice 0 = pares, índice 1 = ímpares

for c in range(7):
    num = int(input(f"{AZUL}🔢 Digite o {c+1}º valor: {RESET}"))
    if num % 2 == 0:
        valores[0].append(num)  # pares
    else:
        valores[1].append(num)  # ímpares

print(f"\n{VERDE}✅ Cadastro concluído!{RESET}")
print("-=" * 30)

print(f"{AMARELO}✨ Os valores pares digitados foram:{RESET} {sorted(valores[0])} {VERDE}⚖️{RESET}")
print(f"{VERMELHO}✨ Os valores ímpares digitados foram:{RESET} {sorted(valores[1])} {AZUL}🎯{RESET}")
'''