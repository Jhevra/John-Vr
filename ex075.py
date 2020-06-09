print(f'\033[40;33;1m{"Desafio 75":=^20}\033[m\n\033[40;31;1m{"BREAKDOWN":^20}\033[m')
tupla = (int(input('Dígite um numero: ')),
         int(input('Dígite um numero: ')),
         int(input('Dígite um numero: ')),
         int(input('Dígite um numero: ')))

print('-='*35)
if tupla.count(9) > 0:
    print(f'O número 9 apareceu {tupla.count(9)} vezes')
else:
    print(f'O número 9 não apareceu')

if tupla.count(3) > 0:
    print(f'O número 3 apareceu na {tupla.index(3)}º posição')
else:
    print(f'O número 3 não apareceu')

print()

print(f'Os números pares foram:')
print('-='*35)
for i, v in enumerate(tupla):
    if v % 2 == 0:
        print(f'O número {v} na {i}º posição')
print()
