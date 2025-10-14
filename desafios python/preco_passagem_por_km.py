distancia = float(input('Qual é a distância da sua viagem em Km? '))
print('Você está prestes a começar uma viagem de {}Km'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preco da sua passagem será de R${:.2f}'.format(preco))


#import time

#while True:
#    print("🚍" + "====-====" *5 + "🚍")
#    distancia = float(input("📏 Qual a distância da sua viagem em Km? "))

#    print("====-====" *5)
#    print("Calculando o preço da sua passagem... ⏳")
#    time.sleep(1.5)  # simula processamento

#    if distancia <= 200:
#        preco = distancia * 0.50
#    else:
#        preco = distancia * 0.45

#    print(f"💰 O preço da sua passagem é R${preco:.2f}")
#    print("====-====" *5)

    # Pergunta se o usuário quer continuar
#    repetir = input("🔄 Deseja calcular outra passagem? (s/n): ").strip().lower()
#    if repetir != "s":
#        print("👋 Obrigado por usar o sistema de cálculo de passagens! Boa viagem! ✈️🚗🚍")
#        break
#    print("====-====" *5)