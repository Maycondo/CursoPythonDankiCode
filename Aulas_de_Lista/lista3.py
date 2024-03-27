# index
lista = ["carro", "barco", "aviao"]
print(lista)


for x in lista:
    print(x)

print(len(lista))  # conta o número de elementos na lista


for x in range(3):
    print(x)

for x in range(len(lista)):
    print(x)

texto = "Carro, aviao"
lista2 = list(texto)
print(lista2)

texto = texto.split(',')
print(texto)


lista.append("Moto") # Adicionar um elemento no final da lista

lista.insert(1, "bicicleta") # Insiri um elemento no index desejado sem renovo o que ja tem

lista.extend(["moto","onibus"]) # Adiciona varios itens em uma só vez