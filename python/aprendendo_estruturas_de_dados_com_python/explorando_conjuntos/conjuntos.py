print(set([1,2,3,1,3,4]))
print(set("abacaxi"))
print(set(("palio", "gol", "celta", "palio")))


linguagens = {"python", "java", "python"}
print(linguagens)

numeros = {1, 2, 3, 4}

numeros= list(numeros)

print(numeros[0])

for numero in numeros:
    print(numero)

for index, numero in enumerate(numeros):
    print(f"{index}: {numero}")

# union
conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))

# intersection
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b))

# diference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print("====difference")
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))


conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print("====symmetric_difference")
print(conjunto_a.symmetric_difference(conjunto_b))

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}
print("====issubset")
print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}
print("====isdisjoint")
print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

conjunto_al = {1, 2, 3, 4, 5}
conjunto_bl = {6, 7, 8, 9}
conjunto_cl = {1, 0}

conjunto_al.isdisjoint(conjunto_bl)
conjunto_al.isdisjoint(conjunto_cl)

# add

sorteio = {1, 23}

sorteio.add(25)
sorteio.add(42)
sorteio.add(25)

print(sorteio)

sorteio.copy()

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

numeros.discard(1)
numeros.discard(45)
print(numeros)

numeros.pop()
print(numeros)

numeros.remove(5)
print(numeros)

print(len(numeros))

print(1 in numeros)
print(4 in numeros)

sorteio.clear()