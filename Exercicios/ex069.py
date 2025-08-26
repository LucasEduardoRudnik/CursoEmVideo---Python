count_idade = 0
count_homem = 0
count_mulher = 0
while True:
    print('CADASTRO DE PESSOA')
    nome = str(input('Qual o seu nome? '))
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual o seu sexo [M/F]? ')).strip().upper()

    if idade > 18:
        count_idade += 1
    if sexo == 'M':
        count_homem += 1
    if sexo == 'F' and idade < 20:
        count_mulher += 1

    escolha = str(input('Você deseja continuar [S/N]?: ').strip().upper())
    if escolha == 'N':
        break

print(f'Foram cadastradas {count_idade} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {count_homem} homens')
print(f'Foram cadastradas {count_mulher} mulheres com menos de 20 anos.')