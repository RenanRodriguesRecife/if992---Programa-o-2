## Singleton

O padrão Singleton garante que apenas uma instância de uma classe seja criada e que a instância seja acessível globalmente.

```python

class SingletonClass(object):
  def __new__(cls):
    if not hasattr(cls,'instance'):
      cls.instance = super(SingletonClass,cls).__new__(cls)
    return cls.instance
    
  #adicione conteúdo que você quer implementar
  
#main
if __name__ == '__main__':
  singleton = SingletonClass()

```

## Facade

## Flyweight


## Iterator 

## Proxy

## Memento


## Abstract Factory

## Bridge
