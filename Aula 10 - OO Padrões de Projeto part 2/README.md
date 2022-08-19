# Iterator

O padrão **Iterator** nos permite percorrer containeres de dados sem preocupação com a estrutura dos mesmos.

<img src="./.assets/iterator.JPG">

<img src="./.assets/iteratorclass.JPG">

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