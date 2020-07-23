from time import sleep
from random import randint
from datetime import datetime


lista = []


def contagem(inico, fim, passo):
    print('-=' * 35)
    print(f'Contagem de {inico} até {fim} de {passo} em {passo}')

    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
        print('\033[31;1mERRO!\033[m A variavel "PASSO" é \033[33;1m0\033[m trocando para \033[33;1m1\033[m\n')

    if inico < fim:
        for c in range(inico, fim, passo):
            print(c, end=' ')
        print()
    else:
        passo *= -1
        while inico >= fim:
            print(inico, end=' ')
            inico += passo
        print()


def maior(*num):
    mai = cont = 0
    print('-=' * 35)
    print('Analisando os valores informados...')
    for numeros in num:
        print(numeros, end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            mai = numeros
            cont += 1
        else:
            if numeros > mai:
                mai = numeros

    print(f'''Foram informados {len(num)} ao todo.
O maior valor informado foi {mai}.''')


def sortea_dor():
    print(f'Sorteando \033[33;1m5\033[m valores da lista:', end=' ')
    for valor in range(5):
        lista.append(randint(0, 10))
    for nums in lista:
        print(nums, end=' ')
    print('PRONTO!!')


def soma_dor():
    soma = 0
    print(f'Somand os valores pares de', end=' ')
    for nums in lista:
        if nums % 2 == 1:
            print(f'\033[31;1m{nums}\033[m', end=' ')
        elif nums % 2 == 0:
            print(f'\033[32;1m{nums}\033[m', end=' ')
            soma += nums
    print(f'Temos \033[36;1m{soma}\033[m')


def voto(ano):
    idade = datetime.today().year - ano
    print('-='*35)
    if idade < 16:
        print(f'Com {idade} anos: NEGADO')
    elif 16 <= idade <= 17 or idade >= 65:
        print(f'Com {idade} anos: OPCIONAL')
    elif idade > 18:
        print(f'Com {idade} anos: OBRIGATÓRIO')


def fatorial(valor=1, show=''):
    if show == 'S':
        show = True
    else:
        show = False

    f = 1
    for valores in range(valor, 0, -1):
        if show:
            print(valores, end='')
            if valor > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= valores
    print()
    return f


def ficha(nome='<DESCONHECIDO>', gols=0):
    print(f'O jogador \033[32;1m{nome}\033[m fez \033[33;1m{gols}\033[m gols no campeonato')


def notas(*num, show=False):
    dicio = dict()

    dicio['Total'] = len(num)
    dicio['Maior'] = max(num)
    dicio['Menor'] = min(num)
    dicio['Média'] = sum(num) / len(num)

    if show:
        if dicio['Média'] >= 6:
            dicio['Situação'] = 'Aprovado'
        else:
            dicio['Situação'] = 'Reprovado'

    return dicio


def leiaint(valor):
    while True:
        try:
            n = int(input(valor))
        except (TypeError, ValueError):
            print(f'\033[31;1mTIVEMOS UM ERRO NO VALOR INFORMADO!\033[m\n')
            continue
        except KeyboardInterrupt:
            print(f'\033[31;1mO usuario preferiu não informar o valor.\033[m')
            return 0
        else:
            print('-' * 45)
            return n


def leiafloat(valor):
    while True:
        try:
            n = float(input(valor).replace(',', '.'))
        except (TypeError, ValueError):
            print(f'\033[31;1mTIVEMOS UM ERRO NO VALOR INFORMADO!\033[m\n')
            continue
        except KeyboardInterrupt:
            print('\033[31;1mO usuario preferiu não informar os valor.\033[m')
            return 0
        else:
            return n
