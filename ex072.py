print(f'\033[40;33;1m{"Desafio 72":=^20}\033[m\n\033[40;31;1m{"TUPLARRR":^20}\033[m')
numeros = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'NOVE', 'OITO', 'DEZ', 'ONZE', 'DOZE',
           'TREZE', 'CARTORZE', 'QUINZE', 'DEZESSESIS', 'DEZESETE', 'DEZIOTO', 'DEZENOVE', 'VINTE')


while True:
    num = int(input('Dígite um valor entre 0 e 20: '))
    if num <= 0 and num <= 20:
        break
    print('Tente novamente...')
print(f'O número dígitad foi {numeros[num]}')
