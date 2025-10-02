numeros = ()
pares = ()
for count in range(4):
  n = int(input('Digite um valor: '))
  numeros += (n,)

print(f'O valor de 9 apareceu {numeros.count(9)} vezes')

if 3 in numeros:
  print(f'O valor 3 apareceu na posição {numeros.index(3) + 1}')
else:
  print(f'O número 3 não foi digitado')

for valor in numeros:
  if valor % 2 == 0:
    pares += (valor,)
if pares:
  print(f'Foram digitados os seguintes valores pares: {pares}')
else:
  print('Não foram digitados números pares.')