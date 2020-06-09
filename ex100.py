from random import randint

print(f'\033[40;33;1m{"Desafio 100":=^100}\033[m\n\033[40;31;1m{"SORTEARRr":^100}\033[m')

valores = [randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)]


def sorteador(numeros):
    print(f'Sorteandos 5 números da lista:', end=' ')
    for num in numeros:
        print(num, end=' ')
    print('FIM!', end=' ')
    print()


pares = valores[:]


def soma(nums):
    somar = 0
    for valor in nums:
        if valor % 2 == 0:
            somar += valor
    print(f'A soma de todos os números pares de {valores} é igual a {somar}')


sorteador(valores)
soma(pares)
