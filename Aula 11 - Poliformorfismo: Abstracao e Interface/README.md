# Polimorfismo: Abstração e Interface

# Polimorfismo

Polimorfia, literalmente, significa **múltiplas formas**

Em programação, polimorfia se aplica a métodos que possuem o mesmo nome mas com corpos ou assinaturas diferentes

Existem dois tipos de polimorfismo: sobrescrita e sobrecarga

## Override & Overload

### Override (sobrepor, sobrescrever):

- Classe substitui método existente na superclasse

### Overload (sobrecarga):

- Classe possui diversas possibilidades de função com parâmetros diferentes e escolhe a correta por meio da chamada. (**não é possível no Python, por padrão**)

A não existência de sobrecarga em Python se dá ao conjunto de *args, **kwargs e tipagem dinâmica

# Abstração

Além da remoção de complexidade, abstração em OO pode ser utilizada ao se referir a classes, nas chamdasd **classes abstratas**

**nos diagramas de classes, a abstração é representada por itálico**

## Classes Abstratas

Classes abstratas representam modelos imaginários para outros objetos.

- Definem comportamentos base, podendo ter atributos e métodos **sejam concretos ou abstratos**

- Estas classes são abstratas, não podendo ser instanciadas!

- No entanto, uma classe abstrata **deve** possuir ao menos um componente abstrato

- Em Python, utilizamos o pacote **abc** para definir classes abstratas.

- ABS = Abstract Base Class

```python
from abc import ABC, abstractmethod

class ClasseAbstrata(ABC):
  pass

```

<img>

Considere um **Mamífero**.

Um mamífero por si só não existe, apenas define um modelo para que criaturas dessa categoria sigam. 

Como por exemplo, Baleia, Humano, Morcego, todos compartilham as características definidas por mamíferos.

Mas não é possível ter um objeto Mamífero **puro**.

<img>

Logo, **Mamífero** é uma classe **abstrata**!

Porém, como mencionado, alguma coisa do nosso mamífero deve ser abstrata para que ela possa ser abstrato. Podendo ser:

- Atributos; ou
- Métodos

Métodos abstratos não possuem implementação, eles existem apenas como assinatura.

Garantem a conformidade das subclasses com o “modelo” definido pela classe abstrata, mas esperam que a implementação seja individual da subclasse.

A diferença para apenas o polimorfismo vista anteriormente é que não existe implementação base para o método.

Definimos um método como **abstrato** utilizando o decorador:

```python

@abstractmethod
def metodo_abstrato(self):
  pass

```

<img>



