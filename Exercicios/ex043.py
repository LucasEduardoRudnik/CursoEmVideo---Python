peso = float(input('Informe o seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Abaixo do peso.\nIMC: {:.2f}'.format (imc))
elif imc >= 18.5 and imc < 25:
    print('Peso ideal.\nIMC: {:.2f}'.format (imc))
elif imc >= 25 and imc < 30:
    print('Sobrepeso.\nIMC: {:.2f}'.format (imc))
elif imc >= 30 and imc < 40:
    print('Obesidade.\nIMC: {:.2f}'.format (imc))
else:
    print('Obesidade Mórbida.\nIMC: {:.2f}'.format (imc))