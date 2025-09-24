largura = float(input('Digite a largura da parede (em metros): '))
altura = float(input('Digite a altura da parede (em metros): '))

area = largura * altura
tinta = area / 2  # 1 litro para cada 2 m²

print(f'A parede tem {largura}m de largura e {altura}m de altura.')
print(f'Sua área é de {area:.2f} m².')
print(f'Você precisará de {tinta:.2f} litros de tinta para pintá-la.')
