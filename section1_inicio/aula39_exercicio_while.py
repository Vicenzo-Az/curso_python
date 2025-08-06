"""
Iterando strings com while
"""
nome = input("Digite seu nome: ")
tamanho_nome = len(nome)
novo_nome = ''

cont = 0
while cont < tamanho_nome:
    novo_nome += nome[cont]

    if nome[cont] == ' ':
        cont += 1
        continue

    print(novo_nome)
    cont += 1

print('\n')
print('Process Terminated')