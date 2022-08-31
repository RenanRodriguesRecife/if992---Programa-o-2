# Iterator

O padrão **Iterator** nos permite percorrer containeres de dados sem preocupação com a estrutura dos mesmos (lista, pilha, árvore, etc.).

<img src="./.assets/iterator.JPG">

<img src="./.assets/iteratorclass.JPG">



### Pontos positivos

- permite a você percorrer elementos de uma coleção sem expor as representações dele (lista, pilha, árvore, etc.)

- Caso você insira novos dados na lista, o Interator evita precisar sempre modificar os valores do tamanho da lista em um loop quando você percorre a lista 

- Todos os iteradores devem implementar a mesma interface. Isso faz que o código cliente seja compatível com qualquer tipo de coleção ou qualquer algoritmo de travessia desde que haja um iterador apropriado. Se você precisar de uma maneira especial para a travessia de uma coleção, você só precisa criar uma nova classe iterador, sem ter que mudar a coleção ou o cliente.

```python
class Iterable(object):
    pass #Qualquer dado aqui


class Container(object):
    def __init__(self):
        self.data = list()
    
    def __iter__(self):
        return Iterator(self)
    
    def get_ith(self,i):
        if len(self.data) > i:
            return self.data[i]
        return None


class Iterator(object):
    def __init__(self,container):
        self.container = container
        self.current = 0

    def __next__(self):
        value = self.container.get_ith(self.current)
        if value is None:
            raise StopIteration
        self.current+=1
        return value

```

# Proxy

O padrão Proxy permite a criação de uma estação de acesso ou um placeholder para controlar o acesso de um outro objeto.

Nós dividiremos nossos objetos em Proxy e Real, o objeto Proxy será acessado e carregará o que precisarmos do objeto real **apenas quando necessário**.

<img src="./.assets/proxyUml.JPG">

```python

class Subject(object):
    def __init__(self):
        pass #Qualquer dado aqui

class RealSubject(Subject):
    def operation(self):
        pass

class ProxySubject(Subject):
    def __init__(self,*args,**Kwargs):
        self.real = None

    def operation(self):
        if self.real is None:
            self.real = RealSubect()
        self.pre_operation()
        self.real.operation()
        self.post_operation()

    def pre_operation(self):
        pass

    def post_operation(self):
        pass
```

Proxies podem ser usadas como:

- Proteção: controlando acesso e permitindo visibilidade apenas de atributos e métodos que são necessários para o cliente;

- Referências: permitindo acessos sofisticados, como contagem de referências a determinado objeto;

- Velocidade: atrasando a criação e inicialização de objetos caros, criando sob demanda.

# Memento

