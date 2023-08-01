# Positional only
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="fiat", motor="1.0", combustivel="Gasolina")
criar_carro("Palio", 1999, "ABC-1234", "fiat", "1.0", "Gasolina")
# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="fiat", motor="1.0", combustivel="Gasolina") # exemplo inválido

# keyword only
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="fiat", motor="1.0", combustivel="Gasolina")

# Keyword and positional only
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="fiat", motor="1.0", combustivel="Gasolina")

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operacao {a} +  {b} = {resultado}")

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)

op = somar

print(op(1,23))