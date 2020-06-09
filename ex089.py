print(f'''\033[40;31;1m{"Desafio 89":=^20}\033[m\n\033[33;1m{"MEDIARRR":^20}\033[m''')
ficha = list()

while True:
    nome = input('Nome: ')
    nota1 = float(input('1º Nota: '))
    nota2 = float(input('2º Nota: '))
    media = (nota2 + nota1) / 2
    ficha.append([nome, [nota1, nota2], media])
    res = input('Quer continuar [S/N]? ').strip().upper()
    while res[0] != 'N' and res[0] != 'S':
        res = input(f'\033[31;1mERRO!\033[m Quer continuar [S/N]? ').strip().upper()
    if res[0] == 'N':
        break

print('-='*35)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for a, i in enumerate(ficha):
    print(f'{a:<4}{i[0]:<10}{i[2]:>8.1f}')

while True:
    opc = int(input('De qual aluno você quer as informações? [999 interrompe]: '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'As notas do aluno {ficha[opc][0]} é {ficha[opc][1]}')
