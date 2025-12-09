expr = str(input('Digite a expressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão está correta!')
else:
    print('A expressão está incorreta!')
    

'''
# Função para verificar se os parênteses estão corretos
def verifica_parenteses(expressao):
    pilha = []  # usamos uma lista como pilha

    for caractere in expressao:
        if caractere == "(":
            pilha.append(caractere)  # empilha quando encontra um "("
        elif caractere == ")":
            if len(pilha) > 0:
                pilha.pop()  # desempilha quando encontra um ")"
            else:
                return False  # há um ")" sem correspondente "("

    # se a pilha estiver vazia, todos os parênteses foram fechados corretamente
    return len(pilha) == 0


# Programa principal
exp = input("Digite uma expressão: ")

if verifica_parenteses(exp):
    print("A expressão está correta!")
else:
    print("A expressão está incorreta!")
'''