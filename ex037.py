from time import sleep
print(f'''\033[40;31;1m{"Desafio 37":=^20}\033[m\n\033[33;1m{"Conversor":^20}\033[m''')
num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão: 
[1] Binario
[2] Octal
[3] Hexadecimal ''')
opcao = int(input('Sua opção: '))
print('-='*20)
print(f'{"Analisando...":^40}')
print('-='*20)
sleep(1)
if opcao == 1:
    print(f'\033[33;1m{num}\033[m converstido para a base binaria é \033[32;1m{bin(num)}\033[m')
elif opcao == 2:
    print(f'\033[33;1m{num}\033[m convertido para a base octal é \033[32;1m{oct(num)}\033[m')
elif opcao == 3:
    print(f'\033[33;1m{num}\033[m convertido para a base hexadecimal é \033[32;1m{hex(num)}\033[m')
else:
    print('\033[31;1mOpção INVÁLIDA!\033[m')
