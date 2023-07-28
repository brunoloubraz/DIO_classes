lista = []

lista.append(1)
lista.append("Python")
lista.append([40,30,20])
print(lista)


l2 = lista.copy()
print(id(l2))


lista.clear()
print(lista)


cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))

linguagens = ["python", "js", "c"]

print(linguagens)

linguagens.extend(["java","csharp"])

print(linguagens)


print(linguagens.index("java"))


print(linguagens)
linguagens.pop()
linguagens.pop(0)
print(linguagens)


linguagens.remove("c")
print(linguagens)

linguagens.reverse()
print(linguagens)



linguagens.extend(["c", "csharp", "python"])
print(linguagens)


linguagens.sort()
print(linguagens)

linguagens.sort(reverse=True)
print(linguagens)

linguagens.sort(key=lambda x: len(x))
print(linguagens)

linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

print(len(linguagens))

# abaixo é a mesma coisa que acima, muda só a forma de fazer
print(sorted(linguagens, key=lambda x: len(x)))

print(sorted(linguagens, key=lambda x: len(x), reverse=True))

print(sorted(linguagens, reverse=False))

