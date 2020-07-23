from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 26', 'AAArr')

nome = input('Frase: ').lower().strip()
print(f'''A letra A aparece {nome.count('a')} vezes
A primeira letra A aparece na {nome.index('a')+1} posição
A ultima letra A aparace na {nome.rindex('a')} posição''')