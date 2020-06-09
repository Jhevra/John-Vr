print(f'\033[40;33;1m{"Desafio 64":=^20}\033[m\n\033[40;31;1m{"999er":^20}\033[m')
cont = soma = tot = 0

while cont != 999:

    valor = int(input('Dígite o primeiro valor, ou, dígite [999] para parar: '))
    tot += 1

    if valor == 999:
        tot -= 1
        break

    soma += valor

print(f'A soma de todos os valores foi de {soma}, foram dígitados {tot} valores')
