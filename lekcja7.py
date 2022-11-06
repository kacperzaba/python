zmienna = 1
zmienna2 = "ABC"
lista = [1, 2, "c", "d", "e", ]
print(lista)
print(lista[0:2])
lista[2] = 3
print(lista)
tekst = "Hello world"
print(tekst[0])
print(lista + ["f", "g"])
print(lista * 3)
print("Ilość elementów: ", len(lista))
lista.append("f")
print(lista)
lista.append(["g", "h"])
print(lista)
print(lista[6][:2])
lista.insert(3, 3)
print(lista)
print("Ilość: ", lista.count(3))
print("Index: ", lista.index(3))
lista.remove("f")
print(lista)
lista2 = [1, 20, 35, -5, 0]
print("MIn: ", min(lista2))
print("Max ", max(lista2))
lista2.sort()
print(lista2)
lista2.reverse()
print(lista2)
lista2.clear()
print(lista2)
