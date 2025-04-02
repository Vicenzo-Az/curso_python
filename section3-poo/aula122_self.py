# Entendendo self em classes Python
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

    def quebrar(self):
        print(f'{self.nome} quebrou...')

fusca = Carro('fusca')
print(fusca.nome)
fusca.acelerar()
Carro.acelerar(fusca)

print('')

celta = Carro('celta')
print(celta.nome)
celta.acelerar()
celta.quebrar()