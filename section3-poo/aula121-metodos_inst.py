# Métodos em instâncias de classes Python
class Carro:
    def __init__(self, alguma_coisa='sei lá'):
        self.nome = alguma_coisa

fusca = Carro()
print(fusca.nome)