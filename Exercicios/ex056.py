soma = 0
mulheres = 0

nome_homem_maior = ''
idade_homem_maior = -1
nome_homem_menor = ''
idade_homem_menor = None

for i in range(4):
    print('Pessoa {}'.format(i+1))

    nome = input('Digite seu nome: ').strip()
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo (M/F): ').strip().upper()

    soma += idade

    if sexo == 'M':
        if idade > idade_homem_maior:
            idade_homem_maior = idade
            nome_homem_maior = nome

        if idade_homem_menor is None or idade < idade_homem_menor:
            idade_homem_menor = idade
            nome_homem_menor = nome

    if sexo == 'F' and idade < 20:
        mulheres += 1

media = soma / 4

print('A média de idade do grupo foi de: {:.1f} anos!'.format(media))
if nome_homem_maior:
    print('O homem mais velho do grupo é: {} ({} anos)!'.format(nome_homem_maior, idade_homem_maior))
    print('O homem mais novo do grupo é: {} ({} anos)!'.format(nome_homem_menor, idade_homem_menor))
else:
    print('Não houve homens no grupo.')
print('Existem {} mulheres com menos de 20 anos'.format(mulheres))
