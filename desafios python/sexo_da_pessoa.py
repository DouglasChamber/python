sexo = str(input('Informae seu Sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados Inválidos. Por favor, informe seu sexo')).strip().upper()[0]
print('Sexo {} registrado com Sucesso.'.format(sexo))

'''
sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
while sexo not in ('M', 'F'):
    sexo = str(input('Dados inválidos. Por favor, digite seu sexo [M/F]: ')).strip().upper()
print('Sexo {} registrado com sucesso.'.format(sexo))
'''