distancia = float(input('Digite a distancia de sua viagem em km: '))

if (distancia <= 200):
    preco = distancia * 0.50
    print('O valor da passagem é de R${}'.format(preco))
else:
    preco = distancia * 0.45
    print('O valor da passagem é de R${}'.format(preco))