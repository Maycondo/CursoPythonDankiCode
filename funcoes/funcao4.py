

"""
def imprimir_name(name, surname, age):
    print("Name: ", name)
    print("Surname: ", surname)
    print("Age: ", age)


name = 'Maycon'
surname = "Douglas"
age = 23

imprimir_name(name=name, surname=surname, age=age)

"""

# Parametro Padrao

"""

def imprimir_imovel(nameImovel, n_quartos, vagasGaragem=None):
    print("-----")
    print("Titulo: ", nameImovel)
    print("Quartos: ", n_quartos)
    if vagasGaragem != None:
        print("Vagas na garagem: ", vagasGaragem)

# Exemplos de n de argumentos <= b dos paramentos
imprimir_imovel("Casa 3 quartos - SP", 3)
imprimir_imovel("Apartemento - MG", 2 ,1)

"""

# O Argumentos Arbitrario *args que receber varios argumento

def imprimir_imovel(nameImovel, n_quartos, vagasGaragem=None, *args):
    print("-----")
    print("Titulo: ", nameImovel)
    print("Quartos: ", n_quartos)
    if vagasGaragem != None:
        print("Vagas na garagem: ", vagasGaragem)



def imprimir_nomes(names):
    print(names)
    print(type(names))


lista = ["Maycon", "Luiza", "Fabiana"]
imprimir_nomes(*lista)