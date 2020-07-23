from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 30', 'PARRrr ou IMPARRrr?')

valor = int(input('Me diga um número qualquer: '))

if valor % 2 == 0:
    print(f'\033[32mO número {valor} é\033[m \033[36mPAR\033[m')
else:
    print(f'\033[32mO número {valor} é\033[m \033[31mIMPAR\033[m')