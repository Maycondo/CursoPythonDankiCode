class Aluno:
    def __init__(self , name, age , matricula):
        self.name = name
        self.age = age
        self._matricula = matricula
        self.__notas = None


