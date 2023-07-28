frutas = ["laranja", "maca", "uva"]
print(frutas)
frutas = []

letras = list("python")
print(letras)
numeros = list(range(10))
print(numeros)
carro = ["ferrari", "F8", 4200000, 2020, 2900, "são paulo", True]

frutas = ["maçã", "laranja", "maca", "uva"]
print(frutas[0])
print(frutas[-1])

# Lista Aninhada

matriz = [
  [1, "a", 2],
  ["b", 3, 4],
  [6, 5, "c"]    
]

print(matriz[0])
print(matriz[0][0])
print(matriz[1][-1])

lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


# filtro versao 1
numeros = [1, 30, 21, 2, 9,65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

# filtro versao 2 compreehennsion
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)


# Modificando valores versao 1
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(f" esse é o quadrado {quadrado}")

# Modificando valores versão 2
quadrado = [numero ** 2 for numero in numeros]

print(f" esse é o quadrado comprehension{quadrado}")