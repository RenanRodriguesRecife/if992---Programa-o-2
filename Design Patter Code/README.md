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

```

## Memento

Permite forma de realizar backups e restaurações de objetos.

```python

```

## Abstract Factory

O padrão Abstract Factory provê uma interface para a criação de Famílias de objetos relacioandos ou depedentes.

revisar
```python
# Interface
class AbstractFactory(ABC):
  @abstractmethod
	def getObject(self, type):
	  pass
    
# Factory
class ObjectFactory(object):
  def getObject(self, type):
    if type == something:
      return ObjectClass1(arguments)
    elif type == something_else:
      return ObjectClass2(arguments)
    return None
```

```python

# Factory
class ObjectFactory(object):
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

```python

```
