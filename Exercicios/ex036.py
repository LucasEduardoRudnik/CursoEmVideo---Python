valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos você deseja pagar o valor da casa? '))

prest_mensal = valor_casa / (anos * 12)

if prest_mensal <= salario * 0.3:
    print('A prestação das parcelas da compra de sua casa é de R$ {:.2f} e a mesma está aprovada :)'.format(prest_mensal))
else:
    print('A prestação da compra de sua casa foi negada, pois o valor de R$ {:.2f} da prestação supera 30% de seu rendimento liquido.'.format(prest_mensal))