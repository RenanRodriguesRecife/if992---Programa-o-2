# Diagramas de Sequência

## Modelagem de Interações

### Diagramas de Caso de Uso

O diagrama de Caso de Uso não responde algumas perguntas:

- Quais operações devem ser executadas internamente?

- A que classes essas operações pertencem?

- Quais objetos participam da realização do caso de uso?

### Digramas de Classe

O diagrama de Classes não responde essas perguntas:

- Como objetos colaboram para que um determinado caso de uso seja realizado?

- Qual a ordem das mensagens enviadas durante a realização?

- Que informações enviar em uma mensagem de um objeto?

- Há classes e reponsabilidade ainda não identificadas?

### Modelagem de Interações 

- Modelos anteriores são representação **incompletas** do sistema;

- Possuem objetivos de fornecer entendimento do problema;

- Precisamos de um **modelo de interações** para responder as questões levantadas.

#### Validação

Por meio do modelo de interações podemos validar as classes, reponsabilidades e colaboradores anteriormente identificados.

#### Refinamento

Esse modelo nos permite refinar as classes de domínio, pois as operações de cada classe são identificadas.

### Mensagens

Uma **mensagem** é uma solicitação de execução de operação em um outro objeto.

Podemos ver um sistema baseado em OO como uma rede de objetos. Nessa rede, mensagens são a única forma de comunicação entre objetos.

### Tipos de Mensagens

UML define três tipos de mensagens:

<img src="tipos de mensagens">

- Mensagens Simples

- Mensagens Síncronas;

- Mensagens Assíncronas

Objetos também podem enviar mensagens a si próprios, requisitando execução de uma função de sua própria classe. Chamamos de **mensagens reflexivas**.

- **Mensagens Simples**: são utilizadas quando a natureza das mensagens não é relevante. Esse é o tipo de mensagem mais comum.

- **Mensagens Síncronas**: são utilizadas quando o objeto remetente espera o objeto receptor concluir o processamento da mensagem antes de retornar o seu. Isso significa que o objeto remetente fica bloqueado até o receptor terminar de atender a requisição.

(No diagrama Obrigatóriamente ele requisita uma mensagem de retorno (pontilhada))

- **Mensagens Assíncronas**: são mensagens nas quais o objeto remetente não espera a conclusão do processamento da mensagem para prosseguir com seu comportamento.

(No diagrama Mensagem de retorno não é obrigatória, caso deseje colocar a respresentação da mensagem de retorno deve ser do tipo assíncrona)

## Sintaxe UML - Mensagem

Em UML, mensagens são representadas graficamente por uma seta.

A seta segue o sentido do objeto remetente ao objeto receptor.

As setas possuem rótulos que define a especificação da mensagem sendo enviada. A especificação segue o seguinte formato.

**expressão-sequência recorrência:v := mensagem**

#### expressão-sequência

**expressão-sequência** recorrência:v := mensagem

A mensagem pode estar associada a uma expressão de sequência, usada para remover ambiguidades.

Pode ser definida como formato de níveis, por exemplo: 1, 1.1, 1.2, 2, 2.1, etx.

Também podemos usar sufixos de letras para indicar paralelismo: 1.1a, 1.1b

#### recorrência

expressão-sequência **recorrência**:v := mensagem

Às vezes é necessário indicar que o envio de uma mensagem está condicionado á uma expressão lógica. Outras é necessário indicar a quantidade de vezes que uma mensagem é enviada.

Para cada um utilizamos uma sintaxe:

- [cláusula-condição],ex: [a>b]
- *[cláusula-iteração], ex: *[i:=1..10]

#### v

expressão-sequência recorrência:**v** := mensagem

Com o elemento v, podemos indicar o nome de variável que receberá o valor de retorno da operação a ser executada no objeto receptor.

#### mensagem

expressão-sequência recorrência:v := **mensagem**

O elemento mensagem representa a expressão chamada de uma operação definida na classe do objeto receptor.

Pode incluir a lista de parâmetros, possivelmente vazia, utilizando parênteses. Parâmetros são delimitados por vígulas.

Exemplos:

- 1:adicionarItem(Item)
- 3 [a > b]:trocar(a,b)
- 2 *:desenhar()
- 2 *[i:=1..10]:figuras[i],desenhar()
- 1.2.1:x:=selecionar(e)

expressão-sequência recorrência:v := mensagem

## Diagramas de Interações

Os diagrams de interações modelam a lógica de um **cenário de caso de uso** ou **uma parte** de um cenário, caso esse seja muito complexo.

O diagrama irá descrever a sequencia de mensagens enviadas e recebidas pelos objetos que participam do caso de uso.

