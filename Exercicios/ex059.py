v1 = float(input('Insira o primeiro valor: '))
v2 = float(input('Insira o segundo valor: '))

soma = 0
multiplicar = 0
maior = 0

print("""Escolha abaixo qual operação você deseja prosseguir.
[1] Somar!
[2] Multiplicar!
[3] Maior!
[4] Novos números!
[5] Sair do programa!""")

escolha = int(input('Digite sua escolha de operação: '))

while escolha != 5:

    if escolha == 1:
        soma = v1 + v2
        print('A soma dos dois valores digitados é: {}'.format(soma))
    elif escolha == 2:
        multiplicar = v1 * v2
        print('A multiplicação dos dois valores digitados é: {}'.format(multiplicar))
    elif escolha == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('O maior valor digitado foi {}'.format(maior))
    elif escolha == 4:
        v1 = float(input('Insira o primeiro valor: '))
        v2 = float(input('Insira o segundo valor: '))
    print('A operação desejada foi concluída, selecione a nova operação novamente e prossiga com o programa abaixo!')
    escolha = int(input('Digite novamente a escolha de operação: '))
print('Você decidiu deixar o programa, até a próxima :)')
print('Fim!')