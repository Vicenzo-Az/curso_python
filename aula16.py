# if / elif      / else
# se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? e. entrar  s. sair ')

if entrada == 'e':
    print('Você entrou no programa')

elif entrada == 's':
    print('Você saiu')

else:
    print('FATAL ERROR:\nUNIDENTIFIED CHARACTER')