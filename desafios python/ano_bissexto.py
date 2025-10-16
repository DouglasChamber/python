from datetime import date

ano = int(input('Digite um ano qualquer e descubra se é ano bissexto: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO'.format(ano))


'''
import time

ano = int(input('Digite um ano qualquer e descubra se é ano bissexto: '))
print('Analisando o ano {}...'.format(ano))
time.sleep(2)
if (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
    print('✅ O ano bissexto é {}'.format(ano))
else:
    print('❌ O ano {} não é bissexto'.format(ano))
    '''