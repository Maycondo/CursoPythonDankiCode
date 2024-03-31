from datetime import date

class Paciente:

    def  __init__(self, name, age, cpf, email):
        self.name = name
        self.age = age
        self.cpf = cpf
        self.email = email


    @classmethod
    def ageAnoNascimeto(cls, name, nascimento, cpf, email):
        age = (date.today().year - nascimento)
        return Paciente(name, age, cpf, email)

class Medico:
    pass


paciente = Paciente("Beatriz", 23, "000.000.00-0", "beatriz@gmail.com")
print(paciente.__dict__)
print(paciente.ageAnoNascimeto(2001))