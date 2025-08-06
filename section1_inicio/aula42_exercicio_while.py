frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'

contador = 0
count_max = 0
letra = ''
while contador <= len(frase):
    int_frase = int(frase.count(frase[contador]))
    if int_frase > count_max:
        count_max = int_frase
        letra = frase[contador]

print(f'Letra que mais se repetiu: {letra}\nEla apareceu {count_max} vezes!')