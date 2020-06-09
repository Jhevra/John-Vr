from random import randint
print(f'\033[40;33;1m{"Desafio 68":=^20}\033[m\n\033[40;31;1m{"par or impar":^20}\033[m')
print('Vamos jogar par ou ímpar')
vits = 0
while True:

    # ENTRADA DO JOGADOR

    escolha = int(input('''[1] ÍMPAR
[2] PAR
Sua escolha: '''))

    while escolha != 1 and escolha != 2:
        escolha = int(input('''\033[31;1mERRO! [VOCÊ DEVE ESCOLHER ENTRE '1' OU '2']\033[m Sua escolha: '''))
    jogada = int(input('Sua jogada é: '))

    while jogada > 10:
        jogada = int(input('\033[31;1mERRO! [SUA JOGADA DEVE SER ENTRE 0 E 10]\033[m Sua jogada é: '))
    print('-'*30)
    # ENTRADA DA IA

    ia = randint(1, 10)

    # ESCOLHEU PAR

    soma = jogada + ia
    if escolha == 2:
        if soma % 2 == 0:
            print(f'''\033[32;1mVocê ganhou! [+1 PONTO]\033[m 
Você jogou \033[32;1m{jogada}\033[m e o Computador \033[31;1m{ia}\033[m, \033[36;1m{soma} é PAR\033[m''')
            print('-' * 30)
            vits += 1
        else:
            print(f'''\033[31;1mVocê Perdeu... GAMER OVER\033[m
Você jogou \033[32;1m{jogada}\033[m e o Computador \033[31;1m{ia}\033[m, \033[36;1m{soma} é ÍMPAR\033[m''')
            print('-' * 30)
            break

    # ESCOLHEU ÍMPAR

    elif escolha == 1:
        if soma % 2 == 1:
            print(f'''\033[32;1mVocê ganhou! [+1 PONTO]\033[m
Você jogou \033[32;1m{jogada}\033[m e o Computador \033[31;1m{ia}\033[m, \033[36;1m{soma} é ÍMPAR\033[m''')
            print('-' * 30)
            vits += 1
        else:
            print(f'''\033[31;1mVocê Perdeu... GAMER OVER\033[m
Você jogou \033[32;1m{jogada}\033[m e o Computador \033[31;1m{ia}\033[m, \033[36;1m{soma} é PAR\033[m''')
            print('-' * 30)
            break

print(f'\nSeu Total de pontos foi de \033[33;1m{vits}\033[m')
