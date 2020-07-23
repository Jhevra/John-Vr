from funções.UtilidadesCev.Dados import cabecalho
from random import randint

cabecalho('Desafio 68', 'PARRrr OU IMPARRrr')

print('-=' * 35)
print(f'{"VAMOS JOGAR PAR OU ÍMPAR":^70}')
print('-=' * 35)

while True:
    jogada = int(input('Diga um valor: '))
    escolha = input('Par ou Ímpar? [P/Í] ').upper().strip()

    if escolha == 'P':
        cpu = randint(1, 10)
        result = jogada + cpu

        print('-' * 30)

        print(f'Você jogou {jogada} e o computador {cpu}.')

        if result % 2 == 0:
            print(f'Total de {result}, DEU PAR.')
            print(f'''Você VENCEU!
Vamos jogar novamente...''')

        else:
            print(f'''Total de {result}, DEU ÍMPAR.
Você perdeu...''')
            print('-' * 30)
            break

        print('-' * 30)
########################################################################################################################

    if escolha == 'I':
        cpu = randint(1, 10)
        result = jogada + cpu

        print('-' * 30)

        print(f'Você jogou {jogada} e o computador {cpu}.')

        if result % 2 == 1:
            print(f'Total de {result}, DEU ÍMPAR.')
            print(f'''Você VENCEU!
        Vamos jogar novamente...''')

        else:
            print(f'''Total de {result}, DEU PAR.
Você perdeu...''')
            print('-' * 30)
            break

        print('-' * 30)
