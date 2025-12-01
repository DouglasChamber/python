tot18 = totH = totM20 = 0
while True: 
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')





'''
from time import sleep

# Cores ANSI
verde = '\033[32m'
vermelho = '\033[31m'
amarelo = '\033[33m'
azul = '\033[34m'
ciano = '\033[36m'
reset = '\033[m'

print(ciano + '=-=-=-=- CADASTRO DE PESSOAS =-=-=-=-=' + reset)
sleep(0.5)

mais18 = homens = mulheresmenos20 = 0

while True:
    print(azul + '\n--- Nova Pessoa ---' + reset)
    nome = str(input(ciano + 'Nome: ' + reset)).strip()
    idade = int(input(ciano + 'Idade: ' + reset))

    # Loop de validação do sexo
    sexo = str(input(ciano + 'Sexo [M/F]: ' + reset)).strip().upper()
    while sexo not in 'MF':
        print(vermelho + f'{sexo} inválido! Digite apenas M ou F.' + reset)
        sexo = str(input(ciano + 'Sexo [M/F]: ' + reset)).strip().upper()

    # Processamento
    if idade >= 18:
        mais18 += 1

    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheresmenos20 += 1

    print(verde + '\nCadastro realizado com sucesso!' + reset)
    sleep(0.5)

    # Loop de validação do "continuar"
    resposta = str(input(amarelo + 'Quer continuar [S/N]? ' + reset)).strip().upper()
    while resposta not in 'SN':
        print(vermelho + f'{resposta} inválido! Digite apenas S ou N.' + reset)
        resposta = str(input(amarelo + 'Quer continuar [S/N]? ' + reset)).strip().upper()

    if resposta == 'N':
        print(vermelho + '\nEncerrando cadastro...' + reset)
        sleep(0.7)
        break

# Resultado final
print(ciano + '\n===== RESULTADO FINAL =====' + reset)
sleep(0.5)
print(f'{azul}Pessoas com 18 anos ou mais: {verde}{mais18}{reset}')
print(f'{azul}Homens cadastrados: {verde}{homens}{reset}')
print(f'{azul}Mulheres com menos de 20 anos: {verde}{mulheresmenos20}{reset}')
print(ciano + '============================' + reset)

'''