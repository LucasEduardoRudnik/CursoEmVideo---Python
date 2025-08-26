frase = str(input('Digite sua frase: ')).upper().strip()
print('A frase possuí {} a'.format(frase.count('A')))
print('A primeira ocorrência é na posição {}'.format(frase.find('A')+1))
print('A ultima ocorrência é na posição {}'.format(frase.rfind('A')+1))