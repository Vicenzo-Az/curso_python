"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""
condicao = True
i = 1

while condicao:
    nome = input('Digite seu nome: ')
    print(i)
    i += 1
    if i == 11:
        condicao = False
    if nome == 'sair':
        break