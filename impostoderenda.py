salario = 0

entrada = input("Digite o salário do colaborador: R$ ")
entrada = entrada.replace(',', '.')  # Substitui vírgula por ponto
try:
    salario = float(entrada)

    if salario <= 2259.20:
        print("O colaborador é isento de pagar o Imposto de Renda.")
        print(f"Salário à receber = R$ {salario:.2f}")

    elif salario <= 2826.65:
        print("O colaborador deve pagar 7,5% de Imposto de Renda que equivale a R$ 169,44.")
        print(f"Salário à receber = R$ {(salario - 169.44):.2f}")

    elif salario <= 3751.05:
        print("O colaborador deve pagar 15% de Imposto de Renda que equivale a R$ 381,44.")
        print(f"Salário à receber = R$ {(salario - 381.44):.2f}")

    elif salario <= 4664.68:
        print("O colaborador deve pagar 22,5% de Imposto de Renda que equivale a R$ 662,77.")
        print(f"Salário à receber = R$ {(salario - 662.77):.2f}")

    else:
        print("O colaborador deve pagar 27,5% de Imposto de Renda que equivale a R$ 896,00.")
        print(f"Salário à receber = R$ {(salario - 896.00):.2f}")

except ValueError:
    print("Entrada inválida. Por favor, digite um número válido.")
