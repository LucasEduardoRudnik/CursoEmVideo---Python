num = int(input('Digite um número inteiro: '))

print('Escolha a sua base de conversão!\n1 Para binário.\n2 Para octal.\n3 Para hexadecimal.')
escolha = int(input('Sua escolha: '))

if escolha == 1:
    binario = bin(num)
    print('O número digitado convertido para binário é o seguinte: {}'.format(binario))

elif escolha == 2:
    octal = oct(num)
    print('O número digitado convertido para octal é o seguinte: {}'.format(octal))

else:
    hexadecimal = hex(num)
    print('O número digitado convertido para hexadecimal é o seguinte: {}'.format(hexadecimal))