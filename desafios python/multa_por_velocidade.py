velocidade = float(input('Qual é a velocidade atual do carro?'))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')



#import time

#velocidade = float(input('Qual é a velocidade atual do carro? km/h: '))
#if velocidade > 80:
#    excesso = velocidade - 80
#    multa = excesso * 7
#    time.sleep(2)
#    print('=-=' *18)
#    print(f"Você foi multado! 🚨")
#    print(f"Velocidade registrada: {velocidade:.1f} Km/h")
#    print(f"Excedeu o limite em {excesso:.1f} Km/h")
#    print(f"Valor da multa: R${multa:.2f}")
#    print('=-=' *18)
#else:
#    print('=-=' *18)
#    print("Velocidade dentro do limite. Boa viagem! ✅")
#    print('Dirija com segurança! 🚗💨')
#    print('=-=' *18)
#print('--FIM--')