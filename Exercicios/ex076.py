produtos = ('Pão', 3.00, 'Leite', 6.20, 'Carne', 12, 'Refrigerante', 1.50, 'Ovo', 2.35)

for i in range (0, len(produtos), 2):
  nome = produtos[i]
  preco = produtos[i + 1]
  print(f'{nome:<15} R$ {preco:>6.2f}')