from math import hypot

co = float(input('comprimento  do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente:' ))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))


###############################

#import math

#cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
#cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

#hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

#print(f"A hipotenusa do triângulo é {hipotenusa:.2f}")

###############################

#co = float(input('comprumento do cateto oposto: '))

#ca = float(input('comprimento do cateto adjacente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('A hipotenusa vai medir {}'.format(hi))