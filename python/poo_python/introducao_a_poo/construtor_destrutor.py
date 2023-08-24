class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
      print('Destruindo a instância')
    
    def falar(self):
       print('auau')

def criar_cachorro():
  c = Cachorro('Zeus', 'Branco e Preto', False)
  print(c.nome)

c = Cachorro('Chappie', 'Amarelo')
c.falar()

print('Ola mundo')

del c
# criar_cachorro()

print('Ola mundo')
print('Ola mundo')
print('Ola mundo')