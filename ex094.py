print(f'''\033[40;31;1m{"Desafio 94":=^20}\033[m\n\033[33;1m{"CADASTRADORRr":^20}\033[m''')
sala = list()
pessoas = dict()
media = 0

while True:
    pessoas.clear()
    pessoas['Nome'] = input('Nome: ')
    pessoas['Sexo'] = input('Sexo [M/F]: ').strip().upper()
    while pessoas['Sexo'][0] != 'M' and pessoas['Sexo'][0] != 'F':
        pessoas['Sexo'] = input('\033[31;1mERRO!\033[m Sexo [M/F]: ').strip().upper()
    pessoas['Idade'] = int(input('Idade: '))
    media += pessoas['Idade']
    resp = input('Quer continuar ? [S/N]: ').upper().strip()
    sala.append(pessoas.copy())
    while resp[0] != 'S' and resp[0] != 'N':
        resp = input('\033[31;1mERRO!\033[m Quer continuar ? [S/N]: ').strip().upper()
    if resp[0] == 'N':
        break
media = media / len(sala)

print('-='*35)
print(sala)

# FIM DA LEITURA DE DADOS

print('-='*35)
print(f'''A) Ao todo temos {len(sala)}  pessoas cadastradas.
B) A média de idade é de {media}
C) As mulheres cadastradas foram''', end=' ')
for p in sala:
    if p['Sexo'] == 'F':
        print(f'[{p["Nome"]}]', end=' ')

print()
print(f'D) Lista das pessoas com idade acima da media: ')
for p in sala:
    if p['Idade'] >= media:
        print('     ', end=' ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< ENCERRADO >>>')