# Operadores lógicos 
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser 
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy
# 0 0.0 '' False
# Também exite o tipo None que é
# usado para representar um não valor
entrada = input('[e]ntrar [s]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '12345'

if entrada == 'e' and senha_digitada == senha_permitida:
    print('    Entrou')
elif entrada == 's':
    print('    Sair')
else:
    print('    Senha não informada')
