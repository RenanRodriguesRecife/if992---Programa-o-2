from abc import ABC, abstractmethod


class Box(ABC):

  @abstractmethod
  def add(self,item):
      pass

  @abstractmethod
  def esvaziar(self):
      pass

  @abstractmethod
  def contar(self):
      pass

class Item():
  def __init__(self,nome,valor):
      self.nome = nome
      self.valor = valor


class ListBox(Box):
  def __init__(self):
      self.itemList = []

  def add(self,item):
      self.itemList.append(item)

  def esvaziar(self):
      list = self.itemList
      self.itemList = []
      return list

  def contar(self):
      return len(self.itemList)

class DictBox(Box):
  def __init__(self):
      self.itemDict = {}

  def add(self,item):
      self.itemDict[item.nome] = item.valor

  def esvaziar(self):
      aux = self.itemDict.items()
      list = []
      for x in aux:
           list.append(Item(x[0],x[1]))
      self.itemDict = {}
      return list

  def contar(self):
      return len(self.itemDict)


i1 = Item('ren',543)
i2 = Item('ren1',5343)
i3 = Item('ren2',54233)
i4 = Item('ren3',5434)

l = ListBox()
l.add(i1)
l.add(i3)

print(l.contar())
l.esvaziar()
print(l.contar())


d = DictBox()
d.add(i1)
d.add(i4)
d.add(i3)

print(d.contar())
d.esvaziar()
print(d.contar())


