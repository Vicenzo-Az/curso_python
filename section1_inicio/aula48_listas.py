"""
Listas en Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append, insert, pop, del, clear, extend, +
Create, Read, Update, Delete
Criar, ler, alterar, apagar = lista[i (CRUD)]
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
#         0     1    2      3   4
#        -5    -4   -3     -2  -1
lista = [123, True, 'luy', 1.2, []]

print(lista[2].upper())

lista[-3] = 'ectro'

print(lista)

print()
# ----------------------------------------------

lista = [10, 20, 30, 40]
lista[2] = 300
del lista[2]
numero = lista[2]
print(numero)

lista.append(50)  # Adiciona no final
lista.pop()  # Remove no final
print(lista)
lista.append(60)
lista.append(1)
ultimo_valor = lista.pop(2)
lista.pop()
print(lista, 'Removido:', ultimo_valor)