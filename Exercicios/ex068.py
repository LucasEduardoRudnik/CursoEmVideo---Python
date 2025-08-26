import random
count = 0

print('VAMOS JOGAR PAR OU ÍMPAR ?')

while True:
    numero_user = int(input('Digite um valor: '))
    escolha_user = str(input('Par ou Ímpar [P / I]? ')).strip().upper()
    numero_comp = random.randint(1, 10)
    numero_total = numero_user + numero_comp
    print(f'Você jogou {numero_user} e o computador jogou {numero_comp}')
    print(f'O total foi de {numero_total}')
    if numero_total % 2 == 0:
        if escolha_user == 'P':
            print('Parabéns, você venceu!')
            count += 1
        elif escolha_user == 'I':
            print('O computador venceu!')
            print(f'Você venceu {count} vezes')
            break
    if numero_total % 2 != 0:
        if escolha_user == 'P':
            print('O computador venceu!')
            print(f'Você venceu {count} vezes')
            break
        elif escolha_user == 'I':
            print('Parabéns, você venceu!')
            count += 1
print('FIM DO PROGRAMA!')