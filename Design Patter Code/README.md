## Singleton

O padrão Singleton garante que apenas uma instância de uma classe seja criada e que a instância seja acessível globalmente.

```python

class SingletonClass(object):
  def __new__(cls):
    if not hasattr(cls,'instance'):
      cls.instance = super(SingletonClass,cls).__new__(cls)
    return cls.instance
    
  #adicione conteúdo que você quer implementar da class
  
#main
if __name__ == '__main__':
  singleton = SingletonClass()

```

## Facade

Fachadas é uma classe que provém uma interface mais transparente e unificada para processos complexos, permitindo acesso mais simplificado a subsistemas.

```python

class SocialSharing:
  def shareURL(self,url):
    facebookAPI.share(url)
    twitterAPI.share(url)
    instagramAPI.share(url)

```

## Flyweight

Flyweight é um padrão de projetos que visa reduzir a quantidade de objetos instanciados necessários para um programa. Um objeto flyweight é criado que é compartilhado em múltiplos contextos

```python

class ObjectoQualquerFlyweight:
  obj_qualquer = {}
  
  def __new__(cls,id_atribute,atribute1):
    try:
      id = cls.obj_qualquer[id_atribute]
    except KeyError:
      id = object.__new__(cls)
      cls.obj_qualquer[id_atribute] = id
    return id
    
  #adicione conteúdo que você quer implementar da class

```

## Iterator 

O padrão Iterator nos permite percorrer containeres de dados sem preocupação com a estrutura dos mesmos.

Possui 3 partes

```
Iterable - O dado individual

Container - O tipo de estrutura (lista, arvore, dicionário...)

Interator - Responsável por interagir com a estrutura (buscar elemento do lado,...)
```

Ex: usando uma lista

```python

class Iterable(object):
    pass #Qualquer dado

class Container(object):
    def __init__(self):
        self.data = list()

    def __iter__(self):
        return Iterator(self)

    def get_ith(self,i):
        if len(self.data) > i:
            return self.data[i]
        return None

class Iterator(object):
    def __init__(self,container):
        self.container = container
        self.current = 0

    def __next__(self):
        value = self.container.get_ith(self.current)
        if value is None:
            raise StopIteration
        self.current+=1
        return value

```

## Proxy

O padrão Proxy permite a criação de uma estação de acesso ou um placeholder para controlar o acesso de um outro objeto.

Nós dividiremos nossos objetos em Proxy e Real(o objeto final que você quer usar), o objeto Proxy será acessado e carregará o que precisarmos do objeto real apenas quando necessário. (pode escolher como e quando repassar chamadas de métodos para o objeto real).

O Proxy pode executar ações antes e depois das chamadas dos métodos do objeto real.

O Proxy é algo que fica no meio do caminho.

```python

class Subject(object): #Qualquer coisa
	def __init__(self):
		pass #Qualquer dado aqui

class RealSubject(Subject):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		

class ProxySubject(Galeria):
	def __init__(self,subject,*args,**Kwargs):
		self.real = subject

	def operation(self): #operação pode ser qualquer método do Subject que você deseja mexer
		if self.real is None:
			self.real = RealSubject()

		self.pre_operation()
		self.real.operation()
		self.post_operation()
	
	def pre_operation(self):
		pass
	def post_operation(self):
		pass


```

## Memento

Permite forma de realizar backups e restaurações de objetos.

```
Originator - o objeto central que será usado (pode ter qualquer nome)

Memento - os objeto beckups

Caretaker - Classe responsável por administrar quando salvar e desfazer
```

```python
		
class Memento(object):
	def __init__(self,data):
		self.data = data #Qualquer dado
		
class Originator(object):
	def __init__(self,data):
		self.data = data #Qualquer dado aqui
		
	def save(self):
		return Memento(self.data)
	
	def undo(self,memento):
		self.data = memento.data
		
class Caretaker(object):
	def __init__(self,originator):
		self.mementos = list()
		self.originator = originator
	
	def save(self):
		self.mementos.append(self.originator.save())
		
	def undo(self):
		if not len(self.mementos):
			return None
		
		memento = self.mementos.pop()
		
		if len(self.mementos) == 0:
            		return None
			
		self.originator.undo(self,memento)

```

## Abstract Factory

O padrão Abstract Factory provê uma interface para a criação de Famílias de objetos relacioandos ou depedentes.

```python

# Interface
class AbstractFactory(ABC):
	@abstractmethod
	def getObject(self, type):
		pass

# Factory
class ObjectFactory(AbstractFactory):
	def getObject(self, type): # type define que classe vamos instanciar.
		if type == something:
			return ObjectClass1(arguments)
		elif type == something_else:
			return ObjectClass2(arguments)
		return None

# ObjectClass1  e ObjectClass2 representam
# nossa família de classes. Ambas herdam de
# uma mesma classe de forma sejam substituíveis
# nas regras de negócio.

```

## Bridge

Bridge é um padrão de projeto estrutural que permite dividir uma classe grande ou um conjunto de classes intimamente relacionadas em duas hierarquias separadas — abstração e implementação — que podem ser desenvolvidas independentemente uma da outra.

Problema: Quando se faz cominações de classes usando Hierarquina o número de classes combinadas tende a crescer de maneira geométrica

<img src="./.assets/problem.jpg">

Solução: A solução é criar uma **"ponte"** entre o elemento abstrato e o elemento implementador. O elemento Abstrato pode ter uma implementação

<img src="./.assets/solution.jpg">

```python
#Abstração
from abc import ABC, abstractmethod

#Interface
class IAbstraction(ABC) 
	@abstractmethod
	def method(self): 
		pass
		
#RefinedAbstraction
class RefinedAbstractionA(IAbstraction):
	def __init__(self,implementer): #leitura
		self.implementer = implementer
	
	def method(self, type):
		self.implementer.method()

```

```python
#Implementer

# Interface
class IImplementer(ABC):
	@abstractmethod
	def method(self):
		pass

class ImplementerA(IImplementer):
	def method(self, type):
		"The method implementation"

class ImplementerB(IImplementer):
	def method(self, type):
		"The method implementation"

```
```python

if __name__== "__main__":
	ImplA = ImplementerA()
	ImplB = ImplementerB()
	
	A1 = IAbstraction(ImplA)
	A2 = IAbstraction(ImplB)
	
	A1.method()
	A2.method()
```
