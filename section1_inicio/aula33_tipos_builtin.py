"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = 'qwerty qwerty'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
# string = 'ABC'

print(string)
print(outra_variavel)
print(string.capitalize())