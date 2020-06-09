from random import randint

print(f'''\033[40;31;1m{"Desafio 45":=^20}\033[m\n\033[33;1m{"JOKENPOR":^20}\033[m''')
itens = ('Pedra', 'Papel', 'Tesoura')  # é dado as opção de jogada
computador = randint(0, 2)  # o comp. vai retornar 0 a 2
print('-=' * 20)
print('Suas escolhas são: ')
print('''[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Sua jogada é... '))
print('-=' * 20)

# Vai mostrar a var 'itens' na posição em que a var comp. escolher, É randomico por causa do "RANDINT" de 0 a 2 (0.1.2)
print(f'O computador escolheu \033[31;1m{itens[computador]}\033[m')
print(f'Jogador jogou \033[32;1m{itens[jogador]}\033[m')
if computador == 0:  # comp. jogou PEDRA
    if jogador == 0:
        print('\033[33;1mEMPATE\033[m')
    elif jogador == 1:
        print('\033[32;1mJOGADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[31;1mCOMPUTADOR VENCE\033[m')
    else:
        print('\033[31;1mJOGDAVA INVÁLIDA\033[m')
elif computador == 1:  # comp. jogou PAPEL
    if jogador == 1:
        print('\033[33;1mEMPATE\033[m')
    elif jogador == 0:
        print('\033[31;1mCOMPUTADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[32;1mJOGADOR VENCE\033[m')
    else:
        print('\033[31;1mJOGADA INVÁLIDA\033[m')

elif computador == 2:  # comp. jogou TESOURA
    if jogador == 2:
        print('\033[33;1mEMPATE\033[m')
    elif jogador == 1:
        print('\033[32;1mJOGADOR VENCE\033[m')
    elif jogador == 0:
        print('\033[31;1mCOMPUTADOR VENCE\033[m')
    else:
        print('\033[31;1mOGADA INVÁLIDA\033[m')
