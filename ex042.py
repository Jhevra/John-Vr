from time import sleep
from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 42', 'TRIANGULORRrr 2.5')

r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

print('-='*12)
print('Analisando...')
print('-='*12)
sleep(1)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os segmentos acima formam um triângulo')
    if r1 == r2 == r3:
        print(f'CLASSIFICAÇÃO: EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('CLASSIFICAÇÃO: ESCALENO')
    else:
        print('CLASSIFICAÇÃO: ISÓSCELES')