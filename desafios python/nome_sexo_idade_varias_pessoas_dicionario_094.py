galera = []
pessoa = {}
soma = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']   # acumula idade
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer Continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 20)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista de pessoas que estão acima da média:')
for p in galera:
    if p['idade'] >= média:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')



'''
# 🎨 Códigos de cores ANSI para personalizar a saída
VERDE = '\033[92m'
VERMELHO = '\033[91m'
AZUL = '\033[94m'
AMARELO = '\033[93m'
RESET = '\033[0m'

pessoas = []  # Lista que vai guardar os dicionários
soma_idades = 0

print(f"{AZUL}📝 Cadastro de Pessoas{RESET}\n")

while True:
    pessoa = {}
    pessoa['nome'] = str(input(f"{AMARELO}👤 Nome: {RESET}"))
    pessoa['sexo'] = str(input(f"{AMARELO}⚧ Sexo [M/F]: {RESET}")).strip().upper()
    pessoa['idade'] = int(input(f"{AMARELO}🎂 Idade: {RESET}"))
    
    pessoas.append(pessoa.copy())  # Adiciona o dicionário à lista
    soma_idades += pessoa['idade']
    
    continuar = str(input(f"{AZUL}Deseja continuar? [S/N]: {RESET}")).strip().upper()
    if continuar == 'N':
        break

print(f"\n{VERDE}{'-=' * 30}{RESET}")

# A) Quantas pessoas foram cadastradas
print(f"{AMARELO}A){RESET} Total de pessoas cadastradas: {VERDE}{len(pessoas)}{RESET}")

# B) Média de idade
media = soma_idades / len(pessoas)
print(f"{AMARELO}B){RESET} Média de idade do grupo: {VERDE}{media:.2f}{RESET}")

# C) Lista com todas as mulheres
mulheres = [p['nome'] for p in pessoas if p['sexo'] == 'F']
print(f"{AMARELO}C){RESET} Mulheres cadastradas: {VERDE}{mulheres if mulheres else 'Nenhuma'}{RESET}")

# D) Pessoas com idade acima da média
acima_media = [p['nome'] for p in pessoas if p['idade'] > media]
print(f"{AMARELO}D){RESET} Pessoas com idade acima da média: {VERDE}{acima_media if acima_media else 'Nenhuma'}{RESET}")

print(f"{VERDE}{'-=' * 30}{RESET}")
'''