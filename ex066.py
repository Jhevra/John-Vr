print(f'\033[40;33;1m{"Desafio 66":=^20}\033[m\n\033[40;31;1m{"BREAKDOWN":^20}\033[m')
soma = 0
while True:
    num = int(input('Dígite um número [999 para sair]: '))
    if num == 999:
        break
    soma += num
print(soma)
