"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erroa ao tentar executar
"""
numero_str  = input('Vou dobrar o número que vc digitar: ')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_float} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')

try:
   numero_float = float(numero_str)
   print('FLOAT:', numero_float)
   print(f'O dobro de {numero_float} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')
