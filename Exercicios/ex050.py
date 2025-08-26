n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
n4 = int(input('Digite o quarto valor: '))
n5 = int(input('Digite o quinto valor: '))
n6 = int(input('Digite o sexto valor: '))

valores = [n1, n2, n3, n4, n5, n6]
soma = 0

for n in valores:
    if n % 2 == 0:
        soma += n
print('A soma dos valores pares foi de {}!'.format(soma))
print('FIM!')