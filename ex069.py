from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 69', 'CADASTRARRrr')

pessoaoito = mulheresvinte = homem = 0

while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').upper().strip()

    if idade >= 18:
        pessoaoito += 1

    if sexo == 'M':
        homem += 1

    if sexo == 'F' and idade <= 20:
        mulheresvinte += 1

    print('-'*35)
    resp = input('Quer continuar? [S/N] ').strip().upper()
    print('-' * 35)

    if resp[0] == 'N':
        break


print(f'''Total de pessoas com mais de 18 anos: {pessoaoito}
Ao todo temos {homem} homens cadastrados
E temos {mulheresvinte} mulheres com menos de 20 anos''')