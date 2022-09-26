from abc import ABC, abstractmethod
import json

#interface
#IAbstraction
class Forma(ABC):
   @abstractmethod
   def registrar_dados(self):
       pass

#RefinedAbstraction
class Forma1(Forma):
   def __init__(self,content,escreve):
       self.escreve = escreve
       self.content = content

   def registrar_dados(self):
       self.escreve.method(self.content)


#Implementer
class Escreve(ABC):
   @abstractmethod
   def method(self):
       pass

#Concrete Implementer
class EscreveConsole(Escreve):
   def method(self,content):
       print(content)

#Concrete Implementer
class EscreveTXT(Escreve):
   def method(self,content):
       with open("content.txt","w") as arq:
           arq.write(content)

#Concrete Implementer
class EscreveJSON(Escreve):
   def method(self,content):
       content = json.loads(content)
       with open("content.json","w",encoding='utf-8') as f:
           json.dump(content,f,ensure_ascii=False, indent=4)

   def convertJson(self,content):
       return json.loads(content)



wconsole = EscreveConsole()
wtxt = EscreveTXT()
wjson = EscreveJSON()

f = Forma1( '{"first_name": "Michael", "last_name": "Rodgers", "department": "Marketing"}',wjson)
f.registrar_dados()
f = Forma1( '{"first_name": "Michael", "last_name": "Rodgers", "department": "Marketing"}',wconsole)
f.registrar_dados()
f = Forma1( '{"first_name": "Michael", "last_name": "Rodgers", "department": "Marketing"}',wtxt)
f.registrar_dados()

