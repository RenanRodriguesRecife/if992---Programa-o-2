```python
#exercício 2

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
```
