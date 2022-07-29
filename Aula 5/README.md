# Diagramas de Sequência

## Modelagem de Interações

### Diagramas de Caso de Uso

- Quais operações devem ser executadas internamente?

- A que classes essas operações pertencem?

- Quais objetos participam da realização do caso de uso?

### Digramas de Classe

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

- Mensagens Simples

- Mensagens Síncronas;

- Mensagens Assíncronas

Objetos também podem enviar mensagens a si próprios, requisitando execução de uma função de sua própria classe. Chamamos de **mensagens reflexivas**.

- **Mensagens Simples**: são utilizadas quando a natureza das mensagens não é relevante. Esse é o tipo de mensagem mais comum.

- **Mensagens Síncronas**: são utilizadas quando o objeto remetente espera o objeto receptor concluir o processamento da mensagem antes de retornar o seu. Isso significa que o objeto remetente fica bloqueado até o receptor terminar de atender a requisição.

- **Mensagens Assíncronas**: são mensagens nas quais o objeto remetente não espera a conclusão do processamento da mensagem para prosseguir com seu comportamento.

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

