somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print(f"----- {p}ª PESSOA -----")
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade

    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome

    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo == 'F' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade:.1f} anos.')
print(f'O homem mais velho é {nomevelho} com {maioridadehomem} anos.')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')


'''
soma_idade = 0
homem_mais_velho = ""
idade_homem_mais_velho = 0
mulheres_menos_20 = 0

for i in range(1, 5):
    print(f"\n--- Pessoa {i} ---")
    nome = input("Digite o nome: ").strip()
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo [M/F]: ").strip().upper()

    soma_idade += idade

    # Verifica homem mais velho
    if sexo == "M":
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            homem_mais_velho = nome

    # Verifica mulheres com menos de 20 anos
    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1

# Média de idade
media = soma_idade / 4

print("\n📊 RESULTADOS 📊")
print(f"➡️ A média de idade do grupo é {media:.1f} anos.")
if homem_mais_velho != "":
    print(f"➡️ O homem mais velho é {homem_mais_velho}, com {idade_homem_mais_velho} anos.")
else:
    print("➡️ Não há homens no grupo.")
print(f"➡️ Há {mulheres_menos_20} mulheres com menos de 20 anos.")
'''