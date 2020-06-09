from time import  sleep
print(f'\033[40;33;1m{"Desafio 99":=^100}\033[m\n\033[40;31;1m{"MAIORRRr":^100}\033[m')


def maior(*num):
    mario = cont = 0
    print('-='*35)
    print('Analisando os valores passados...')
    for numero in num:
        print(f'\033[33;1m{numero}\033[m', end=' ')
        sleep(0.5)
        if numero > mario:
            mario = numero
        cont += 1
    print(f'''Foram informados \033[33;1m{cont}\033[m valores ao todo
O maior valor foi \033[33;1m{mario}\033[m''')


# Programa pincipal

maior(2, 9, 4, 5, 1, 7)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
