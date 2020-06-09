print(f'''\033[40;31;1m{"Desafio 33":=^20}\033[m\n\033[33;1m{"M & M":^20}\033[m''')
n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
n3 = float(input('Digite o 3º número: '))
maior = n1
menor = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'''O maior número é {maior}
O menor número é {menor}''')
