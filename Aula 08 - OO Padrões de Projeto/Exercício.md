Exercício 1:

Crie uma classe Singleton Writer que permite um usuário modificar um arquivo.

Writer possui os métodos: write, close_session.

```python
#exerciocio 1

class SingletonClass(object):
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance


class Write(SingletonClass):
    
    
    def write(self):
        print('Editando algo:')
        raw_input()

    def close_session(cls):
        print("fechando a sessao")
        cls.instance = None
        


m = Write();

m.write()
m.close_session()
```

Exercício 2:

Um software de uma máquina de lavar possui três subsistemas: Lavador, Enxaguante, e Secador, os sistemas ocorrem sequencialmente durante uma lavagem.
Crie uma classe de Fachada que englobe os três subsistemas.


```python
#exercicio 2

class Lavador:
    def lavar(self):
        print('lavando...')

class Enxaguante:
    def enxaguar(self):
        print('enxaguando...')

class Secador:
    def secar(self):
        print('secando...')


class Fachada:
    def __init__(self):
        self.lavador = Lavador()
        self.enxaguante = Enxaguante()
        self.secador = Secador()

    def initLavar(self):
        self.lavador.lavar()
        self.enxaguante.enxaguar()
        self.secador.secar()


m = Fachada()
m.initLavar()

```

Exercício 3:

Um sistema de gráfico faz uso de uma classe Linha, que possui dois Ponto(s), cada um com um x e um y, e uma Cor.
No entanto, para poupar em processamento, é ideal reaproveitar uma linha, mudando seus Ponto(s), caso já exista uma linha com as mesmas cores.
Crie uma classe LinhaFlyweight que realiza essa operação.



```python
#exercicio 3

class Point:
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color


class LinhaFlyweight(object):
    linha_family = {}
    

    
    def __new__(cls,x1,y1,x2,y2,color1,color2):
        
        try:
            
            id = cls.linha_family[hash(color1+color2)]
            
        except KeyError:
            id = object.__new__(cls)
            cls.linha_family[hash(color1+color2)] = id
        return id

    def __init__(self,x1,y1,x2,y2,color1,color2):
        self.p1 = Point(x1,y1,color1)
        self.p2 = Point(x2,y2,color2)

    def printLine(self):
        print(self.p1.x,self.p1.y,self.p2.x,self.p2.y,self.p1.color,self.p2.color)




l1 = LinhaFlyweight(1,2,3,4,'red','red')
l1.printLine()
l2 = LinhaFlyweight(1,2,3,4,'red','blue')
l2.printLine()
l3 = LinhaFlyweight(1,2,3,4,'red','red')
l3.printLine()

print(LinhaFlyweight.linha_family)


```

