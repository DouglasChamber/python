from datetime import date

atual = date.today().year

sexo = input('''Você é do sexo MASCULINO ou FEMININO:
    [ M ] - MASCULINO
    [ F ] - FEMININO 
Qual a sua opção: ''').strip().upper()

if sexo == 'M':
    print('Bem-vindo ao serviço militar brasileiro.')
elif sexo == 'F':
    print('O serviço militar não é obrigatório para o sexo feminino.')
    exit()
else:
    print('Opção inválida.')
    exit()

nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(f'Ainda faltam {saldo} ano(s) para o alistamento.')
    print(f'Seu alistamento será em {ano}.')
else:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Você já deveria ter se alistado há {saldo} ano(s).')
    print(f'Seu alistamento foi em {ano}.')

'''
from datetime import datetime
from colorama import Fore, init

init(autoreset=True)

def interpretar_data(data_str):
    formatos = ["%d/%m/%Y", "%d.%m.%Y", "%d%m%Y"]
    for formato in formatos:
        try:
            return datetime.strptime(data_str, formato)
        except ValueError:
            continue
    return None

data_str = input("Informe sua data de nascimento (ex: XX/XX/XXXX, XX.XX.XXXX ou XXXX): ")
nascimento = interpretar_data(data_str)

if nascimento:
    hoje = datetime.now()
    idade = hoje.year - nascimento.year
    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
        idade -= 1

    print(f"\nVocê tem {idade} anos.")

    if idade < 18:
        print(Fore.YELLOW + f"Ainda faltam {18 - idade} anos para o alistamento.")
    elif idade == 18:
        print(Fore.GREEN + "Você está na idade de se alistar! Procure a junta militar mais próxima.")
    else:
        print(Fore.RED + f"Você já passou da idade de alistamento há {idade - 18} anos.")
else:
    print(Fore.RED + "Formato de data inválido! Tente usar: xx/xx/xxxx, xx.xx.xxxx ou xxxxxxxx.")
'''