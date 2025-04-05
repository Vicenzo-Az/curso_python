# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que está dentro da
# classe, mas não tem acesso ao self ne, ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.
class Classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('Oi', args, kwargs)

    def funcao(self, *args, **kwargs):
        print('Oi', args, kwargs)


c1 = Classe()
c1.funcao_que_esta_na_classe(1, 2, 3)
c1.funcao(1, 2, 3)
Classe.funcao_que_esta_na_classe(nomeado=1)
c1.funcao(nomeado=1)