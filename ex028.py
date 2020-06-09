print(f'\033[40;31;1m{"Desafio 28":=^20}\033[m\n\033[33;1m{"Adivinhador":^20}\033[m')
print(f'''\033[34;1m{"-"*200}\033[m
\033[33;1mEstou pensando em um numero de\033[m \033[32;1m0\033[m \033[33;1ma \033[31;1m5\033[m\033[33;1m, 
Adivinhe...\033[m 
\033[34;1m{"-"*200}\033[m''')
chute = int(input('O numero é... '))
if chute == 0:
    print('\033[31;1mErrou! otario\033[m')
elif chute == 1:
    print('\033[32;1mAcertou! caralho... tu é brabo\033[m')
elif chute == 2:
    print('\033[31;1mErrou! otario\033[m')
elif chute == 3:
    print('\033[31;1mErrou! otario\033[m')
elif chute == 4:
    print('\033[31;1mErrou! otario\033[m')
elif chute == 5:
    print('\033[31;1mErrou! otario\033[m')
else:
    print('Amigão... tu é idiota é de 0 a 5')
print(f'{"Fim":=^20}')
