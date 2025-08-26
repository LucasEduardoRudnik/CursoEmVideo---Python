s = 0
count = 0
while True:
    n = int(input('Digite o valor [999 para parar]: '))
    if n == 999:
        break
    count += 1
    s += n
print(f'A soma dos {count} números digitados foi de: {s}!')