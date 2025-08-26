primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

contador = 0
total = 10

while True:
    while contador < total:
        termo = primeiro_termo + (razao * contador)
        print(termo)
        contador +=1

    mais = int(input('Você deseja verificar quantos termos a mais ? Digite 0 para finalizar o programa: '))
    if mais == 0:
        print('Você finalizou o programa!')
        break
    else:
        total += mais