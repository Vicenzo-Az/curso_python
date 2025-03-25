# Operadores lógicos 
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser 
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy
# 0 0.0 '' = False
# Também exite o tipo None que é
# usado para representar um não valor
entrada = input('[e]ntrar [s]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '12345'

if (entrada == 'e' or entrada == 'E') and senha_digitada == senha_permitida:
    print('    Entrou')
else:
    print('    Sair')

# print(True and False and True)
print(0 or False or 0 or 'abc' or True)

senha = input('Senha: ') or 'Sem senha'
print(senha)