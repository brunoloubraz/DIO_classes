nome = "Bruno"
idade = 24
profissao = "Dev"

print("Olá eu sou o {} tenho {} anos e quero ser {}".format(nome, idade, profissao))
print("Olá eu sou o {0} tenho {2} anos e quero ser {1}".format(nome, idade, profissao))
print("Olá eu sou o {nome} tenho {idade} anos e quero ser {profissao}".format(nome=nome, idade=idade, profissao=profissao))

print(f"Olá eu sou o {nome} tenho {idade} anos e quero ser {profissao}")

PI = 3.14159

print(f"valor de PI:{PI: .3f}")
print(f"valor de PI: {PI:10.2f}")