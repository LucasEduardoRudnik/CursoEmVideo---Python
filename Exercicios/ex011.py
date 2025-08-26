altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura

print ('Sua parede tem a dimensão de {}x{}.\nA área da sua parede é de {} metros quadrados' .format(altura, largura, area))

tinta = area / 2

print ('Você precisa de {} Litros de tinta para pintar a parede.'.format(tinta))