import math

angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo,seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo,tangente))



###############################

#import math

#angulo = float(input("Digite um ângulo em graus: "))

#radianos = math.radians(angulo)

#seno = math.sin(radianos)
#cosseno = math.cos(radianos)
#tangente = math.tan(radianos)

#print(f"O ângulo de {angulo}° tem:")
#print(f"→ Seno: {seno:.4f}")
#print(f"→ Cosseno: {cosseno:.4f}")
#print(f"→ Tangente: {tangente:.4f}")
