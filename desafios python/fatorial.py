print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ➡ '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')



'''
from time import sleep

# Códigos ANSI para cores
VERDE = '\033[92m'
VERMELHO = '\033[91m'
AMARELO = '\033[93m'
AZUL = '\033[94m'
RESET = '\033[0m'

print(AZUL + "=== Calculadora de Fatorial ===" + RESET)
n = int(input(AMARELO + 'Digite um número para calcular o fatorial: ' + RESET))

fatorial = 1
c = n

print(AZUL + f"\n🔢 Calculando {n}! passo a passo..." + RESET)
sleep(1)

# Exibe o processo de multiplicação
while c > 0:
    print(f"{VERDE}{fatorial} x {c} = {fatorial * c}{RESET}")
    fatorial *= c
    c -= 1
    sleep(0.5)

print(VERDE + f"\n🎉 Resultado final: {n}! = {fatorial}" + RESET)
print(AZUL + "=== Fim da execução ===" + RESET)
'''