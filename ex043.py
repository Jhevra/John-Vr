print(f'''\033[40;31;1m{"Desafio 43":=^20}\033[m\n\033[33;1m{"IMCR":^20}\033[m''')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura**2)

if imc < 18.5:
    print('\033[31;1mAbaixo\033[m')
    print(f'Seu imc é {imc:.2f}')
elif imc <= 25:
    print('\033[32;1mPeso ideal\033[m')
    print(f'Seu imc é {imc:.2f}')
elif imc <= 30:
    print('\033[31;1mSobrepeso\033[m')
    print(f'Seu imc é {imc:.2f}')
elif imc <= 40:
    print('\033[31;1mObesidade\033[m')
    print(f'Seu imc é {imc:.2f}')
else:
    print('\033[31;1mObesidade mórbida\033[m')
    print(f'Seu imc é {imc:.2f}')
