from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 56', 'CADASTRARRrr')
hvelho = ''
soma = hidade = mcont = maior = menor = 0

for c in range(4):

    print(f'----- {c+1}º PESSOA -----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()

    soma += idade

    if c == 0:
        maior = menor = idade
    else:
        if idade > maior:
            maior = idade
        if idade < menor:
            menor = idade

    if sexo == 'M' and idade > hidade:
        hvelho = nome
        hidade = idade

    if sexo == 'F' and idade <= 20:
        mcont += 1


media = soma / 4
print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {hidade} anos e se chama {hvelho}')
print(f'Ao todo são {mcont} mulheres com menos de 20 anos')