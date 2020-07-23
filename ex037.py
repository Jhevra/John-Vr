from funções.UtilidadesCev.Dados import cabecalho
from time import sleep

cabecalho('Desafio 37', 'ConversoRRrr')

numero = int(input('Dígite um número inteiro: '))

print(f'''Escolha uma das bases para conversão:
[ 1 ] CONVERTER PARA BINÁRIO
[ 2 ] CONVERTER PARA OCTAL
[ 3 ] CONVERTER PARA HEXADECIMAL''')

opc = int(input('Sua opção: '))

if opc == 1:
    print(f'\033[34m{numero} convertido para BINÁRIO é igual a {bin(numero)}\033[m')
elif opc == 2:
    print(f'\033[34m{numero} convertido para OCTAL é igual a {oct(numero)}\033[m')
elif opc == 3:
    print(f'\033[34m{numero} convertido para HEXADECIMAL é igual a {hex(numero)}\033[m')
else:
    print(f'\033[31mERRO! ----- FECHANDO O SISTEMA.... -----\033[m')
    sleep(0.5)
