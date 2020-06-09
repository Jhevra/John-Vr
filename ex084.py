print(f'\033[40;33;1m{"Desafio 84":=^20}\033[m\n\033[40;31;1m{"LISTARR":^20}\033[m')
tempo = list()
principal = list()
mai = men = 0
while True:
    tempo.append(input('Nome: '))
    tempo.append(float(input('Peso: ')))
    if tempo[1] > len(principal):
        if len(principal) == 0:
            mai = men = tempo[1]
        else:
            if tempo[1] > mai:
                mai = tempo[1]
            if tempo[1] < men:
                men = tempo[1]
    principal.append(tempo[:])
    tempo.clear()
    res = input('Quer continuar [S/N]? ').strip().upper()
    while res[0] != 'S' and res[0] != 'N':
        res = input('\033[31;1mERRO!\033[m Quer continuar [S/N]? ').strip().upper()
    if res[0] == 'N':
        break

print(f'Ao todo foram registradas {len(principal)} pessoas')

print(f'O maior peso registrado foi {mai}Kg de: ', end='')
for p in principal:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print()

print(f'O menor peso registrado foi {men}Kg de: ', end='')
for p in principal:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
