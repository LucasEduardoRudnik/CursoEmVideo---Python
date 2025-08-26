print('LOJA SUPER BARATO!')
total = 0
count = 0
produtos = []

mais_barato_nome = ''
mais_barato_preco = 0
primeiro = True

while True:
    nome = str(input('Digite o nome do produto: '))
    produtos.append(nome)
    preco = float(input('Digite o preço do produto: R$ '))
    total += preco

    if preco > 1000:
        count += 1

    if primeiro or preco < mais_barato_preco:
        mais_barato_nome = nome
        mais_barato_preco = preco
        primeiro = False

    escolha = str(input('Você deseja continuar [S/N]? ')).strip().upper()
    if escolha == 'N':
        break

print(f'O total da compra foi de R$ {total:.2f}!')
print(f'{count} produtos custam mais de 1000 reais!')
print(f'O produto mais barato foi {mais_barato_nome} que custou R$ {mais_barato_preco:.2f}')