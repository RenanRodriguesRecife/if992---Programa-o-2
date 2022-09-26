class Cargo:
    def __init__(self,id,nome,salario):
        self._id = id
        self._nome = nome
        self._salario = salario

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def salario(self):
        return self._salario
    @salario.setter
    def salario(self, salario):
        self._salario = salario


class Funcionario:
    def __init__(self,id,nome,dataC,diasFM,diasFA,Cargo):
        self._id = id
        self._nome = nome
        self._dataC = dataC #data de contratação
        self._diasFM = diasFM #dias de férias máximo
        self._diasFA = diasFA #dias de férias atual
        self._Cargo = Cargo

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def dataC(self):
        return self._dataC
    @dataC.setter
    def dataC(self, dataC):
        self._dataC = dataC

    @property
    def diasFM(self):
        return self._diasFM
    @diasFM.setter
    def diasFM(self, diasFM):
        self._diasFM = diasFM

    @property
    def diasFA(self):
        return self._diasFA
    @diasFA.setter
    def diasFA(self, diasFA):
        self._diasFA = diasFA

    @property
    def Cargo(self):
        return self._Cargo
    @Cargo.setter
    def Cargo(self, Cargo):
        self._Cargo = Cargo   




class FuncionarioView:
    def mostrarFuncionario(self, id,nome,dataC,diasFM,diasFA,Cargo):
        print("Funcionario:")
        print(f"id: {id}")
        print(f"Nome: {nome}")
        print(f"dataC: {dataC}")
        print(f"diasFM: {diasFM}")
        print(f"diasFA: {diasFA}")
        print(f"Cargo: {Cargo.nome}")


class CargoView:
    def mostrarCargo(self, id,nome,salario):
        print("Cargo:")
        print(f"id: {id}")
        print(f"Nome: {nome}")
        print(f"salario: {salario}")
                

class FuncionarioController:
    def __init__(self, model: Funcionario, view: FuncionarioView):
       	self.model = model
       	self.view = view
    def atualizarView(self):
        self.view.mostrarFuncionario(self.model.id,self.model.nome,self.model.dataC,self.model.diasFM,self.model.diasFA,self.model.Cargo)

    def setIdFuncionario(self, id):
        self.model.id = id
    def getIdFuncionario(self):
        return self.model.id

    def setNomeFuncionario(self, nome):
        self.model.nome = nome
    def getNomeFuncionario(self):
        return self.model.nome
    
    def setDataCFuncionario(self, dataC):
        self.model.dataC = dataC
    def getDataCFuncionario(self):
        return self.model.dataC

    def setDiasFMFuncionario(self, diasFM):
        self.model.diasFM = diasFM
    def getDiasFMFuncionario(self):
        return self.model.diasFM

    def setDiasFAFuncionario(self, diasFA):
        self.model.diasFA = diasFA
    def getDiasFAFuncionario(self):
        return self.model.diasFA

    def setCargoFuncionario(self, Cargo):
        self.model.Cargo = Cargo
    def getCargoFuncionario(self):
        return self.model.Cargo

class CargoController:
    def __init__(self, model: Cargo, view: CargoView):
        self.model = model
        self.view = view
        
    def atualizarView(self):
        self.view.mostrarCargo(self.model.id, self.model.nome, self.model.salario)

    def setIdCargo(self, id):
        self.model.id = id
    def getIdCargo(self):
        return self.model.id

    def setNomeCargo(self, nome):
        self.model.nome = nome
    def getNomeCargo(self):
        return self.model.nome

    def setSalarioCargo(self, salario):
        self.model.salario = salario
    def getSalarioCargo(self):
        return self.model.salario




#DEMO

def recebeCargoDaBD(id,nome,salario):
    cargo = Cargo(id,nome,salario)
    return cargo

def recebeFuncionarioDaBD(id,nome,dataC,diasFM,diasFA,Cargo):
    funcionario = Funcionario(id,nome,dataC,diasFM,diasFA,Cargo)
    return funcionario

if __name__ == "__main__":
        cargo = recebeCargoDaBD(id,"programador",1000000)
        funcionario = recebeFuncionarioDaBD(1,"renan",32,32,32,cargo)
        view = FuncionarioView()
        controlador = FuncionarioController(funcionario , view)
        controlador.atualizarView()
        controlador.setNomeFuncionario("Renan")
        controlador.atualizarView()





