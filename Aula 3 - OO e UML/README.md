## UML

Softwares se tornam mais difíceis de criar conforme seus escopos crescem. O paradigma OO facilita a construção criando agentes autónomos.


### Unified Modelling Language (UML)

A Linguagem de Modelagem Unificada é uma metodologia visual para projetar sistemas OO. Cada conceito de OO possui uma representação gráfica, uma sintaxe e uma semântica.

<img src="/.assets/equivalencia em classe e uml.JPG"/>

O JAVA é baseado em UML. Você pode simplismente criar o diagrama em UML colocar em um programa que irá convertar em código java.


### Casos de Uso

Casos de Uso são representações das funcionalidades externas observáveis no sistema.

O Diagrama de Casos de Uso vai modelar os requisitos funcionais do nosso sistema

```
- Requisito Funcional (Está relacionado ao motivo real do software existir)

Ex: Consulta de Saldo ou estoque

- Requisito não Funcional (Não está relacionado ao motivo do software existir)

Ex: O tamanho pode ser medido em kbytes e número de Chip de RAM.

```

-- Formatos Casos de Uso

- Formato de descrição contínua: (um parágrafo ou dois descrevendo como será a funcionalidade)

```
O Cliente chega ao caixa eletrônico e insere seu cartão. O Sistema requisita a senha do Cliente. Após o Cliente fornecer sua senha e esta ser validada, o Sistema exibe as opções de operações possíveis. O Cliente opta por realizar um saque. Então o Sistema requisita o total a ser sacado. O Sistema fornece a quantia desejada e imprime o recibo para o Cliente.
```

- Formato Numerado:

```
1. Cliente insere seu cartão no caixa eletrônico.
2. Sistema apresenta solicitação de senha.
3. Cliente digita senha.
4. Sistema exibe menu de operações disponíveis.
5. Cliente indica que deseja realizar um saque.
6. Sistema requisita quantia a ser sacada.
7. Cliente retira a quantia e o recibo.
```

- Formato de descrição parcionada:

Divide o caso de uso em usuário e como o sistema responde

<img src="/.assets/parcionado.JPG"/>


Esses exemplos representam um cenário, ou seja, uma descrição de como o caso de uso pode ser realizado. Na realidade costuma haver diversos cenários para cada caso de uso.

E se o caixa não tiver dinheiro suficiente?

E se o cliente errar a senha?

## Representação no diagrama

Um caso de uso é representado por uma elipse com seu nome posicionado abaixo ou dentro desta.

<img src="/.assets/caso de uso.JPG">


### Atores

Atores são agentes que interagem com o sistema. De forma mais abstrata, são papéis.

Ou seja, uma mesma pessoa pode atuar como atores diferentes dependendo do seu papel em relação ao sistema.

<img src="/.assets/atores.JPG">


Em UML atores são representados por um boneco, com o nome do ato abaixo deste. Atores podem ser primários ou secundários.

<img src="/.assets/d_atores.JPG">

Atores primários são os que dão início a uma sequência de interações de um caso de uso.

Atores secundários interagem com o sistema para possibilitar a conclusão do objetivo do ator primário

### Relacionamentos

As interações entre Casos de Uso e Atores (e entre Casos de Uso) são chamadas relacionamentos.

Em UML são representados por linhas contínuas.

<img src="/.assets/d_atores.JPG">


A UML define quatro tipos de relacionamentos:

- Comunicação (caso de uso está sendo iniciado por um ator)

- Inclusão (um caso de uso está acontecendo dentro de outro caso de uso)(está dizendo que dentro do caso de uso obrigatoriamente o caso de uso interno deve ser chamado)

- Extensão (são casos de uso opcionais caso um caso de uso seja chamado)

- Generalização (herança) (pode ocorrer tanto entre atores como em caso de uso)

#### Relacionamento de Inclusão

Relacionamentos de inclusão ocorrem exclusivamente entre casos de uso. E representam sequências de interações compartilhadas.

Se o Caso de Uso A inclui o Caso de Uso B, os passos existentes em B são passos obrigatórios em A.

Em UML são representados por linhas traçadas com uma seta na direção do Caso de Uso incluído.

O estereótipo <<inclui>> é adicionado à relação.

<img src="/.assets/inclusão.JPG">

#### Relacionamento de Extensão

Relacionamentos de extensão ocorrem exclusivamente entre casos de uso. E representam sequências de interações que podem existir em um caso de uso.

Se o Caso de Uso A estende o Caso de Uso B, os passos existentes em B são passos opcionais em A.

Em UML são representados por linhas traçadas com uma seta na direção do Caso de Uso extensor.

O estereótipo <<estende>> é adicionado à relação.

<img src="/.assets/extensao.JPG">

#### Relacionamento de Generalização (Herança)

Relacionamentos de extensão ocorrem entre dois casos de usos ou dois atores. E representam uma reutilização óbvia de comportamento.

Se um ator A herda de um ator B, o ator A possui os mesmo relacionamentos que o ator B e mais os seus próprios..

Se a herança ocorre entre casos de uso, A é um caso especial de B, onde o comportamento é modificado.

Em UML são representados por linhas contínuas com uma seta na direção do Caso de Uso herdado.

<img src="/.assets/heranca.jpg">

OBS: **Manter ou CRUD** são palavras que representam as ações Create, READ, UPDATE e DELETE em um único caso de uso.

