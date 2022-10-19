## Lâmpadas no corredor

Um homem chamado José é o responsável por ligar e desligar as luzes de um corredor. Cada lâmpada tem seu próprio interruptor que liga e a desliga. Inicialmente todas as lâmpadas estão desligadas.

José faz uma coisa peculiar: se existem n lâmpadas no corredor, ele caminha até o fim do corredor e volta n vezes. Na iésima caminhada, ele aperta apenas os interruptores aos quais sua posição é divisível por i. Ele não aperta nenhum interruptor na volta à sua posição inicial, apenas na ida. A iésima caminhada é definida como ir ao fim do corredor e voltar.

Determine qual é o estado final de cada lâmpada. Está ligada ou desligada?

Exemplo:

Entrada: 3          

Saída: [on, off, off]

```python
class Lampada:
   def __init__(self):
       self.estado = 'off'

   def mudarEstado(self):
       if(self.estado == 'off'):
           self.estado = 'on'
       else:
           self.estado = 'off'

   def __str__(self):
       return self.estado

class Corredor:
   def __init__(self,num_lampadas):
       self.__num_lampadas = num_lampadas
       self.__lampadas = []
       self.init_corredor()
       self.loucuraDeJose()
       
   def init_corredor(self):
       for num in range(self.__num_lampadas):
           p = Lampada()
           self.__lampadas.append(p)

   def loucuraDeJose(self):
       
       for i in range(self.__num_lampadas):
           for j in range(self.__num_lampadas):
               if((j+1)%(i+1)==0):
                   self.__lampadas[j].mudarEstado()
              
                
                
   def list_lampadas(self):
       lista = []
       for num in range(self.__num_lampadas):
           lista.append(str(self.__lampadas[num].estado))
       print(lista)
  
while(1):
   number = int(input("Entrada: "))
   correr = Corredor(number)
   print(correr.list_lampadas())
```
