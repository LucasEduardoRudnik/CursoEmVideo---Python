times_ordenado = ('Operário - PR', 'Novorizontino', 'Goiás', 'Volta Redonda', 'Atlético - GO', 'Votuporanguense',
                  'Chapecoense', 'Barra - SC', 'América - RJ', 'Rio Branco', 'Fluminense', 'Maricá', 'Botafogo - SP',
                  'Vila Nova', 'Vitória', 'Maringá', 'Athletico - PR', 'Coritiba', 'Londrina', 'Maricá')

print(f'Os 5 primeiros colocados são: {times_ordenado[0:5]}')
print(f'Os últimos colocados da tabela são: {times_ordenado[-4:]}')
print(f'A lista com os 20 times em ordem alfabética fica assim: {sorted(times_ordenado)}')
print(f'A Chapecoense está na {times_ordenado.index('Chapecoense') + 1} posição')