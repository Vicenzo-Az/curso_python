"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[5:])
print(variavel[0:5])

print(len(variavel))
print(variavel[5:len(variavel)])

print(variavel[::-1])