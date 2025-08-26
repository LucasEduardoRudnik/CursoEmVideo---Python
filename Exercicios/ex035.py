r1 = float(input('Primeiro lado do triângulo: '))
r2 = float(input('Segundo lado do triângulo: '))
r3 = float(input('Terceiro lado do triângulo: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os 3 lados podem formar um triângulo')
else:
    print('Os 3 lados não podem formar um triângulo')