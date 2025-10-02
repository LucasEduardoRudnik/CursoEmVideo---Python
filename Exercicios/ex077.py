palavras = ('COMPUTADOR', 'MOUSE', 'CPU', 'TECLADO', 'FONE DE OUVIDO', 'MONITOR')
vogais = 'AEIOU'

for palavra in palavras:
  vogais_na_palavra = []
  
  for letra in palavra:
    if letra in vogais:
      vogais_na_palavra.append(letra)

  print(f'A palavra {palavra} tem as seguintes vogais: {vogais_na_palavra}')