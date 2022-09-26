from abc import ABC,abstractmethod


class OpcaoAlimento(ABC):
   @property
   @abstractmethod
   def preco(self):
       pass

   @preco.setter
   @abstractmethod
   def preco(self,valor):
       pass

   @property
   @abstractmethod
   def peso(self):
       pass

   @peso.setter
   @abstractmethod
   def peso(self, valor):
       pass

   @property
   @abstractmethod
   def proteina(self):
       pass

   @proteina.setter
   @abstractmethod
   def proteina(self, valor):
       pass

   @property
   @abstractmethod
   def gordura_total(self):
       pass

   @gordura_total.setter
   @abstractmethod
   def gordura_total(self, valor):
       pass

   @property
   @abstractmethod
   def gordura_saturada(self):
       pass

   @gordura_saturada.setter
   @abstractmethod
   def gordura_saturada(self, valor):
       pass

   @property
   @abstractmethod
   def carboidratos(self):
       pass

   @carboidratos.setter
   @abstractmethod
   def carboidratos(self, valor):
       pass

   @property
   @abstractmethod
   def acucares(self):
       pass

   @acucares.setter
   @abstractmethod
   def acucares(self, valor):
       pass

   @property
   @abstractmethod
   def sodio(self):
       pass

   @sodio.setter
   @abstractmethod
   def sodio(self, valor):
       pass










#IAbstraction
class Proteina(OpcaoAlimento):
   @abstractmethod
   def method(self):
      pass


#RefinedAbstractionA
class Presunto(Proteina):
   preco = 15.90
   peso = 201
   proteina = 15.2
   gordura_total = 3.8
   gordura_saturada = 0.9
   carboidratos = 39.2
   acucares = 5.9
   sodio = 683


   def __init__(self,sanduiche):  # leitura
       self.sanduiche = sanduiche
   
   def method(self):
       self.sanduiche.method(self.preco,self.peso,self.proteina,self.gordura_total,self.gordura_saturada,self.carboidratos,self.acucares,self.sodio)


#RefinedAbstractionB
class Frango(Proteina):
   preco = 13.00
   peso = 218
   proteina = 18.0
   gordura_total = 11.0
   gordura_saturada = 3.1
   carboidratos = 43.1
   acucares = 5.3
   sodio = 809
   
   def __init__(self,sanduiche):  # leitura
       self.sanduiche = sanduiche
   
   def method(self):
       self.sanduiche.method(self.preco,self.peso,self.proteina,self.gordura_total,self.gordura_saturada,self.carboidratos,self.acucares,self.sodio)


#RefinedAbstractionC
class BMT(Proteina):
   preco = 18.95
   peso = 216
   proteina = 20.2
   gordura_total = 14.8
   gordura_saturada = 5.3
   carboidratos = 39.7
   acucares = 5.7
   sodio = 1010

   def __init__(self,sanduiche):  # leitura
       self.sanduiche = sanduiche
   
   def method(self):
       self.sanduiche.method(self.preco,self.peso,self.proteina,self.gordura_total,self.gordura_saturada,self.carboidratos,self.acucares,self.sodio)

#RefinedAbstractionD
class Veggie(Proteina):
   preco = 14.75
   peso = 248
   proteina = 16.0
   gordura_total = 11.7
   gordura_saturada = 2.2
   carboidratos = 54.4
   acucares = 7.3
   sodio = 573
   
   def __init__(self,sanduiche):  # leitura
       self.sanduiche = sanduiche
   
   def method(self):
       self.sanduiche.method(self.preco,self.peso,self.proteina,self.gordura_total,self.gordura_saturada,self.carboidratos,self.acucares,self.sodio)



    
# Interface
#IImplementer
class Sanduiche(OpcaoAlimento):
   @abstractmethod
   def method(self):
       pass

   
#ImplementerA
class PaoBranco(Sanduiche):
   preco = 10.00
   peso = 67.0
   proteina = 7.4
   gordura_total = 2.1
   gordura_saturada = 0.3
   carboidratos = 35.2
   acucares = 2.7
   sodio = 239
   

   def method(self,pr_preco,pr_peso,pr_proteina,pr_gordura_total,pr_gordura_saturada,pr_carboidratos,pr_acucares,pr_sodio):
      print(f'\nPreço Total: {self.preco + pr_preco}\nPeso Total: {self.peso + pr_peso}\nProteina: {self.proteina + pr_proteina}\nGordura Total: {self.gordura_total + pr_gordura_total}\nGordura Saturada Total: {self.gordura_saturada + pr_gordura_saturada}\nCarboidratos Total: {self.carboidratos + pr_carboidratos}\nAcucares Total: {self.acucares + pr_acucares}\nSodio Total: {self.sodio + pr_sodio}\n')


