n = int(input('Digite um valor pra verificar o fatorial: '))
original = n
fatorial = 1

while n > 0:
    fatorial *= n
    n -= 1
print('O fatorial de {} é o seguinte: {}!'.format(original, fatorial))