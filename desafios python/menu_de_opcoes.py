from time import sleep

n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opção = 0
while opção != 5:
    print('''
          [1] Somar
          [2] Multiplicar
          [3] Maior
          [4] Novos Números
          [5] Sair do Programa
          ''')
    opção = int(input('>>>>> Qual é a sua opção?' ))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opção == 5:
        print('Finalizando... Até logo!')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
        





'''
from time import sleep

# Códigos ANSI para cores
VERDE = '\033[92m'
VERMELHO = '\033[91m'
AMARELO = '\033[93m'
AZUL = '\033[94m'
RESET = '\033[0m'

n1 = int(input(AZUL + 'Digite o primeiro número: ' + RESET))
n2 = int(input(AZUL + 'Digite o segundo número: ' + RESET))

opcao = 0
while opcao != 5:
    print(f"""\n{AMARELO}=== MENU DE OPÇÕES ==={RESET}
    [1] ➕ Somar
    [2] ✖️ Multiplicar
    [3] 🔝 Maior
    [4] 🔄 Novos números
    [5] 🚪 Sair do programa""")
    
    opcao = int(input(AZUL + 'Sua opção: ' + RESET))
    
    if opcao == 1:
        sleep(1)
        print(VERDE + f'A soma entre {n1} e {n2} é {n1 + n2}' + RESET)
    elif opcao == 2:
        sleep(1)
        print(VERDE + f'A multiplicação entre {n1} e {n2} é {n1 * n2}' + RESET)
    elif opcao == 3:
        sleep(1)
        if n1 > n2:
            print(VERDE + f'O maior número é {n1}' + RESET)
        elif n2 > n1:
            print(VERDE + f'O maior número é {n2}' + RESET)
        else:
            print(AMARELO + 'Os dois números são iguais!' + RESET)
    elif opcao == 4:
        n1 = int(input(AZUL + 'Digite o primeiro número: ' + RESET))
        n2 = int(input(AZUL + 'Digite o segundo número: ' + RESET))
    elif opcao == 5:
        sleep(1)
        print(VERMELHO + 'Finalizando programa... Até logo! 👋' + RESET)
    else:
        sleep(1)
        print(VERMELHO + 'Opção inválida. Tente novamente.' + RESET)

print(AZUL + 'Programa encerrado.' + RESET)
'''