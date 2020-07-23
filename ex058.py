from random import randint
from funções.UtilidadesCev.Dados import cabecalho

cabecalho('Desafio 58', 'ADIVINHARRrr')
tnt = 0

palpite = int(input('Dígite seu palpite: '))

valor = randint(1, 10)

print(valor)

while palpite != valor:
    if palpite >= valor:
        print(f'O número é menor.')
        palpite = int(input('Dígite seu palpite: '))
        tnt += 1
    elif palpite <= valor:
        print(f'O número é maior.')
        palpite = int(input('Dígite seu palpite: '))
        tnt += 1

print(f'Suas tentativas foram: {tnt} vezes.')
