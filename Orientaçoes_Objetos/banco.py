"""

class Conta:

    def  __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def extrato(self):
        print(f"Saldo: {self.saldo}$ Reais")

    def depositar(self, valor):
        self.saldo =  self.saldo + valor
        return self.saldo

    def sacar(self, valor):
        self.saldo = self.saldo - valor
        return self.saldo



Maycon = Conta("454", "Maycon Douglas", 1000)
print(f"O titular {Maycon.titular} da conta {Maycon.numero}, depositou {Maycon.depositar(5050)}$ Reais") # Saldo
Maycon.extrato()
print(Maycon.sacar(3000))  

"""


"""

Visibiidade - Modificador de Acesso

Privada (private) - restritiva -> Define que os atributos e metodos só podem ser manipulados dentro da class.
Protegida (projected) - intermediaria -> Define que os atributos e metodos só podem ser manipulados dentro da class e nas 
class que herdam da class onde foram definidos.

publica (public) - menos restritiva -> Define qe os atributos e metodos são acessivéis em qualquer lugar.

"""


class Conta:

    # Metedos de class 
    @classmethod
    def retornarCodigo(cls):
        print("Codigo: 555")

    @staticmethod
    def retornarCodigoBanco():
        return 12345

     # Atributo de class 
    taxa = 0.50
     # Atributos de instancias
    
    def  __init__(self, numero, titular, saldo):
        self._numero = numero # Visibilidade protegida (protected)
        self.titular = titular # Visibilidade publica (public)
        self.__saldo = saldo # Visibilidade privada (private)
        self.__historico = [saldo]

    def saldo(self):
        print(f"Saldo: R${self.__saldo}")

    def His_transaçao(self, saldo):
        self.__historico.append(saldo)

    def extrato(self):
        taxa = 0.50
        self.__saldo = self.__saldo - taxa
        for saldo in self.__historico:
            print(f"Saldo: {self.__saldo}")

    def depositar(self, valor):
        self.__saldo =  self.__saldo + valor
        self.His_transaçao(self.__saldo)

    def sacar(self, valor):
        self.__saldo = self.__saldo - valor
        self.His_transaçao(self.__saldo)
    
    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)


# Instancias de Classe Conta 

conta1 = Conta(123 , "Ana Silva", 500)
conta2 = Conta(232 , "Joãozinho Silva", 800)    
conta3 = Conta(265 , "Beatriz Ferreira", 900)

conta3.transferir(300, conta1)
conta1.extrato()
conta3.extrato()



"""
print(conta1.titular)
print(conta2.titular)

print(conta1.__dict__)
print(conta2.__dict__)
print(conta3.__dict__)
"""

# Metodo da Class 
#Conta.retornarCodigo() # Concençao
#conta1.retornarCodigo()

# Metodo Estatico 
#onta.retornarCodigoBanco()
