class Bicicleta:
  def __init__(self, cor, modelo, ano, valor, aro = 18):
    self.cor = cor
    self.modelo = modelo
    self.ano = ano
    self.valor = valor
    self.aro = aro
  
  def buzinar(self):
    print("Plim plim plim...")

  def parar(self):
    print("Parado")
    print("Bicicleta parada")

  def correr(self):
    print("Vrummmmmmmmmmmmmmmmmmm...")
    print("Bicicleta correndo")

  # def __str__(self):
  #   return f"Bicicleta: Cor: {self.cor}, Modelo: {self.modelo}, Ano: {self.ano}, Valor: {self.valor}"

  def __str__(self):
    return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

# b1 = Bicicleta('Vermelha', 'Caloi', 2022, 600)
# b1.buzinar()
# b1.buzinar()
# b1.parar()
# b1.correr()
# print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("Verde", "Monark", 2000, 189)
Bicicleta.buzinar(b2)
print(b2)
