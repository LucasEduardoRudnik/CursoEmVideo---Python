n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))

if (n1 > n2 and n1 > n3):
    print('{} é o maior valor'.format(n1))
elif (n2 > n1 and n2 > n3):
    print('{} é o maior valor'.format(n2))
else:
    print('{} é o maior valor'.format(n3))

if (n1 < n2 and n1 < n3):
    print('{} é o menor valor'.format(n1))
elif (n2 < n1 and n2 < n3):
    print('{} é o menor valor'.format(n2))
else:
    print('{} é o menor valor'.format(n3))