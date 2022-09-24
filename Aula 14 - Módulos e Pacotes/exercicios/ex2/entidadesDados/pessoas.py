class Empregado():
    def __init__(self,id,nome,cargo,id_projeto):
        self._id = id
        self._nome = nome
        self._cargo = cargo
        self._id_projeto = id_projeto

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
        self._nome = nome

    @property
    def cargo(self):
        return self._cargo
    @cargo.setter
    def cargo(self,cargo):
        self._cargo = cargo

    @property
    def id_projeto(self):
        return self._id_projeto
    @id_projeto.setter
    def cargo(self,id_projeto):
        self._id_projeto = id_projeto

    def toJson(self):
        fdict = {"id":self._id,
                 "nome":self._nome,
                 "cargo":self._cargo,
                 "id_projeto":self._id_projeto
                 }
        return fdict
    

class Cliente():
    def __init__(self,id,nome,id_projeto):
        self._id = id
        self._nome = nome
        self._id_projeto = id_projeto

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
        self._nome = nome

    @property
    def id_projeto(self):
        return self._id_projeto
    @id_projeto.setter
    def cargo(self,id_projeto):
        self._id_projeto = id_projeto


    def toJson(self):
        fdict = {"id":self._id,
                 "nome":self._nome,
                 "id_projeto":self._id_projeto
                 }
        return fdict


