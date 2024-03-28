
lista = ["item1", "item2", "item3"]
tupla = ("item1", "item2", "item3")

dicionario = {"name": "Michael", "surname": "Douglas", "age": "20 anos"}
print(dicionario)

# Acessando os valores do dicionário
dicionario["name"] = "Pedro"
print(dicionario)

# Adicionar  um novo par chave-valor no dicionário
dicionario.update({"nascimento": "2003"})
print(dicionario)

# A funçao popitem() removem o ultimo item adicionado ao dicionario
dicionario.popitem()
print(dicionario)

# Remove a chave e com valor explecifico 
""""
dicionario.pop()
print(dicionario)
"""

for x in enumerate(dicionario.items()):
    print(x)


# Crinado uma copia de  um dicionário
dicionario = dicionario.copy()
print(dicionario)


