p1 = int(input('Digite o ano de seu nascimento: '))
p2 = int(input('Digite o ano de seu nascimento: '))
p3 = int(input('Digite o ano de seu nascimento: '))
p4 = int(input('Digite o ano de seu nascimento: '))
p5 = int(input('Digite o ano de seu nascimento: '))
p6 = int(input('Digite o ano de seu nascimento: '))
p7 = int(input('Digite o ano de seu nascimento: '))

anos = [p1, p2, p3, p4, p5, p6, p7]

soma = 0

for maioridade in anos:
    maioridade = 2025 - maioridade
    if maioridade >= 18:
        soma += 1
print('{} são maiores de idade!'.format(soma))