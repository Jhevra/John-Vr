from time import sleep
print(f'''\033[40;31;1m{"Desafio 46":=^20}\033[m\n\033[33;1m{"ANONOVOR":^20}\033[m''')
for fogos in range(1, 10):
    print(f'{fogos}...')
    sleep(1)
print(f'''*******************************
              BUM!
*******************************''')