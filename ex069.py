print(f'\033[40;33;1m{"Desafio 68":=^20}\033[m\n\033[40;31;1m{"ANALISADORRRRRRR":^20}\033[m')
homem = pessoasdez = mulher = 0


print('-'*30)
print(f'{"CADASTRE PESSOAS":^25}')
print('-'*30)

while True:

    # enre
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip().upper()

    while sexo[0] != 'M' and sexo[0] != 'F':
        sexo = str(input('\033[31;1mERRO!\033[m SEXO [M/F]: ')).strip().upper()
    if idade >= 18:
        pessoasdez += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    print('-'*30)
    resposta = str(input('Quer continuar [S/N]?: ')).strip().upper()
    print('-' * 30)
    while resposta != 'N' and resposta != 'S':
        resposta = str(input('\033[31;1mERRO!\033[m Quer continuar [S/N]?: ')).strip().upper()
    if resposta == 'N':
        break
print(f'''Total de pessoas com mais de 18: {pessoasdez}
Homens registrados: {homem}
Mulheres com menos de 20 anos: {mulher}''')