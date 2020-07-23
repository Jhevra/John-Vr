from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 53', 'PALINDROMORRrr')
frase = input('Dígite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase não é um palindromo')