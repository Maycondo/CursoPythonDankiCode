# Sets: coleçao nao ordenada, imutavel e que nao permite valores dublicados

# Os sets tambem sao conhecidos como conjuntos


conjunto = {"item1", "item2", "item3"}
print(type(conjunto))
print(conjunto)
print(len(conjunto))  # Retorna o tamanho do conjunto (quantidade de elementos)


conjunto = {"item1", "item2", "item3", "item4"}

for x in conjunto:
    print(x)