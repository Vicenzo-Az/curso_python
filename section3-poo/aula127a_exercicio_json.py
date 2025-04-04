# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

CAMINHO_ARQUIVO = 'aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Jo', 31)
p2 = Pessoa('Jaa', 32)
p3 = Pessoa('Ju', 33)
bd = [vars(p1), p2.__dict__, vars(p3)]

def fazer_dump():
    with open (CAMINHO_ARQUIVO, 'w') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

# if __name__ == '__main__':
#     print('Ele é main')
#     fazer_dump()