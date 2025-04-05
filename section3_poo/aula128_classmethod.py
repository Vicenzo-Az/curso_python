# Métodos de classe + factories
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receveremos a própria classe.
class Pessoa:
    ano = 2025  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    # @staticmethod
    @classmethod
    def metodo_de_classe(cls):  # cls == classe
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_pessoa_anonima(cls, idade):
        return cls('Anônimo', idade)


p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa.criar_pessoa_anonima(39)

print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(Pessoa.ano)
Pessoa.metodo_de_classe()