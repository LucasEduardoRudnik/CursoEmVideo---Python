primeiro_termo = int(input('Digite o primeiro termo de sua PA: '))
razao = int(input('Digite a razão de sua PA: '))

for pa in range(10):
    termo = primeiro_termo + (pa * razao)
    print(termo)