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
i5 = Item('ren4',54233)
i6 = Item('ren5',5434)
i7 = Item('ren6',54233)
i8 = Item('ren7',5434)

l = ListBox()
l.add(i1)
l.add(i2)


d = DictBox()
d.add(i3)
d.add(i4)
d.add(i5)


l1 = ListBox()
l1.add(i6)
l1.add(i7)

def repack_boxes(*args):
  itens = []
  for x in args:
    x = x.esvaziar()
    for y in x:
      itens.append(y)
  
  aux = 0
  for i in itens:
      args[aux].add(i)
      aux += 1
      
      if(aux > len(args) - 1):
        aux = 0



repack_boxes(l,d,l1)
print(l.esvaziar())
print(d.esvaziar())
print(l1.esvaziar())
