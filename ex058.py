from random import randrange
print(f'''\033[40;31;1m{"Desafio 58":=^20}\033[m\n''')
print('\033[33;1m-=\033[m'*20)
print(f'\033[32;1m{"Adivinhador":^21}\033[m \033[31;1m2.0\033[m')
print('\033[33;1m-=\033[m'*20)
tnt = 0
cpu = randrange(1, 10)
# Inicio do Codigo
print('O jogo é o seguinte , chute um número de 0 a 10.')
palpite = int(input('Qual é o seu 1º palpite: '))

# Vai ficar peguntando seu palpite e dando dica até o usuário acertar
while palpite != cpu:

    # Se o palpite for maior que 10, o usuário toma bronca.
    if palpite > 10:
        print('AMIGÃO!, se liga é de 0 a 10')
        palpite = int(input('Qual é o seu palpite? '))
        # TNT = var contador, cada tentativa tnt recebe + 1
        tnt += 1

    # Se palpite for menor que o valor ja definido pelo algorimito
    if palpite < cpu:
        print('Mais... Tente novamente.')
        palpite = int(input('Qual é o seu palpite? '))
        # TNT = var contador, cada tentativa tnt recebe + 1
        tnt += 1

    # Se palpite for maior que o valor ja definido pelo algorimito
    elif palpite > cpu:
        print('Menos... Tente novamente.')
        palpite = int(input('Qual é o seu palpite? '))
        # TNT = var contador, cada tentativa tnt recebe + 1
        tnt += 1

# Se tnt = 0 logo, o usuári ocertou de primeira
if tnt == 0:
    print('Parabéns! de primeira')

# Se não a var tnt, vai mostras as quantidades de vezes que o usuário chutou
else:
    print(f'Você consegui adivinhar, com {tnt} tentivas.')