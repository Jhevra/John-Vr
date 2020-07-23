from funções.UtilidadesCev.Dados import cabecalho

cabecalho('Desafio 106', 'PyHelper')


def ajuda(msg):
    print('\033[36;40;1m-=' * 35)
    print(f'{f"Acessando o manual do commando {msg}":^75}')
    print('-=' * 35)
    print('\033[m')
    help(msg)


# Programa principal
while True:
    print('\033[32;40;1m-=' * 35)
    print(f'{"SISTEMA DE AJUDA PyHELP":^75}')
    print('-=' * 35)
    comando = input('\033[mFunção ou Biblioteca: ')
    if comando == 'fim':
        break
    ajuda(comando)
