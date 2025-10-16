a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))


'''
import time

print('=-=- 🔢 Verificador de maior e menor número =-=-')

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

print('⏳ Analisando os valores...')
time.sleep(2)

# Se quiser mostrar com casas decimais (ex.: 10.5)
print('⬆️ O maior valor digitado foi: {:.1f}'.format(maior))
print('⬇️ O menor valor digitado foi: {:.1f}'.format(menor))

# Se quiser mostrar apenas número inteiro (mesmo que o usuário digite quebrado)
print('\nVersão em inteiro:')
print(f'⬆️ O maior valor digitado foi: {int(maior)}')
print(f'⬇️ O menor valor digitado foi: {int(menor)}')

print("\n🏁 --FIM--")
'''