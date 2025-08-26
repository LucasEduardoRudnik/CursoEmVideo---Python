primeiro_termo = int(input('Digite o primeiro termo de sua PA: '))
razao = int(input('Digite a razão de sua PA: '))

contador = 0

while contador < 10:
    termo = primeiro_termo + (razao * contador)
    print(termo)
    contador += 1