```python
def lights(n):
  interruptores = [False] * n

  for i in range(n):
     for j in range(i, n):
        if (j + 1) % (i + 1) == 0:
          interruptores[j] = not interruptores[j]

  return interruptores

number_input = 5
print(lights(number_input))

```
