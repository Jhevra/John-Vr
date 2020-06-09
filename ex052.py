print(f'\033[40;33;1m{"Desafio 52":=^20}\033[m\n\033[40;31;1m{"PRIMOR":^20}\033[m')
num = int(input('Dígite um número: '))
div = 0
for cont in range(1, num+1):
    if num % cont == 0:
        print(f'\033[32;1m{cont}\033[m', end='\033[36;1m ==> \033[m')
        div += 1
    elif num % cont == 1:
        print(f'\033[31;1m{cont}\033[m', end='\033[36;1m ==> \033[m')
    else:
        print(f'\033[31;1m{cont}\033[m', end='\033[36;1m ==> \033[m')
print('\033[34;1mAcabou!\033[m')
if div > 2:
    print(f'\033[31;1mO número {num} não é primo pois é divido {div} vezes\033[m')
else:
    print(f'\033[32;1mO número {num} é número primo\033[m')