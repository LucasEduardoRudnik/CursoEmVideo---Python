n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2

if media >= 70:
    print('Você passou, parabéns, sua média foi de: {}.'.format(media))
elif media >= 50 and media <= 69:
    print('Você está de recuperação, sua média foi de: {}.'.format(media))
else:
    print('Sua média foi abaixo do esperado, você reprovou, com uma média de {}.'.format(media))