Existem **dois** tipos de diagramas de interações:
- diagramas de sequência.
- diagramas de colaboração.

Em nossa disciplina veremos **diagramas de sequência**. Mas ambos são equivalentes

- diagramas de sequência possuem ênfase na ordem temporal

- diagramas de colaboração, por sua vez, enfatizam as relações entre objetos

## Diagrama de Sequência

Diagramas de sequência são formados por diversos componentes gráficos:

<img src="">

- Atores
- Objetos
- Classes
- Linhas de vida
- Mensagens
- Focos de Controle
- Criação de Objetos
- Destruição de objetos

<img src="">

**Atores** podem ser opcionalmente representados, caso participem da realização do caso de uso.

São representados da mesma maneira que no diagrama de casos de uso.

**Objetos** que participam da realização do caso de uso devem aparecer no diagrama. São representados por retângulos com o nome do objeto, sublinhado.

Objetos podem ser nomeados ou anônimos.

A ordem horizontal não possui significado. Mas geralmente segue (esquerda->direita): atores, fronteira, controle, entidade.

**Classes** Na maioria das vezes, apanas objetos são representados.

Mas caso uma mensagem seja endereçada à uma classe, não a um objeto, podemos representar a própria classe no diagrama. (Operação estáticas)

Uma classe é representada da mesma maneira que um objeto, mas o nome não é sublinhado.

**Linha de vida** No diagrama de sequência, cada objeto aparece no topo de uma linha vertical tracejada. Essa linha é denominada **Linha de vida**.

**Mensagens** são representadas por uma flecha horizontal, ligando uma linha de vida a outra.

O objeto do qual a flecha parte é o remetente, e a flecha aponta para o receptor.

O formato da ponta da seta indica o tipo de mensagem. O rótulo da mensagem fica acima da linha.

**Linha de vida**
A passagem do tempo é percebida na direção vertical, de cima para baixo

Quando mais baixo se encontra uma mensagem, mais tarde no decorrer do caso de uso ela é enviada.

Embora nem sempre seja possível, deve se tentar organizar o diagrama na ordem em que as mensagens são enviadas.

**Foco de controle** são os blocos retangulares que ficam sobre as linhas de vida. Um foco de controle representa o tempo em que um objeto realiza uma ação

O topo coincide com o recebimento de uma mensagem, enquanto o fundo coinide com a finalização de uma operação.

O retorno se torna opcional pois o fundo corresponde com o retorno.

<img src = "">

A posição vertical de um objeto no diagrama indica o momento em que começa a participar da interação.

<img src = "">

A instanciação de um objeto pode ser requisitada por meio de uma mensagem, comummente a mensagem é rotulado com o nome criar

<img src = "">

O diagrama também pode mostrar a **destruição de um objeto** no decorrer de um interação.

Um X abaixo do foco de controle do objeto representa que ele está sendo destruído.

Um objeto normalmente é destruído quando ele não é mais necessário na interação

<img src = "">

Objetos podem precisar de ajuda para realizar suas responsabilidades. Para isso ele deve enviar mensagens.

Essa mensagem indica que existe uma operação no objeto receptor.

## Estudo de Caso

### Sequência

Para construir um diagrama de sequência devemos seguir os passos abaixo:

1 - Para cada caso de uso, definir um conjunto de cenários relevantes

2 - Para cada cenário, faça o seguinte:
    -   Posicione os atores, objeto de fronteira e objeto de controle no diagrama
    -   Para cado passo do cenário, defina as mensagens a serem enviadas de um objeto a outro
    -   Defina as cláusula de condição e iteração, se existirem, para as mensagens;
    -   Adicione multi objectos e objetos de entidade à medida que a sua participação se faça necessária no cenário selecionado.

1 - Para cada caso de uso, definir um conjunto de cenários relevantes.

A escolha depende da complexidade dos cenários. Esses podem ser cenário de fluxo principal, alternativo ou de exceção, ou até parte de um fluxo.

2 - Para cada cenário, faça o seguinte:
    b - Para cada passo do cenário, defina as mensagens a serem enviadas de um objeto a outro;

A seleção das mensagens parte das responsabilidades dos objetos. Com isso podemos definir: o nome da mensagem, os argumentos, valores de retorno, cláusulas de condição e repetição.

**É possível identificar a necessidade de novas classes durante a criação do diagrama de sequência!**

Por fim, o modelador (nós) deve verificar a consistência do diagrama resultante.

-   Cada cenário relevante para cada caso de uso foi considerado?

-   As mensagens recebidas pelos objetos são consistentes com suas responsabilidades?

Mensagens enviadas por atores não indicam operações, geralmente são rotuladas com a informação solicitada. Ex.: item pedido, id e senha.
