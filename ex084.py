print(f'\033[40;33;1m{"Exercise 84":=^100}\033[m\n\033[40;31;1m{"Registration of people":^100}\033[m')
tempo = list()
principal = list()
mai = men = 0

while True:

    # Requesting user information
    tempo.clear()
    tempo.append(input('Name: '))
    tempo.append(float(input('Weight: ')))
    principal.append(tempo[:])

    # Analyzing the heaviest person
    for p in principal:
        if p == 0:
            mai = men = p[1]
        else:
            if p[1] > mai:
                mai = p[1]
            if p[1] < men:
                men = p[1]

    # Loop Closure or Repeat
    res = input('Do you want to continue registering people? [Y/N]: ').upper().strip()
    while res != 'Y' and res != 'N':
        res = input('\033[31;1mERROR!\033[m Do you want to continue registering people? [Y/N]: ').upper().strip()
    if res == 'N':
        break


print(f'''You have registered {len(principal)} people
The highest recorded weight was: {mai}Kg; ''', end='')

for pessoas in principal:
    if pessoas[1] == mai:
        print(f'[{pessoas[0]}]', end=' ')
print()

print(f'The lowest recorded weight was {men}Kg; ', end='')

for pessoas in principal:
    if pessoas[1] == men:
        print(f'[{pessoas[0]}] ', end=' ')
