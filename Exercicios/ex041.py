nasc = int(input('Digite o ano de nascimento: '))
idade = 2025 - nasc

if idade <= 9:
    print('Até 9 anos: Mirim! Sua idade é de {}'.format(idade))
elif idade <= 14:
    print('Até 14 anos: Infantil! Sua idade é de {}'.format(idade))
elif idade <= 19:
    print('Até 19 anos: Junior! Sua idade é de {}'.format(idade))
elif idade <= 20:
    print('Até 20 anos: Sênior! Sua idade é de {}'.format(idade))
else:
    print('Acima de 20 anos: Master! Sua idade é de {}'.format(idade))