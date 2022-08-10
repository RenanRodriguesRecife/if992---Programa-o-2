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