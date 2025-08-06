"""
Calculadora com while
"""
while True:
    # Digito 1
    valor_um = input('Digite um valor 1: ')
    proceed = 0
    while proceed == 0:
        try:
            valor_um = float(valor_um)
            proceed = 1

        except ValueError:
            print('Não é um número válido.')
            valor_um = input('Digite um valor: ')

    # Digito 2
    valor_dois = input('Digite um valor 2: ')
    proceed = 0
    while proceed == 0:
        try:
            valor_dois = float(valor_dois)
            proceed = 1

        except ValueError:
            print('Não é um número válido.')
            valor_dois = input('Digite um valor: ')

    # Operador
    print('Escolha a operação:\n[1] Divisão    [2] Multiplicação\n[3] Subtração  [4] Adição')
    operacao = input('Digite: ')

    while operacao != '1' and operacao != '2' and operacao != '3' and operacao != '4':
        operacao = input('Operação inválida\nDigite novamente: ')

    resultado = 0
    if operacao == '1':
        resultado = valor_um / valor_dois
    elif operacao == '2':
        resultado = valor_um * valor_dois
    elif operacao == '3':
        resultado = valor_um - valor_dois
    elif operacao == '4':
        resultado = valor_um + valor_dois

    print(f'Resultado: {resultado}')

    continuar = input('Deseja continuar? [s/n] ').lower().startswith('n')

    if continuar:
        break

        