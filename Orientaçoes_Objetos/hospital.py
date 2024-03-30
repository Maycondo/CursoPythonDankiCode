from datetime import date

class Paciente:

    def  __init__(self, name, age, cpf, email):
        self.name = name
        self.age = age
        self.cpf = cpf
        self.email = email


    @classmethod
    def ageAnoNascimeto(cls, nascimento):
        return date.today().year - nascimento

class Medico:
    pass




paciente = Paciente("Beatriz", 23, "000.000.00-0", "beatriz@gmail.com")
print(paciente.__dict__)
print(paciente.ageAnoNascimeto(2001))