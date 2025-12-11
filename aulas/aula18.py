galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])  # Adiciona uma cópia da lista dado em galera
    dado.clear() # Limpa a lista dado para a próxima iteração

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade. ')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade. ')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade. ')


'''
galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])  # Adiciona uma cópia da lista dado em galera
    dado.clear()  # Limpa a lista dado para a próxima iteração

print(galera)
'''

'''
galera = [['Chambers', 32], ['Douglas', 22], ['Ana', 19], ['Júlia', 21]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade. ')
'''

'''
teste = list()
teste.append('Chambers')
teste.append(32)
galera = list()
galera.append(teste[:]) # Faz uma cópia da lista teste
teste[0] = 'Douglas'
teste[1] = 22
galera.append(teste[:])
print(galera)
'''