count = 1
r = 0

while True:
    n = int(input('Digite o valor da tabuada [Negativo para parar]: '))
    if n < 0:
        break
    while count <= 10:
        r = n * count
        print(f'{n} x {count} = {r}')
        count += 1
    count = 1
print('Fim do programa!')