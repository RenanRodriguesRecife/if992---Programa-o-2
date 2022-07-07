Exercícios

Exercício 1

Crie uma função anônima que some dois valores caso a soma seja menor ou igual a 0 e multiplica os dois valores caso contrário.

```
myFunc = lambda x, y: x + y if x + y <= 0 else x * y

print(myFunc(-3,2))
``` 

Exercício 2

Data as listas L1 e L2 definidas abaixo, crie um código que calcule o quadrado da soma dos elementos paralelos de L1 e L2, mas apenas onde a soma desses elementos for impar.

- L1 = [13,-2,5,82,95,3,-53,12,-21]
- L2 = [3,73,22,31,5,67,-3,39,-87]

```
l1 = [13,-2,5,82,95,3,-53,12,-21]
l2 = [3,73,22,31,5,67,-3,39,-87]

def func(l1, l2):
    if len(l1)!=len(l2):
        print('tamanho das listas diferentes')
        return 0
    for x in zip(l1,l2):
        if (x[0] + x[1])%2 == 1:
            print(x)
            print((x[0] + x[1])**2)

func(l1,l2)

ou

ex2 = list(map(lambda x: (x[0] + x[1])**2 ,filter(lambda x: (x[0] + x[1])%2 ==1,zip(l1,l2))))

print(ex2)    
```

Exercício 3

Crie uma função segundo_lugar que receba dois argumentos: uma lista de notas, contendo todas as notas de uma turma e uma lista de nomes, contendo os nomes dos alunos.
notas e nomes estão na mesma organização, ou seja, notas[0] representa a nota do aluno nomes[0]
Sua função deve retornar a nota e o nome do aluno com a segunda maior nota.
Teste com o seguinte exemplo:

- nome = ['joão','maria','carlos','eduarda','eduardo']
- notas = [10,10,6,8,7]

```
nome = ['joão','maria','carlos','eduarda','eduardo']
notas = [10,10,6,8,7]

def segundo_lugar(notas, nomes):
    segunda_maior_nota = sorted(list(set(notas)))[-2] #set só vai ter uma vez cada valor
    indice = notas.index(segunda_maior_nota)
    return notas[indice],nomes[indice]

print(segundo_lugar(notas, nome))

```