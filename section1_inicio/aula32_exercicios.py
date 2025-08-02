"""
1
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num_usuario = input("Digite um número: ")

# if num_usuario.isdigit():
try:
    num_usuario = int(num_usuario)
    if num_usuario % 2 == 0:
        print('Este número é par.')
    else:
        print('Este número é impar.')
except ValueError:
    print('Isso não é um número. :(')


"""
2
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input("Digite a hora (somente número): ")

try:
    hora_int = int(hora)

    if hora_int >= 0 and hora_int <= 11:
        print('Bom dia')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde')
    elif hora_int >= 18 and hora_int <= 23:
        print('Boa noite')
    else:
        print('Erro')
except ValueError:
    print('Digite um número inteiro.')


"""
3
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
primeiro_nome = input("Digite o primeiro nome: ")
if len(primeiro_nome) <= 4:
    print('Seu nome é curto.')
elif len(primeiro_nome) > 4 and len(primeiro_nome) <= 6:
    print('Seu nome é normal')
elif len(primeiro_nome) > 6:
    print('Seu nome é muito grande')
else:
    print('erro')