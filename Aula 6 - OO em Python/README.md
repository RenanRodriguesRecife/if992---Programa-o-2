# OO em Python

## Classes

Python é uma linguagem com foco na **reusabilidade** de código e projetada para ser orientada à objetos.

- Podemos agrupar dados com os tipos built-ins do python (lista, tupla, dicionário, etc.);

- Podemos definir conjuntos de comandos facilmente reutilizados por meio de funções;

- **Classes** permitem agrupar dados e funções relacionadas de maneira legível.

- Às vezes, OO permite mapear facilmente objetos à coisas do mundo real;

- Nem sempre é necessário, desejável, ou possível codificar analogias perfeitas;

- Muitas vezes criaremos classes sem contrapartes no mundo real, simplesmente pela utilidade de agrupar métodos/atributos


Em python, todo tipo de dado é uma instância de uma classe, incluindo o próprio tipo (type);

Atributos:

Os valores de dados guardados dentro de um objeto são chamados de atributos;

Métodos:

As funções associadas à classe são chamadas métodos.


```python
import datetime # we will use this for date objects
class Person:
    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age

        
person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12), # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)

print(person.name)
print(person.email)
print(person.age())

```

class Person:

- Nós começamos a definição de uma classe com a palavra reservada class, seguida do nome da classe e dois-pontos. 

- Todas as heranças da classe são listadas entre parênteses, entre o nome da classe e os dois-pontos. Por enquanto vamos ignorar essa parte.

De maneira generalizada, classes são definidas como:

```python
class className([superclasses]):
```

- Dentro do corpo da classe podemos definir atributos e métodos.

- Atributos podem ser definidos no escopo da classe, mas comumente são definidos dentro do método construtor.

- No nosso exemplo temos dois métodos, o inicializador (__init__) e um método para calcular a idade (age):
def __init__(self, name, surname, birthdate, address, telephone, email):
def age(self):
    
```python
def __init__(self, name, surname, birthdate, address, telephone, email):
def age(self):
```

- Quando a classe é chamada, um novo objeto dessa classe é gerada e o método __init__ é automaticamente invocado. Esse método irá inicializar as variáveis do objeto com os parâmetros passados.

- O segundo método é uma função personalizada que calcula a idade de uma pessoa dada sua data de nascimento e a data atual.

