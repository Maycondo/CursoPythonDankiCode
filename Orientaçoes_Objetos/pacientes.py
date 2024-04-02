"""
Paradigma Imperaivo - Fortran - Sequencia, Decisao e a Interaçao
paradigma Estrturado - C - structs 
paradigma Procedural - Python

"""

# Paradigma Imperativo

"""
def Registra(name, surname, age, cpf, gmail):
    paciente = {
        "name": name, 
        "surname": surname, 
        "age": age, 
        "cpf": cpf,
        "gmail": gmail
}
    return paciente
"""


# Reuso e coesao

# Paradig Orienta a Objetos

"""
Class
Objeto 
Construtor

"""
"""

Conceitos Estruturais

Class - Um conjunto de objetos com as mesmas caracteristicas 
Objeto - Representaçao do mundo real como um tipo de dados de um classe
Contrutor - E um funçao criada implicitamente com o mesmo nome da classe 
Atributo - São as variaveis de uma class

"""


class Paciente:
    
    def __init__(self, name, surname, age, cpf, gmail):
        self.name = name
        self.surname = surname
        self.age = age
        self.cpf = cpf
        self.gmail = gmail

        return #print (f"{self.name}, {self.surname}, {self.age}, {self.cpf}, {self.gmail}")


#paciente =  Paciente("Fulano", "De Tal", 25, "12345678909", "fulanodetal@gmail.com")
    

# -------------------------------------------------------- !
    

"""
Simulaçao de Eventos Discretos -> Paradigma Orientado á Objetos


Relacao -> Destancando funçoes e variáveis


-----------------------------------------

Conceitos Estruturais

-Classe 

Classe é uma estrutura que abstrai um conjunto de objetos com caracteristicas
similares. Definindo o comportamento dos seus objetos atraves
das estruturas:

1 - Atributos
2 - Metodos

A classe define um tipo de dado abstrato

"""

# Abtraçao
# Reuso e a Coesao
# Acomplamento, herança, polimorfismo, GAP semantico

"""

Conceitos Fundamentos

-Abstraçao

Processo pelo qual se isolam atributos de um objeto,
considerando os que certos grupos de objetos tenham em comum.

-Reuso

Não existe pior pratica em programaçao do que repetir codigo.

"""




