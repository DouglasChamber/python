salário = float(input('Digite o salário do funcionário: R$ '))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)

print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora.'.format(salário, novo))



'''
import time

nome = str(input('Digite seu nome: '))
salario = int(input('Olá, {}, seja bem vindo(a), nos informe seu salário: R$'.format(nome)))

print('Analisando o salário de {}...'.format(nome))
time.sleep(1)

print('Analisando o salário...')
time.sleep(1)

if salario >= 1250:
    novo = salario + (salario * 10/100)
else:
    novo = salario + (salario * 15/100)

print('O salário de {} com o aumento será de R${:.2f}'.format(nome, novo))
print('FIM')
'''