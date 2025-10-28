nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
if 7 > média >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif média < 5:
    print('O aluno está REPROVADO.')
elif média >= 7:
    print('O aluno está APROVADO.')

'''
from colorama import Fore, Style, init

init(autoreset=True)

print("Bem-vindo ao Estudineitor. Verifique se passou de ano!")

# Exibe pergunta com cor, mas input sem cor
print(Fore.CYAN + "Digite seu Nome Completo:" + Style.RESET_ALL)
nome = str(input())

print(Fore.MAGENTA + "Digite sua média do primeiro semestre:" + Style.RESET_ALL)
nota1 = float(input())

print(Fore.MAGENTA + "Digite sua média do segundo semestre:" + Style.RESET_ALL)
nota2 = float(input())

# Calcula a média
resultado = (nota1 + nota2) / 2

# Exibe resultado com cor
if resultado <= 4.99:
    print(Fore.RED + f"{nome}, você ficou abaixo da média ({resultado:.2f}). ESTÁ DE RECUPERAÇÃO.")
elif resultado <= 6.99:
    print(Fore.YELLOW + f"{nome}, você ficou na média ({resultado:.2f}). PASSOU POR POUCO.")
else:
    print(Fore.GREEN + f"{nome}, você foi APROVADO! Sua média foi ({resultado:.2f}). PARABÉNS, PASSOU DE ANO!")
'''