from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 35', 'TRIANGULORRrr')

print('-'*40)
print(f'{"Analisador de Triângulos":^40}')
print('-'*40)

n1 = float(input('1º segmento: '))
n2 = float(input('2º segmento: '))
n3 = float(input('3º segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos podem formar um triângulo')
else:
    print('Os segmentos não podem formar um triângulo')

