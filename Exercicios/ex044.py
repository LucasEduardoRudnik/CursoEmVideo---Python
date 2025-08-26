valor = float(input('Digite o valor do produto: R$ '))

desconto_dinheiro = valor * 0.10
desconto_cartao = valor * 0.05
preco_vista_dinheiro = valor - desconto_dinheiro
preco_vista_cartao = valor - desconto_cartao

print('Selecione a forma de pagamento!')
print('1 - ')