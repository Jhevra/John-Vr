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
print(ficha)
print('-=' * 35)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10} {a[2]:>5}')
print('-='*35)
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')