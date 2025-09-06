import random

numeros = ()

for c in range(5):
  n = random.randint(1, 10)
  numeros += (n,)

print(f'A listagem dos números gerados foi: {numeros}')
print(f'O menor valor da túpla é de {min(numeros)}')
print(f'O maior valor da túpla é de {max(numeros)}')