## UML

Softwares se tornam mais difíceis de criar conforme seus escopos crescem. O paradigma OO facilita a construção criando agentes autónomos.


# Unified Modelling Language (UML)

A Linguagem de Modelagem Unificada é uma metodologia visual para projetar sistemas OO. Cada conceito de OO possui uma representação gráfica, uma sintaxe e uma semântica.

<img src=".assets/equivalencia em classe e uml.JPG"/>

O JAVA é baseado em UML. Você pode simplismente criar o diagrama em UML colocar em programa que irá convertar em código java.


# Casos de Uso

Casos de Uso são representações das funcionalidades externas observáveis no sistema.

O Diagrama de Casos de Uso vai modelar os requisitos funcionais do nosso sistema

- Requisito Funcional (Está relacionado ao motivo real do software existir)

Ex: Consulta de Saldo ou estoque

- Requisito não Funcional (Não está relacionado ao motivo do software existir)

Ex: O tamanho pode ser medido em kbytes e número de Chip de RAM.

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

<img src=".assets/parcionado.JPG"/>


Esses exemplos representam um cenário, ou seja, uma descrição de como o caso de uso pode ser realizado. Na realidade costuma haver diversos cenários para cada caso de uso.

E se o caixa não tiver dinheiro suficiente?

E se o cliente errar a senha?

-- Representação no diagrama

A 