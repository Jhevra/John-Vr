print(f'\033[40;33;1m{"Desafio 63":=^20}\033[m\n\033[40;31;1m{"P.Ar 2.0":^20}\033[m')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
contador = 0
while contador != 10:
    print(primeiro, end=' -> ')
    primeiro += razao
    contador += 1
print('Acabou')
