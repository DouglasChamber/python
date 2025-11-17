primeiro = int(input("Digite o primeiro termo da PA: "))
razão = int(input('Razão da PA: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end='-> ')
print('FIM')