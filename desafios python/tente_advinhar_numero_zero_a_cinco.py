from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' *20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}!'.format(computador, jogador))
#import random
#n = int(input('Tente advinhar o número que estou pensando, entre 0 e 5: '))
#m = random.randint(0, 5)
#if n == m:
#    print('Parabéns! Você conseguiu advinhar o número que eu pensei!')
#else:
#    print('Que pena! Você não conseguiu advinhar o número que eu pensei. Eu pensei no número {} e não no número {}!'.format(m, n))
#print('--FIM--')