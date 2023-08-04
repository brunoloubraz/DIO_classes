def exibir_mensagem():
    print("Hello World!")

def exibir_mensagem2(nome):
    print(f"seja bem vindo {nome}!")

def exibir_mensagem3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def func_3():
    print("hello World!")

def salvar_carro(marca, modelo, ano, placa):
    print(f"""Carro inserido com sucesso 
  Marca: {marca}
  Modelo: {modelo}
  Ano: {ano}
  Placa: {placa}
""")
    
exibir_mensagem()
exibir_mensagem2(nome="Bruno")
exibir_mensagem3()
exibir_mensagem2(nome="Chappie")

print(calcular_total([10,20,34]))
print(retorna_antecessor_e_sucessor(10))
print(func_3())

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo= "Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca":"Fiat", "modelo":"Palio", "ano":1999, "placa":"ABC-1234"})



def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem  = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Zen of Python", "Beautiful is better than ugly", autor="Tim Peters", ano= 1999)