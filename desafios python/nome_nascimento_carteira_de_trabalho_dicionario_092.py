from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - nasc)
print('-=' * 20)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')


'''
from datetime import datetime

# 🎨 Códigos de cores ANSI
VERDE = '\033[92m'
VERMELHO = '\033[91m'
AZUL = '\033[94m'
AMARELO = '\033[93m'
RESET = '\033[0m'

# Ano atual para calcular idade
ano_atual = datetime.now().year

# Entrada de dados
print(f"{AZUL}📝 Cadastro de Funcionário{RESET}\n")
nome = str(input(f"{AMARELO}👤 Nome: {RESET}"))
ano_nasc = int(input(f"{AMARELO}🎂 Ano de nascimento: {RESET}"))
ctps = int(input(f"{AMARELO}💼 Carteira de Trabalho (0 se não tiver): {RESET}"))

# Criação do dicionário
pessoa = {
    "nome": nome,
    "idade": ano_atual - ano_nasc,
    "ctps": ctps
}

# Se tiver carteira de trabalho
if ctps != 0:
    ano_contratacao = int(input(f"{AMARELO}📅 Ano de contratação: {RESET}"))
    salario = float(input(f"{AMARELO}💰 Salário: R$ {RESET}"))
    
    pessoa["ano_contratacao"] = ano_contratacao
    pessoa["salario"] = salario
    
    # Tempo de contribuição até aposentadoria (35 anos)
    aposentadoria = (ano_contratacao + 35) - ano_nasc
    pessoa["aposentadoria"] = aposentadoria

# Exibição dos dados
print(f"\n{AZUL}📋 Cadastro Final{RESET}")
print(f"{'-'*30}")
for k, v in pessoa.items():
    emoji = "👤" if k == "nome" else "🎂" if k == "idade" else "💼" if k == "ctps" \
        else "📅" if k == "ano_contratacao" else "💰" if k == "salario" else "🛑"
    print(f"{emoji} {k.capitalize()}: {VERDE}{v}{RESET}")
'''