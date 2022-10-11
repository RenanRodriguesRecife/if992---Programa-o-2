# Revisão

Lembre-se:

**Diagrama de Classe**

manter-se atento a 

sublinhados - Quer dizer que o atributo ou o método é estático

itálicos - Quer dizer que o atributo ou o método é abstrato

<img src="exer1.jpg">


tensor2d (curiosidade tensor é uma matrix)(tensor2d é uma matrix bidimensional)

```python

class Tensor2D():
  def __init__(self, shape: list, values: list):
    self.shape = shape
    self.values = values

  @staticmethod
  def zeroes(shape: list): #shape[0] - X shape[1] - Y
    values = []
    for i in range(shape[0]):
      line = [0]*shape[1]
      values.append(line)
    return Tensor2D(shape, values)

  def ones(shape: list):
    values = []
    for i in range(shape[0]):
      line = [1]*shape[1]
      values.append(line)
    return Tensor2D(shape, values)

if __name__ == '__main__':
  t1 = Tensor2D.ones([10,10])
  t0 = Tensor2D.zeroes([5,4])
  for i in range(t0.shape[0]):
    print(t1.values[i])
  print()
  for i in range(t0.shape[0]):
    print(t0.values[i])

```

StringPrint

```python
from abc import abstractmethod, ABC
class StringPrint(ABC):
  def __init__(self, s: str):
    self.s = s

  @abstractmethod
  def print(self):
    pass

class TitleStringPrint(StringPrint):
  def print(self):
    nova_s = ''
    last_char = ''
    for i in range(len(self.s)):
      if i == 0 or last_char == ' ':
        nova_s+=self.s[i].upper()
      else:
        nova_s+=self.s[i]
      last_char = self.s[i]
    print(nova_s)

class CapsStringPrint(StringPrint):
  def print(self):
    nova_s = ''
    for i in range(len(self.s)):
      nova_s+=self.s[i].upper()
    print(nova_s)

if __name__ == '__main__':
  TSP = TitleStringPrint("teste de uma string")
  TSP.print()
  CSP = CapsStringPrint("teste de uma string")
  CSP.print()
  SP = StringPrint("teste de uma string")
  SP.print()

```


**Diagrama de Classe**

lembrar que associações informam atributos que podem não estar presentes em uma classe.

<img src="exer2.jpg">

Nesse caso Bingo tem uma lista de cartelas

```python

from random import randint
class Bingo:
  def __init__(self):
    self.cartelas = []
    self.valores_possiveis = list(range(60))

  def gerar_numero(self):
    idx = randint(0, len(self.valores_possiveis)-1)
    valor = self.valores_possiveis[idx]
    del self.valores_possiveis[idx]
    return valor

class Cartela:
  def __init__(self):
    self.numeros = []
    valores_possiveis = list(range(60))
    for i in range(20):
      idx = randint(0, len(valores_possiveis)-1)
      self.numeros.append(valores_possiveis[idx])
      del valores_possiveis[idx]

  def checar_numero(self, numero):
    idx = self.numeros.find(numero)
    if idx >=0:
      del self.numeros[idx]

if __name__ == '__main__':
  b = Bingo()
  for i in range(10):
    b.cartelas.append(Cartela())

```

<img src="exer3.jpg">

```python

class Ingrediente:
    def __init__(self,nome,tipo,quantidade):
        self.nome = nome
        self.tipo = tipo
        self.quantidade = quantidade

class Receita:
    def __init__(self,medida_unidade,medida_volume):
        self.medida_unidade = medida_unidade
        self.medida_volume = medida_volume
        self.ingredientes = []

    def add_ingrediente(self,ingrediente: Ingrediente):
        self.ingredientes.append(ingrediente)

    def get_ingrediente(self,indice):
        if indice < len(self.ingredientes) and indice >= 0:
            return self.ingredientes[indice]

    def imprimir_ingrediente(self):
        for i in self.ingredientes:
            print(i.nome)
            print(i.tipo)
            print(i.quantidade)
            print('\n')

if __name__ == '__main__':
    i1 = Ingrediente("oregano","tempero","20g")
    i2 = Ingrediente("queijo","laticínio","200ml")
    i3 = Ingrediente("massa","massa","500g")

    r = Receita("1 proção","500ml")
    r.add_ingrediente(i1)
    r.add_ingrediente(i2)
    r.add_ingrediente(i3)

    test = r.get_ingrediente(2)
    print(test.nome)

    r.imprimir_ingrediente()

```

<img src="herancaInter.jpg">

**Diagrama de Sequência**

Demonstra sequência temporal de chamadas de funções para realização de um cenário

<img src="sequencia.jpg">

<img src="receita.jpg">
