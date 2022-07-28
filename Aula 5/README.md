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
