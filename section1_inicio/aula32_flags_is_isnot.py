"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = [e ou não é (tipo, valor, identidade)
id = Identidade
"""
# condicao = False
#
# if condicao:
#     passou_no_if = True  # ruim
#     print('Faça algo')
# else:
#     print('Não faça algo')
#
# print(passou_no_if)


# Melhor versão

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if)

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')