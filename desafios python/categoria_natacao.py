from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')



'''
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

def interpretar_data(data_str):
    formatos = ["%d/%m/%Y", "%d.%m.%Y", "%d%m%Y"]
    for formato in formatos:
        try:
            return datetime.strptime(data_str, formato)
        except ValueError:
            continue
    return None

data_str = input("Informe sua data de nascimento (ex: XX/XX/XXXX, XX.XX.XXXX ou XXMMYYYY): ")
nascimento = interpretar_data(data_str)

if nascimento:
    hoje = datetime.now()
    idade = hoje.year - nascimento.year
    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
        idade -= 1

    # Determina a categoria
    if idade <= 9:
        categoria = "Mirim"
        cor = Fore.CYAN
    elif idade <= 14:
        categoria = "Infantil"
        cor = Fore.BLUE
    elif idade <= 20:
        categoria = "Sênior"
        cor = Fore.YELLOW
    else:
        categoria = "Master"
        cor = Fore.GREEN

    print(cor + f"\nVocê tem {idade} anos. E está na categoria {categoria}.")
else:
    print(Fore.RED + "Data inválida! Tente novamente com o formato correto.")
'''