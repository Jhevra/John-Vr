from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 5', 'AntecesoRRrr e SucessoRRrr')

valor = int(input('Digite um numero e mostrarei seu sucessor e antecessor: >> '))

print(f'''O antecessor de \033[32;1m{valor}\033[m é \033[33;1m{valor-1}\033[m
O sucessor de \033[32;1m{valor}\033[m é \033[33;1m{valor+1}\033[m''')