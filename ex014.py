from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 14', 'TA QUENTE AI?')
celsius = float(input('Informe a temperatura em ºC: '))
print(f'A temperatura de \033[31;1m{celsius}ºC\033[m corresponde a \033[33;1m{(celsius * 9/5)+32}ºF\033[m.')