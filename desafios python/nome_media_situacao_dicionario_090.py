aluno = dict()
aluno['nome'] = str(input('Nome do Aluno: '))
aluno['Média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print()
print('-=' * 20)
print()
print(f'{"-= DADOS DO ALUNO =-":^40}')
print()
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')



'''
# Códigos de cores ANSI
VERDE = '\033[92m'
VERMELHO = '\033[91m'
AZUL = '\033[94m'
AMARELO = '\033[93m'
RESET = '\033[0m'

# Entrada de dados
nome = str(input(f'{AZUL}📝 Nome: {RESET}'))
media = float(input(f'{AZUL}📊 Média de {nome}: {RESET}'))

# Situação com cores e emojis
situacao = f'{VERDE}✅ Aprovado{RESET}' if media >= 7 else f'{VERMELHO}❌ Reprovado{RESET}'

# Dicionário
aluno = {'nome': nome, 'media': media, 'situacao': situacao}

# Saída formatada
print("\n🎓 Resultado Final")
print(f'{AMARELO}👤 Nome: {RESET}{aluno["nome"]}')
print(f'{AMARELO}📈 Média: {RESET}{aluno["media"]:.2f}')
print(f'{AMARELO}📌 Situação: {RESET}{aluno["situacao"]}')
'''