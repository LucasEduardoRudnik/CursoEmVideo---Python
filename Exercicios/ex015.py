quantidade_rodado = float(input('Quantidade de km rodados: '))
dias_alugados = float(input('Quantidade de dias alugados: '))

preco = (quantidade_rodado * 0.15) + (dias_alugados * 60)

print ('O valor total do aluguel do carro é de: {} R$'.format(preco))