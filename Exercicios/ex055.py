peso1 = float(input('Digite o primeiro peso: '))
peso2 = float(input('Digite o segundo peso: '))
peso3 = float(input('Digite o terceiro peso: '))
peso4 = float(input('Digite o quarto peso: '))
peso5 = float(input('Digite o quinto peso: '))

pesos = [peso1, peso2, peso3, peso4, peso5]

peso_maior = pesos[0]
peso_menor = pesos[0]

for peso in pesos:
    if peso > peso_maior:
        peso_maior = peso
    if peso < peso_menor:
        peso_menor = peso

print('O maior peso é {} e o menor peso é {}'.format(peso_maior, peso_menor))
