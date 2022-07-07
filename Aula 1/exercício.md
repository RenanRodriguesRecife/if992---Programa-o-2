Atividade

Números Primos

Escreva uma função em Python que recebe um
valor inteiro n e retorne os n primeiros números primos, a partir de 1.

Números primos são números divisíveis apenas por 1 e eles mesmos.


<code>
def listPrimos(num):

    for n in range(num):
        if n >= 1:
            qtd_divisores = 0
            for div in range(2,n):
                if n % div == 0:
                    qtd_divisores += 1
            if qtd_divisores == 0:
                print(n)


listPrimos(10)
</code>