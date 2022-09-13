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


Voltando ao nosso **Mamífero**, podemos entender que todo mamífero amamenta de forma igual.

- A implementação pode ser concreta, ou seja, definida para todas as subclasses

- Mas Baleia, Humano e Morcego se movem e soam de formas diferentes. Logo, definimos esse métodos como abstratos, para que cada subclasse o implemente de forma devida.

Uma classe **abstrata** pode definir atributos que devem ser implementados por suas subclasses.

Esses atributos podem variar de tipo ou lógica de acesso/modificação para cada subclasse.

E cada subclasse será responsável em definir sua lógica.

Em Python criaremos atributos abstratos como métodos abstratos, junto com o decorador de propriedades.

```python

@property
@abstractmethod
def atributo_abstrato(self): #leitura
	pass
	
@atributo_abstrato.setter
@abstractmethod
def atributo_abstrato(self, valor): #escrita
	pass

```

<img>

Em nosso **Mamífero**, talvez a lógica de como nosso atributos são definidos não seja clara.

- Baleia pode receber um valor em Milhas/h e Humano em Quilômetro/h, para que ambos devem ser convertidos no **getter**

- Não é um problema em Python, mas em outras linguagens, podemos ter atributos de tipos diferentes definidos nas subclasses

# Interfaces

```
- Veja, nós só aceitamos as coisas assim.

- Ok, vou escrever desse jeito
```

Classes abstratas são classes, mas principalmente, são **superclasses**. Usadas para definir a base das classes que a estendem.

No entanto, existem casos onde queremos definir não as propriedades completas de um objeto, mas apenas realizar um "contrato", garantindo que determinada funcionalidade ocorra como esperado.
