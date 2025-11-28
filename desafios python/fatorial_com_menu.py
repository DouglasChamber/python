print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ➡ '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))




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

# Exibe o processo de multiplicação inicial
while c > 0:
    print(f"{VERDE}{fatorial} x {c} = {fatorial * c}{RESET}")
    fatorial *= c
    c -= 1
    sleep(0.5)

print(VERDE + f"\n🎉 Resultado final: {n}! = {fatorial}" + RESET)

# Pergunta se o usuário quer continuar mostrando mais termos
while True:
    termos = int(input(AMARELO + "\nQuantos termos adicionais deseja mostrar? (Digite 0 para encerrar): " + RESET))
    if termos == 0:
        print(VERMELHO + "Encerrando o programa... Até logo! 👋" + RESET)
        break
    else:
        # Animação de carregamento
        print(AZUL + "\n⏳ Processando", end="")
        for _ in range(3):
            sleep(0.5)
            print(".", end="")
        print(RESET)

        print(AZUL + f"\n📌 Mostrando mais {termos} termos da sequência do fatorial..." + RESET)
        sleep(1)
        extra = n + 1  # começa a partir do próximo número
        for i in range(extra, extra + termos):
            fatorial *= i
            print(f"{VERDE}{fatorial // i} x {i} = {fatorial}{RESET}")
            sleep(0.5)
        n += termos  # atualiza o último número mostrado
        print(VERDE + f"\n✅ Agora temos {n}! = {fatorial}" + RESET)
'''