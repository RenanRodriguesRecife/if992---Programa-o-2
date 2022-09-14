# Abstract Factory e Bridge

## Abstract Factory

O padrão **Abstract Factory** provê uma **interface** para a criação de Famílias de objetos relacioandos ou depedentes.

<img>

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
