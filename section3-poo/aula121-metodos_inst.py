# Métodos em instâncias de classes Python

# class Carro:
#     def __init__(self, alguma_coisa='sei lá'):
#         self.nome = alguma_coisa

# fusca = Carro()
# print(fusca.nome)

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('celta')
print(celta.nome)
celta.acelerar()