

def minha_funçao():
    return "Esse e minha funçao"

minha_funçao()


# Paramento de uma funçao

def imprime_nome(name: str):
    print(f'Olá {name}!')


#name = input("Qual e o seu nome?: ")
#imprime_nome(name)


def perso(name=str, surname=str):
    print (f"Hello! My name is {name} {surname}.")

perso1 = perso("Joao", "Silva")
print(perso1)