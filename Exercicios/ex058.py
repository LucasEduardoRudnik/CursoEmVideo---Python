import random
palpites = 0
numero_aleatorio = random.randint(0,10)

print('Vamos brincar de adivinha ?')
chute = int(input(('Pense no número que o computador estava pensando, de 1 a 10: ')))

while chute != numero_aleatorio:
    print('Você errou, tente de novo!')
    chute = int(input(('Pense no número que o computador estava pensando, de 1 a 10: ')))
    palpites += 1
print('Parabéns, você acertou!\nPara acertar, você precisou de {} tentativas.'.format(palpites+1))