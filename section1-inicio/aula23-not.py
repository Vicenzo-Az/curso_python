# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
senha = input('Senha: ')

if senha != '12345':
    print('Senha incorreta')

if not senha:
    print('Você não digitou nada')
