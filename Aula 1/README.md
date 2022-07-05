Algumas coisas básicas de Python

Nessa disciplina foi escolhido Python como linguagem porque em python tudo é classe (inclusive class)

```
print(type(1))
'<type 'int'>'
```

Cada comando de python devem ser escritos em uma linha
Obs: Em python pode pular uma linha usando '\'

```
    varlor = \
    4300.6
```

String

Com aspas triplas você define uma string com várias linhas

```
string = """Lorem ipsum dolor sit
            amet, consectetur
            adipiscing elit. Cras
            venenatis fermentum magna,
            quis aliquet leo eleifend quis."""
```


Imprime o valor hash de objeto
(lembrando em python tudo é objeto)
```
print(hash("aaa"))
-145432768704
```

Compreensão de listas

Syntax

newlist = [expression 'for' item 'in' iterable 'if' condition == 'True']

Ex:
```
lista = [i * i for in range(10) if i%2 == 0]
```

Algumas funções de Python

map() - função que executa uma especifica função para cada item em uma interação. Os itens são mandados para a função como parametro

Syntax

map(function, iterables)

Ex:
```
def myfunc(n):
    return len(n)

x = map(myfunc,('apple','banana','cherry'))

[5, 6, 6]
```

filter() - a função retorna um iterador onde os itens são filtrados por meio de uma função para testar se o item é aceito ou não.

Syntax

filter(function, iterable)

Ex:
```
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
    if x < 18:
        return False
    else:
        return True

adults = filter(myFunc, ages)

for x in adults:
    print(x)

18
24
32
```

+ Algumas funções de Python

help - usado para exibir a documentação de módulos, funções, classes, palavras-chave, etc.

Ex:
```
help(str)
```

dir - retorna uma lista dos atributos e métodos de qualquer objeto

Ex:
```
dir(str)
```