from random import choice
aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
aluno4 = input('Digite o nome do aluno: ')

escolha_aluno = choice([aluno1, aluno2, aluno3, aluno4])

print('O aluno escolhido para apagar o quadro foi: {}'.format(escolha_aluno))