import random
print('Neste jogo, pensarei em um número de 0 a 5, seu trabalho é descobrir qual número pensei :)')
numero_aleatorio = random.randint(0,5)

numero_escolhido = int(input('Qual número eu estou pensando ? \n'))

if(numero_escolhido == numero_aleatorio):
    print('Parabéns, você acertou!')
else:
    print('Infelizmente você errou, eu estava pensando no número {}'.format(numero_aleatorio))