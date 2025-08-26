from random import shuffle
aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
aluno4 = input('Digite o nome do aluno: ')

escolha_aluno = ([aluno1, aluno2, aluno3, aluno4])
shuffle(escolha_aluno)

print('A ordem de apresentação é: {}'.format(escolha_aluno))