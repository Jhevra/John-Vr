from funções.UtilidadesCev.Dados import cabecalho
from random import randint
cabecalho('Desafio 28', 'Tenta SORTERRrr')

numero = randint(0, 5)

print('\033[33;1m-=\033[m'*45)
print('\033[36mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[33;1m-=\033[m'*45)

chute = int(input('Em que número eu pensei? '))

while True:
    if chute > 5:
        print(f'\033[32;1mOh AMIGÃO... é entre 0 e 5. ¬¬\033[m')
        chute = int(input('Em que número eu pensei? '))

    elif chute != numero:
        print(f'''\033[31mIIIIIHHH ALA ERRO OTARIO\033[m
\033[33mO número que eu pensei era {numero}\033[m''')
        break

    else:
        print('\033[32mAcertou, parabéns hein amigo.\033[m')
        break
