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


Algumas funções de Python

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