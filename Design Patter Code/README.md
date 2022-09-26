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

## Proxy

## Memento


## Abstract Factory

## Bridge
