n = 0
contador = 0
soma = 0
n = int(input('Digite um número inteiro [999 Para Parar]: '))
while n != 999:
    soma += n
    contador += 1
    n = int(input('Digite um número inteiro [999 Para Parar]: '))
print('Você digitou {} números!'.format(contador))
print('A soma dos {} números foi de {}!'.format(contador, soma))
print('Fim!')