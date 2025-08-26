preco = int(input('Digite o valor do produto: '))

desconto = preco * 0.05
preco_final = preco - desconto

print ('Valor total do produto: R$ {}\nValor do produto com 5% de desconto: R$ {}'.format(preco, preco_final))