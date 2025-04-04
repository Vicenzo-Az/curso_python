# Atributos de classe
class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)

print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

dados = {'idade': 35, 'outra': 'coisa'}
# p1 = Pessoa(**dados)
# p1.nome = 'EITA'

p1.__dict__['outra'] = 'coisa'
p1.__dict__['nome'] = 'EITA'
del p1.__dict__['nome'] 
print(p1.__dict__)
print(vars(p1))
# print(p1.outra)