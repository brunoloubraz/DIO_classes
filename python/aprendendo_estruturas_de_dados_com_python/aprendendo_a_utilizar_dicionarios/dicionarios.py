pessoa = {"nome": "Bruno", "idade": 28}

pessoa = dict(nome= "Bruno", idade= 28)

pessoa["telefone"] = "1234-5678"


# ---

dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

print(dados["nome"])
print(dados["idade"])
print(dados["telefone"])

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9998-1781"



# dados aninhados
contatos = {
    "bruno@gmail.com": {"nome": "bruno", "telefone": "3213-4930"},
    "Karina@gmail.com": {"nome": "karina", "telefone" : "3249-5893"},
}
print(contatos["Karina@gmail.com"]["nome"])

# utilizando iteracao

for chave in contatos:
    print(chave, contatos[chave])

print("=============")

for chave, valor in contatos.items():
    print(chave, valor)