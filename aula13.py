nome = 'Pessoa teste'
altura = 1.80
peso = 95
imc = peso / (altura * altura)

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso}kg e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)