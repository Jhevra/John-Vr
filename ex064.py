from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 64', 'TRATARRrr')

s = nums = n = 0

while n != 999:
    if n == 999:
        break
    n = int(input('Dígite um valor [999 para sair]: '))
    nums += 1
    s += n
print(f'Foram {nums-1} números, e a soma deles foi de {s-999}')