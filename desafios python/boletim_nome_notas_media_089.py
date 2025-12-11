ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')





'''
# Códigos ANSI para cores
VERDE = "\033[92m"
AZUL = "\033[94m"
AMARELO = "\033[93m"
VERMELHO = "\033[91m"
RESET = "\033[0m"

# Lista principal
alunos = []

# Cadastro dos alunos
while True:
    nome = str(input(f"{AZUL}📝 Nome do aluno: {RESET}"))
    nota1 = float(input(f"{AZUL}📘 Primeira nota: {RESET}"))
    nota2 = float(input(f"{AZUL}📗 Segunda nota: {RESET}"))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    
    resp = str(input(f"{AMARELO}👉 Quer continuar? [S/N] {RESET}")).strip().upper()
    if resp in ['N', 'NAO', 'NÃO']:
        break

print(f"\n{VERDE}📊 BOLETIM FINAL{RESET}")
print("-=" * 30)
print(f"{'Nº':<4}{'NOME':<15}{'MÉDIA':>6}")
print("-" * 30)

# Mostra boletim com médias
for i, aluno in enumerate(alunos):
    print(f"{i:<4}{aluno[0]:<15}{aluno[2]:>6.1f}")

# Permite consultar notas individuais
while True:
    opc = int(input(f"\n{AZUL}🔍 Mostrar notas de qual aluno? (999 interrompe) {RESET}"))
    if opc == 999:
        print(f"{VERDE}✅ Encerrando consulta...{RESET}")
        break
    if 0 <= opc < len(alunos):
        print(f"{AMARELO}📘 Notas de {alunos[opc][0]}: {alunos[opc][1]}{RESET}")
    else:
        print(f"{VERMELHO}⚠️ Número inválido!{RESET}")
'''