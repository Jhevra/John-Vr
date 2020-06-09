print(f'\033[40;33;1m{"Desafio 77":=^20}\033[m\n\033[40;31;1m{"BREAKDOWN":^20}\033[m')
palavras = ('Palavras', 'Carro', 'Borboleta', 'Tenis', 'Andarilho', 'Trompete', 'Bicicleta', 'Teclado', 'Antena', 'Celular')
for p in palavras:
    print(f'\nNa palavra {p} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')