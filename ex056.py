print(f'\033[40;33;1m{"Desafio 56":=^20}\033[m\n\033[40;31;1m{"ANALISADORR":^20}\033[m')
muie = maior = media = 0 # Mulheres com mais de 20 | Maior idade do homem mais velho | Media das idades
hvelho = '' # Nome do homem mais velho

for cont in range(1, 5):

    # Repete o mini formulario 4 vezes
    print(f'----- {cont}ª pessoa -----')
    nome = str(input('Nome: ')).upper().strip()
    idade = int(input('Idade: '))

    # A idade é somada em uma var chamada media
    media += idade

    sexo = str(input('Sexo [M/F]: ')).upper().strip()

    # Verifica e conta a quantidade de mulheres com menos de 20 anos
    if sexo == 'F' and idade <= 20:
        muie += 1

    # Verifica e atribui o homem com maior idade
    if cont == 0 and sexo == 'M':
        maior = idade
    else:
        if idade > maior and sexo == 'M':
            maior = idade
            hvelho = nome


print(f'A media da idades das pessoa foi de \033[33;1m{media/4}\033[m')

if hvelho != '':
    print(f'O homem mais velho se chama \033[36;1m{hvelho}\033[m e tem \033[33;1m{maior}\033[m anos')
else:
    print('Não registrado nenhum homem')

if muie > 0:
    print(f'Ao todo foi registrado {muie} mulheres menores de 20')
else:
    print(f'Não foi registrado mulheres com menos de 20')