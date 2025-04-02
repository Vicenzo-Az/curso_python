# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de 
# classes.

# string = 'luy'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('ectro', 'luy')
# p1.nome = 'ectro'
# p1.sobrenome = 'luy'

p2 = Pessoa('sponsored', 'by')
# p2.nome = 'sponsored'
# p2.sobrenome = 'by'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)