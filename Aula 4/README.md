# Modelo de Classes

Em posse da visão de caso de uso do sistema, os desenvolvedores devem prosseguir no desenvolvimento

Atores:

Externamente ao sistema, os atores visualizam resultados. Cálculos, gráficos, relatórios, etc.

Objetos: 

Internamente, objetos colaboram entre si para produzir os resultados visíveis de fora.
Colaboração pode ser vista sob aspecto dinâmico ou sob aspecto estrutural estático.

## Objetivos

- Descrever método para identificação das classes de objetos de um sistema a partir dos casos de uso;

- Apresentar alguns dos elementos do diagrama de classes;

- Descrever a construção do modelo de domínio;

- Descrever a inserção do modelo de classes no desenvolvimento.

É importante notar que a modelagem de classes é um processo evolutivo.
Existem três níveis:
- Modelo de classes de domínio
- Modelo de classes de especificação
- Modelo de classes de implementação.

### Padrão de Nomeclatura:

- Espaço e preposições são removidos

- Nomes de classes e relacionamentos são escritos com iniciais maiúsculas

ex: Cliente, ItemPedido, OrdemServiço.

- Atributos e operações possuem primeira letra minúscula e junções iniciadas por letra maíuscula, ex: idade, numeroPedidos, obterTotal.

- OU junções substituídas por '_' Ex: numero_pedidos, obter_total.

## Diagrama de Classes

### Classes

Classes são uma representação abstrata de um conjunto de objetos que compartilham atributos e operações. No Diagrama de Classes, uma classe é representada como uma caixa que possui no máximo 3 compartimentos:

- Um compartimento com o nome da classe;
- Um compartimento com os atributos da classe;
- Um compartimento com as operações da classe.

<img src="../.assets/classes.jpg">

Atributos: representam a descrição dos dados armazenados pelos objetos de uma classe. Podem incluir possíveis valores (tipagem).

- idade: Integer

Operações: correspondem às ações que os objetos de uma classe sabem realizar. Operações são as mesmas para todos os objetos de uma classe. Podem incluir possíveis valores de retorno (tipagem).

- somar (valor1, valor2): Float


### Relacionamentos

Para representar que objetos/instâncias podem se relacionar durante a execução do sistema, utilizamos a associação.

- No diagrama, utilizamos uma linha reta entre classes para mostrar associações.

Exemplos:

Vendas: um cliente compra produtos

<img src="../.assets/clienteproduto.jpg">

Bancário: uma conta-corrente possui um histórico de transações.

<img src="../.assets/contahist.jpg">

Associações são entre classes, mas representam ligações possíveis entre objetos.

Associações podem também informar os limites inferiores e superiores de quantidade de objetos. Em UML, chamamos de Multiplicidade. Os valores são mostrados em cada extremo da linha de associação.

<img src="../.assets/tabmult.jpg">

Quando existe uma relação entre duas classes quer dizer que uma contem atributo da outra
