
import math
from abc import ABC, abstractmethod



class Point(object):
   def __init__(self,x,y):
       self.x = x
       self.y = y

class Forma(object):
   def __init__(self):
       self.points = list()

   @abstractmethod
   def calculaArea(self):
       pass

   @abstractmethod
   def addColor(self):
       pass

class ObjectCirculo(Forma):
   def __init__(self,p1,raio,*args,**kwargs):
       super().__init__(*args,**kwargs)
       self.points.append(p1)
       self.points.append(p2)
       self.raio = raio
       self.color = None

   def calculaArea(self):
       return math.pi * self.raio * self.raio

   def addColor(self,color):
       self.color = color
       

class ObjectRetangulo(Forma):
   def __init__(self,p1,p2,*args,**kwargs):
       super().__init__(*args,**kwargs)
       self.points.append(p1)
       self.points.append(p2)

   def calculaArea(self):
       return (self.points[1].x - self.points[0].x) * (self.points[1].y - self.points[0].y)

   def addColor(self,color):
       self.color = color



class Cor(object):
   @abstractmethod
   def printColor(self):
       pass

class ObjectVermelho(Cor):
   def printColor(self):
       print("Vermelho")

class ObjectVerde(Cor):
   def printColor(self):
       print("Verde")

class ObejctAzul(Cor):
   def printColor(self):
       print("Azul")





class AbstractFactory(ABC):
   @abstractmethod
   def getObject(self,type):
       pass

class ObjectFactoryForma(AbstractFactory):
   def getObject(self,type,p1,p2):
       if type == "circulo":
           return ObjectCirculo(p1,p2)
       elif type == "retangulo":
           return ObjectRetangulo(p1,p2)
       return None


class ObjectFactoryCor(AbstractFactory):
   def getObject(self,type):
       if type == "vermelho":
           return ObjectVermelho()
       elif type == "verde":
           return ObjectVerde()
       elif type == "azul":
           return ObejctAzul()
       return None



p1 = Point(0,0)
p2 = Point(12,3)
p3 = Point(3,21)

r1 = ObjectFactoryForma().getObject("retangulo",p1,p2)
c1 = ObjectFactoryForma().getObject("circulo",p1,2)
r1 = ObjectFactoryForma().getObject("retangulo",p1,p3)
r1.addColor(ObjectFactoryCor().getObject("vermelho"))
c1.addColor(ObjectFactoryCor().getObject("verde"))
r1.addColor(ObjectFactoryCor().getObject("azul"))
            
print(r1.calculaArea())
print(c1.calculaArea())
print(r1.color.printColor())

