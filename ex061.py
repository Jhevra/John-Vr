print(f'\033[40;33;1m{"Desafio 61":=^20}\033[m\n\033[40;31;1m{"P.Ar":^20}\033[m')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 0
while cont != 10:
    print(primeiro)
    primeiro += razao
    cont += 1
