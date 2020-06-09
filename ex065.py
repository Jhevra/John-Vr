import math
print(f'\033[40;33;1m{"Desafio 65":=^20}\033[m\n\033[40;31;1m{"M&M":^20}\033[m')

lista = list()
resposta = ''
tot = media = 0

while resposta != 'N':

    valor = int(input('Dígite um valor: '))
    media += valor
    lista.append(valor)
    tot += 1
    resposta = str(input('Quer continuar [S/N]? ')).upper().strip()

    while resposta[0] != 'S' and resposta[0] != 'N':
        resposta = str(input('\033[31;1mERRO!\033[m Quer continuar [S/N]? ')).upper().strip()

print(f'''Foram dígitados {tot} valores, e a media entre ele é de {media/tot}, o maior valor foi {max(lista)} 
e o menor foi {min(lista)}''')