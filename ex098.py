from time import sleep

print(f'\033[40;33;1m{"Desafio 98":=^100}\033[m\n\033[40;31;1m{"CONTARRr":^100}\033[m')
exemplo = dict()


def contador(inicio, fim, passo):

    print('-='*35)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if passo < 0:
        passo *= -1

    if passo == 0:
        passo = 1
        print(f'\033[31;1mERRO!\033[m "PASSO" = 0, MUDANDO PARA "PASSO" = 1')

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'\033[33;1m{cont}\033[m', end=' ')
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'\033[33;1m{cont}\033[m', end=' ')
            sleep(0.5)
            cont -= passo
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*35)
print(f'Agora é sua vez de personalizar a contagem!')
exemplo['INICO'] = int(input('INÍCIO: '))
exemplo['FIM'] = int(input('FIM: '))
exemplo['PASSO'] = int(input('PASSO: '))
contador(exemplo['INICO'], exemplo['FIM'], exemplo['PASSO'])
