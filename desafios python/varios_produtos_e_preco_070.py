total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')







'''
from time import sleep

# Cores ANSI
verde = '\033[32m'
vermelho = '\033[31m'
amarelo = '\033[33m'
azul = '\033[34m'
ciano = '\033[36m'
reset = '\033[m'

print(ciano + '=-=-=-=- BARATÃO DA ECONOMIA =-=-=-=-=' + reset)
sleep(0.5)

total = 0
mais1000 = 0
menor_preco = None
nome_menor_preco = ""

while True:
    print(azul + '\n--- NOVO PRODUTO ---' + reset)
    nome = input(ciano + 'Nome do Produto: ' + reset).strip()

    # VALIDAÇÃO DE PREÇO
    while True:
        valor_str = input(ciano + 'Valor em R$: ' + reset).strip()
        if valor_str.isdigit():
            valor = int(valor_str)
            break
        print(vermelho + 'Valor inválido! Digite apenas números inteiros.' + reset)

    # TOTAL GASTO
    total += valor

    # PRODUTOS ACIMA DE 1000
    if valor >= 1000:
        mais1000 += 1

    # PRODUTO MAIS BARATO
    if menor_preco is None or valor < menor_preco:
        menor_preco = valor
        nome_menor_preco = nome

    print(verde + '\nProduto cadastrado com sucesso!' + reset)
    sleep(0.4)

    # VALIDAÇÃO DE CONTINUAÇÃO
    resposta = input(amarelo + 'Quer continuar [S/N]? ' + reset).strip().upper()
    while resposta not in 'SN':
        print(vermelho + 'Resposta inválida! Digite apenas S ou N.' + reset)
        resposta = input(amarelo + 'Quer continuar [S/N]? ' + reset).strip().upper()

    if resposta == 'N':
        print(vermelho + '\nEncerrando cadastro...' + reset)
        sleep(0.7)
        break

# RESULTADO FINAL
print(ciano + '\n===== RESULTADO FINAL =====' + reset)
sleep(0.5)
print(f'{azul}Total gasto: {verde}R$ {total}{reset}')
print(f'{azul}Produtos que custam mais de R$1000: {verde}{mais1000}{reset}')
print(f'{azul}Produto mais barato: {verde}{nome_menor_preco} (R$ {menor_preco}){reset}')
print(ciano + '============================' + reset)
'''