#ImplementerB
class PaoQueijoErvasItalianas(Sanduiche):
   preco = 20.00
   peso = 78.4
   proteina = 9.4
   gordura_total = 4.5
   gordura_saturada = 2.0
   carboidratos = 37.4
   acucares = 2.8
   sodio = 424


   def method(self,pr_preco,pr_peso,pr_proteina,pr_gordura_total,pr_gordura_saturada,pr_carboidratos,pr_acucares,pr_sodio):
      print(f'\nPreço Total: {self.preco + pr_preco}\nPeso Total: {self.peso + pr_peso}\nProteina: {self.proteina + pr_proteina}\nGordura Total: {self.gordura_total + pr_gordura_total}\nGordura Saturada Total: {self.gordura_saturada + pr_gordura_saturada}\nCarboidratos Total: {self.carboidratos + pr_carboidratos}\nAcucares Total: {self.acucares + pr_acucares}\nSodio Total: {self.sodio + pr_sodio}\n')

#ImplementerC
class PaoCenteio(Sanduiche):
   preco = 15.00
   peso = 79.0
   proteina = 10.6
   gordura_total = 4.5
   gordura_saturada = 0.7
   carboidratos = 37.8
   acucares = 2.6
   sodio = 364



   def method(self,pr_preco,pr_peso,pr_proteina,pr_gordura_total,pr_gordura_saturada,pr_carboidratos,pr_acucares,pr_sodio):
      print(f'\nPreço Total: {self.preco + pr_preco}\nPeso Total: {self.peso + pr_peso}\nProteina: {self.proteina + pr_proteina}\nGordura Total: {self.gordura_total + pr_gordura_total}\nGordura Saturada Total: {self.gordura_saturada + pr_gordura_saturada}\nCarboidratos Total: {self.carboidratos + pr_carboidratos}\nAcucares Total: {self.acucares + pr_acucares}\nSodio Total: {self.sodio + pr_sodio}\n')


#RefinedAbstractionD
class PaoTrigo(Sanduiche):
   preco = 13.50
   peso = 69.0
   proteina = 7.5
   gordura_total = 2.1
   gordura_saturada = 0.3
   carboidratos = 35.0
   acucares = 2.6
   sodio = 271


   def method(self,pr_preco,pr_peso,pr_proteina,pr_gordura_total,pr_gordura_saturada,pr_carboidratos,pr_acucares,pr_sodio):
      print(f'\nPreço Total: {self.preco + pr_preco}\nPeso Total: {self.peso + pr_peso}\nProteina: {self.proteina + pr_proteina}\nGordura Total: {self.gordura_total + pr_gordura_total}\nGordura Saturada Total: {self.gordura_saturada + pr_gordura_saturada}\nCarboidratos Total: {self.carboidratos + pr_carboidratos}\nAcucares Total: {self.acucares + pr_acucares}\nSodio Total: {self.sodio + pr_sodio}\n')



if __name__ == '__main__':

   while(1):

       print("1 - Pao branco")
       print("2 - Pao de Queijo")
       print("3 - Pao de Centeio")
       print("4 - Pao de Trigo")
       opcao1 = str(input('escolha um tipo de sanduíche: '))

       if opcao1 == "1":
           pao = PaoBranco()
       if opcao1 == "2":
           pao = PaoQueijoErvasItalianas()
       if opcao1 == "3":
           pao = PaoCenteio()
       if opcao1 == "4":
           pao = PaoTrigo()


      
       print("1 - Presunto")
       print("2 - Frango")
       print("3 - B.M.T")
       #print("4 - Veggie")
       opcao2 = str(input('escolha um tipo de proteina: '))

       if opcao2 == "1":
           proteina = Presunto(pao)
       if opcao2 == "2":
           proteina = Frango(pao)
       if opcao2 == "3":
           proteina = BMT(pao)
       #if opcao2 == "4":
       #    proteina = Veggie(pao)
       


       proteina.method()

