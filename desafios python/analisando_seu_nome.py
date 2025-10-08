#nome = input("Digite seu nome completo: ")

#print("Analisando seu nome...")

#print("Seu nome em maiúsculas é: ", nome.upper())

#print("Seu nome em minúsculas é: ", nome.lower())

#print("Seu nome tem ao todo: ", len(nome) - nome.count(" "), "Letras")

#print("Seu primeiro nome é: ", nome.split()[0])

#print("Seu primeiro nome tem: ", len(nome.split()[0]), "Letras")

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

