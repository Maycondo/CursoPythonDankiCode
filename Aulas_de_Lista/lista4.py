# index 
lista = ["carro", "barco", "aviao"]


# lista.pop() remove elementos da lista, Tambem pode removo  um elemento especificado por indice
# lista.remove(lista[1])   #Remove o elemento barco, pois é acessado pelo indice 1
# del lista # Remove ah lista completamente, Utilizando o index [] pode mos deletar apenas os valores desejados


carrinho_de_compras = ["produto1", "produto2", "produto3"]
carrinho_de_compras.clear( )    #Limpa todos os itens do carrinho de compras

for x in range(len(lista)):
    print(x, lista[x])