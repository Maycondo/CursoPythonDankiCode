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
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def extrato(self):
        taxa = 0.50
        self.saldo = self.saldo - taxa
        print(f"Saldo: {self.saldo}")

    def depositar(self, valor):
        self.saldo =  self.saldo + valor

    def sacar(self, valor):
        self.saldo = self.saldo - valor


# Instancias de Classe Conta 

conta1 = Conta(123 , "Ana Silva", 500)
conta2 = Conta(232 , "Joãozinho Silva", 800)
conta3 = Conta(265 , "Beatriz Ferreira", 900)

print(conta1.titular)
print(conta2.titular)

print(conta1.__dict__)
print(conta2.__dict__)
print(conta3.__dict__)

# Metodo da Class 
Conta.retornarCodigo() # Concençao
conta1.retornarCodigo()

# Metodo Estatico 
Conta.retornarCodigoBanco()
