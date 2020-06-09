print(f'\033[40;33;1m{"Desafio 73":=^20}\033[m\n\033[40;31;1m{"BREAKDOWN":^20}\033[m')
tabela = ('Palmaeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético', 'Athletico', 'Cruzeiro',
          'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'Sport',
          'América', 'Vitória', 'Paraná')

print('-='*50)
print(f'Os cinco primeiros colocados foram: {tabela[0:5]}')
print('-='*50)
print(f'Os ultimos quatro colocados fora: {tabela[16:]}')
print('-='*50)
print(f'{sorted(tabela)}')
print('-='*50)
print(f'O Chapecoense está na posição {tabela.index("Chapecoense")}')
