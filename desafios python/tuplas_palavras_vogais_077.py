palavras = (
    'lapis',
    'borracha',
    'caderno',
    'estojo',
    'transferidor',
    'compasso',
    'mochila',
    'canetas',
    'livro',
    'papel')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')


'''
import time
from colorama import Fore, Style, init

# Inicializa o Colorama
init(autoreset=True)

palavras = (
    'lapis',
    'borracha',
    'caderno',
    'estojo',
    'transferidor',
    'compasso',
    'mochila',
    'canetas',
    'livro',
    'papel'
)

# Definindo cores para cada vogal
cores_vogais = {
    'a': Fore.RED,
    'e': Fore.BLUE,
    'i': Fore.GREEN,
    'o': Fore.MAGENTA,
    'u': Fore.CYAN
}

for palavra in palavras:
    print(Fore.YELLOW + f'\nNa palavra {palavra.upper()} temos ', end='')
    time.sleep(0.5)
    for letra in palavra:
        if letra.lower() in 'aeiou':
            cor = cores_vogais[letra.lower()]
            print(cor + letra, end=' ')
            time.sleep(0.3)  # pausa para dar efeito de revelação
print(Fore.YELLOW + '\n\n✅ Fim da análise de palavras!')
'''