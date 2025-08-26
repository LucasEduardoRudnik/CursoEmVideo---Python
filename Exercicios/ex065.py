soma = 0
contador = 0
escolha = 'S'.strip().upper()
lista = []
while escolha == 'S':
    n = int(input('Digite um valor: '))
    lista.append(n)
    soma += n
    contador += 1
    escolha = input('Deseja continuar? [S/N] ').strip().upper()

media = soma / contador
print('Você inseriu {} números!'.format(contador))
print('A média dos números digitados foi de {}!'.format(media))
print('O maior número digitado foi {} e o menor foi {}.'.format(max(lista), min(lista)))