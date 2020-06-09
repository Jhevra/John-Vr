print(f'''\033[40;31;1m{"Desafio 50":=^20}\033[m\n\033[33;1m{"PAREADOR":^20}\033[m''')
somaimp = soma = impar = par = 0

for cont in range(1, 7):
    nums = int(input('Dígite um número: '))
    if nums % 2 == 0:
        soma += nums
    else:
        somaimp += nums
print(f'A soma dos números pares foi de \033[32;1m{soma}\033[m e dos números ímpares foi de \033[31;1m{somaimp}\033[m')