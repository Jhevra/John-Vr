from time import sleep
print(f'''\033[40;31;1m{"Desafio 42":=^20}\033[m\n\033[33;1m{"Triangulor 2.0":^20}\033[m''')
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
print('-='*12)
print('Analisando...')
print('-='*12)
sleep(1)
if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r1 + r2:
    print('Os segmentos formam um triangulo')
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Os segmentos não formam um triangulo')
