vel = int(input('Qual a velocidade do carro? '))
multa = (vel - 80) * 7

if(vel > 80):
    print('Sua velocidade ultrapassou 80km/h e você foi multado')
    print('Sua velocidade era de {}km/h'.format(vel))
    print('Sua multa será no valor de {}R$'.format(multa))
else:
    print('Você estava a {}km/h e não ultrapassou o limite da via, prossiga viagem!'.format(vel))