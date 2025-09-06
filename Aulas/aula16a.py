lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

'''for count in range(0, len(lanche)):
  print(f'Eu vou comer {lanche[count]} na posição {count}')'''

for pos, comida in enumerate (lanche):
  print(f'Eu vou comer {comida} e na posicao {pos}')