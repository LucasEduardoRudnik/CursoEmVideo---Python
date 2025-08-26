print('Segue abaixo a soma de todos os números ímpares que são múltiplos de três!')
soma = 0
for s in range(1, 501):
    if s % 3 == 0 and s % 2 != 0:
            soma += s
print(soma)
print('FIM!')