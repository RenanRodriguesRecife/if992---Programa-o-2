class Cargo():
    def __init__(self,id,nome,salario):
        self._id = id
        self._nome = nome
        self._salario = salario

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,id):
        self._id = id

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,nome):
        self._id = nome

    @property
    def salario(self):
        return self._salario
    @salario.setter
    def salario(self,salario):
        self._salario = salario

    def toJson(self):
        fdict = {"id":self._id,
                 "nome":self._nome,
                 "salario":self._salario,
                 }
        return fdict

class Projeto():
    def __init__(self,id,valor):
        self._id = id
        self._valor = valor

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,id):
        self._id = id

    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor(self,valor):
        self._valor = valor

    def toJson(self):
        fdict = {"id":self._id,
                 "valor":self._valor,
                 }
        return fdict
