contatos = {
    "bruno@gmail.com": {"nome": "bruno", "telefone": "3213-4930"},
    "Karina@gmail.com": {"nome": "karina", "telefone" : "3249-5893"},
}

# copy
copia = contatos.copy()

#fromKeys
print(contatos.fromkeys(["nome", "telefone"]))
print(contatos.fromkeys(["nome", "telefone"], "vazio"))

# get
# print(contatos["chave"]) ---> Erro
print(contatos.get("chave"))
print(contatos.get("chave", {}))
print(contatos.get("bruno@gmail.com", {}))

# items
print(contatos.items())


# keys
print(contatos.keys())

# pop
print(contatos.pop("nomegenerico@gmail.com", "nao encontrou nenhum email assim"))
# contatos.pop("Karina@gmail.com")
# print(contatos)

# popitem
# contatos.popitem()
print(contatos)

# setdefault
print("==========setdefault==========")
contato = {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")
print(contato)
# contato.setdefault("idade", 28)
# print(contato)

# update
print("========update=========")
contat = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}  
}

contat.update({"guilherme@gmail.com" : {"nome": "Gui"}})
print(contat)

contat.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
print(contat)

# values
print(contatos.values())

# in
print("bruno@gmail.com" in contatos)
print("macacoprego@gmail.com" in contatos)
print("telefone" in contatos["bruno@gmail.com"])
print("idade" in contatos["bruno@gmail.com"])

# del
del contatos['bruno@gmail.com']["telefone"]
print(contatos)
del contatos["Karina@gmail.com"]
print(contatos)

# clear
contatos.clear()
print(contatos)