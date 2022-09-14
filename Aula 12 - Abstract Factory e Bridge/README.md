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

Pontos positivos:

- **Isolamento**: a criação de objetos concretos é encapsulada, isolando clientes das implementações;

- **Facilidade na troca**: a Fábrica aparece apenas uma vez, quando é instanciada, tornando fácil a troca de fábrica concreta para mudança de configurações ou lógica;

- **Consistência**: quando objetos são projetados para trabalharem juntos, é importante usar objetos de apenas uma família por vez.

Pontos negativos:

- **Dificuldade com novos tipos de objetos**: Fábricas definem o números de tipos possíveis para objetos, a adição de novos se torna trabalhosa.


## Bridge

**Bridge** é um padrão de refatoração utilizado para desacoplar as interfaces das implementações. Criando uma ponte entre abstração e implementação

Tome as classes por si próprias como a **abstração** e o que elas fazem como a **implementação**.
O padrão se divide em quatro elementos:

 - Abstraction Interface;

 - Refined abstraction;

 - Implementer interface;

 - Concrete implementer;

