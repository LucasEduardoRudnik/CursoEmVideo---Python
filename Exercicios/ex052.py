n = int(input('Digite um valor: '))
tot = 0

for c in range(1, n + 1):
    if n % c == 0:
        tot += 1;

if tot == 2:
    print('O número é primo!')
else:
    print('O número não é primo!')