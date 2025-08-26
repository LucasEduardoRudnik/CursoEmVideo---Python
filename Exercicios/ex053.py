"""palavra = str(input('Digite sua palavra: ')).strip().upper()
palavra_sem_espaco = palavra.replace(" ", "")

if palavra_sem_espaco == palavra_sem_espaco[::-1]:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')"""

frase = str(input('Digite sua palavra: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print('Você digitou {}'.format(junto))

inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('É palíndromo!')
else:
    print('Não é palíndromo!')