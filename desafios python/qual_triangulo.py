print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')

'''
import time

print('🔺 Verificador de Triângulos 🔺')

a = float(input('Digite o comprimento de um dos lados: '))
b = float(input('Digite o comprimento de outro lado: '))
c = float(input('Digite o comprimento do último lado: '))

print("\n⏳ Analisando os valores...\n")
time.sleep(2)

if a < b + c and b < a + c and c < a + b:
    print('✅ Os dados acima PODEM FORMAR um triângulo!')

    if a == b == c:
        print('🔺 EQUILÁTERO: Todos os lados iguais.')

    elif a == b or b == c or a == c:
        print('🔻 ISÓSCELES (dois lados iguais)')

    else: 
        print("▶️ Tipo: ESCALENO (todos os lados diferentes)")
else:
    print('❌ Os dados acima NÃO PODEM FORMAR um triângulo!')
'''