num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
       'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
       'Dezenove', 'Vinte')

while True:
  n = int(input('Informe um número de 0 a 20: '))
  if 0 <= n <= 20:
    print(f'O número selecionado foi {num[n]}')
    break
  else:
    print('Número inválido, tente novamente!')