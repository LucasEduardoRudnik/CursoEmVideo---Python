sexo = input('Insira o sexo da pessoa [M]/[F]: ').strip().upper()
while sexo != 'M' and sexo != 'F':
    print('Realize a digitação novamente do sexo da pessoa.')
    sexo = input('Insira o sexo da pessoa [M]/[F]: ')
print('O sexo da pessoa é {}!'.format(sexo))
print('Fim!')