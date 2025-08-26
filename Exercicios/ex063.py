n = int(input('Digite o número de termos da Sequência de Fibonacci: '))

contador = 0
t1 = 0
t2 = 1

print(t1)
print(t2)

while contador < n:
    t3 = t1 + t2
    print(t3)
    t1 = t2
    t2 = t3
    contador += 1
print('Fim!')