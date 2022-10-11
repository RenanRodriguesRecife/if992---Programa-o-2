# Revisão

Lembre-se:

**Diagrama de Classe**

manter-se atento a 

sublinhados - Quer dizer que o atributo ou o método é estático

itálicos - Quer dizer que o atributo ou o método é abstrato

<img src="exer1.jpg">


tensor2d
python```

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



**Diagrama de Classe**

lembrar que associações informam atributos que podem não estar presentes em uma classe.

<img src="exer2.jpg">

<img src="exer3.jpg">

<img src="herancaInter.jpg">

**Diagrama de Sequência**

Demonstra sequência temporal de chamadas de funções para realização de um cenário

<img src="sequencia.jpg">

<img src="receita.jpg">
