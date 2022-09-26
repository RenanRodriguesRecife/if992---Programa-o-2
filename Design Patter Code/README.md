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

Fachadas é uma classe que provém uma interface mais transparente e unificada para processos complexos, permitindo acesso mais simplificado a subsistemas.

```python

class SocialSharing:
  def shareURL(self,url):
    facebookAPI.share(url)
    twitterAPI.share(url)
    instagramAPI.share(url)

```

## Flyweight


## Iterator 

## Proxy

## Memento


## Abstract Factory

## Bridge
