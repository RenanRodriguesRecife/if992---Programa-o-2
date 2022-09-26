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

## Memento


## Abstract Factory

## Bridge
