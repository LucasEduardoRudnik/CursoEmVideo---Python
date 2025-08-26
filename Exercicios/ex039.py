ano_nasc = int(input('Informe o seu ano de nascimento: '))
idade = 2025 - ano_nasc

if idade > 18:
    print('Você já se alistou no exército!')
elif idade == 18:
    print('Você deve se alistar este ano!')
else:
    print('Você ainda não está na idade para se alistar!')