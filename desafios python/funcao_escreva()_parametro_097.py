def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

escreva('Douglas Chambers')
escreva('Curso de Python')
escreva('CWB')

'''
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

def escreva(texto, moldura='~', cor=Fore.CYAN):
    tamanho = len(texto) + 4
    print(cor + moldura * tamanho)
    print(cor + f'  {texto}  ')
    print(cor + moldura * tamanho)

# Programa Principal
print(f'{Fore.GREEN}{Style.BRIGHT}=== Função escreva personalizada ==={Style.RESET_ALL}\n')

escreva('Olá, Mundo!', moldura='*', cor=Fore.YELLOW)
escreva('Curso de Python', moldura='-', cor=Fore.MAGENTA)
escreva('Função escreva() adaptável', moldura='=', cor=Fore.BLUE)
escreva('Desafio concluído!', moldura='#', cor=Fore.RED)
'''