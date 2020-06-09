print(f'\033[40;31;1m{"Desafio":=^20}\033[m\n\033[33;1m{"A dor":^20}\033[m')
frase = input('Digite uma frase: ')
frase = frase.strip().upper()
print(f'''Quantas vezes aparece a letra A: {frase.count('A')}
Em que posição ela aparece a primeira vez: {frase.find('A')+1}
Em que posição ela apacrece a ultima vez: {frase.rfind('A')+1}
''')
