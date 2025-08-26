sal = float(input('Digite o valor do seu salário: '))

if sal > 1250.00:
    aumento = sal * 0.10
    sal_real = sal + aumento
    print('Seu novo salário é de R$ {}!'.format(sal_real))
else:
    aumento = sal * 0.15
    sal_real = sal + aumento
    print('Seu novo salário é de R$ {}!'.format(sal_real))