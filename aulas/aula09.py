frase = 'Curso em Vídeo Python'
print(frase.find('ola'))  # Retorna -1, pois não encontrou  

print(frase.find('Vídeo'))  # Retorna 9, pois encontrou a palavra Vídeo começando na posição 9
print(frase.lower().find('vídeo'))  # Retorna 9, pois encontrou a palavra vídeo começando na posição 9, ignorando o case sensitive      

print(frase.split())  # Retorna uma lista com as palavras da frase
print(frase.split()[2])  # Retorna a palavra na posição 2 da lista  

print(frase.replace('Python', 'Android'))  # Retorna a frase com a palavra Python substituída por Android
print(frase)  # A frase original permanece inalterada   

frase = frase.replace('Python', 'Android')  # Atribui a nova frase à variável frase
print(frase)  # Agora a frase foi alterada

print('Curso' in frase)  # Retorna True, pois a palavra Curso está na frase
print('curso' in frase)  # Retorna False, pois a palavra curso (com c minúsculo) não está na frase
print('curso' in frase.lower())  # Retorna True, pois a palavra curso (com c minúsculo) está na frase, ignorando o case sensitive

print(frase.count('o'))  # Retorna 3, pois a letra o aparece 3 vezes na frase
print(frase.count('o', 0, 13))  # Retorna 1 

print(len(frase))  # Retorna 21, que é o tamanho da frase
print(len(frase.strip()))  # Retorna 21, que é o tamanho da frase, removendo espaços extras no início e no fim

print(frase.strip())  # Retorna a frase sem espaços extras no início e no fim
print(frase.lstrip())  # Retorna a frase sem espaços extras no início

print(frase.rstrip())  # Retorna a frase sem espaços extras no fim  

print(frase.upper())  # Retorna a frase toda em maiúsculas
print(frase.lower())  # Retorna a frase toda em minúsculas      

print(frase.capitalize())  # Retorna a frase com a primeira letra maiúscula e o resto minúsculo 

print(frase.title())  # Retorna a frase com a primeira letra de cada palavra maiúscula

print(frase.center(50))  # Retorna a frase centralizada em um campo de 50 caracteres
print(frase.ljust(50))  # Retorna a frase alinhada à esquerda em um campo de 50 caracteres

print(frase.rjust(50))  # Retorna a frase alinhada à direita em um campo de 50 caracteres

print(frase.zfill(50))  # Retorna a frase preenchida com zeros à esquerda até completar 50 caracteres

print(frase.split())  # Retorna uma lista com as palavras da frase
print(frase.split()[0])  # Retorna a primeira palavra da lista
