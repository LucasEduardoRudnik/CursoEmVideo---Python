import math

cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))

print('A hipotenusa do triângulo retângulo é: {}'.format(math.hypot(cateto_oposto, cateto_adjacente)))