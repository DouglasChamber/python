from random import shuffle
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)

################################

#import random

#nome1 = input("Digite o nome da primeira pessoa: ")
#nome2 = input("Digite o nome da segunda pessoa: ")
#nome3 = input("Digite o nome da terceira pessoa: ")
#nome4 = input("Digite o nome da quarta pessoa: ")

#lista_nomes = [nome1, nome2, nome3, nome4]

#random.shuffle(lista_nomes)

#print("\n📢 Ordem de apresentação:")
#for i, nome in enumerate(lista_nomes, start=1):
#    print(f"{i}º - {nome}")
