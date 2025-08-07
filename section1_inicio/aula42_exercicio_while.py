frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'

count_max = 0
maior_letra = ''

i = 0
while i < len(frase):

    letra = frase[i].lower()
    if letra == ' ':
        i += 1
        continue
    num_frase= frase.count(letra)
    int_frase = int(num_frase)

    if int_frase > count_max:
        count_max = int_frase
        maior_letra = letra

    i += 1

print(f'Letra que mais se repetiu: {maior_letra}\nEla apareceu {count_max} vezes!')